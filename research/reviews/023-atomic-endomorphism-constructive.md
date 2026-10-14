# Task 017 A — Constructive atomic-endomorphism test

**2026-10-14. Frozen baseline:** `f2d7fcb1b00c36fdc4dfc3ab2a3e9ac487f566e7`, on `research/task016-pure-bridge-gate`. Independent constructive assignment, performed in an isolated clone on `research/atomic-endomorphism-constructive`. No consultation with the adversarial investigator, reading of its developing work, additional agents, implementation, or changes to frozen documents.

**Verdict: INFORMAL POSITIVE ARGUMENT.** The argument below gives an equality-preserving elimination of explicit cuts in an auxiliary, typed sequent presentation of the stipulated operations. At the exact boundary `∅ | p ; p`, a derivation without explicit cuts has only the identity rule available. Consequently every representative at this boundary is E*-equal to `id_p`. The argument is informal and has not been mechanically checked or independently certified. It does **not** establish full SC, the pure-net bridge, the identification of the pure unit extension, or the finite-schema clause.

Evidence labels: **VERIFIED_SOURCE** means I inspected the indicated primary statement, hypotheses, and relevant surrounding text in this investigation; it does not certify its entire published proof. **INFERENCE** labels the argument here. **UNKNOWN** marks literature coverage or an unverified broader obligation. Nothing is FORMALIZED. No novelty claim is made.

## 1. Exact question and coverage

Let `B=A*(∅,{p})` be the frozen free D*-structure, with no nonidentity generating proof arrows. The tested statement is

```text
∀ t ∈ B_L(∅ | p ; p),   t = id_p in E*.
```

The mutually generated object grammar is

```text
X ::= 1_N | X × X | X ⇒ X | U A
A ::= p | I | ⊥ | A ⊗ A | A ⅋ A | A* | F X.
```

There are no declared nonlinear atoms, but there are arbitrarily nested nonlinear objects and proofs. The arity base is `lnlpoly`. Write `N(Θ;X)` for a nonlinear judgment and `L(Θ|Γ;Δ)` for a linear judgment. Θ supports finite-function actions, including contraction and weakening; Γ and Δ support only permutations. Each displayed linear port is a distinct occurrence, even when two ports have the same type.

E* is the **entire** frozen congruence: the LNL structural/composition laws and the principal universal β/η laws in Shulman 2023 §8, at every admissible ambient profile. No MIX, `FU=id`, identification of I with ⊥, proof irrelevance, strict raw double-dual equation, proof constants, or imported equality is used. The atom stays `p`, rather than `FX`.

The source at this atomic boundary is independently a singleton: the forest `p^⊥,p` has only its one atomic axiom link, and the unit-free no-MIX sequent rules introduce no connective at this conclusion. This fact does not depend on report 022's proposed `N≅T₀` comparison.

An arbitrary target class is covered because Shulman §8 Proposition 8.3 supplies a representative using identities, cuts, structural actions, the selected projections, and inverse factorizations. Section 3 translates **every one of those operations**, at arbitrary contexts, into the auxiliary presentation. Section 4 handles both kinds of cut. This includes nested nonlinear homs, U of arbitrary linear types, F of arbitrary nonlinear types, raw iterated duals, and both linear units. There is no premise that the representative already has a pure interior.

## 2. Direct primary-source audit

The prior Task 016 PDFs and text extracts were read directly as public source material; older report labels were not substituted for theorem statements. The source versions are recorded at the end of this report.

| Primary passage inspected | Exact hypothesis and conclusion relevant here | Applicability and limitation |
|---|---|---|
| Shulman, *LNL polycategories and doctrines of linear logic*, LMCS 19(2:1), 2023, Defs. 2.1, 2.8, 2.10, 2.14–2.15; Props. 2.9, 2.11–2.12, 2.16, 3.15; Thm. 7.4; §8/Figure 2/Prop. 8.3 and following quotient paragraph, pp. 1:43–47. [Primary PDF](https://arxiv.org/pdf/2106.15042) | Def. 2.1 specifies the two judgments, the two cuts, nonlinear finite-function actions, and linear permutations. The chosen operations are universal morphisms with the displayed hom-set bijections. Prop. 2.11 equates nonlinear product projections with a context-universal product pairing, including linear ambient contexts. Thm. 7.4 assumes a **small** doctrine/sketch and gives a free completion with a surjective-equivalence universal property using invertible 2-cells. §8 restricts to unsorted doctrines with subterminal base and finite discrete cones; Prop. 8.3 supplies derivations of every morphism and the following paragraph specifies the full quotient. | **VERIFIED_SOURCE.** This is the presentation/existence input. It does not itself prove mixed conservativity. On p. 1:45 the author explicitly leaves cut elimination for future study. The cut argument in §4 below is supplied here for the selected grammar, rather than attributed to this theorem. |
| Shulman, *Star-Autonomous Envelopes and Conservativity*, EPTCS 353, 2021, §6; §10/Thm. 10.1, Cor. 10.6, Remark 10.7, pp. 189–192. [Primary PDF](https://arxiv.org/pdf/2004.08487) | A small symmetric polycategory P with designated existing tensor/cotensor products J has a fully faithful **universal** extension to a star-autonomous category preserving J up to isomorphism. Cor. 10.6 is the closed symmetric monoidal specialization. Remark 10.7 identifies an internal-hom preservation gap in an older ordinary-presheaf double-gluing argument. | **VERIFIED_SOURCE.** No nonlinear CCC sort or F/U adjunction appears in the universal extension being quantified over. This theorem is not an atomic theorem about B. No gluing lift is assumed here. |
| Hasegawa, *Categorical glueing and logical predicates for models of linear logic*, 1999 author manuscript, §§4.4–4.5, 5.1–5.3, Thms. 5.2, 5.3, 5.6; Appendix B. [Author PDF](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/full.pdf) | MILL→MLL is stated fully complete; the relatively free star-autonomous extension of a small SMCC is stated full and faithful; MILL→DILL is fully complete at `∅;Δ⊢σ`. DILL has linear tensor/unit/hom and ! with two contexts; it is intuitionistic on its linear side. Base types/constants are fixed in the translations. | **VERIFIED_SOURCE.** These separate extensions are not the simultaneous classical/CCC/F/U free completion in this task. The older classical gluing method must retain Shulman's stated warning. |
| Hasegawa, *Girard translation and logical predicates*, JFP 10(1), 2000, §2, Props. 3.1/3.3/3.4, Lem. 3.2, Thm. 5.6, pp. 79–86. [DOI](https://doi.org/10.1017/S0956796899003615) | Source types are base types and implication, with STLC βη. Target types are base types, linear implication and ! in the specified dual-context calculus and its βη/let equations. Thm. 5.6: every term at `Γ°;∅⊢σ°` equals a translated source term, where `(σ⇒τ)°=!σ°⊸τ°`. | **VERIFIED_SOURCE.** A full-completeness theorem for a different translation and target. It is not used to infer native atomic fullness in the complete classical mixed doctrine. |
| Heijltjes–Straßburger, *Proof nets and semi-star-autonomous categories*, MSCS 26(5), 2016, Defs. 2.1–2.5, Props. 2.3/2.6, Def. 5.8, Thm. 5.10, author-PDF pp. 3–5, 18–19. [Version inspected](https://github.com/willemheijltjes/willemheijltjes.github.io/blob/25044f45477b9a2fdf0d4fb09de5b6d4400b8640/pdf/2016-heijltjes-strassburger.pdf) | Annotated unit-free nets use connected/acyclic switchings; LM has no MIX. Cut is admissible and preserves the net. An atom functor into a **∂-strict** semi-star-autonomous category extends uniquely up to natural isomorphism; the ssa-functor includes the virtual-unit natural transformation γ and preserves λ. | **VERIFIED_SOURCE.** Strong pure prior art, without modalities or nonlinear homs. Neither its strictness nor a broader polycategorical comparison is assumed as a dependency here. |
| Hughes, *Simple free star-autonomous categories and full coherence*, §4/Thms. 2–4, pp. 12–13. [Primary PDF](https://arxiv.org/pdf/math/0506521) | Linkings modulo rewiring of negative unit edges form the free star-autonomous category generated by a base category; composition respects that equivalence. | **VERIFIED_SOURCE.** A pure linear theorem with units. It gives no mixed recovery theorem. |
| van Glabbeek–Hughes, *MALL proof nets identify proofs modulo rule commutation*, §2, Tables 2–4, Thm. 1, p. 7. [Primary PDF](https://arxiv.org/pdf/1609.04693) | Two cut-free unit-free MALL proofs on the tracked conclusion have the same net iff related by the listed commutations. MIX is optional; the relevant multiplicative restriction omits it. | **VERIFIED_SOURCE.** Matches the frozen pure source equality, not the complete mixed E*. The atomic singleton classification needs only the one axiom link. |

No inspected statement exactly settles the displayed mixed atomic claim. This bounded source finding is **UNKNOWN** as an exhaustive literature claim; it does not establish novelty or that the statement is open. The positive verdict rests on the following **INFERENCE**, not on composing unmatched fullness theorems.

## 3. A typed auxiliary presentation of the same operations

Use the ordinary logical rules below as abbreviations for fixed target templates. An auxiliary derivation may still have **explicit** nonlinear and linear cut rules. A derivation called “without explicit cuts” below may contain logical rules whose target templates use composition. This distinction matters: I am not asserting literal cut elimination in Figure 2's unusual zero-premise projection-only presentation.

Let J mean either `N(Υ;Z)` or `L(Υ|Γ;Δ)`. Adding a nonlinear slot to J changes only Υ. Ambient linear contexts always retain their named occurrences. All variables bound by a displayed logical rule are fresh for unrelated substitutions.

### 3.1 Nonlinear rules, including their use in a linear continuation

The rules are nonlinear identity and structural actions, terminal introduction, product pairing and contextual product-left, implication-right and implication-left:

```text
⋆_Θ                       : N(Θ;1_N)
pair(a,b)                 : N(Θ;X×Y)       [a:N(Θ;X), b:N(Θ;Y)]
P_L(d)                    : J(Θ,X×Y)      [d:J(Θ,X,Y)]
λ_X d                     : N(Θ;X⇒Y)      [d:N(Θ,X;Y)]
H_L(a,q)                  : J(Θ,Υ,X⇒Y)    [a:N(Θ;X), q:J(Υ,Y)].
```

Here `J(Θ,...)` abbreviates the corresponding nonlinear context, leaving the rest of J's boundary fixed. Concatenations in implication-left are explicit; sharing them is a subsequent nonlinear structural action. A terminal nonlinear slot can be introduced by weakening, denoted `T_L`. Product-left substitutes the two projections and uses contraction; it is equivalently inverse factorization through the context-universal pairing `X,Y→X×Y` of Prop. 2.11. Its availability for a linear continuation is **derived**, not an assumption that nonlinear product is a linear additive.

Write `ev_N:(X⇒Y),X→Y`. Implication-left is exactly substitution of `ev_N(h,a)` into the Y-slot of q. Implication-right is inverse factorization through `ev_N`. Product and implication β hold by their selected universal properties; nonlinear terminal η says every map into `1_N` equals `⋆`. Prop. 2.11 and the cartesian laws give contextual product β/η. These are E* equations, also when q is linear.

### 3.2 Linear multiplicatives, raw duals, and the two units

Let `κ_{A,B}:A,B→A⊗B` and `π_{A,B}:A⅋B→A,B` be the frozen universal morphisms.

| Auxiliary rule | Premises and conclusion | Target template |
|---|---|---|
| `⊗R(a,b)` | `a:L(Θ|Γ;Δ,A)`, `b:L(Υ|Γ';Δ',B)` give `L(Θ,Υ|Γ,Γ';Δ,Δ',A⊗B)` | Cut a and b into the two distinct inputs of κ. No free juxtaposition/MIX is used. |
| `⊗L(d)` | `L(Θ|Γ,A,B;Δ)` gives `L(Θ|Γ,A⊗B;Δ)` | Inverse factorization through κ. |
| `⅋R(d)` | `L(Θ|Γ;Δ,A,B)` gives `L(Θ|Γ;Δ,A⅋B)` | Inverse factorization through π. |
| `⅋L(a,b)` | `a:L(Θ|Γ,A;Δ)`, `b:L(Υ|Γ',B;Δ')` give `L(Θ,Υ|Γ,Γ',A⅋B;Δ,Δ')` | Cut the two outputs of π into a and b, respectively. |
| `IR` | `L(∅|;I)`, with optional nonlinear weakening | The unit universal morphism. |
| `IL(d)` | `L(Θ|Γ;Δ)` gives `L(Θ|Γ,I;Δ)` | Unit inverse factorization. |
| `⊥L` | `L(∅|⊥;)`, with optional nonlinear weakening | The counit universal morphism. |
| `⊥R(d)` | `L(Θ|Γ;Δ)` gives `L(Θ|Γ;Δ,⊥)` | Counit inverse factorization. |

Duality supplies the typed rotations

```text
R_A : L(Θ|Γ,A;Δ) → L(Θ|Γ;Δ,A*)
L_A : L(Θ|Γ;Δ,A) → L(Θ|Γ,A*;Δ).
```

They use the evaluation `e_A:A,A*→` and the corresponding coevaluation `c_A:→A,A*`. Def. 2.10 explicitly gives the equivalent evaluation/coevaluation universal presentations. Choose the coevaluation corresponding to that evaluation; the inverse-factorization β/η equations give their snake equations. For example, rotating `id_A` gives `e_A` or `c_A`, and rotating evaluation back gives `id_{A*}` by η. Thus these are derived templates in the frozen doctrine.

The useful principal equality, with all other ports retained, is

```text
cut_{A*}(R_A d, L_A q) = cut_A(q,d).                 (D)
```

Expand the rotations as composition with c_A and e_A. Associativity/interchange first exposes `cut_{A*}(c_A,e_A):A→A`; the snake equation makes it `id_A`, giving (D). Swapping the two ambient nonlinear context lists uses their specified exchange action. This is a typed equality at **raw** A and A*, not an equation setting A** equal to A. Canonical double-dual and De Morgan comparison arrows are composites of these universal templates and identities; they can be expanded before the argument. No new type-conversion rule is introduced.

### 3.3 F and U, with their exact zone restrictions

Let `f_X:X|;FX` and `u_A:UA|;A` be the frozen universal morphisms. The auxiliary rules are

```text
F_R(a) : L(Θ|;FX)          [a:N(Θ;X)]
F_L(d) : L(Θ|Γ,FX;Δ)      [d:L(Θ,X|Γ;Δ)]
U_R(c) : N(Θ;UA)          [c:L(Θ|;A)]
U_L(q) : L(Θ,UA|Γ;Δ)      [q:L(Θ|Γ,A;Δ)].
```

`F_R` substitutes a into f_X. `F_L` is inverse factorization through f_X. `U_R` is inverse factorization through u_A. `U_L` cuts u_A into q. The restrictions on F_R and U_R are essential: the first has no other linear ports, and the latter's premise has **empty linear input and exactly one output A**. A linear hypothesis is never promoted to a nonlinear slot.

Their principal equations are precisely

```text
cut_{FX}(F_R(a), F_L(d)) = cut_X(a,d)
cut_{UA}(U_R(c), U_L(q)) = cut_A(c,q),                (M)
```

where the first right side is nonlinear cut and the second is linear cut. For the second equality, nonlinear substitution into u_A first gives c by U-β, and then linear associativity composes it with q. This accounts for the U case even when q has arbitrary other linear ports.

### 3.4 Coverage and the commutation equation

Every Figure 2 primitive for the selected cones has a template in this list: product projections are `P_L` of a weakened identity; pairing is `pair` of identities; evaluation is `H_L` on identities; unit/counit and f/u use their indicated rules; κ, π, and evaluation/coevaluation use identities and the linear rules. Their inverse factorizations are the corresponding listed introductions or contextual left rules. If nonlinear product is presented by projections rather than positive pairing, Prop. 2.11 supplies both the alternate projection and factorization templates and their equations. Terminal has the analogous nullary comparison. Cuts and structural actions remain explicit. There is no residual nonidentity input generator to translate.

The equation used for every nonprincipal permutation has a short derivation. Let `V_ψ` be inverse factorization through a selected universal projection ψ. For a cut C at a different free port, or a permitted structural action σ, the equations are

```text
C(V_ψ(d)) = V_ψ(C(d));       V_ψ(d)σ = V_ψ(dσ).       (Nat)
```

Cut both candidate sides with ψ. β, associativity, interchange and equivariance give the same d-side expression. Universal η at that **ambient** profile then cancels ψ. In a multi-projection cone, do this for each projection and use its η uniqueness. Bound nonlinear variables are renamed first, so the cut is at a free port. For rules built by composition with κ, π, evaluation, f or u, the same equations follow immediately from associativity/interchange. For pairing, use its two projection β laws followed by product η. These checks cover the whole listed rule set and all ambient contexts, rather than only modal-free ones.

This is also why arbitrary factorization contexts in the original representative cause no omission: they are precisely the context parameters of these templates. No equation relating representatives is being replaced by equality of their conclusions.

## 4. An equality-preserving explicit-cut lemma

**INFERENCE.** Define ranks mutually by `r(p)=0`, nullary former rank 1, unary former rank `1+r(argument)`, and binary former rank `1+r(left)+r(right)`. This includes `r(UA)=1+r(A)` and `r(FX)=1+r(X)`. Height is the ordinary finite auxiliary derivation-tree height. The aim is **existence of a finite E*-equal derivation without explicit cuts**, not termination of every rewrite order, confluence, decidable equality, or uniqueness of general normal forms.

The lemma has two mutually proved clauses:

1. **Linear cut:** for derivations a and q without explicit cuts, with one specified A output of a and one specified A input of q, their linear cut has an E*-equal derivation without explicit cuts, at exactly the polycategorical cut boundary.
2. **Nonlinear simultaneous substitution:** for `a:N(Θ;X)` and a derivation q without explicit cuts, replace any specified finite family of X-slots of q by a, sharing Θ by its nonlinear finite-function action. This composite has an E*-equal derivation without explicit cuts. q may be nonlinear or linear; its linear boundary is retained.

For clarity, the simultaneous composite `M_X(a;q)` means: use a fresh renamed copy of a for each selected slot, perform the ordinary nonlinear cuts, then apply the diagonal structural map that identifies corresponding copies of Θ. With zero selected slots it is q weakened by Θ. This is an abbreviation built from allowed nonlinear cuts/actions, **not** a linear multiport MIX rule. It duplicates no external linear port: a is a nonlinear judgment, even if it contains nested U-derived linear subproofs.

Prove the clauses by induction on the lexicographic triple

```text
(rank of the cut/substituted type, height of a, height of q).
```

Ranks are primary, so a lower-rank recursive problem may have arbitrary height. At fixed rank, moving through a producer premise decreases the second entry, and moving through a consumer premise decreases the third. The following cases exhaust identities, structural actions and the rule list of §3.

### 4.1 Identity and structural cases

Linear identity removes the cut by the unit law. Nonlinear identity makes simultaneous substitution an appropriate renaming/structural action on a. If the selected slots are absent, nonlinear weakening discards a, by structural equivariance of nonlinear substitution. Permutations commute with cuts by equivariance, with occurrence names retained.

For a nonlinear contraction in q, select **all of its preimage slots** in its premise and recurse on that premise. The producer and type are unchanged; consumer height has decreased. Structural equivariance equates this recursive composite with `M_X(a;q)`. This deals with any number of copies, including copies in different branches. It avoids the invalid argument “do one binary cut, then use the original height bound for the next”: the first replacement can increase height.

Structural actions on a are moved to its external context after substitution, by the same finite-function equivariance. Recurse on the producer premise when needed. Actions on unselected consumer slots are simply rebuilt. None of these operations deletes or contracts a linear occurrence.

### 4.2 Nonprincipal rules and nonlinear source eliminations

If a selected consumer slot is not principal in its last rule, distribute the cut/substitution to exactly the premise occurrences from which it comes, recurse, and rebuild the rule using (Nat). A linear occurrence goes to one premise only: in the binary linear rules the linear contexts split. A nonlinear slot may have preimages in several premises; apply simultaneous substitution to each and share Θ using the permitted actions. Each such premise has smaller consumer height. Nonlinear argument premises have no external linear boundary to duplicate.

If the cut output is nonprincipal in the producer's last linear rule, move the cut into its unique containing premise and rebuild, using (Nat). Producer height decreases. Linear output occurrences are never copied in this case.

For nonlinear simultaneous substitution there is one additional source case. A nonlinear producer may end with `P_L`, `T_L`, `H_L`, or a structural action rather than an introduction of its output X. Its proper continuation premise d still has output X. Move the simultaneous substitution through that last rule, recursively replacing the chosen X-slots by d, and then apply that same **nonlinear left rule to the resulting judgment J**. For example,

```text
M_X(H_L(b,d);q) = H_L(b, M_X(d;q)).                  (S)
```

For exact typing in (S), take `b:N(Ξ;D)`, `d:N(Υ,Y;X)`, and `q:J(Λ,X₁,...,X_k)`, with h a fresh slot of type `D⇒Y`. The producer on the left is `H_L(b,d):N(Ξ,Υ,h:D⇒Y;X)`. The recursive continuation on the right is `M_X(d;q):J(Λ,Υ,Y)`, with the copies of Υ,Y shared; applying H_L gives `J(Ξ,Λ,Υ,h:D⇒Y)`. The left has the same slots in a different order, aligned by their named exchange map. Every selected copy shares those same external nonlinear variables.

To verify (S), expand `H_L` as substitution of `ev_N(h,b)` into d. Associativity and cartesian structural equivariance equate substitution into each copy of d with substitution into their shared continuation. That latter substitution is exactly the H_L template at J. The analogous equality for P_L substitutes the two projections; T_L and structural actions use deletion/finite functions. These rules are available for both choices of J in §3.1. The recursive producer is the proper premise d, so the second induction entry decreases. No cut of a possibly larger *argument* type is recursively introduced: the original left rule is rebuilt as a logical rule.

The source case is indispensable when q is linear. It uses the action of nonlinear substitution on linear homs already present in Def. 2.1; it never treats a linear producer as copyable.

### 4.3 Principal cases

First process any **other** selected nonlinear slots in the consumer's proper premises, leaving its one principal selected occurrence distinguished. Those recursive calls have smaller consumer height at the original rank. Then use the following equations. All newly introduced explicit cuts have strictly smaller type rank.

| Principal pair | E*-equal replacement and why it is legal |
|---|---|
| Nonlinear pair / P_L | Substitute a's X and Y components simultaneously into the X,Y slots of the continuation. Product β gives both components; contraction shares the original Θ. Both types have smaller rank than X×Y. |
| Nonlinear `λ_X d` / H_L(b,q) | Substitute b into the bound X-slot of d, then substitute its Y-result into q. The equation is evaluation/transpose β, also in the linear continuation q by associativity. The new types X and Y have smaller rank than X⇒Y. |
| Nonlinear terminal / T_L or deletion | Rebuild the continuation with the unused producer context weakened in. Nullary product/terminal reconstruction and structural deletion give this equality. No linear deletion is involved. |
| `U_R(c)` / U_L(q) | Use `cut_A(c,q)` by (M). A has smaller rank than UA. c has empty linear input and one A output, so the cut has exactly the original boundary and introduces no copied linear input. |
| `⊗R(a,b)` / ⊗L(q) | Cut a and b into q's distinct A and B inputs. Expand ⊗R through κ, reassociate, and use tensor β to remove κ/⊗L. The two new cuts have smaller types A,B and disjoint retained resources. |
| ⅋R(d) / `⅋L(a,b)` | Cut d's separate A and B outputs into a and b. Expand ⅋L through π and use cotensor β. The retained linear ports remain disjoint. |
| IR / IL(q) | Remove unit factorization/projection by unit β; weaken the producer's nonlinear context into q if present. |
| ⊥R(d) / ⊥L | Remove counit factorization/projection by counit β; weaken the consumer's nonlinear context into d if present. |
| `R_A d` / `L_A q`, on A* | Replace by `cut_A(q,d)` using (D). A is smaller than the raw A*. No raw double-dual identification occurs. |
| `F_R(a)` / F_L(q) | Replace by nonlinear substitution `cut_X(a,q)` using (M). X is smaller than FX. a has no external linear ports, so the nonlinear induction clause applies. |

Terminal assumptions have no additional elimination constructor of their own; if one is used inside another logical rule, §4.2 handles that rule until identity, deletion or a terminal slot is reached. For all introductions the only nonidentity principal consumer cases are the matching left rules in this table. A producer that ends in a left rule was already handled in §4.2. Thus there is no appeal to a general normalization theorem to fill a remaining case.

Apply the induction hypotheses to the lower-rank cuts and rebuild the displayed rules. Every step is an E* equality: unit/structural laws, (Nat), the associativity/equivariance equality (S), or one of the explicit universal β equations in the table. Structural maps introduced for sharing are nonlinear maps only. This proves both cut clauses.

Finally, induct on an arbitrary auxiliary derivation: first replace its proper premises by E*-equal derivations without explicit cuts; if its root is a cut, apply the proved clause. If its root is a logical or structural rule, rebuild it. This induction covers every finite representative supplied by §3.4. It constructs an equal derivation without explicit cuts, without claiming strong normalization or confluence.

## 5. Final classification and equality compatibility

**INFERENCE.** Consider a derivation without explicit cuts at `L(∅|p;p)`. Remove terminal exchange/identity structural actions. No nonlinear weakening or contraction can be its final nontrivial action: their conclusion would contain a nonlinear slot, whereas Θ is empty.

Every remaining logical rule has a recognizable principal object at its conclusion:

* The nonlinear contextual left rules and U_L leave a nonlinear assumption.
* F_L leaves an FX linear input; F_R leaves an FX output and has empty linear input.
* A linear multiplicative, unit, counit or dual rule leaves its displayed compound/unit/dual principal object as an input or output.
* Nonlinear introduction and U_R conclude a nonlinear judgment.

None can conclude the syntactically atomic input/output pair p;p. The only remaining rule is linear identity on that occurrence of p. Its interpretation is `id_p`. This is a last-rule classification, not a subformula/normalization assumption.

For any chosen representative of t, §§3–4 give a chain of equalities in the **original** E* to the interpretation of such a derivation, hence to `id_p`. No class decoder or choice of normal form is being used to define E*. Compatibility with the full congruence follows directly: every representative at this boundary has that same E*-equality, so replacing one by any E*-equivalent representative gives the same final class. Extra applications of ambient η do not need to preserve an intermediate reduction strategy. The claim is an equality in E*, not merely that some pure proof of the same sequent exists.

## 6. Attempts to defeat the argument

### Modal/unit scalar

Let `f:I≅F1_N` be the canonical unit comparison. With F⊣U's unit η and counit ε, all the following arrows type:

```text
I --f--> F1_N --Fη_1--> FUF1_N --ε_(F1_N)--> F1_N --f⁻¹--> I.
```

F/U universal β/η supplies the adjunction triangle, so this scalar s equals `id_I`. Then `ρ_p (id_p⊗s) ρ_p⁻¹=id_p`, by the tensor/unit laws. This independently checked cancellation uses genuine mixed interior types; it assumes neither `FU=id` nor the pure-net bridge. It is one instance of the F/U principal cases, not a substitute for §4.

### Opposite-zone duplication of a closed identity function

Let `H=p*⅋p`, with its **derived** internal-hom structure for `p⊸p`, and `e:H,p→p` its derived evaluation. Let `k:L(∅|;H)` be the transpose of `id_p` and `q=U_R(k):N(∅;UH)`. Define `c:H,H→H` by transposing the double evaluation `e(h₂,e(h₁,x))`. It uses each of the two H ports once. In nonlinear slots z₁,z₂:UH, cut one copy of `u_H` into each of c's two distinct H inputs. This yields `L(UH,UH|;H)`, and U_R yields a nonlinear multiplication `m:N(UH,UH;UH)`. This is a genuinely permitted duplication route: duplicate a **closed function value**, not the live linear p input.

By U-β, substituting q in both slots of m gives `U_R(c(k,k))`. Evaluate `c(k,k)` on the named linear p: the derived hom β law gives `e(k,e(k,x))=x`. Hom η therefore gives `c(k,k)=k`. U-β again followed by evaluation gives the resulting atomic map `e(k,x)=x`. Thus the duplicated-function detour cancels. Products and nonlinear homs may organize or iterate such values; the nonlinear simultaneous-substitution and implication cases of §4 cover arbitrary nesting rather than just this example.

### Invalid promotions and traces

`U_R(id_p)` is ill typed: `id_p` has a linear input. Neither the empty nonlinear atom set nor terminal weakening permits discarding that input to repair it. Likewise, after composing coevaluation with evaluation along one port, an operation that self-connects the remaining two ports would be a trace, not a polycategory cut between two separate arrows. No such rule is included. The binary rules of §3 use designated ports of κ or π and do not insert MIX or a self-trace.

### Strongest self-critique

The vulnerable part is **§4's mutually typed cut/substitution lemma**, especially source commutation (S), sharing across nonlinear contraction, and the raw-dual principal case. It would be insufficient to cite ordinary linear cut admissibility, normalize an external translation, or use a binary-height induction after duplicating a cut. This report supplies the simultaneous composite, the lexicographic measure, the nonlinear precomposition derivation of (S), and the dual snake expansion to address those particular failures.

A reviewer can overturn the positive argument by finding (i) a selected Figure 2 operation or ambient factorization not covered in §3.4, (ii) a commutation whose compared boundaries differ or whose η cancellation is inadmissible, or (iii) a recursion that does not decrease the stated measure or duplicates an external linear occurrence. That would reopen this atomic statement; failure of an unexamined generic normalization theorem is not itself such a finding. The argument has no machine certificate, independent mathematical review, or exhaustive literature search, and should not be promoted beyond its **INFERENCE** status without those checks.

## 7. Dependency ledger and scope

| Dependency/obligation | Status in this investigation | Role |
|---|---|---|
| Frozen D*, E*, grammar and generator ledger | Fixed by Task 017/017 §6/020 §8; primary meanings checked directly | Exact proposition being tested. |
| Shulman §8 representation/quotient | VERIFIED_SOURCE | Covers every representative and licenses the target equations. |
| Nonlinear product contextual equivalence; universal dual/modal operations | VERIFIED_SOURCE definitions/Props. 2.11/2.16, plus INFERENCE typed calculations | Supplies all auxiliary rule templates and their β/η equations. |
| (Nat), (D), (M), (S), and mutual explicit-cut lemma | INFERENCE, supplied in §§3–4 | Actual reduction argument; no global normalization assumption. |
| Atomic last-rule classification | INFERENCE, §5 | Gives the singleton target hom-set after the reduction. |
| Source atomic singleton | Direct source-rule/linking classification; INFERENCE | Interprets the atomic result as the relevant SC instance. |
| Report 022's whole pure bridge `N≅T₀` | Not assumed; pending independent verification | Not needed. |
| Identification/full faithfulness of pure unit extension | Not assumed | Not needed. |
| Finite-schema extraction for D* | Not certified here | Separate SC clause. |
| Full SC: both fragments, all boundaries, source equality reflection and naturality | Not established here | A positive atomic instance does not establish this conjunction. |
| Mechanical or independent proof certification | Absent | No FORMALIZED/accepted-theorem claim. |

The scope-to-north-star bridge is small but concrete: the complete mixed structural grammar has no additional proof class at this native pure atomic linear boundary, on the argument given here. It does not cover dependent foundations, cyclic validity, arbitrary imported rules, causal history, minimality, or a universal finite core. Even if the auxiliary cut lemma is accepted more broadly, source equality comparisons and the remaining SC clauses require their own arguments; this assignment stops at the displayed atomic classification.

## 8. Verification and provenance record

Read AGENTS.md and its mandatory README/charter/definitions/falsification/protocol/prior-art documents; RESEARCH_PLAN.md; research/OPERATING_PROTOCOL.md; reports 017–022; Tasks 015–017. The seven primary texts in §2 were inspected at the specified passages, using the prior published-source scratch files outside the repository. The old reports remain evidence, not independently certified dependencies.

Source PDF SHA-256 values, identifying the copies used:

```text
Shulman LNL:       253d5e39a3eb0c3410a93c8443d3109721d75c80f5ea9f823c6b305e2c8b240e
Shulman envelope:  a91e80c76cf0b211bcf4ad80c4208808c277a9847d1bf8566025ea05e3a8e668
HS 2016:          f26b991401baf30a72d6da0c7724b4e4766a0b9150d2c674f3426be03264d3fe
Hughes:           be814e88bc80ffe1af9dace01c5d903e56aefbd3f0cf5b68011b1a2f1770a698
van Glabbeek–H:   1ff20d34d6ee16b9722d3c05fc0f13f440780e4840bfde9512589ec8d3a51320
Hasegawa glueing:  6635175212b0501a2ddb8c3e1bc379edab644a0d7b40a94885de42b27a2307d0
Hasegawa Girard:   4ea0d32679758fb67a4933ea62f81bc52dc37a880188a1d92675414e4407749f
```

The managed-runtime skills were read, the nonsecret network policy inspected, and actual GitHub HTTPS read/API operations succeeded with inherited proxy and TLS trust. No credentials were printed. No dependency installation or reusable environment-configuration change was needed for this report-only workflow. Validation is a document/typing/equality audit, not a test suite or a formal proof check. Only this report is added; the frozen mathematical files and the primary workspace are preserved.
