# Fresh adversarial critique of reports/002-fundamentality.md

Reviewer: independent subagent (same underlying model family; no shared drafting). Date 2026-10-08.
Repository NOT modified. Labels: CONFIRMED = checked against the report text or a downloaded source text;
INFERENCE = my informal argument (not machine-checked); UNVERIFIED = memory or unchecked.

Bottom line: the narrow claim "SN excludes interpreters that inspect *formula instances*" survives. The broader claims
do not survive as stated:
- "SN excludes checker-as-proof";
- "SN/HN forces HOM";
- "no per-instance computation";
- "D2 is a meaningful fixed-core notion";
- "Yamada is a conservative D2 witness".

One construction (B1) passes SN ∧ HN ∧ ADQ1 with an empty per-logic environment, which makes D2 vacuous under one
reading of the wrapper clause. The ledger is the only thing standing between the definition and that construction,
and the ledger's "logical role" is not well-defined (D-section).

---

## A. Lemma 1 (SN ∧ HN ⇒ HOM) and Lemma 2 (acceptance is schematic)

### A1. Lemma 1 has a missing hypothesis: premise holes must be substitutable variables (INFERENCE; report text CONFIRMED)

The proof takes M_r := F(r(u⃗)) and writes r(d⃗) = r(u⃗)[d⃗/u⃗]. That needs two things:
- each premise hole u_i is a hypothesis of S's own declared discipline (for hypothetical premises, a
  *second-order* hypothesis);
- HN covers substitution for it.

For sources without a hypothetical judgment, HN is vacuous and the lemma has no premise to use. The report explicitly
admits such sources ("Hilbert, sequent calculi", L-a). Examples: LK and theorem-only Hilbert systems.

**Concrete counterexample to Lemma 1 and T1.**
- *Source.* S is theorem-only Hilbert implicational logic: axiom schemas K and S, rule MP. It is finitely
  schematic.
- *Target.* A is LF with constants k, s, mp. ≡_A is βη of LF.
- *Map.* F(d) := the LF code of the weak-normal form of d, read as a typed combinatory term.
- *SN holds exactly.* Typed CL weak reduction is SN and confluent. It is blind to types, so
  nf(d[θ]) = nf(d)[θ] syntactically.
- *HN holds vacuously.* *ADQ1 holds* (same LF signature).
- *HOM fails.* F(mp(d1,d2)) = nf(app(F d1, F d2)) is not M_mp[F d1, F d2] for any fixed LF template, because LF's ≡
  does not contain CL weak reduction.

Generalisation: F may run any total computation on the type-erased skeleton of d, provided the output is a valid
derivation of the same end-sequent. This is a falsifier for T1 exactly as T1 itself words its falsifier.

**Fix.** Require naturality for *derivation metavariables*, i.e. premise holes of every judgment form. That is, SN must
hold at the proof sort too. But then HOM is close to a definition, and the rhetoric that "rule locality is a
*consequence* … not an independent stipulation" (§3) is weakened.

### A2. The Fiore–Plotkin–Turi analogy is misapplied (INFERENCE)

Initiality says that an *F-algebra/monoid morphism* out of the initial Σ-monoid is determined by its values on
generators. SN gives only the *substitution* (monoid) half. The *algebra* half (preservation of rule constructors)
is exactly what Lemma 1 sets out to prove, and A1 shows it does not follow without premise variables.

### A3. Lemma 2 conflates schematic validity with absence of computation (INFERENCE; violates AGENTS.md rule 5's computation/complexity distinction)

Lemma 2 says: "Any computation the representation performs while accepting a step of r is carried out once, at the
schema." This is false for the report's own loophole L-a.
- The checker `valid` recurses on the *certificate*, which grows with the derivation.
- It is insensitive only to *formula* instantiation.
- It can do unbounded (for example, Ackermann-padded) work per derivation and per step, and still be stable under
  metasubstitution.

What is true is narrower: "acceptance is invariant under instantiating formula metavariables." That is a validity
statement, not a cost statement. The corollary in T1 ("SN cannot implement per-instance computation") must be
restricted to *per-formula-instance* computation.

### A4. Other hypotheses to state (INFERENCE / UNVERIFIED)

1. **Typing stable under substitution.** In λΠ-modulo this needs more than "≡ stable". Subject reduction and product
   compatibility are needed (UNVERIFIED-MEMORY: Blanqui-style conditions). The report lists λΠ-modulo as a framework
   with "substitution-stable rewriting" without these conditions.
2. **Side conditions.** §2.1 excludes side conditions. So *type theories with a conversion rule* (side condition
   A ≡ B) are not finitely schematic at all. L-f is therefore not an over-exclusion by SN; such systems are outside
   the source class by §2.1. The two statements are inconsistent.
3. **ADQ2.** "Bijection … canonical inhabitants (modulo ≡_A)" is redundant or ill-typed. Canonical forms are already
   ≡-representatives. η-long form should be stated.
4. **Second-order HN.** The second-order case of HN (hypotheses of rule type φ ⊢ ψ) is not part of NJ's own
   discipline. So HN quantifies over an *LF-style extension* of S's derivations. That is mildly framework-tailored.

---

## B. Constructions that pass the definition

### B1. Universal reflected-signature framework: D2 becomes vacuous (INFERENCE; this breaks D2 as literally stated)

**The fixed signature.** Fix one LF signature Σ_univ, with no rewriting, independent of S:
- universal HOAS syntax `tm`, with operator names as numerals and a `bind : (tm→tm) → arg`;
- rule codes `rl` and signatures `sig` as lists;
- `Prf : sig → tm → type`;
- relational judgments `mem`, `inst` (pattern instantiation, with second-order metavariables applied by LF β);
- `prems`, whose constructors take LF functions (Prf s h → Prf s c) for hypothetical premises and (Πx:tm. …) for
  parametric ones;
- one rule `use : Πs r. mem r s → Πσ c. inst r σ c → prems s r σ → Prf s c`.

**The representation of any finitely schematic S.**
- ⌜φ⌝ is componentwise into tm, with metavariables sent to LF variables.
- ⌜⊢_S φ⌝ := Prf code_S ⌜φ⌝. This is a "fixed judgment-level wrapper", which §2.3 allows.
- F(r(d⃗)) := use code_S ⌜r⌝ (mem-pf) σ c (inst-pf) (prems built from F(dᵢ), λu.F(dᵢ)).

**Why it passes.**
- mem-pf and inst-pf depend only on the closed code ⌜r⌝ and on opaque σ. So SN, HN and HOM hold, with hypotheses as
  LF variables of type Prf code_S ψ.
- ADQ1 should follow by canonical-form inversion (ADQ2 is plausible, since mem and inst proofs are unique).
- E_S = ∅.

**Consequence.** LF + Σ_univ is D2-generative for every class of finitely schematic calculi. The rules are smuggled
in as *data*, which is AGENTS.md rule 6's "user-defined trusted rules smuggled into the environment".

The report dismisses this variant in its I-E row: "the ledger counts [S's patterns] as role (c)". By its own test for
(c) ("rule-typed item whose removal is non-conservative"), code_S is:
- not rule-typed;
- not an E_S item at all when it sits in the wrapper;
- a removable definition, so role (d), if it is placed in E_S.

**Partial repair** (INFERENCE):
- Require the judgment wrapper to be S-independent: `Prf : tm → type`, with `use` referring to an opaque constant
  `theSig` that E_S must define.
- Then removing `theSig := code_S` is non-conservative, so the removal test classifies it as (c), and the attack is
  caught.

The report must state this amendment explicitly. As written, "fixed" is ambiguous. D3 has the same problem: with
𝒦 unrestricted, rule codes count as structural data.

### B2. Checker-as-proof passes SN ∧ HN ∧ HOM ∧ ADQ1 for sequent and Hilbert sources (INFERENCE; partly conceded by the report as L-a)

**Construction.**
- F(d) := acc ⌜Δ⊢Γ⌝ (π(d)) refl.
- π maps the LK derivation into a certificate of any Cook–Reckhow system whose verifier treats atoms and
  metavariables as opaque leaves. Examples are a Frege system via fixed per-rule derivations (Cook–Reckhow style), or
  extended Frege.
- `valid` is that system's checker, written as rewrite rules with a non-left-linear `eq`.

**Why it passes.**
- SN holds: the code is componentwise, and rewriting is stable.
- HOM holds via `getcert`.
- ADQ1 holds.

This is "proof-checker-in-an-axiom" for *another* proof system. The report calls L-a "benign" because "its derivation
algebra is … isomorphic to the LF image". That is false here: the certificates are π-images in a different calculus,
and the checker's acceptance language is that calculus.

**Consequences.**
- §0's list "excludes every universal-interpreter construction examined … EF + reflection … Dedukti conversion
  checker" is overstated.
- I-R (EF + Refl_S) is excluded only because of *bit-encoding*. An atom-uniform, term-structured encoding of Refl for
  an atom-uniform verifier is not excluded.

### B3. L-a likely extends to ND sources, contrary to the I-C′ row (INFERENCE, plausible, not checked)

The I-C′ row says HN "Fails for ND sources (hypotheses become certificate data)". Proposed repair of the attack:
1. Make certificate leaves `hypcert ψ (getcert u)`, with u : Prf ψ an *A-variable*.
2. Let `getcert (acc ψ c refl) ↪ c`.
3. Let `valid` traverse HOAS binders `lamcert φ (λu.c[u])` using higher-order (Miller) patterns, which Dedukti
   supports.

HN then holds up to ≡ by `getcert` reduction. If this is right, checker-as-proof passes the full D1 test for NJ too.

### B4. HN is what does the excluding, and the Recommendation drops it (CONFIRMED textually)

- D1 = SN + HN + ADQ1 (§2.4).
- §10.3 recommends "adopting SN + ADQ1 + ledger".
- Without HN, a whole-derivation checker for NJ with hypotheses coded as data passes SN + ADQ1 directly (the I-C′
  row's own analysis).

Also, the §6.2 table entry "D1 without HN" is not a category the definitions allow: D1 *requires* HN. Internal
inconsistency.

---

## C. Over-exclusion beyond L-f and L-g

### C1. HN over-excludes every first-order or deep embedding of hypothetical logics (INFERENCE)

These all fail HN, by the report's own §6.2 row "contexts as data: HN No":
- rewriting-logic encodings of ND (Martí-Oliet–Meseguer);
- Metamath;
- Coq/Lean/Isabelle-HOL inductive-predicate embeddings with explicit contexts;
- de Bruijn deep embeddings.

These are legitimate, not interpreters. The task's gate (ii) asks for no exclusion "by fiat". This cost is not
listed.

Isabelle/Pure meta-level encodings and Dedukti "decoding" encodings (Prf(imp A B) ↪ Prf A → Prf B) do pass SN and
HN. Generic X is stuck harmlessly.

### C2. Negative translations fail at the proof level (INFERENCE; standard facts from memory, UNVERIFIED-MEMORY)

**The problem.**
- At formula level, Gödel–Gentzen and Kolmogorov translations are Σ-homomorphisms (atoms ↦ ¬¬p, metavariable
  X ↦ X), so they satisfy SN.
- At proof level, the NK rule RAA needs ¬¬φᴺ → φᴺ, which is built *by induction on φ*.
- At a generic X there is no template. If X ↦ ¬¬X instead, SN fails syntactically (¬¬¬¬ …).

So the standard classical→intuitionistic proof translations fail SN/HOM. This is a third over-exclusion, not listed.

**Possible repair.** Translate metavariables into a Σ-sort of "stable propositions", ⟨X, stab_X⟩, with
compositional stability proofs. This is analogous to the wrapper repair, and needs checking.

**Related.** Call-by-value CPS commutes with substitution only for values (Plotkin; UNVERIFIED-MEMORY). So HN fails
for CBV CPS with non-value substitutions.

### C3. Modal → FOL (INFERENCE)

The wrapper repair needs a target with second-order metavariables (ST_x as λx…), because plain FOL has no predicate
variables. That is fine via Fiore–Mahmoud. Separately, ADQ1 fails for Kripke-incomplete or non-first-order-definable
logics (for example GL). That is not SN's fault, but the report should not suggest that the wrapper repairs "the
standard translation" in general.

---

## D. D1, D2, D3: definitional problems

**D1. "Logical role" is not well-defined.** It is partly syntactic, partly by examples (CONFIRMED textually; INFERENCE on consequences).
- **(b) vs (c) collapses under shallow embedding.** Take `raa : ΠA. ((A→⊥)→⊥) → A` in STLC/LF.
  - It is a closed inhabitant of the judgment type pf(¬¬A ⊃ A), so role (b).
  - It is also rule-typed with non-conservative removal, so role (c).
  - D2 allows (b) but not (c). So the D2 status of NK-in-STLC is undetermined.
  - More generally, any Hilbert system can be made "D2" by declaring all logic as schematic axioms (b) and deriving MP
    as application.
- **The removal test is not item-wise coherent.**
  - *(i) Redundant rule:* removal is conservative, so it is not (c), yet it is not "a term over other items" unless
    one substitutes the derivation. Is it (d)? Arguably yes, but only at derivability level. Under ADQ2 it is not
    eliminable.
  - *(ii) Mutually redundant pair r1, r2:* removing either alone is conservative, removing both is not. Neither is (c)
    item-wise, yet the pair is. The role is not a property of items.
  - *(iii) Admissible but non-derivable primitive* (Cut declared in an LF encoding of LK): removal is conservative
    (cut admissible), so it is not (c). It is not definable, so it is not (d). It falls into no role.
  - *(iv)* "Conservative" over which language and judgments is unstated (removing syntax changes the language).
- **(c′) is defined only by enumeration.** "A mode, a 1-cell/2-cell, …". So D3's admissible data and D2/D3's boundary
  ("Adjoint logic … D2 only if structural data are not counted as rules") depend on an undefined classification.
- **"D2 ⇒ D3" is not literally true.** D3 additionally demands that each logical rule be "an instance of one of A's
  finitely many generic rule schemas". A D2 representation may realise a rule as a composite derived term.
  "Instance of a generic schema" is undefined. Under any liberal reading, Σ_univ's single `use` rule (B1) is one
  generic schema, with codes as structural data.
- **Inequivalence.** The witnesses show that *a given A* can be D1 and not D2. Given B1, they do not show that D2 is a
  stronger *class-level* demand than D1.

---

## E. Citation and claim checks

1. **Yamada — OVERSTATED (CONFIRMED against unity.txt).**
   - Cor 3.18 maps LK into **ILCι**. Yamada says ILCι "does not enjoy cut-elimination", and the maps ( )! and ( )? on
     ILLeι "are not conservative". He also says "we cannot show that this translation T! is conservative as ILCι does
     not enjoy cut-elimination" (around l.1270).
   - Conservativity (Cor 3.37) holds only for **LKρ → … → ILCρ**.
   - ILCρ and LKρ are defined by restricting proofs to "tractable" ones (Defs 3.27–3.28, 3.35–3.36). The conditions
     are a *hereditary purity condition on whole subtrees* plus a ban on ?!R!?. That is a global, non-schematic
     condition, outside §2.1's finitely schematic class, and not obviously closed under proof substitution.
   - The Cut translation (Remark 3.17) uses ?!R!?, which is forbidden in ILCρ.
   - So the report's "LK, LJ and ILL translate connective-wise and conservatively" (§0.5; §9.3) does not satisfy its
     own HOM/SN notion for full LK.
   - Possible salvage (INFERENCE): cut-free LK into the cut-free fragment of ILCι minus ?!R!? (schematic), with
     conservativity via Thm 3.30 / Cor 3.37. This is at provability level only, and calculus-to-calculus, not a
     framework with environment.
   - Also, Yamada's own paper says Girard's LU already embodies CL, IL and LL "as its fragments". So prior art at
     R1–R2 is better cited to LU (NOT_ACCESSED).
2. **KKNS Thm 8 — MISUSED in §0 and §8 (CONFIRMED vs gfu notes).**
   - The gfu notes record that "the undecidable instance's computation is in the end-sequent's formulas, not in Σ".
   - That is undecidability of the *logic*, like Lambek+!, full LL or FOL. It is not "the environment becoming a
     universal rewriting layer".
   - The report's own L-b says exactly this, so §0's "Without a restriction, the problem just moves into the
     environment" contradicts L-b.
3. **Buszkowski (via KKS Thm 10) — category slip (CONFIRMED vs gfu).**
   - These are *non-logical axioms* (role (b)) in the non-commutative Lambek calculus, not (c′) structural data.
   - Finiteness of A is unverified (the report flags this in §8 but not in §0).
   - "Bipoles do not prevent this" combines Lambek-setting results with LK. The notes call it INFERENCE, and §0
     states it as fact.
4. **CSZ Thm 3.27 — §0 omits "infinite" (CONFIRMED vs own/gfu notes).**
   - The base has infinitely many generating arrows (DPP: infinite hom-sets).
   - It is about proof *identity*, not derivability.
   - §8 is accurate; §0 is not.
5. **Cook–Reckhow (CONFIRMED vs cyc notes).**
   - Omitted hypotheses: classical propositional only; sound and *implicationally complete* rules; same connective
     set K. The cross-connective case is Reckhow's thesis (SECONDARY).
   - §7.2 juxtaposes this with connective bases ({nand} vs {∧,¬}), which C–R Thm 2.3 does not cover.
   - "Exactly a HOM translation" is fine for same-language Frege.
6. **Jeřábek, PAL, LSR Conj 8.5, Gardner (6.4.4 / 6.5.7 / Cor 5.1.8), MDT, Pelletier–Urquhart, Caleiro–Gonçalves** —
   consistent with the notes (CONFIRMED).
   - Gardner's Thms 5.2.11/5.2.13 (Hilbert systems adequate but not natural in the obvious signatures) are unmentioned
     but relevant to L-a's isomorphism claim.
   - The bnd notes' own caveat ("compositionality is AUTOMATIC for any syntactic translation … discriminating power
     comes from adequacy") is not reflected in §0's emphasis.
7. **Prop 4** (no schematic conservative IPC → CPC). The argument is correct given Rieger–Nishimura (a standard fact;
   still UNVERIFIED-MEMORY in the report). INFERENCE: sound.

---

## F. Recommendation, uncertainty, next test

**NARROW does follow from the evidence** (INFERENCE). But the gate (ii) entry "Met, with stated loopholes and
over-exclusions" should be downgraded to "Partly":
- B1 needs an explicit wrapper amendment;
- B2 is checker-as-proof passing for sequent and Hilbert sources;
- C1 and C2 are unlisted over-exclusions.

**Strongest uncertainty.** "Independently motivated restricted class" is not a mathematical predicate. It should be
re-posed with an explicit candidate menu.

**Next test is not well-posed (INFERENCE).**
- "Possibly with multiple conclusions added" changes A, so outcome (a) can be manufactured by extending the core.
  LU or LNL polycategories may already be that extension.
- "D3 … instance of a generic schema" is undefined (section D), so (a) versus (b) cannot be adjudicated.
- A cheaper prior check is missing: LK into intuitionistic adjoint logic with σ ⊆ {W, C} via a ⌜Γ⊢Δ⌝ := Γ, ¬Δ ⊢ ⊥
  wrapper and a stable-sort negative translation (C2 repair). If this is SN ∧ HN ∧ ADQ1 with derived (composite)
  rules, the question reduces to the undefined D3 clause.

**Suggested amendments.**
1. SN at derivation metavariables (premise holes).
2. An S-independent judgment wrapper, or wrapper parameters counted in the ledger.
3. Redefine roles over *sets* of items, by derivability-level and identity-level conservativity separately, with an
   explicit slot for admissible primitives.
4. Restate Lemma 2 as invariance, not cost.
5. Correct the Yamada, KKNS, Buszkowski and CSZ statements in §0.
6. List C1 and C2 as over-exclusions.
