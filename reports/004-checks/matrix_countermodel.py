"""Countermodel showing that the Lindenbaum-matrix interpreter (report 004, section 6.1)
fails substitution naturality / HOM at a generic formula metavariable.

Written by the fresh-context critic of report 004 (see 004-source-notes/fresh-critique.md, F1).
Bounded search: it finds a 2-element structure that satisfies the Horn restatement of
p -> (q -> p) (for all values a, b), totality/functionality of F_->, and MP-closure of D,
yet a value of X -> (Y -> X) lies outside D when X is a 2-element (non-singleton) set.

Run with: python3 -I reports/004-checks/matrix_countermodel.py
"""
import itertools
def search(n):
    U=range(n)
    for Fv in itertools.product(U,repeat=n*n):
        F=lambda a,b:Fv[a*n+b]
        # D must contain all K-instances and be MP-closed; take least such D
        D=set(F(a,F(b,a)) for a in U for b in U)
        ch=True
        while ch:
            ch=False
            for a in U:
                for b in U:
                    if a in D and F(a,b) in D and b not in D: D.add(b); ch=True
        for Xs in itertools.product([0,1],repeat=n):
            X={i for i in U if Xs[i]}
            for Ys in itertools.product([0,1],repeat=n):
                Y={i for i in U if Ys[i]}
                for y in X:
                    for u in Y:
                        for v in X:
                            x=F(y,F(u,v))
                            if x not in D:
                                return n,Fv,sorted(D),X,Y,(y,u,v,x)
    return None
for n in (2,3):
    r=search(n); print(n, r)
    if r: break
