# Task 018 B — Independent adversarial reconstruction of the atomic argument

**Verdict: ACCEPT AS INDEPENDENTLY REVIEWED INFORMAL ARGUMENT.** I reconstructed report 023's target templates, its nonlinear source commutations with multiple selected slots, and the mutual explicit-cut/simultaneous-substitution induction. I found no missing selected operation, illegal linear sharing, or nondecreasing recursive call. The resulting equality chain covers every representative at the frozen atomic boundary. This is acceptance of an **informal argument**, not FORMALIZED, an independently refereed theorem, full SC, or acceptance of the broader pure prerequisites.

**Pinned provenance.** Review baseline `032369a5a03c8eed97d5ad5ca3a58cbf3ff602fe`, branch `research/task017-reciprocal-review`; isolated clone `/tmp/proofbasis-atomic-b`, new branch `research/atomic-cross-review-adversarial`. Original constructive report 023: `e2cd91095a39e3b63541747fd3e02390e7e92282`. Original adversarial report 024: `d9a5272f9f31694331beb68f975e73e92436b572`. Corrected report 022: `024189fdc3a91479c94dbdd7a822e6b12a478b8a`. All these pins were fetched and explicitly shown. The mathematical baseline remains `f2d7fcb1b00c36fdc4dfc3ab2a3e9ac487f566e7`.

This is the existing Agent B, using the user-selected gpt-6.1-sol replacement model. I read Task 018 in full, AGENTS.md and its required documents, RESEARCH_PLAN.md, research/OPERATING_PROTOCOL.md, Task 017, both pinned originals, corrected 022's status, and coordinator review 025. There was no rebase, contact with A, reading of A's developing cross-review, additional agent, implementation, broader survey, or change to either original or canonical documents. The expansions below reconstruct the equations and algorithm already claimed in 023; they do not amend its doctrine or impose a new normalization assumption.

## 1. Contract and dispositions

The only final boundary under review is `B_L(∅|p;p)` in `B=A*(∅,{p})`. Its nonlinear objects include terminal, product, nonlinear hom and U of arbitrary generated linear objects; the linear grammar includes p, tensor, cotensor, raw duals, I, bottom and F. Full E* consists of the frozen structural/composition and universal principal β/η equations at all admissible ambient contexts. No MIX, self-trace, strict raw involution, `FU=id`, `I=bottom`, proof irrelevance, proof constants or changed atom map is allowed.

| Claim of pinned 023 | Disposition and decisive reconstruction below |
|---|---|
| Figure 2 representative coverage, §3.4 | Accepted: every chosen projection/inverse factorization has the explicit template in §2, including nullary cases and exact ambient restrictions. |
| Natural inverse factorization (Nat) | Accepted: β of each projection followed by ambient η, with cut at a different named port; §2.3. |
| Nonlinear source equation (S) | Accepted: two selected slots, typed sharing maps, linear continuation and nested U-derived premises expanded in §§3–4. |
| Raw-dual principal equation (D) | Accepted: inverse-to-evaluation construction gives both snakes at raw A,A*, then associativity exposes the single-cut snake; §5. |
| F/U principal equations (M) | Accepted with their stated zone restrictions; §5.2. |
| Mutual cut/substitution induction | Accepted: selection preimages, producer-left rebuilding, principal preprocessing and all principal pairs checked against the stated lexicographic measure; §6. |
| Last-rule classification and E*-equality for every atomic representative | Accepted as informal consequence of that lemma; §7. |
| Full SC/pure bridge/unit-extension/finite-schema certification | Not claimed by 023 and not supplied by this review. |

Here **accepted** means independently reconstructed informal mathematical reasoning. VERIFIED_SOURCE below identifies original passages actually inspected. No proof checker or automated mathematical verification was run.

## 2. Projection and factorization coverage

Write `N(Θ;X)` and `L(Θ|Γ;Δ)` for the two judgment sorts. All list entries have occurrence labels. J means either `N(Θ;Z)` or `L(Θ|Γ;Δ)`; nonlinear precomposition acts on either. An auxiliary rule is a fixed B-template; it may use target cuts. “Without explicit cuts” concerns auxiliary syntax, not literal absence of composition in its interpretation.

### 2.1 Nonlinear chosen operations

Let `W=X×Y`, `K=X⇒Y`. Distinct occurrences are shown by subscripts when needed.

| Target operation and exact boundary | Auxiliary template and reconstruction |
|---|---|
| `π₁:N(W;X)`, `π₂:N(W;Y)` | `P_L` applied to `id_X:N(X,Y;X)` or `id_Y:N(X,Y;Y)` after weakening the unused slot. Its interpretation substitutes π₁,π₂ and shares their W input. |
| Product tuple factorization `a:N(Θ;X), b:N(Θ;Y) ↦ N(Θ;W)` | `pair(a,b)`. Its two composites with πᵢ are a,b by β; product η identifies this template with the prescribed tuple factorization. The same Θ is shared only by nonlinear structural maps. |
| Positive context product `v:N(X,Y;W)` | `pair(id_X,id_Y)` with the required weakenings. Shulman Prop. 2.11(iv) gives `πᵢv=idᵢ` and `v(π₁,π₂)=id_W` with the nonlinear diagonal. |
| Contextual product inverse `d:J(Θ,X,Y) ↦ J(Θ,W)` | `P_L(d)=d[π₁w/x,π₂w/y]`. Cutting with v recovers d by the preceding equations; rebuilding with P_L gives the original W-slot proof. This holds with any retained Γ;Δ in a linear J. |
| Nonlinear terminal projection/pairing `N(∅;1_N)` | `⋆_∅`; with nonlinear ambient Θ, `⋆_Θ` is weakening. For a negative/nullary product presentation there are zero projections and its inverse constructs exactly this unique terminal-output proof. |
| Nullary positive terminal inverse `d:J(Θ) ↦ J(Θ,1_N)` | `T_L(d)`, nonlinear weakening by 1_N. Cutting the closed `⋆_∅` back into that slot recovers d; terminal uniqueness and structural equivariance give the converse. No linear slot is removed. |
| `ev_N:N(K,X;Y)` | `H_L(id_X,id_Y)` with exchange identifying the added K slot with h. In general `H_L(a,d)` is exactly `d[ev_N(h,a)/y]`. |
| Nonlinear hom inverse `d:N(Θ,X;Y) ↦ N(Θ;K)` | `λ_Xd`; hom β/η give the prescribed inverse. There is no hom-right rule with a linear conclusion: admissibility forbids a positive nonlinear output in a profile containing linear objects. Evaluation can nevertheless be substituted into a nonlinear slot of a linear J. |

This checks both product presentations without assuming product-left on linear J as a new universal property: it is the explicit substitution template justified by the product equations. The nullary case is likewise nonlinear weakening, not a linear deletion permission.

### 2.2 Linear operations and modalities

Let `κ:A,B→A⊗B`, `π:A⅋B→A,B`, `i:→I`, `o:bottom→`, `e_A:A,A*→`, `f_X:X|;FX`, and `u_A:UA|;A` be the designated universal morphisms.

| Target primitive / inverse | Auxiliary template; ambient boundary |
|---|---|
| κ | `⊗R(id_A,id_B):L(∅|A,B;A⊗B)`; its interpretation cuts two identities into κ. |
| Inverse through κ | `⊗L(d):L(Θ|Γ,A⊗B;Δ)` from `d:L(Θ|Γ,A,B;Δ)`. |
| π | `⅋L(id_A,id_B):L(∅|A⅋B;A,B)`. |
| Inverse through π | `⅋R(d):L(Θ|Γ;Δ,A⅋B)` from `d:L(Θ|Γ;Δ,A,B)`. |
| i / inverse through i | `IR:L(∅|;I)`; `IL(d):L(Θ|Γ,I;Δ)` from `d:L(Θ|Γ;Δ)`. Γ or Δ may be empty. |
| o / inverse through o | `bottomL:L(∅|bottom;)`; `bottomR(d):L(Θ|Γ;Δ,bottom)` from `d:L(Θ|Γ;Δ)`. No I/bottom conversion is present. |
| e_A / inverse in its A* slot | `L_A(id_A):L(∅|A,A*;)`; `R_A(d):L(Θ|Γ;Δ,A*)` from `d:L(Θ|Γ,A;Δ)`. Definitions and snakes are reconstructed in §5. |
| Corresponding coevaluation `c_A:→A,A*` / its inverse | `R_A(id_A)`; `L_A(q):L(Θ|Γ,A*;Δ)` from `q:L(Θ|Γ;Δ,A)`. It is derived from e_A, not an independent choice. |
| f_X | `F_R(id_X):L(X|;FX)`. More generally `F_R(a)` from `a:N(Θ;X)` has no other linear ports. |
| Inverse through f_X | `F_L(d):L(Θ|Γ,FX;Δ)` from `d:L(Θ,X|Γ;Δ)`, for arbitrary linear Γ;Δ. |
| u_A | `U_L(id_A):L(UA|;A)`; generally U_L cuts u_A into q's one selected A input and retains q's other linear ports. |
| Inverse through u_A | `U_R(c):N(Θ;UA)` from `c:L(Θ|;A)` only: empty linear input, single A output. |

Binary rule templates attach the two independent premises through κ or π. They do not juxtapose unrelated proofs by MIX. Nested constructors simply instantiate this list recursively; no type-height restriction is imposed. Identities, both cuts and all structural actions translate directly. Since the initial generator ledger has no nonidentity arrows, Figure 2c adds no unlisted operation.

If an inverse rotation at the other raw dual port is expressed using A**, expand the canonical comparisons into these templates and cuts. For example the two maps at raw types

```text
A→A** : R_(A*)(L_A(id_A)),
A**→A : L_(A*)(R_A(id_A))
```

are typed without equating their objects. Their inverseness follows from the snakes. Thus a syntactically convenient boundary comparison adds no residual opaque constructor that could escape the cut lemma.

### 2.3 Ambient naturality is an equality, not a boundary comparison

For an inverse factorization Vψ and a cut C at a different free port, compare `C(Vψd)` with `Vψ(Cd)`. Cut both with ψ. Principal β gives Cd on each side after associativity/interchange. Ambient η therefore equates them. For a multi-projection product cone this is done for each πᵢ and then its tuple η is used. For structural actions, equivariance gives the same argument. Bound variables are renamed before applying C.

For H_L, U_L and rules defined by composition rather than inverse factorization, associativity/interchange proves the analogous equation directly. In particular, commuting nonlinear precomposition into a linear continuation does not invoke an inadmissible nonlinear-hom transpose of a linear judgment. Pairing naturality follows by its projection β and product η. These are exactly the operations needed when rebuilding nonprincipal rules in §6.

## 3. Equation (S) with two slots, sharing maps and a linear continuation

A sharing map is written `sh_E:(Λ,E)→(Λ,E¹,E²)` in the context-action convention of Shulman Def. 2.1: its underlying function sends each copied position eⁱ to its corresponding position e and fixes Λ. The induced action is contravariant on proofs. It touches only nonlinear positions; the identity permutations retain all named Γ;Δ.

Take

```text
b:N(Ξ;D),       d:N(Υ,y:Y;X),
v=ev_N(h,b):N(Ξ,h:D⇒Y;Y),
a=H_L(b,d)=d[v/y]:N(Ξ,Υ,h:D⇒Y;X),
q:L(Λ,x₁:X,x₂:X|Γ;Δ).
```

All contexts are first renamed apart. Put E=(Ξ,Υ,h), R=(Υ,y). The two-slot simultaneous composites have types

```text
M_X(a;q) : L(Λ,Ξ,Υ,h|Γ;Δ),
M_X(d;q) : L(Λ,Υ,y|Γ;Δ).
```

On the unshared contexts, write `q[d¹/x₁,d²/x₂]` for two ordinary nonlinear cuts. Expanding a on each occurrence gives the E*-chain

```text
M_X(a;q)
 = sh_E* q[d¹[v¹/y¹]/x₁, d²[v²/y²]/x₂]
 = sh_E* (q[d¹/x₁,d²/x₂])[v¹/y¹,v²/y²]
 = (sh_R* q[d¹/x₁,d²/x₂])[v/y]
 = H_L(b,M_X(d;q)).
```

The second equality is nonlinear cut associativity and interchange: no new universal law is needed. For the third, equivariance moves sharing across the two substitutions. Explicitly, on the left both Ξ¹,Ξ² are mapped to Ξ, both Υ¹,Υ² to Υ and h¹,h² to h; on the right Υ¹,Υ² map to Υ and y¹,y² map to y, then substituting v once supplies Ξ,h. The two resulting nonlinear context substitutions agree position by position. Equivariance of nonlinear cut and its interchange with structural actions give the third equality; merely having the same endpoints would not suffice. This equivariance applies equally to a linear q. There is exactly one Γ;Δ block at every line: neither q nor an external linear port is duplicated. This is the claimed (S), with its named exchange alignment, for two genuine selected occurrences. The same finite function sends any finite number of copies to their original positions.

### 3.1 A concrete nested-U instance in the frozen atom grammar

To check that the argument is not tacitly assuming producers have modal-free syntax, let

```text
H=p*⅋p,        N=UH,        S=U(FN).
```

Define the following auxiliary proofs without explicit cuts:

```text
u=U_L(id_H)                      : L(N|;H),
ε=F_L(u)                         : L(∅|FN;H),
b=U_R(U_L(ε))                    : N(s:S;N),
j=U_R(U_L(id_H))                  : N(y:N;N).
```

Each U_R premise has empty linear input and exactly H as output. The nested construction b uses U of F of U of a derived linear hom; j uses U-right after U-left, so it is not treated as a syntactic nonlinear atom identity. U-η does identify j with id_N, but that simplification is unnecessary for (S).

Take

```text
d=H_L(id_N,j) : N(k:N⇒N,y:N;N),
a=H_L(b,d)    : N(s:S,k:N⇒N,h:N⇒N;N).
```

Let `e:H,p→p` be the derived evaluation. It has the explicit cut-free auxiliary template `⅋L(L_p(id_p),id_p)` with exchange. Let `c:H₁,H₂,p→p` apply the H₂ function first and H₁ second. Its cut-free auxiliary template is another `⅋L`, using `L_p(e)` as its p* branch and `id_p` as its p branch, with H₂ in the former branch. Therefore

```text
q=U_L(U_L(c)) : L(z₁:N,z₂:N|p;p)
```

is a permitted linear continuation with two selected nonlinear slots and a single named linear input/output. The general chain above gives

```text
M_N(a;q)=H_L(b,M_N(d;q)) : L(s:S,k:N⇒N,h:N⇒N|p;p).
```

Its sharing function identifies `(s¹,k¹,h¹,s²,k²,h²)` with `(s,k,h)`. On the other side it identifies `(k¹,y¹,k²,y²)` with `(k,y)` before substituting v(h,s). Expanding U_L inside q gives two occurrences of dereferencing the same resulting N-value and two sequential evaluations on the one p port. Nonlinear-cut associativity and sharing, not linear copying, equate these expansions. This instance checks exactly the linear/nested-U source commutation requested by the task.

## 4. Product-left source commutation, also with two slots

Take

```text
d:N(Υ,y:Y,z:Z;X),       W=Y×Z,
a=P_L(d)=d[π₁w/y,π₂w/z]:N(Υ,w:W;X),
q:L(Λ,x₁:X,x₂:X|Γ;Δ).
```

Share E=(Υ,w) on the left and R=(Υ,y,z) on the right. Its explicit E*-chain is

```text
M_X(P_Ld;q)
 = sh_E* q[d¹[π₁w¹,π₂w¹]/x₁,d²[π₁w²,π₂w²]/x₂]
 = sh_E* (q[d¹/x₁,d²/x₂])[π₁w¹,π₂w¹,π₁w²,π₂w²]
 = (sh_R* q[d¹/x₁,d²/x₂])[π₁w/y,π₂w/z]
 = P_L(M_X(d;q)).
```

The underlying sharing functions map Υ¹,Υ² to Υ and w¹,w² to w on the left; on the right they map Υ¹,Υ² to Υ, y¹,y² to y and z¹,z² to z. Substitution of the two projections makes those context maps agree. The middle steps use associativity and structural equivariance; product β/η ensures P_L is the fixed contextual inverse rather than a new rule.

A concrete frozen instance reuses N=UH, j and the linear q from §3.1. Take

```text
k:(N×N)⇒N,
d=H_L(pair(id_N,id_N),j):N(k,y:N,z:N;N),
a=P_Ld:N(k,w:N×N;N).
```

In the pairing premise the two identities are weakened to the common `(y,z)` context, so it returns `(y,z)`, not `(y,y)`. Then

```text
M_N(a;q)=P_L(M_N(d;q)):L(k,w:N×N|p;p).
```

The output of j remains the explicitly U-derived subproof from §3.1. Both sides feed `j(k(π₁w,π₂w))` into each nonlinear slot of q. The sharing maps are respectively `(k¹,w¹,k²,w²)↦(k,w)` and `(k¹,y¹,z¹,k²,y²,z²)↦(k,y,z)` before the projection substitutions. The lone p occurrence is untouched. The terminal-source analogue replaces these projection substitutions by nonlinear deletion and follows from the same equivariance law.

## 5. Raw duals and modal principal equations

### 5.1 Both snakes follow from inverse factorization at raw A,A*

Start with the chosen `e_A:L(∅|A,A*;)`, universal in A*. Define `R_A(d)` by its prescribed inverse factorization, so

```text
cut_(A*)(R_A(d),e_A)=d,
R_A(cut_(A*)(z,e_A))=z
```

at the appropriate remaining ambient ports. Put `c_A=R_A(id_A):L(∅|;A,A*)`. Define `L_A(q)=cut_A(q,e_A)`; q's output A becomes e_A's input A, leaving input A*.

The first displayed β gives the A snake `cut_(A*)(c_A,e_A)=id_A`. Now cutting `cut_A(c_A,d)` with e_A on A* yields d by this snake and associativity/interchange; η therefore gives the useful explicit expression `R_A(d)=cut_A(c_A,d)`. Finally `R_A(L_A(q))=q` is the second displayed reconstruction equation, yielding the A* snake on taking `q=id_(A*)`. Also `L_A(R_A(d))=d` is β. These comparisons occur between two separate arrows along one port. Neither snake performs a second self-cut or identifies A** with A.

For `d:L(Θ|Γ,A;Δ)` and `q:L(Υ|Σ;Π,A)`, expanding the rotations gives

```text
cut_(A*)(R_A(d),L_A(q))
 = cut_(A*)(cut_A(c_A,d),cut_A(q,e_A))
 = cut_A(q,d) : L(Θ,Υ|Γ,Σ;Δ,Π),
```

after the named exchange of ambient contexts. Associativity/interchange exposes the A snake while retaining d and q's other ports. This is (D) at raw A,A*, and the replacement type A has strictly smaller rank than A*. It remains valid if A itself is an iterated raw dual or contains modalities/units.

### 5.2 Modal equations retain all their zone restrictions

For `a:N(Θ;X)` and `d:L(Υ,X|Γ;Δ)`,

```text
cut_(FX)(F_R(a),F_L(d))=d[a/x]:L(Θ,Υ|Γ;Δ).
```

Expand F_R as substitution into f_X and F_L as inverse factorization through f_X. F-β removes that factorization after associativity. The replacement is a nonlinear substitution at the smaller type X; a has no external linear ports.

For `c:L(Θ|;A)` and `q:L(Υ|Γ,A;Δ)`,

```text
cut_(UA)(U_R(c),U_L(q))=cut_A(c,q):L(Θ,Υ|Γ;Δ).
```

U_L is q composed with u_A; substituting U_R(c) into u_A recovers c by U-β. The lower-rank linear cut retains exactly Γ;Δ. Duplicated nonlinear U_R(c) values can contain copies of closed linear subproofs, but c has no external linear input to copy. These formulas do not hold with `c=id_p`, whose linear input p makes U_R inadmissible. No equation ε⁻¹ or `FU=id` has been introduced.

## 6. Reconstruction of the mutual induction, including all principal cases

Use the original rank and height definitions, and induct on

```text
(r(T), h(a), h(q)).
```

There are two clauses: a single named linear cut at T, and a nonlinear simultaneous replacement of a finite chosen family S of T-slots by `a:N(Θ;T)`, with final sharing of Θ. Selection cardinality is deliberately **not** an induction coordinate: taking contraction preimages may increase it while decreasing consumer height. Source and continuation variables are renamed apart before substitution.

### 6.1 Structural, source-left and nonprincipal calls

| Case | Exact recursive input and strict decrease / retained resources |
|---|---|
| Identity | Linear cut removes identity; nonlinear substitution into the one selected identity returns a, with named renaming. No recursive call. |
| Zero selected slots | Return q weakened by Θ. Deletion concerns only nonlinear inputs; Γ;Δ remains unchanged. |
| Nullary consumer with nonlinear ambient context | Expand `⋆_Υ`, nonlinear-weakened IR or nonlinear-weakened bottomL as a structural action on its empty-nonlinear-context base. Its selected-slot preimage is empty, so the preceding cases return the same base with the final context weakening. No recursive premise or hidden linear deletion is required. |
| Consumer structural action `q=σ* q₀` | Select every q₀-slot whose σ-image lies in S, including all preimages of contraction. Recurse `(T,a,q₀,S₀)`, then rebuild the appropriate sharing/permutation. Rank and producer height fixed; `h(q₀)<h(q)`. A selected linear port has exactly one preimage because its action is a permutation. |
| Producer structural action `a=τ* a₀` | Recurse on a₀, transport its external context action after substitution/cut. `h(a₀)<h(a)`. Nonlinear duplication of its context is legal; linear actions are permutations. |
| Nonprincipal nonlinear consumer rule | Recurse on each proper premise carrying preimages of S; share Θ across nonlinear premise blocks after rebuilding. Every such premise has smaller q height. Linear argument premises cannot be duplicated: arguments of H_L and F_R are nonlinear; U_R has one linear premise traversed once. |
| Nonprincipal linear consumer rule | Recurse into the unique premise containing the selected linear input, rebuild other premises once. Linear contexts split in the binary rules; consumer height decreases. |
| Nonprincipal linear producer rule | Recurse into its unique premise containing the selected output and rebuild. Producer height decreases; all other linear ports and the other binary premise are retained once. |
| Nonlinear producer P_L/T_L/H_L | Recurse `M_T(d;q,S)` on its proper continuation d, then rebuild that same nonlinear left rule at J. Producer height strictly decreases. §§3–4 prove the equalities for multiple S. For H_L(b,d), b is retained as a logical-rule premise; **no recursive cut on b's possibly larger argument type is introduced**. |

Rebuilt auxiliary logical rules may have B-templates containing cuts. That does not reintroduce an **explicit auxiliary cut**, and is the exact distinction made in report 023. Height growth in the recursive result is harmless: at this stage it is rebuilt, not fed into a same-rank call justified by an obsolete height bound.

These cases cover every source-left output producer. For example the concrete a from §3.1 has height `1+max(h(b),h(d))`; the call uses d, whose height is strictly smaller even if b is taller than d. The consumer q is unchanged. The two-slot cardinality and sharing are preserved in the occurrence annotation, not paid for by an invalid binary-cut height argument.

### 6.2 Principal preprocessing and complete rank ledger

After structural/source-left/nonprincipal steps, the selected principal consumer is a matching left rule. For nonlinear substitution it has one distinguished principal selected occurrence s₀ and may have other selected occurrences S'. Before using β, process S' in each **proper original premise** of the consumer, leaving s₀ and the newly exposed component/bound slots unselected. Those calls have `(r(T),h(a),h(q_i))` with `h(q_i)<h(q)`. They produce cut-free premises of possibly larger height. The remaining principal cuts have types strictly below T, so that growth does not invalidate the next recursive call. External copies of Θ are finally shared by the annotated finite functions.

| Principal pair and original T | Replacement cuts/substitutions; measure and exact boundary check |
|---|---|
| Nonlinear pair `(a_X,a_Y)` / P_L, T=X×Y | Substitute a_X into all exposed X-slots and a_Y into all exposed Y-slots of the preprocessed continuation. Each rank is `<r(T)`. Share their common Θ nonlinearly. A linear continuation's Γ;Δ is traversed once, not paired with a copy. |
| Nonlinear `λ_Xd` / H_L(b,q₀), T=X⇒Y | First preprocess S' in b and q₀ at original rank with smaller consumer heights. Hom-β replaces the principal step by substitution of b' into d's bound X slot, followed by substitution of its Y-result into q₀'. Both ranks X,Y are `<r(T)`. H_L's argument is nonlinear; no linear boundary is copied. |
| Nonlinear ⋆ / T_L or deletion, T=1_N | Remove the distinguished unused slot and weaken in the producer's nonlinear Θ; other slots were preprocessed below the original consumer root. No remaining recursive call or linear deletion. |
| U_R(c) / U_L(q₀), T=UA | Preprocess S' below U_L, then use the single linear A-cut in §5.2; `r(A)<r(UA)`. c has no linear input and one output. Its lower-rank cut into q₀' retains q₀'s Γ;Δ. |
| ⊗R(a,b) / ⊗L(q₀), T=A⊗B | Tensor β yields q₀ with distinct A,B inputs. Cut a's named A output into the A input, then b's B output into the still named B input. Each type has smaller rank. After the first cut its result may be taller; the second rank is still below T. Retained Γ_a,Γ_b,Γ_q and Δ_a,Δ_b,Δ_q each occur once. |
| ⅋R(d) / ⅋L(a,b), T=A⅋B | Cotensor β yields d's distinct A,B outputs. Cut output A into a, then the remaining B output into the separate b proof. Both types are smaller; the second cut is not a self-cut. Context/output blocks from d,a,b are each retained once. |
| IR / IL(q₀), T=I | Unit β returns q₀, with optional nonlinear weakening. IR has empty input and a single I output, so no other linear port disappears. |
| bottomR(d) / bottomL, T=bottom | Counit β returns d, retaining all its other input/output ports. bottomL has exactly one input and no output. Only optional nonlinear context is weakened. |
| R_A(d) / L_A(q₀), T=A* | (D) gives cut_A(q₀,d). Swapping producer/consumer heights is allowed because `r(A)<r(A*)`. All other ports are retained by the displayed equation in §5.1. |
| F_R(a) / F_L(q₀), T=FX | F-β gives nonlinear substitution at X into q₀. `r(X)<r(FX)`; a has no external linear ports. Any contraction of that X slot is handled by the simultaneous nonlinear clause. |

These are all the principal combinations in the auxiliary rule list. A nonlinear identity producer and non-introducing producer have already been handled. There is no separate nonlinear hom right rule for linear J, no additional nonlinear atom elimination, and no additive rule. If the principal object is introduced only after a structural contraction, pulling back S first separates its individual named preimages; the preceding preprocessing applies to that separated family.

For a linear binary reduction the two component cuts are sequential lower-rank calls, not repeated calls at the original type with an assumed unchanged height. For a nonlinear principal reduction the copies of an introduced component are consumed simultaneously by the nonlinear clause. Neither construction requires a linear multi-substitution or imports MIX.

Thus every recursive call either lowers type rank, keeps rank and lowers producer height, or keeps both and lowers consumer height. Each step is an E* equation from §§2–5, structural laws or the listed principal β. This checks the well-foundedness and the equality claim, rather than merely observing that cut admissibility is plausible in a neighboring calculus.

## 7. Every atomic representative and its class

Shulman §8 Prop. 8.3 supplies a finite representative built from the selected projections, inverse factorizations, identities, cuts and structural actions. §2 supplies an auxiliary derivation with the **same B-interpretation** for each such generator. Replacement at inverse factorizations is justified by the appropriate β/η equations at its actual ambient profile, so this is equality in E* rather than recompilation at the same boundary.

Induct on the resulting auxiliary derivation: replace proper premises by equal derivations without explicit cuts; at a cut root use the mutual lemma of §6; at a logical/structural root rebuild. The result remains at `L(∅|p;p)`. A structural action concluding empty nonlinear context cannot have a premise with a nonempty nonlinear context: there is no function from a nonempty list of premise positions to the empty list of conclusion positions. Linear actions here are only the identity on each single port. Strip those vacuous actions.

Every nonlinear left rule or U_L would leave a nonlinear assumption; F_L leaves an FX input and F_R an FX output; multiplicative/unit/dual rules leave their syntactically compound principal type at a linear input or output. Nonlinear right rules and U_R conclude the other judgment sort. None has conclusion `∅|p;p`. The remaining rule is exactly linear identity on p.

This establishes, on the independently reviewed informal argument, `t=id_p` in E* for **every** permitted representative. Nested nonlinear homs, products, U/F, both units and raw duals were neither forbidden nor deleted from the representative quantifier. The auxiliary rule templates can use target composition; that does not weaken the final equality conclusion. No class decoder, confluence, strong normalization, subformula theorem or equality decision procedure is needed: each chosen representative has its own finite equality chain to the same id_p.

## 8. Reconciliation with report 024

The closed-name bijections in pinned 024 are valid:

```text
B_L(∅|p;p) ≅ B_L(∅|;p*⅋p) ≅ B_N(∅;U(p*⅋p)).
```

Their first inverse is evaluation composed with the linear name; their second inverse is substitution into u_H. Both reconstruct by the corresponding β/η. Therefore the reviewed atomic argument implies that every definable closed name is equal to the named identity. This supplies the positive evidence my earlier witness search did not supply; it does not retroactively make that search a proof.

The copied-name construction from 024 expands into nonlinear substitution into two U_L slots of a linear continuation, precisely the kind checked in §3.1. Its cancellations by product/modal/hom equations remain correct. The sound FinSet/F₂-vector-space model interprets its closed name as the element id_V, copies the basis vector `[id_V]`, then derelicts/composes two identities. Other matrices in End(V) remain model arrows. Choosing one does not make it a definable proof of the frozen grammar.

The compact trace suggestion still lacks an exhibited B-term: the frozen dual maps bundle as `I→p⅋p*` and `p*⊗p→bottom`, whereas the compact scalar route wants tensor coevaluation and I-valued evaluation or feedback. My earlier report did not prove those individual interfaces impossible; it identified the failed construction. A **definable** term with separated atomic interpretation would contradict the reviewed cut lemma and require locating its failed case. No such term is supplied by the arbitrary compact-model maps. This review is a reconstruction of A's argument, not another finite witness search.

## 9. Primary-source verification, strongest objection and limits

I directly re-inspected the supplied published Shulman text, *LNL polycategories and doctrines of linear logic*, LMCS 19(2:1), 2023, [primary PDF](https://arxiv.org/pdf/2106.15042):

- Def. 2.1, pp. 1:4–5: the two cuts, contravariant nonlinear finite-function actions and linear permutations; these license the explicit sharing/equivariance chains.
- Defs. 2.8/2.10/2.14/2.15 and Props. 2.9/2.11/2.16, pp. 1:8–12: exact universal bijections, dual evaluation/coevaluation, contextual product equivalence, modality zone restrictions and hom definitions. In particular Prop. 2.11(i) includes linear ambient contexts, and Def. 2.15's nonlinear hom inverse has a nonlinear output.
- Def. 4.1, p. 1:24: a signed profile has at most one positive nonlinear object; if present there are no linear objects. This rules out an illicit U-right or nonlinear-hom transpose with retained linear ports.
- §8 assumptions, Figure 2, Prop. 8.3 and following quotient paragraph, pp. 1:43–47: unsorted doctrine, subterminal base and finite discrete cones; representation surjectivity, structural laws, principal β, and ambient η. The paper explicitly leaves cut elimination for future study. It is not a published theorem of the auxiliary lemma reconstructed here.

The inspected PDF SHA-256 is `253d5e39a3eb0c3410a93c8443d3109721d75c80f5ea9f823c6b305e2c8b240e`. Statement numbering and hypotheses were checked against that copy, not inherited from the reports. These passages and the informal calculations above are the decisive dependencies. The broader envelope, semi-star-autonomous net, and Hasegawa fullness statements reviewed in the original work have different hypotheses/targets/translations and are not imported as an unexamined mixed conservativity theorem here. No new exhaustive prior-art claim or novelty claim is made; their whole proofs were not independently certified in this review.

The strongest objection was that §4 of 023 might conceal a nondecreasing recursion after duplicating a producer, or rebuild a nonlinear source elimination as a linear copying operation. A simple binary-cut induction would indeed fail that audit. The occurrence-preimage construction, equations (S) with the displayed sharing maps, and same-rank calls on proper original premises resolve that objection for the submitted algorithm. Producer-left rebuilding retains a logical rule rather than recursively cutting at its possibly larger argument type; lower-rank principal calls allow the rebuilt heights to grow. Raw-dual principal reduction decreases rank before reversing producer/consumer roles. These checks are why I accept the argument rather than count agreement or a failed witness search as certification.

| Dependency / scope obligation | Review status |
|---|---|
| Frozen D*/E* and empty proof ledger | Preserved; exact selected operations audited. |
| Shulman representative/quotient and universal definitions | VERIFIED_SOURCE for the stated version/hypotheses. |
| Target-to-auxiliary equality, (Nat), two-slot (S), dual/modal β/η, induction and last-rule classification | Independently reconstructed **INFERENCE**, detailed above. |
| Closed-name reformulation and cancelled witness in 024 | Compatible, independently checked at the required typing/equality level. |
| Certified negative witness / typed falsifier | None. A future definable separated term would challenge the lemma. |
| Corrected 022 pure bridge and unit-extension identification | Not assumed; remain separately pending verification. |
| Finite-schema extraction, full SC, all pure boundaries | Not accepted or established by this bounded atomic review. |
| Mechanical checking, independent referee certification, exhaustive literature resolution | Absent. No FORMALIZED or novelty assertion. |

The bounded review ends here. The outcome supports acceptance of the submitted atomic informal argument as independently reviewed evidence, while preserving both original submissions and the broader pending obligations. It neither certifies a universal finite core nor converts auxiliary cut elimination into source equality reflection or full SC.
