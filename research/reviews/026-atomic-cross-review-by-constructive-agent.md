# Task 018 A — Reconstruction of the adversarial atomic submission

**2026-10-14. Review baseline:** `032369a5a03c8eed97d5ad5ca3a58cbf3ff602fe`, branch `research/task017-reciprocal-review`. The mathematical contract remains Task 017 at `f2d7fcb1b00c36fdc4dfc3ab2a3e9ac487f566e7`.

**Verdict on report 024: VALID UNRESOLVED ADVERSARIAL EVIDENCE.** Its closed-name bijections are valid, its copied-name candidate is well typed and E*-equal to identity, and its finite-vector-space interpretation is a sound whole-doctrine model. The compact trace supplies a semantic value, but its displayed syntactic construction lacks the required interfaces. The report correctly stops short of claiming impossibility or a definable separated witness.

**Effect on report 023:** this reconstruction exposes no counterexample to its atomic conclusion and verifies the particular reductions exercised by report 024. It supplies missing worked expansions of the derived hom and the copying construction, and an explicit composition-port alignment. It does not independently certify report 023's entire auxiliary coverage/mutual induction. That broader informal argument remains subject to the reciprocal review bottleneck in 025. No theorem, full SC, pure bridge, or finite-schema claim is promoted here.

## 1. Immutable inputs, evidence, and dispositions

Both submissions were fetched by full SHA and inspected with `git show`, even though neither original report is in the starting review tree:

| Input | Exact pinned commit |
|---|---|
| [Constructive report 023](https://github.com/yzm1/proofbasis/blob/e2cd91095a39e3b63541747fd3e02390e7e92282/research/reviews/023-atomic-endomorphism-constructive.md) | `e2cd91095a39e3b63541747fd3e02390e7e92282` |
| [Adversarial report 024](https://github.com/yzm1/proofbasis/blob/d9a5272f9f31694331beb68f975e73e92436b572/research/reviews/024-atomic-endomorphism-adversarial.md) | `d9a5272f9f31694331beb68f975e73e92436b572` |
| [Corrected report 022](https://github.com/yzm1/proofbasis/blob/024189fdc3a91479c94dbdd7a822e6b12a478b8a/research/reviews/022-pure-bridge-gate.md) | `024189fdc3a91479c94dbdd7a822e6b12a478b8a` |
| Task 018 and coordinator review 025 | `032369a5a03c8eed97d5ad5ca3a58cbf3ff602fe` |

Work used the existing isolated clone `/tmp/proofbasis-atomic-a`, on the new branch `research/atomic-cross-review-constructive`. No rebase, merge, contact with Agent B, reading of its developing review, additional agents, or implementation occurred. Only this review is added; amendments below are proposals, not edits to either original report.

**VERIFIED_SOURCE** means a primary passage was inspected directly at the specified location. **INFERENCE** means the typed reconstruction/model argument here. **UNKNOWN** means an undischarged obligation or unverified literature coverage. Nothing is FORMALIZED; neither agreement nor automated PR review is mechanical certification.

The exact target is `B=A*(∅,{p})`, with the frozen nonlinear terminal/product/hom, linear tensor/cotensor/unit/counit/dual, covariant F/U, `lnlpoly` arities, no nonidentity proof generators, and **full E***. All admissible ambient β/η laws remain available. There is no MIX, self-trace, `FU=id`, unit/counit identification, strict raw double-dual equality, or replacement of p by FX. Write `N(Θ;X)` and `L(Θ|Γ;Δ)` for its two judgments. All repeated linear ports below have distinct names.

| Claim in 024 | Disposition and evidence |
|---|---|
| Atomic source has one class | Correct direct two-leaf axiom-link classification; does not need `N≅T₀`. |
| Atomic linear maps correspond to closed nonlinear names | Correct; both directions and E* inverses reconstructed in §2. |
| Copying a closed identity name is legal | Correct; §3 exhibits the auxiliary templates and the exact nonlinear sharing map. |
| Copied candidate and wrappers cancel | Correct E* calculations; §4 gives the actual primitive reductions and induction changes. |
| FinSet/finite-F₂-vector interpretation satisfies D* | Correct as an informal sound-model argument; expanded in §5. |
| Some model endomorphisms differ from identity | Correct; no syntactic definability or fullness follows. |
| Compact trace would separate a permitted scalar candidate | Correct conditional semantic calculation. No such candidate was supplied; §6 keeps the failed construction separate from impossibility. |
| Neither failed search nor canceled candidate proves the universal atomic statement | Correct. This review preserves that limit. |

## 2. The two bijections, in both directions

Set `H=p*⅋p` and `N=UH`. Let `D_p:L(∅|p*,p;)` be the chosen dual evaluation, with its input order obtained by named exchange from report 023's `L_p(id_p)`. Let `π_H:L(∅|H;p*,p)` be the cotensor universal morphism. Cutting π_H's p* output into D_p's p* input leaves

```text
E : L(∅|H,p_in;p_out).
```

The retained p output comes from π_H, and the retained p input comes from D_p. Shulman Def. 2.10/Prop. 2.16 makes this composite universal in H; it is the derived evaluation for `p⊸p`. This uses the actual chosen raw p*, not a strictified p**.

In report 023's auxiliary rules one may write the same arrow as

```text
D_p = L_p(id_p),                       [with its named input exchange]
E   = ⅋L(D_p,id_p),                    [principal input H=p*⅋p].
```

For a linear map `a:L(Θ|Γ,p_in;Δ,p_out)`, define its transpose

```text
Λ(a) = ⅋R(R_p(a)) : L(Θ|Γ;Δ,H).
```

The output exchange orders the two distinguished outputs as p*_in,p_out before ⅋R; Γ and Δ retain every old named port. Define its inverse on `b:L(Θ|Γ;Δ,H)` by

```text
D(b) = cut_H(b,E) : L(Θ|Γ,p_in;Δ,p_out).
```

Cotensor β followed by dual β gives `DΛ(a)=a`. Conversely, composing `ΛD(b)` and b with the universal E gives the same `D(b)` by that β calculation, so H-η gives `ΛD(b)=b`. Equivalently, use cotensor reconstruction and dual reconstruction successively. These are equations at arbitrary Θ,Γ,Δ in E*, including mixed interiors. They are not existence-only translations.

For the second bijection restrict to **empty linear input and the single H output**, as U requires. With `u_H:L(N|;H)`, define

```text
G(r) = cut_N(r,u_H) : L(Θ|;H)      [r:N(Θ;N)],
Q(b) = U_R(b)      : N(Θ;N)        [b:L(Θ|;H)].
```

The primitive U β/η equations give `GQ(b)=b` and `QG(r)=r`. Thus, at Θ empty,

```text
B_L(∅|p;p)  --Λ-->  B_L(∅|;H)  --Q-->  B_N(∅;N)
             <--D--               <--G--
```

is an isomorphism of E*-class sets. Each map is a target template, so it respects the full congruence. With `n=Λ(id_p)` and `q=Q(n)`, the inverse takes r to `D(G(r))`. It follows directly that `r=q` iff `D(G(r))=id_p`. No classification of all r is implied. U_R is never applied to `id_p` itself: linear transposition removes its input first.

## 3. Translation of the exact copying candidate

Use the auxiliary rule meanings in 023, not an added exponential/trace calculus. Let `σ_z:(z:N)→(z₁:N,z₂:N)` be the structural map whose underlying function sends both target positions to 1. For a two-slot proof T, write `σ_z^*T` for its contraction to the one nonlinear slot z. This action never acts on a linear port.

### Unit and F-on-arrow templates

For a nonlinear map `g:N(X;Y)`, the induced F map is

```text
F(g)=F_L(F_R(g)) : L(∅|FX;FY).
```

A closed linear name b is represented as an I-input arrow by `I_L(b)`; conversely cut `I_R:∅|;I` into that I input. Unit β/η makes these maps inverse.

For the strong-monoidal unit comparison use the concrete template

```text
φ=I_L(F_R(⋆)) : I→F1_N,
φ⁻¹=F_L(T_L(I_R)) : F1_N→I.
```

Their inverse equations are F/terminal/unit β/η: the composite universal morphisms for I and F1_N are the same nullary universal structure. This is a local universal-property comparison, not the pending pure-unit-extension theorem.

Here `q₁=T_L(q):N(s:1_N;N)` is precisely 024's weakening of the closed q. Its `!` notation does not add a nonlinear morphism with empty output. The point `b=F(q₁)φ:I→FN` has the E*-equal auxiliary form

```text
b=I_L(F_R(q)).
```

### Product comparison and nonlinear sharing

Let `d=pair(id_N,id_N):N(z:N;N×N)`. Both premises use the same nonlinear z, as permitted by pairing. For two separately named slots define

```text
T_F = ⊗R(F_R(id_{z₁}), F_R(id_{z₂}))
      : L(z₁:N,z₂:N|;FN⊗FN),
m   = F_L(P_L(T_F)) : F(N×N)→FN⊗FN.
```

This m is the canonical comparison in 024: its composites with the universal F/product maps give T_F. The other direction is obtained by F_R of the two-slot product pairing, F_L on each of its two nonlinear slots, then ⊗L. Product, tensor, and F β/η make these inverse, or equivalently identify their two presentations of the universal `N,N|;F(N×N)`/`FN⊗FN` object. No proof-constant or arbitrary object isomorphism is selected.

Consequently 024's `Δ=m F(d)` has the auxiliary form

```text
Δ = F_L(σ_z^* T_F) : FN→FN⊗FN.
```

Let `ε_H=F_L(U_L(id_H)):FN→H`. Tensor functoriality uses ⊗R followed by ⊗L. Applying it to Δ replaces each `F_R(id_{z_i})` channel by `U_L(id_H)` through F-β. Define

```text
T_U = ⊗R(U_L(id_H)_{z₁},U_L(id_H)_{z₂})
      : L(z₁:N,z₂:N|;H⊗H),
K   = F_L(σ_z^* T_U) : FN→H⊗H.
```

Then the original `a=(ε_H⊗ε_H)Δb:I→H⊗H` is E*-equal to

```text
a = I_L(M_N(q;σ_z^* T_U)).
```

`M_N` here is the explicit simultaneous composite from 023: fresh copies of the nonlinear q fill the chosen slots, followed by the corresponding context action. Since q is closed, both copies have **empty external linear and nonlinear contexts**. Their latent linear identity proofs have already been transposed into the closed H names. The live p input of the final candidate is never duplicated.

### Composition and final evaluation, preserving order

Write `E_g:H_g,p_x→p_mid` and `E_f:H_f,p_mid→p_y`. Their ordinary linear cut gives `v:H_f,H_g,p_x→p_y`. At the auxiliary level its E*-equal form without an explicit cut is

```text
v₀ = ⅋L(D_p,E_f),                    [principal input H_g]
c_B = Λ(v₀) : H_f,H_g→H,
C_B = ⊗L(c_B) : H⊗H→H.
```

All contexts are aligned by named exchanges. This is precisely 024's order `C_B(f,g)(x)=f(g(x))`. The c in 023 §6 was instead defined by `e(h₂,e(h₁,x))`. For general values, translating 024 via that c requires the **swap of its two named H inputs**: `c_B=c_023∘swap`. These arrows are not assumed commutative. Identity on both slots makes their particular closed evaluations agree, but does not license forgetting this port comparison.

The remaining original arrows are

```text
z = C_B a : I→H,
t = (⊗L E) ∘ (z⊗id_p) ∘ λ_p⁻¹ : p→p.
```

The final evaluation has been bundled by ⊗L only to write ordinary unary category composition. `λ_p⁻¹:p→I⊗p` is `⊗R(I_R,id_p)`; its inverse is the tensor factorization of `I_L(id_p)`. Thus the entire candidate is accounted for by explicit auxiliary templates, permitted nonlinear structural maps, and ordinary typed cuts.

## 4. Actual cancellation and induction parameters

All equations in this section are **INFERENCE in E***, independent of the universal conclusion claimed in 023. Use its rank function and let h count each logical/structural rule in a finite auxiliary derivation. Exchanges below may be counted as additional structural nodes; every named commutation still replaces the relevant producer or consumer by a proper premise.

The concrete ranks are

```text
r(p)=0, r(p*)=1, r(H)=2, r(N)=3, r(FN)=4,
r(N×N)=7, r(F(N×N))=8, r(FN⊗FN)=9,
r(H⊗H)=5, r(H⊗p)=3, r(I⊗p)=2,
r(I)=r(1_N)=1, r(F1_N)=2.
```

The lexicographic parameter is `(r,h(producer),h(consumer))`. A lower-rank call can have any height. The following are the calls actually made, rather than an assertion that a general theorem must make them:

| Part of candidate | Equality/rebuilding and parameter change |
|---|---|
| `b=F(q₁)φ` | Move the F1_N cut through φ's I_L: same rank 2, smaller producer height. F_R(⋆)/F_L(F_R(q₁)) then gives a nonlinear cut on 1_N, rank **2→1**. Commute it through F_R to q₁, decreasing consumer height at rank 1. q₁ ends in weakening by its unused terminal slot; deletion removes that slot, or recurses to q at smaller consumer height. Rebuild F_R and I_L, giving `b=I_L(F_R(q))`. |
| `m F(d)` | The producer F_L is nonprincipal for its F(N×N) output; commute through it, decreasing producer height at rank 8. F_R(d)/F_L(P_L(T_F)) gives a nonlinear product cut, **8→7**. Pair/P_L β substitutes the two identity components into the N slots of T_F, **7→3**. Move those substitutions through ⊗R and their F_R premises at smaller consumer heights; nonlinear identity removes them. σ_z shares the two resulting nonlinear contexts. Rebuild F_L to obtain Δ's displayed form. |
| `(ε_H⊗ε_H)Δ` | Move through the producer's F_L and σ_z structural node, decreasing producer height at rank 9. Tensor-R/tensor-L β lowers **9→4** for the two FN channels. Each new cut moves into its corresponding ε_H premise of ⊗R, decreasing consumer height at rank 4. The F_R(id_N)/F_L(U_L(id_H)) pair then lowers **4→3**; nonlinear identity substitution gives U_L(id_H). Rebuild ⊗R, the **same σ_z**, and F_L, yielding K. |
| `K b` | Move through b's I_L at rank 4, with smaller producer height. F_R(q)/F_L(σ_z^*T_U) lowers **4→3**, giving `M_N(q;σ_z^*T_U)`. The nonlinear contraction step selects both preimage slots z₁,z₂ and calls `M_N(q;T_U)` at the same rank and producer height, but strictly smaller consumer height. |
| Two substituted modal channels | Distribute M_N through ⊗R: the two UL premises each have smaller consumer height. In each, `q=U_R(n)` / `U_L(id_H)` β gives a **linear H cut, 3→2**. Its consumer is id_H, so the identity cut law gives n. Rebuild `⊗R(n_f,n_g)` and I_L: `a=I_L(⊗R(n,n))`. No external linear context has been copied. |

The contraction call is simultaneous. Sequential binary substitutions would not justify reusing the old consumer-height bound after the first branch was replaced. Here both selected positions are processed in the proper premise of the contraction, exactly as specified in 023 §4.1.

For an explicit parameter check, put `h_n=h(n)`, retaining whatever named exchange nodes n requires. The two U_L(id_H) premises have height 1, T_U has height 2, and its displayed contraction has height 3. The calls in `M_N(q;σ_z^*T_U)` are therefore

```text
(3,h_n+1,3) → (3,h_n+1,2) → (3,h_n+1,1) → (2,h_n,0).
```

The first two arrows decrease consumer height; the last decreases rank and reaches linear identity. There is no claim that the reconstructed tensor proof must have smaller total height.

For composition v, its explicit p cut has rank 0. Its producer E_g is ⅋L with p output in the identity branch, so commute into that proper producer premise, strictly decreasing producer height. The identity cut law replaces that branch with E_f; rebuilding ⅋L gives v₀. This accounts for the composition macro before applying a cut lemma that expects premises without explicit cuts.

Now `C_B a` first commutes its H⊗H cut through I_L, decreasing producer height at rank 5. Tensor β lowers **5→2**, inserting the two closed n names into the distinct H_f,H_g inputs of `Λ(v₀)`. To expose each evaluation, commute the corresponding H cut through ⅋R and R_p, at rank 2 and fixed producer height, decreasing consumer height twice. The H_g evaluation is the principal ⅋L of v₀; removing it leaves E_f. The H_f evaluation then has the same following primitive expansion, with its current smaller continuation:

```text
cut_H(⅋R(R_p(id_p)), ⅋L(L_p(id_p),id_p))
  = two cuts of R_p(id_p)'s p*,p outputs into L_p(id_p),id_p
  = cut_{p*}(R_p(id_p),L_p(id_p)), followed by the p identity cut
  = cut_p(id_p,id_p), followed by the p identity cut
  = id_p.
```

The first principal par step lowers **2→1 and 0**. The raw-dual step is 023's equation (D), lowering **1→0**. Its snake is one cut of coevaluation and evaluation along p*, leaving one p input and one p output; it is not a self-cut. The remaining rank-0 cuts are unit laws. Rebuilding the **original named** R_p and ⅋R around the resulting `id_p` yields n. Rebuilding I_L gives `z=I_L(n)=n̂`.

Finally, expand `λ_p⁻¹`, tensor functoriality, and the bundled E in t. Tensor β removes the I⊗p bundle at **2→1 and 0**, and the H⊗p bundle at **3→2 and 0**, leaving the unit cut `I_R/I_L(n)` and the distinct H and p cuts. Unit β removes that cut at rank 1; the p identity cuts have rank 0. The remaining H evaluation is exactly the par/dual calculation just displayed, **2→1→0**. Therefore `t=id_p` in E*, not merely in a model.

### The optional modal and nonlinear-hom wrappers

The first wrapper in 024 is `ε_(FN) Fη_N`. Expand `η_N=U_R(F_R(id_N))`, `ε_A=F_L(U_L(id_A))`, and F on arrows as above. After the source F_L commutation, the principal calls have ranks

```text
FUFN: 6  →  UFN: 5  →  FN: 4.
```

They are F β, U β, then linear identity. Rebuild F_L(F_R(id_N)); F reconstruction makes this `id_FN`. For the second wrapper, first expand `Uε_H∘η_N`. Nonlinear cut commutes through the outer U_R, decreasing consumer height. U β gives a linear FN cut **5→4**; F β lowers it to nonlinear N substitution **4→3**. Nonlinear identity leaves u_H, and U reconstruction makes `U_R(u_H)=id_N`. Applying F yields `id_FN`. These are the two adjunction triangles with their actual intermediate types; no `FU=id` is used.

For the nonlinear-hom wrapper, let `k=λ_N(T_L(id_N)):N(1_N;N⇒N)`. Applying it to q₁ uses H_L followed by nonlinear cut on `N⇒N`, and a sharing map from one terminal slot to its two copies. Function β lowers rank **7→3**, followed by identity/weakening substitution, giving q₁. To check source commutation (S) in the relevant linear continuation, before filling that function slot let

```text
b=q₁:N(s:1_N;N),       d=id_N:N(x:N;N),
w=H_L(b,d):N(s:1_N,h:N⇒N;N),
T=T_U:L(z₁:N,z₂:N|;H⊗H).
```

Then the two-slot composite satisfies the **typed** equation

```text
M_N(w;T) = H_L(b, M_N(id_N;T)) : L(s:1_N,h:N⇒N|;H⊗H).
```

On the left the copies (s₁,h₁),(s₂,h₂) are shared by the structural function selecting (s,h) twice. On the right `M_N(id_N;T)` shares z₁,z₂ into the single x slot before applying `ev_N(h,b)`. Expand H_L as nonlinear substitution: associativity and finite-function equivariance equate “insert ev_N(h,b) into each copy” with “insert it into the shared x”. This is an E* equation with a linear continuation, not an endpoints-only diagram. The recursive producer id_N has height 0, strictly less than w, at fixed rank 3; b's height is irrelevant to that recursive call because H_L is rebuilt afterward. Its b contains the nested U_R(n) linear subproof; b nevertheless has no external linear ports. Filling h by k and sharing its extra terminal slot invokes the rank-7 function β case above, and closing the remaining terminal slot discards the weakening. Thus the source-left case and the structural rebuilding also agree with this wrapped construction.

## 5. Whole-doctrine model and separation limits

**INFERENCE.** Use FinSet for nonlinear objects and finite-dimensional F₂-vector spaces for linear objects. Every finite set S has the free vector space `F S=F₂[S]`; U takes underlying finite sets. The natural bijection

```text
Vec(F₂[S],V) ≅ FinSet(S,UV)
```

sends a linear map to its values on basis elements. The basis map `[s,t]↦[s]⊗[t]` makes F strong symmetric monoidal, with `F1_N≅F₂`. Both categories are closed under every chosen type former: function sets of finite sets are finite, underlying sets of finite-F₂-vector spaces are finite, and tensors and duals stay finite-dimensional.

Choose the linear compact closed structure: tensor is the usual tensor, cotensor may be coherently chosen as the same tensor, and I and bottom are both F₂. Evaluation and coevaluation satisfy the finite-dimensional snake equations, with the ordinary canonical double-dual comparison. This is a model choice, not a raw strictness or unit/counit equation imposed on B.

For `S_Θ=∏⟦X_i⟧`, mixed homs are

```text
L(Θ|Γ;Δ)=Vec(F₂[S_Θ]⊗⊗⟦Γ⟧, ⊗⟦Δ⟧),
N(Θ;X)=FinSet(S_Θ,⟦X⟧),
```

where empty linear input/output products use F₂, respectively as I/bottom in this compact model. Nonlinear structural functions act through the corresponding tuple maps S_Θ'→S_Θ; basis-linearizing a diagonal sends `[s]` to `[s]⊗[s]`. Linear exchanges are tensor permutations. Nonlinear cuts are ordinary substitution of finite-set functions. Linear polycategory cut is the usual contraction along one named finite-dimensional port; the same acyclic composition laws supply identities, associativity, interchange and equivariance.

| Chosen universal structure | Check for full E* soundness |
|---|---|
| Nonlinear terminal/product/hom | The usual FinSet bijections and β/η. Contextual product/terminal bijections in a linear judgment also hold through `F(S×T)≅FS⊗FT` and `F1≅I`, matching Prop. 2.11 and its nullary case. |
| Linear tensor/cotensor, both units, dual | The compact closed/polycategorical universal bijections, with all remaining Γ,Δ and the F S_Θ factor retained. Tensor/cotensor β/η and the two snakes hold at these profiles. |
| F-left | Its two homs have isomorphic domains `F(S_Θ×X)⊗⊗Γ` and `F S_Θ⊗F X⊗⊗Γ`, for **any** output list Δ, including empty. The basis/product comparison gives inverse factorization and β/η. |
| U-right | At its exact profile, `Vec(F S_Θ,⟦A⟧)≅FinSet(S_Θ,U⟦A⟧)`, with empty linear input and single A output. It is not an adjunction formula for an arbitrary live linear input. |

Shulman Prop. 3.15(i)–(iii), checked directly, identifies precisely this strong monoidal adjunction with the classical LNL polycategory; adjoining nonlinear homs uses the actual FinSet CCC just checked. Hence the model satisfies the **whole D*** and every frozen structural/principal β/η generator. Additional compact model arrows and equations are permitted semantically; they are not thereby generated in the free syntax.

With `⟦p⟧=V=F₂²`, `⟦H⟧≅End(V)` has dimension 4, `⟦N⟧` has 16 elements, and `⟦FN⟧` has dimension 16. q picks `id_V`. Thus b sends 1 to `[id_V]`, Δ duplicates this basis element, ε_H sends `[h]` to h, a sends 1 to `id_V⊗id_V`, C_B composes the two maps, and t is identity. The opposite composition order in 023 agrees **on this value**. In general a projection P and swap S satisfy `PS≠SP`, so the named input swap in §3 cannot be omitted as an arrow equality.

The model has nonidentity projections, zero, and swaps on V, as well as corresponding constant functions into the underlying set of End(V). Soundness says a definable syntactic t separated from identity here would refute an E* equality. It does not say every one of these model arrows is definable, nor that equal denotations imply E* equality. No fullness/faithfulness claim for the interpretation is needed or established. The witness's cancellation above is syntactic; its equal denotations alone would not have proved it.

## 6. Trace: exact interfaces and the unsuccessful construction

The frozen dual arrows and their allowed bundlings are

```text
coev:∅|;p,p*        →   I→p⅋p*,
ev:∅|p*,p;         →   p*⊗p→bottom.
```

The first bundling is cotensor-right plus I-left; the second is tensor-left plus counit-right. Exchange changes order, not tensor to cotensor or bottom to I. A compact categorical trace of identity instead uses `I→p⊗p*`, swaps the two tensor factors, then uses `p*⊗p→I`. Neither missing map is supplied in report 024.

Directly cutting the raw coev and ev along p* gives `p→p=id_p` by the snake, leaving one named input and one output. Connecting that remaining pair is a self-cut and is not a permitted polycategory rule. Cutting along p first similarly leaves `p*→p*`. This rules out the proposed **direct two-port feedback operation**. It does not prove that all mixed constructions of a scalar are impossible.

Conversely, if the two correctly typed compact interfaces were supplied by permitted terms, the scalar could be assembled by ordinary unary composition through tensor types and symmetry; no new primitive self-trace would then be necessary. This distinction prevents “no self-cut rule” from being misread as a theorem excluding every indirectly constructed compact scalar.

In the compact model, `tr(id_V)=dim(V)=2=0` in F₂. That scalar acts on V as `0_V`, which differs from `id_V` because V is nonzero. Therefore a **definable** scalar with that interpretation would separate the atomic map obtained by tensoring it with p and inserting unitors. But the model's identification of tensor/cotensor and I/bottom supplies semantic interfaces that are unavailable as displayed target terms. Report 024 explicitly leaves open whether some other permitted modal/CCC construction could supply them. Its trace section is a correctly isolated failed construction, not a no-go theorem and not a certified witness.

## 7. Effect on 023 and explicit proposed amendments

The worked copying candidate checks tensor, product, terminal, contraction, F/U, derived-hom, raw-dual, identity and nonprincipal rebuilding cases. It exposes no copied live p, unlicensed promotion, failed rank decrease, or equality requiring a new axiom in these instances. It therefore supports compatibility of the two initial submissions, without turning B's failed witness search into certification of A's universal argument.

Two clarifications should be appended to report 023 if the coordinator later authorizes amendment; they are stated here only:

1. **Expand its derived hom macro:** add `E=⅋L(L_p(id_p),id_p)` and `Λ(a)=⅋R(R_p(a))` with their named exchanges, and the primitive **H→p*→p rank chain** of §4. Explain that the hom-β/η cited in its §6 is derived from these frozen par/dual β/η operations, rather than an additional primitive cut case. Add the copying translation and σ_z map of §3 as a worked mixed instance of its induction.
2. **Retain composition order and qualify the trace remark:** its c has outer second input, whereas 024's C has outer first. Insert the named swap when comparing them; do not infer general commutativity from the identity-name computation. State that the absence of a primitive self-cut blocks direct raw-port feedback, while an indirect scalar using independently derived compact interfaces would still need examination.

These amendments clarify dependencies and interfaces; they do not change the mathematical claim, equality, ledger, or auxiliary rules. The general coverage argument, (S) for arbitrary producers, and exhaustiveness/decrease of all recursive calls remain the exact broader review obligations from 025. This single reconstruction exercises (S) in a linear continuation with a U-derived argument, but cannot substitute for reviewing its general quantifiers. No substantive defect in 023 is certified by this reconstruction, and its atomic argument is not self-approved here.

The strongest opposing argument remains a definable closed r:N unequal to q. The inverse maps in §2 would turn it into a nonidentity atomic endomorphism, defeating 023's claimed lemma. The model contains separated possible values, and arbitrary nested nonlinear homs/U/F remain permitted; the fact that this particular r-like construction cancels does not exclude all such values from the syntactic image. Resolving that universal obligation requires the complete candidate argument to survive independent review, not more untyped semantic examples.

## 8. Direct sources, verification limits, and stopping point

Primary checking in this review used the supplied original texts directly:

| Primary location | Verified content and exact limit |
|---|---|
| Shulman, *LNL polycategories and doctrines of linear logic*, LMCS 19(2:1), 2023, [PDF](https://arxiv.org/pdf/2106.15042), Def. 2.1; Defs. 2.8/2.10/2.14/2.15; Props. 2.9/2.11/2.16, pp. 1:4–12 | VERIFIED_SOURCE: exact structural actions/cuts, ambient universal bijections, contextual nonlinear products, dual/unit boundaries, F/U restrictions, derived hom and strong monoidal comparisons. This supplies the operations and equations used here; it does not classify all closed names. |
| Same, Prop. 3.15(i)–(iii), pp. 1:20–21 | VERIFIED_SOURCE: F determines general linear homs via its symmetric multicategory functor; U exists exactly for the right adjoint; represented products/tensors/units make F strong monoidal, and duals give the star-autonomous classical case. Nonlinear homs are checked separately in FinSet, rather than asserted as a consequence of this proposition alone. |
| Same, §8/Prop. 8.3 and quotient paragraph, pp. 1:45–47 | VERIFIED_SOURCE: finite discrete cone/subterminal/unsorted presentation; surjection of derivations onto completion; structural plus principal β and ambient η quotient. The text explicitly leaves cut elimination for future study. It does not establish 023's new mutual lemma. |
| Shulman, *Star-Autonomous Envelopes and Conservativity*, EPTCS 353, 2021, [PDF](https://arxiv.org/pdf/2004.08487), §10/Thm. 10.1, Cor. 10.6, Remark 10.7, pp. 189–192 | VERIFIED_SOURCE: full faithfulness of the universal **linear** star-autonomous extension preserving designated tensor/cotensor products, and the older internal-hom gluing warning. The theorem does not adjoin this CCC/F/U grammar; no mixed conservativity or pure-unit-identification inference is made here. |

SHA-256 of the inspected LNL PDF: `253d5e39a3eb0c3410a93c8443d3109721d75c80f5ea9f823c6b305e2c8b240e`; envelope PDF: `a91e80c76cf0b211bcf4ad80c4208808c277a9847d1bf8566025ea05e3a8e668`. These hashes were recomputed. I did not undertake a new broad literature sweep or independently certify the full proofs of all seven papers catalogued by the submissions. The finite linear-algebra model/trace calculations and the E* reductions are informal arguments, without a checker artifact.

AGENTS.md, its required documents, Task 017, the canonical plan and operating protocol were read in the original assignment; their content was checked unchanged against this pin. AGENTS, Task 017, the plan/protocol, Task 018, and coordinator 025 were also inspected at this review pin. Both full pinned submissions and the corrected 022 changes were read explicitly. The runtime skill and policy were checked; actual GitHub fetch succeeded with inherited proxy and CA trust. No new environment configuration was required.

The dependency ledger is consequently: exact universal operations/quotient **VERIFIED_SOURCE**; both boundary isomorphisms, candidate cancellation and model soundness **INFERENCE**; definable separated compact trace **not supplied**; whole mutual lemma independently accepted **not established by this review**; pure bridge, pure unit-extension identification and finite-schema extraction **separate pending obligations**. Full SC and unrestricted finite-core universality are outside this conclusion.

The bounded deliverable is complete at the typed reconstruction, explicit cancellation and proposed clarifications above. No original report or canonical document is amended, and no broader theorem task is begun.
