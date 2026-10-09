"""Bounded check for report 010, Proposition P3 (N_split rejects the free-SMC embedding of C_p).

In the free symmetric monoidal category on one object X, End(X^{(x)p}) is the symmetric group S_p
(Mac Lane coherence; used here only as the motivating fact). Report 005 section 9 / 006 embed the
cyclic source S_p into it by sending the rule r to the p-cycle. N_split would require a group
homomorphism R: S_p -> C_p with R(p-cycle) = 1 (a left inverse of the embedding C_p -> S_p).

This script enumerates every assignment of the generators (1 2) and (1 2 ... p) of S_p to elements
of C_p = Z/p, extends it along all words (breadth-first over the Cayley graph), and reports which
assignments define homomorphisms and whether any of them sends the p-cycle to a generator of C_p.

Run: python3 -I reports/010-checks/retraction_check.py
"""
from itertools import product

def compose(a, b):  # (a*b)(i) = a(b(i))
    return tuple(a[b[i]] for i in range(len(a)))

def homs(p):
    ident = tuple(range(p))
    t = tuple([1, 0] + list(range(2, p)))
    c = tuple([(i + 1) % p for i in range(p)])
    gens = [t, c]
    found = []
    for it, ic in product(range(p), repeat=2):
        img = {ident: 0}
        frontier = [ident]
        ok = True
        while frontier and ok:
            nxt = []
            for g in frontier:
                for s, v in zip(gens, (it, ic)):
                    h = compose(s, g)
                    val = (img[g] + v) % p
                    if h in img:
                        if img[h] != val:
                            ok = False
                            break
                    else:
                        img[h] = val
                        nxt.append(h)
                if not ok:
                    break
            frontier = nxt
        if ok:
            found.append((it, ic, len(img)))
    return found

for p in (3, 5, 7):
    hs = homs(p)
    splits = [h for h in hs if h[1] % p != 0]
    print("p=%d: %d homomorphisms S_p -> C_p; with p-cycle |-> generator: %d" % (p, len(hs), len(splits)))
