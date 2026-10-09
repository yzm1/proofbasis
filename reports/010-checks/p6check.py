"""Critic-supplied check for report 010 (P6 computations and the P6-prime counterexample without F(1)=top).
Run: python3 -I reports/010-checks/p6check.py"""
import itertools
# K = H3 x 2, elements (i,j) with i in {0,1,2} (0<m<1 coded 0,1,2), j in {0,1}
def imp3(a,b): return 2 if a<=b else b
def imp2(a,b): return 1 if a<=b else b
K=[(i,j) for i in range(3) for j in range(2)]
leq=lambda x,y: x[0]<=y[0] and x[1]<=y[1]
meet=lambda x,y:(min(x[0],y[0]),min(x[1],y[1]))
join=lambda x,y:(max(x[0],y[0]),max(x[1],y[1]))
imp=lambda x,y:(imp3(x[0],y[0]),imp2(x[1],y[1]))
bot=(0,0); top=(2,1)
neg=lambda x: imp(x,bot)
# check residuation
for a,b,c in itertools.product(K,repeat=3):
    assert leq(meet(c,a),b)==leq(c,imp(a,b))
F={0:(1,0),1:(2,0)}
Himp=lambda x,y: 1 if x<=y else y
t=lambda x,y: meet(imp(x,y),neg(neg(y)))
for x,y in itertools.product([0,1],repeat=2):
    assert t(F[x],F[y])==F[Himp(x,y)], (x,y)
    assert meet(F[x],F[y])==F[min(x,y)]
    print(x,y,"F(x=>y)=",F[Himp(x,y)],"Fx=>Fy=",imp(F[x],F[y]), "rel:", meet(imp(F[x],F[y]),F[1]))
# P6 check
B4=[(i,j) for i in range(2) for j in range(2)]
a=(1,0);b=(0,1)
print("a=>0 in B4:", (imp2(1,0),imp2(0,0)))
