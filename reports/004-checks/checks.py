"""Machine checks for reports/004-positive-existence.md.

These checks support, but do not prove, the report's claims. Each one is either:
  - a first-order entailment proved by the Z3 SMT solver (an `unsat` answer to the
    negated entailment), or
  - an exhaustive enumeration over all frames up to a small size.

Z3 proofs are FORMALIZED only in the narrow sense of "checked by Z3 5.1.0 with this
script". The finite enumerations are bounded checks, not proofs.

Run with:  python3 -I reports/004-checks/checks.py
"""
import itertools
import z3

results = []


def record(name, ok, detail=""):
    results.append((name, ok, detail))
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))


# ---------------------------------------------------------------------------
# 1. ILLUSTRATION ONLY (not evidence): substitution naturality (SN) for a unary
#    standard translation over the basis {not, and, box, dia}. This is NOT the C1
#    translation of report 004 (which uses bottom, ->, and n-ary diamonds); SN holds for
#    both by construction (induction on formulas), and random testing adds no weight.
#    Formulas are nested tuples:
#      ('p', name), ('not', A), ('and', A, B), ('box', A), ('dia', A).
#    ST maps a formula to a first-order formula (as a string AST), given a world
#    variable. Atoms become predicate letters P_name(x).
# ---------------------------------------------------------------------------
_counter = [0]


def fresh():
    _counter[0] += 1
    return "y%d" % _counter[0]


def ST(phi, x):
    tag = phi[0]
    if tag == "p":
        return ("P", phi[1], x)
    if tag == "not":
        return ("not", ST(phi[1], x))
    if tag == "and":
        return ("and", ST(phi[1], x), ST(phi[2], x))
    if tag == "box":
        y = fresh()
        return ("forall", y, ("imp", ("R", x, y), ST(phi[1], y)))
    if tag == "dia":
        y = fresh()
        return ("exists", y, ("and", ("R", x, y), ST(phi[1], y)))
    raise ValueError(tag)


def subst_formula(phi, name, theta):
    """Source-level substitution phi[theta/name]."""
    tag = phi[0]
    if tag == "p":
        return theta if phi[1] == name else phi
    return (tag,) + tuple(subst_formula(c, name, theta) for c in phi[1:])


def subst_pred(f, name, lam):
    """Target-level substitution of the predicate letter P_name by lam: var -> FO formula."""
    tag = f[0]
    if tag == "P":
        return lam(f[2]) if f[1] == name else f
    if tag == "R":
        return f
    if tag == "not":
        return ("not", subst_pred(f[1], name, lam))
    if tag in ("and", "imp"):
        return (tag, subst_pred(f[1], name, lam), subst_pred(f[2], name, lam))
    if tag in ("forall", "exists"):
        return (tag, f[1], subst_pred(f[2], name, lam))
    raise ValueError(tag)


def alpha_normalize(f, env=None, cnt=None):
    """Rename bound variables canonically, so syntactic comparison is modulo alpha."""
    if env is None:
        env, cnt = {}, [0]
    tag = f[0]
    if tag == "P":
        return ("P", f[1], env.get(f[2], f[2]))
    if tag == "R":
        return ("R", env.get(f[1], f[1]), env.get(f[2], f[2]))
    if tag == "not":
        return ("not", alpha_normalize(f[1], env, cnt))
    if tag in ("and", "imp"):
        return (tag, alpha_normalize(f[1], env, cnt), alpha_normalize(f[2], env, cnt))
    if tag in ("forall", "exists"):
        cnt[0] += 1
        v = "b%d" % cnt[0]
        env2 = dict(env)
        env2[f[1]] = v
        return (tag, v, alpha_normalize(f[2], env2, cnt))
    raise ValueError(tag)


import random

random.seed(4)


def rand_formula(d, atoms=("p", "q")):
    if d == 0 or random.random() < 0.25:
        return ("p", random.choice(atoms))
    t = random.choice(["not", "and", "box", "dia"])
    if t == "and":
        return ("and", rand_formula(d - 1, atoms), rand_formula(d - 1, atoms))
    return (t, rand_formula(d - 1, atoms))


def check_sn(trials=500):
    for _ in range(trials):
        phi = rand_formula(4)
        theta = rand_formula(3, atoms=("q", "r"))
        lhs = alpha_normalize(ST(subst_formula(phi, "p", theta), "x"))
        rhs = alpha_normalize(subst_pred(ST(phi, "x"), "p", lambda v: ST(theta, v)))
        if lhs != rhs:
            return False, repr(phi)
    return True, "%d random formula/substitution pairs" % trials


ok, d = check_sn()
record("Illustration, SN: ST(phi[theta/p]) == ST(phi)[P := lambda y. ST_y(theta)] syntactically (mod alpha)", ok, d)

# ---------------------------------------------------------------------------
# 2. Z3: first-order entailments for frame correspondents (one direction of
#    Sahlqvist correspondence). Predicate letters are uninterpreted, so a proof
#    holds for every valuation.
# ---------------------------------------------------------------------------
W = z3.DeclareSort("W")
R = z3.Function("R", W, W, z3.BoolSort())
P = z3.Function("P", W, z3.BoolSort())
x, y, z, u = z3.Consts("x y z u", W)


def proves(hyps, goal, name):
    s = z3.Solver()
    s.set("timeout", 20000)
    for h in hyps:
        s.add(h)
    s.add(z3.Not(goal))
    r = s.check()
    record(name, r == z3.unsat, "z3: %s" % r)


box = lambda w, body: z3.ForAll([u], z3.Implies(R(w, u), body(u)))
trans = z3.ForAll([x, y, z], z3.Implies(z3.And(R(x, y), R(y, z)), R(x, z)))
refl = z3.ForAll([x], R(x, x))

# Axiom 4: []p -> [][]p
st4 = z3.ForAll(
    [x],
    z3.Implies(
        z3.ForAll([y], z3.Implies(R(x, y), P(y))),
        z3.ForAll([y], z3.Implies(R(x, y), z3.ForAll([z], z3.Implies(R(y, z), P(z))))),
    ),
)
proves([trans], st4, "Z3: transitivity |- forall x ST_x([]p -> [][]p)")

# Axiom T: []p -> p
stT = z3.ForAll([x], z3.Implies(z3.ForAll([y], z3.Implies(R(x, y), P(y))), P(x)))
proves([refl], stT, "Z3: reflexivity |- forall x ST_x([]p -> p)")

# Derived-rule template for necessitation: from forall x ST_x(phi) infer forall x ST_x([]phi).
nec_prem = z3.ForAll([x], P(x))
nec_conc = z3.ForAll([x], z3.ForAll([y], z3.Implies(R(x, y), P(y))))
proves([nec_prem], nec_conc, "Z3: template Nec: forall x P(x) |- forall x [](P)(x)")

# Template for axiom K: [](p -> q) -> ([]p -> []q), valid on all frames.
Q = z3.Function("Q", W, z3.BoolSort())
stK = z3.ForAll(
    [x],
    z3.Implies(
        z3.ForAll([y], z3.Implies(R(x, y), z3.Implies(P(y), Q(y)))),
        z3.Implies(
            z3.ForAll([y], z3.Implies(R(x, y), P(y))),
            z3.ForAll([y], z3.Implies(R(x, y), Q(y))),
        ),
    ),
)
proves([], stK, "Z3: |- forall x ST_x(K) with no frame condition")

# Non-entailment: without transitivity, axiom 4 is not FO-derivable (z3 finds a model).
s = z3.Solver()
s.add(z3.Not(st4))
record("Z3: no frame condition does NOT give axiom 4 (countermodel exists)", s.check() == z3.sat, str(s.check()))

# ---------------------------------------------------------------------------
# 3. Bounded exhaustive check of correspondence at FRAME level (second-order:
#    all valuations), for all frames with at most 3 worlds.
#    [] p -> [][] p is valid on F iff F is transitive.
# ---------------------------------------------------------------------------
def frames(n):
    pairs = [(a, b) for a in range(n) for b in range(n)]
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        yield n, {pr for pr, bit in zip(pairs, bits) if bit}


def valid_on_frame(n, Rel, formula_fn):
    for val in itertools.product([0, 1], repeat=n):
        Pset = {w for w in range(n) if val[w]}
        if not all(formula_fn(w, Rel, Pset, n) for w in range(n)):
            return False
    return True


def ax4(w, Rel, Pset, n):
    boxp = lambda v: all((v, t) not in Rel or t in Pset for t in range(n))
    return (not boxp(w)) or all((w, t) not in Rel or boxp(t) for t in range(n))


def is_trans(n, Rel):
    return all(not ((a, b) in Rel and (b, c) in Rel) or (a, c) in Rel
               for a in range(n) for b in range(n) for c in range(n))


okc, cnt = True, 0
for n in (1, 2, 3):
    for _, Rel in frames(n):
        cnt += 1
        if valid_on_frame(n, Rel, ax4) != is_trans(n, Rel):
            okc = False
record("Bounded: frame validates []p->[][]p  <=>  transitive (all frames <= 3 worlds)", okc,
       "%d frames checked" % cnt)

# ---------------------------------------------------------------------------
# 4. Resource control via ternary (Routley-Meyer / Dosen-style) semantics:
#    x |= A o B  iff  exists y z. R3(y, z, x) and y |= A and z |= B.
#    p |- p o p is NOT derivable without a contraction frame condition
#    (z3 finds a countermodel), but IS derivable from R3(x, x, x).
# ---------------------------------------------------------------------------
R3 = z3.Function("R3", W, W, W, z3.BoolSort())
fus_pp = lambda w: z3.Exists([y, z], z3.And(R3(y, z, w), P(y), P(z)))
seq = z3.ForAll([x], z3.Implies(P(x), fus_pp(x)))
s = z3.Solver()
s.add(z3.Not(seq))
record("Z3: ternary semantics, no contraction condition: p |- p o p has a countermodel",
       s.check() == z3.sat, str(s.check()))
proves([z3.ForAll([x], R3(x, x, x))], seq, "Z3: contraction condition R3(x,x,x) |- forall x ST_x(p -> p o p)")

# ---------------------------------------------------------------------------
print()
print("SUMMARY: %d/%d passed" % (sum(1 for r in results if r[1]), len(results)))
