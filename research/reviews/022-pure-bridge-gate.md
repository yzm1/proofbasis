# Task 016 — Pure MLL bridge and mixed-core conservativity

**2026-10-14. Baseline:** main `bb2dd041a7c68acb175b6591721cbd282eeb8d9c`. The frozen proposition is [017 §6/Card SC](017-structural-contract-repair.md), critically restated in [020 §8](020-cross-review-by-adversarial-agent.md) and selected in [021](021-s2-r2-selection.md). This report changes none of those documents. No additional agents, implementation, or unrestricted S3 investigation were launched.

**Evidence convention:** VERIFIED_SOURCE means the primary passage was inspected in this task. INFERENCE means an informal mathematical argument given here, not a mechanically checked result. UNKNOWN marks an undischarged obligation. Source verification is of the relevant definitions, statements, and proof passages; it is not independent certification of every published proof.

## 1. Executive mathematical verdict

**The frozen SC conjunction is unresolved by this investigation.** No well-typed counterexample was established, and the inspected published theorems do not close it. The pure prerequisite has a concrete candidate comparison argument: tensor/par factorization is root-par insertion/removal, and dual factorization rotates an unchanged labeled forest. These operations model the entire specified pure Shulman quotient, giving inverse interpretations at the original boundaries. This proof uses existing net/sequent results and is an informal bounded transport argument, not a novel universal-existence theorem.

The mixed assertion remains separate. Pure linear unit conservativity also follows from Shulman's envelope theorem after the explicit universal-property comparison below. Neither result supplies recovery of all mixed-target proofs or invariance under all mixed equations. An adjunction triangle cancels one actual modal/unit detour; a finite-vector-space LNL model separates two actual axiom matchings. These are informal instance arguments, not an independently certified mixed conservativity theorem.

All seven original texts in §4 were obtained and their relevant passages inspected. No theorem matching the whole mixed SC conjunction was identified in those texts. This bounded finding does not prove that SC is open in the mathematical literature, and makes no novelty claim. The precise unresolved obligations are mixed linear and nonlinear pure-boundary conservativity under E*.

## 2. Exact frozen proposition

Fix D* with nonlinear terminal/product/internal hom, linear tensor/cotensor/unit/counit/dual, and covariant F/U, with the universal-cone meanings and **full** structural/principal β/η congruence of Shulman §8. The arity base is `lnlpoly`. There is no MIX, identification of the two linear units, proof irrelevance, `FU=id`, or nonidentity generating proof arrow.

The frozen quantifier order is

```text
∃ finite operation/equation-schema presentation K of this D*,
  ∀ finite disjoint nonlinear/linear atom sets X,Y,
    ∀ S ∈ {NJ(X), unit-free no-MIX MLL(Y),
           their finite certified conservative definitional extensions},
      ∀ well-formed source boundaries b:
        i_S : Pr_S(b) → A*(X,Y)(i_S b) is bijective,
        naturally under the declared atom substitutions,
        structural actions, identities, and typed composition/cut.
```

NJ has implication/products and α/βη equality. MLL has named occurrences and identical axiom linking on a fixed forest, equivalently the stipulated rule-commutation quotient. Its composition inserts a designated cut and normalizes; it is not cut-free tree grafting. Linear contexts admit permutations, not duplication/deletion; nonlinear contexts admit finite-function actions. Source atom substitutions stay in their respective fragments. Definitions are handled by their supplied expansion/inverse witnesses.

The object map sends nonlinear atoms to X, linear atoms to Y, products/implication and tensor/par to their named operations, and negation to the chosen dual using the specified canonical De Morgan isomorphisms. Strict involution of raw target type expressions is **not** assumed. Fullness quantifies over **every** target class at the translated boundary, including F/U, units, opposite-zone types, cuts, and universal-factorization detours.

The finite-schema clause does not demand convergence, decidable proof equality, finite higher coherence, a finite admissible-rule basis, or complexity bounds.

## 3. Objects, maps, and obligations

Use the following distinct objects:

* N(Y): the frozen compositional unit-free no-MIX net quotient, including its empty source boundary.
* T₀(Y): the free `sympoly` completion with binary tensor, binary par, and dual only; equality E₀ is the entire specified pure Shulman congruence.
* T₁(Y): the auxiliary pure linear completion adding linear unit/counit. This is an analysis object, not a substitute for SC.
* A*(X,Y): the frozen mixed completion; equality E* includes all its ambient equations.

```text
N(Y) --i--> T₀(Y) --u--> T₁(Y) --v_X--> A*(X,Y)_L
                    j_X = v_X u
                    i_L = j_X i

NJ(X)/βη ---------------------------> A*(X,Y)_NL
```

The canonical maps preserve the designated operations. On source constructors the linear triangle commutes after inserting the frozen boundary isomorphisms. This existence statement does not assert fullness or faithfulness of j_X.

At each pure linear boundary the separate obligations are:

```text
i:  n=m  ⇔ i(n) E₀ i(m);       ∀s∈T₀(i b) ∃n: s=i(n).
j:  s E₀ t ⇔ j(s) E* j(t);     ∀r∈A*(i b) ∃s: r=j(s).
```

With a certified bijection i, the second line is precisely SC's linear bijection. It does not establish SC's nonlinear bijection or finite-schema clause. A model separating images can prove a particular equality-reflection instance; it cannot prove fullness.

## 4. Primary-source theorem correspondence

Every row below is VERIFIED_SOURCE in this task. Conclusions about matching/composing these results are the separate INFERENCE arguments, not additional claims made by the cited authors.

| Primary source and location | Mathematical content and hypotheses | Correspondence and remaining mismatch |
|---|---|---|
| Heijltjes–Straßburger, *Proof nets and semi-star-autonomous categories*, MSCS 26(5), 789–828 (2016), author PDF: Defs. 2.1–2.5, Props. 2.3/2.6, Defs. 3.1/5.1/5.8, Prop. 5.7, Thm. 5.10 (PDF p. 19), proof on pp. 22–23 | Annotated, unit-free forests; connected and acyclic switchings; LM has axiom/tensor/par and no MIX. Cut is admissible and preserves the net. The free net category extends an atom functor into a **∂-strict** semi-star-autonomous category uniquely up to natural isomorphism. An ssa functor is a pair `(G,γ)` preserving virtual-unit data and λ, not just an ordinary functor. | Strong original freeness input for nonempty profiles. Its unary category and virtual-unit functor must be compared with the chosen polycategory. It is not a theorem about F/U, nonlinear CCC structure, or SC. The paper explicitly excludes an empty-conclusion case from its cut-cut permutation discussion (Lemma 8.1, PDF p. 29). |
| Shulman, *LNL polycategories and doctrines of linear logic*, LMCS 19(2:1) (2023), Defs. 2.1/2.8/2.10/2.14/2.15, Props. 2.9/2.16/3.15, Def. 4.16/Prop. 4.17, Thm. 7.4 (p. 1:42), §8/Figure 2/Prop. 8.3 and quotient paragraph (pp. 1:44–47), Thm. 9.1; [original PDF](https://arxiv.org/pdf/2106.15042) | Free completion has a surjective-equivalence universal property on invertible 2-cells. §8 assumes an unsorted doctrine with subterminal base and finite discrete cones. Equality is generated by the composition of the input sketch, base structural axioms, principal projection/factorization β, and η uniqueness at every admissible ambient profile. | Matches T₀ and A*'s stipulated presentations. Supplies syntax/existence, not source adequacy or doctrine-change conservativity. §8, p. 1:45 explicitly leaves cut elimination for future study. §5.4 below extracts the finite schemas without asserting normalization. |
| Shulman, *Star-Autonomous Envelopes and Conservativity*, EPTCS 353 (2021), §6, Thm. 10.1 (p. 189), Cor. 10.6, Remarks 7.7/10.7; [original PDF](https://arxiv.org/pdf/2004.08487) | The universal star-autonomous extension of a small symmetric polycategory preserving designated existing tensor/cotensor products up to isomorphism is fully faithful. The theorem is polycategorical, with arbitrary boundary arities. | Applies to u by §5.5. Its universal property does not adjoin nonlinear CCC operations or F/U. Remark 10.7 identifies the precise internal-hom-preservation gap in the older ordinary-presheaf double-gluing route, without refuting the conclusion supplied here. |
| Hughes, *Simple free star-autonomous categories and full coherence*, §4/Thms. 2–4, pp. 12–13 of the retrieved text; [original PDF](https://arxiv.org/pdf/math/0506521) | A-nets are correct linkings modulo re-targeting an edge from a negatively occurring unit I; composition respects this equivalence. Thm. 3 identifies the free star-autonomous category. | Supports T₁'s unit-rewiring comparison. At the discrete, unit-free atom boundaries here there is no such unit edge to rewire. Its target is not A*. No absolute label-equality algorithm is inferred for arbitrary noneffective base categories. |
| van Glabbeek–Hughes, *MALL proof nets identify proofs modulo rule commutation*, §2, Tables 2–4, Thm. 1 (p. 7); [original PDF](https://arxiv.org/pdf/1609.04693) | Cut-free unit-free MALL proofs have the same translated net iff related by the listed commutations. MIX is optional, absent by default. Subformula occurrences and ordered connective arguments are retained. | Exactly the no-MIX multiplicative source quotient after restriction. The separate theorem about cut-bearing MALL nets is not silently substituted for cut-normalized MLL composition. |
| Hasegawa, *Categorical glueing and logical predicates for models of linear logic*, §5.1–5.3, Thms. 5.2/5.3/5.6 (PDF pp. 26–28), Apps. A/B; [author PDF](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/full.pdf) | MILL→MLL is stated fully complete; a relatively free star-autonomous extension of a small SMCC is stated full and faithful. MILL→DILL is fully complete at `∅;Δ⊢σ`. DILL here has linear tensor/unit/hom/! and two contexts, not classical duality. The base types/constants are fixed in common. | The classical gluing justification must be qualified by Shulman's later Remark 10.7. Cor. 10.6 of Shulman supplies the classical extension conclusion. The distinct MILL→DILL theorem is not refuted by that warning. Neither result states simultaneous conservation of SC's mixed free completion. |
| Hasegawa, *Girard translation and logical predicates*, JFP 10(1) (2000), §2, Props. 3.1/3.3/3.4, Lem. 3.2 (pp. 81–82), Thm. 5.6 (p. 86); [primary article](https://doi.org/10.1017/S0956796899003615) | Source types are `b | σ→σ`, with βη. Target types are `b | τ⊸τ | !τ` with the listed βη and let-! commuting laws. `(σ→τ)°=!σ°⊸τ°`; equality is preserved/reflected and every target term at `Γ°;∅⊢σ°` equals a source image. | A precise full-completeness result at this non-native, arrow-only translation. Extending it to native nonlinear products/hom in A*, with all classical/mixed equations, needs another comparison theorem. |

The HS source was obtained from the [author's website repository](https://github.com/willemheijltjes/willemheijltjes.github.io/blob/25044f45477b9a2fdf0d4fb09de5b6d4400b8640/pdf/2016-heijltjes-strassburger.pdf), whose publication entry identifies the article and DOI `10.1017/S0960129514000395`. PDF SHA-256: `f26b991401baf30a72d6da0c7724b4e4766a0b9150d2c674f3426be03264d3fe`. Use this version's **Theorem 5.10**, rather than the earlier manuscript's Theorem 5.21 cited in 020. This is a version distinction, not a different theorem claim.

## 5. Explicit pure-net bridge argument

**INFERENCE: a bounded comparison proof using the inspected published presentation.** Shulman's Def. 4.16/Prop. 4.17 makes each selected pure cone exactly the universal morphism of Def. 2.10. The entire §8 quotient has only input-sketch composition, base structural laws, and these principal β/η equations. No nonidentity input proof generator or additional cone equation remains to interpret. The argument does not invoke a blanket equivalence between arbitrary semi-star-autonomous categories and all empty-profile polycategories.

### 5.1 Factorization maps

Represent `N(Γ;Δ)` by the forest `Γ^⊥,Δ` with its labeled axiom matching. The following are explicit inverse maps, retaining every old leaf label:

```text
N(Γ,A,B;Δ)  ≅ N(Γ,A⊗B;Δ)
N(Γ;Δ,A,B)  ≅ N(Γ;Δ,A⅋B)
N(Γ,A;Δ)    ≅ N(Γ;Δ,A^⊥).
```

For the first bijection the new input tensor is a **par root in the negative forest**. For the second it is a positive par root. Insert/remove that root. In each switching it has exactly one retained edge, so it is a pendant vertex. Adding it to a tree preserves connectedness/acyclicity; removing it leaves the same old tree. The atomic matching is unchanged, so the maps are inverse on proof classes, not just on inhabitation. Dual rotation leaves the normalized one-sided forest unchanged. These maps apply at every remaining linear context, not only unary homs.

The tensor universal morphism `A,B→A⊗B` is the tensor of the two expanded identities. The par universal morphism `A⅋B→A,B` is its dual counterpart. Cutting with them performs the displayed root-removal operation: path composition through their identity links joins precisely the original corresponding leaves. Dual evaluation and coevaluation are the rotations of the expanded identity. Thus the factorization β/η equations hold by the actual inverse maps.

Cut naturality follows directly: on an unrelated port, root insertion/removal changes no alternating linking path. Identity, associativity, exchange, and interchange have the same path description. HS Def. 2.5 and Prop. 2.6 supply the verified linking-composition/cut-admissibility input. This accounts for the full E₀ generator list just identified. In particular, the conditional η rule is satisfied because the relevant cut map is bijective: equal composites have equal original matchings.

### 5.2 Empty and virtual-unit profiles

The frozen source has `N(;)=∅`: no axiom or final MLL rule proves the empty sequent. Do not deduce a contrary inhabitant from a convention declaring the empty graph connected. Sequentialization (HS Prop. 2.3) connects correctness to LM proofs, and cut admissibility preserves that source restriction.

The factorization operations above always replace a nonempty formula occurrence or pair by another nonempty occurrence. None turns a nonempty profile into the empty profile. The generating universal arrows themselves have nonempty profiles. Closure under cut follows from HS Prop. 2.6 even at this boundary: a pair of source premises whose cut would conclude the underivable empty sequent cannot both exist. N with this empty hom-set is therefore a model of the stated pure structural/universal operations; it does not install an empty proof constant.

Its virtual unit is **the set** `I_v(A)=N(;A)`. The canonical map `I_v(A^⊥⅋B)→N(A;B)` removes the root par; this is exactly the λ described in HS Prop. 5.7. It does not introduce a physical linear unit object. Arbitrary nonempty multiport profiles can likewise be bundled by par-root insertion with specified bracketing. The empty profile is handled separately rather than hidden in such bundling. Thus the published virtual-unit coherence is respected, while the empty case follows from the explicit net model, not Thm. 5.10 alone.

### 5.3 Two-sided inverse

The net model gives a structure-preserving interpretation `R:T₀→N` fixing atoms. The canonical constructor interpretation i sends atomic axiom to dual coevaluation, tensor to composition with its universal morphism, par to factorization, and cut to typed composition.

For independent par/tensor commutations, naturality of inverse factorization on the untouched port and interchange give the equation in T₀. Par/par commutations commute two root insertions. Tensor/tensor commutations are interchange together with the derived associativity/symmetry maps, always tracking the original ports. A principal tensor/par cut cancels the matching factorization and reduces to its constituent cuts; atomic cuts use the identity law. These calculations give the proposed interpretation of the frozen source equations and cut reductions, rather than interpreting raw sequent trees as inert constructors.

On source nets `Ri=id`: all leaf links are retained, and sequentialization supplies the constructors. On generated target proofs `iR=id` follows by induction on the **full** generator list: identities/structural actions/cuts are fixed; universal morphisms are the interpreted axiom/tensor/par nets; inverse factorization is fixed because cutting it with that same universal morphism recovers its premise, and the target η rule cancels that cut map. For raw dual expressions compare the functors using the canonical boundary isomorphisms, not a new strict double-dual equation. These isomorphisms fix atoms and are determined recursively by universal uniqueness (Shulman Prop. 2.9); they are natural under cut, and induce the specified De Morgan comparisons. On the translated, De-Morgan-normalized source grammar, the comparison fixes the reference boundaries. This is why no ∂-strictness axiom is imposed on T₀ to apply the net argument.

Consequently i is bijective on the original pure hom-sets, including the empty profile. R reflects equality by retained labeled matching; `iR=id` supplies intrinsic fullness. Atom substitution replaces each link with the expanded compound identity; the factorization/cut descriptions commute with that replacement, using the same canonical dual comparisons. Certified definitional extensions transport these equations through their supplied inverse expansions. This supplies a candidate informal transport proof built from existing results; acceptance of the pure bridge remains pending independent verification of the full equation and boundary comparison. It contains no F/U recovery and consequently proves nothing about j by cancellation.

### 5.4 Finite schemas

The selected D* has ten logical type-former schemas: three nonlinear, five linear, and F/U. Each has a fixed finite reduct/projection list, expressed by the finite cones in Shulman Defs. 4.16/4.18. Figure 2 therefore gives finitely many noninvertible/invertible schemas, together with identity, typed cuts, and structural actions. Its admissibility test is the finite signed-list condition of Def. 4.1; structural maps are finite functions which duplicate/delete only negative nonlinear entries. Lists, permutations, and finite functions have ordinary finite recursive descriptions. Atomic identity generators need no separate proof constants.

The quotient's conditional η uniqueness can be replaced by reconstruction: a proof t equals the factorization of its composites with all the finitely many projections. Principal β plus η gives reconstruction; reconstruction plus principal β implies conditional uniqueness. The nullary terminal case is a zero-premise factorization/reconstruction schema, not a semantic uniqueness oracle. This yields finitely many equation schemas for the selected fixed cones and base laws, independent of X,Y. It is an **INFERENCE finite-presentation extraction** from the inspected §8 result, not a cut-elimination, higher-coherence, or decidable-equality claim.

### 5.5 Pure linear units

Apply Shulman 2021 Thm. 10.1 to P=T₀ with J its binary tensors and cotensors. T₀ is small. Polycategory functors preserve duals (the paper's §2), so a J-preserving map from T₀ to a star-autonomous target already preserves its chosen dual data up to the canonical isomorphisms.

T₁ has the theorem's universal property: a J-preserving map T₀→Q is determined by its atom interpretation; the free unital tensor/par/dual completion extends it uniquely up to the specified coherent isomorphism. Conversely restricting an interpretation of T₁ gives that map. Thus u is identified with the theorem's universal map and is fully faithful **polycategorically**, including empty profiles. This is an INFERENCE application of the VERIFIED_SOURCE theorem. It supports the linear-unit extension, conditional on verification of this universal-property identification, and has no nonlinear CCC/F/U hypothesis: v_X is still another map.

## 6. Typed tests in the full mixed congruence

### Commutation and cuts

Tensor the p and r axioms into `⊢p^⊥,r^⊥,p⊗r`, and use a q axiom. Introduce `p^⊥⅋r^⊥` either before or after tensoring `(p⊗r)` with q. Both proofs end at

```text
⊢ (p^⊥⅋r^⊥), ((p⊗r)⊗q), q^⊥.
```

The named axiom matching is the same. The root-insertion/cut-naturality calculation above identifies their target interpretations. Cutting an expanded `A→A` into either proof changes no linking; in the target, the compound-identity η equation plus identity/cut laws cancels the cut. These are positive EP/composition instances, not entire-target fullness checks.

### Distinct matchings: a separating D* model

At `⊢p_1^⊥,p_2^⊥,p_3⊗p_4`, straight links `(1,3),(2,4)` and crossed links `(1,4),(2,3)` are both correct trees and are unequal source classes.

Use nonlinear FinSet and linear finite-dimensional vector spaces over F₂, with F the free-vector-space functor and U the underlying finite set. The adjunction holds, F preserves products as tensor and the nonlinear terminal as the linear unit, and the linear category is compact closed, hence star-autonomous. For a mixed profile, interpret arrows as

```text
Hom_Vec(F(∏Θ) ⊗ (⊗Γ), ⅋Δ),
```

with the usual empty products and linear units. The nonlinear homs are the corresponding FinSet maps. Shulman 2023 Prop. 3.15 identifies this star-autonomous LNL adjunction with the relevant LNL polycategory; the nonlinear CCC supplies its chosen homs. These universal properties supply the stipulated D* operations and satisfy the complete E* congruence. Additional equalities in this model are allowed; no equation requiring compact closure is added to the free target.

Let p be V=F₂². After bundling the named negative inputs, the two matchings give `id_(V⊗V)` and the swap. They differ on `e₀⊗e₁`. Therefore E* cannot identify this pair without violating the model's soundness. This is an informal separating-model proof for this **pair**, not all nets. The model also admits maps unavailable in no-MIX MLL, so its existence cannot certify syntactic fullness or rule out hidden MIX.

### Ambient modal equations and a genuine modal/unit detour

With the frozen meanings of F/U, the primitive universal arrows have boundaries

```text
f_N : N | ; FN,       u_A : UA | ; A.
P(Θ,N | Γ;Δ) ≅ P(Θ | Γ,FN;Δ),
P(Θ | ;A)    ≅ P(Θ;UA).
```

For the respective inverse factorizations FL and UR, the principal equations are

```text
cut_F(f_N,FL(d))=d;       FL(cut_F(f_N,t))=t;
cut_N(UR(d),u_A)=d;       UR(cut_N(t,u_A))=t.
```

Their types are those of the displayed bijections; `cut_N` substitutes into a nonlinear slot. Thus these cancellation/reconstruction tests quantify over admissible ambient contexts, and do not restrict their proofs to modal-free interiors. They still do not eliminate arbitrary interleavings with the other universal operations. The full E* generator list is the one inspected in §8: base laws, principal β, and reconstruction/uniqueness for each selected cone. A proposed recovery must respect **all** these generators, including nonlinear terminal/product/hom and linear unit/counit reconstruction. That recovery is not supplied by the four modal equations alone.

Let `f:I_L≅F1_N` be the canonical strong-monoidal unit isomorphism, η the adjunction unit, and ε its counit. Then

```text
s = f⁻¹ ∘ ε_(F1_N) ∘ Fη_(1_N) ∘ f : I_L→I_L,
h = ρ_p ∘ (id_p⊗s) ∘ ρ_p⁻¹        : p→p.
```

All arrows type; the intermediate object is `FUF1_N`. The F⊣U triangle gives `s=id_I`, hence `h=id_p`. Naturality of the unitors makes this equality stable when inserted into any appropriate larger proof. This is an equation in the full mixed congruence; it neither assumes `FU=id` nor forbids mixed interiors.

In contrast, promoting the linear identity `p→p` directly to a nonlinear proof of Up is ill typed: U factorization requires an empty linear input and a single linear output. The hypothetical diagonal `p→Up→FUp→FUp⊗FUp` therefore is not an SC witness. The actual diagonal on FX is well typed, but substituting `p↦FX` changes SC's frozen atom map.

For a nonlinear identity control, the same FinSet/vector-space D* model distinguishes the two projections `x×x→x` when the nonlinear atom x is a two-element set. Product β and function η hold by their universal properties. This excludes collapse of this specific source pair under E*, without classifying all target selectors or proving the native NJ clause.

### Units and MIX

The source forests `⊢p^⊥,p⊗p` (unbalanced leaves) and `⊢p^⊥,p,q^⊥,q` (disconnected switching) have no source class. A well-typed mixed proof at either original boundary would refute SC. No such proof is exhibited here. Identifying `I_L` with its dual/counit would add an unlicensed equation; the compact-closed model above is not evidence that this identification holds in A*.

## 7. Strongest positive argument and strongest obstruction

The strongest positive argument is the explicit net model with inverse universal factorizations in §5, supported by the original sequentialization, commutation, and cut statements. It proposes the bounded N→T₀ comparison including named occurrences, full pure cut/dual detours, virtual units, and the empty boundary; the full inverse and boundary-coherence checks still require independent verification. The source matching identity is independently fixed, not defined to equal the target congruence. The inspected pure unit-extension theorem would establish u fully faithful after verification that u has its precise universal property. For A*, the genuine modal triangle and separating model are the strongest verified instances in this task.

The strongest obstruction is **an unproved mixed recovery/equality-conservativity step**, not a counterexample. An arbitrary target representative can alternate nonlinear hom/product factorization, F/U, duality, and unit operations. The triangle calculation covers one family of detours. Neither that calculation nor the pure net model reduces every such representative or checks every ambient equation relating representatives.

Red-team checks reject the following proposed shortcuts:

* Free initiality constructs j but gives no inverse on its old-boundary homs.
* Pure linear unit conservativity establishes u rather than v_X.
* A faithful separating interpretation does not recover target-only inhabitants.
* No-MIX proof-net coherence does not describe mixed modal equations.
* Syntactic mixed detours are not necessarily nonimage classes: s and h above cancel.
* Strictifying the source's duality does not authorize changing the target congruence; the canonical boundary comparisons still matter.
* An added proof constant, copied linear input, MIX rule, or imported source equality changes the frozen ledger/doctrine.
* A finite list of ordinary equations is not a finite higher-coherence or normalization theorem.

## 8. Exact remaining obligations and next test

The pure bridge and identification of the pure unit extension remain verification obligations: §5 supplies informal candidate arguments, not independently accepted dependencies. In particular, check the inverse interpretation against every pure equation schema, raw dual-type boundary comparisons, composition/substitution naturality, and the universal-property identification of u. The mixed SC obligations are:

1. **Mixed linear conservativity:** for every original X,Y and pure MLL boundary b, prove that `j_X:T₀(i b)→A*(i b)` is bijective, with cut/substitution naturality, under E₀/E*. Equivalently, after §5.5, prove v_X bijective on these old hom-sets. Alternatively refute it by a typed nonimage class or equality witness. The pure arguments do not discharge this.
2. **Mixed nonlinear conservativity:** prove the frozen native NJ bijection against all E* interiors. A theorem for the implicational Girard translation is insufficient without an exact comparison preserving products and the complete ambient doctrine. The standard free-CCC/unit-type comparison is only a pure starting point, not the mixed recovery theorem.

Either can be formulated as equality-stable pure-boundary recovery G with `Gi_S=id` and `i_SG=id`, naturally under the frozen substitutions/cuts. The finite-schema clause has the separate extraction in §5.4. No remaining obligation is a permission to change the target or source equality.

The **smallest immediate positive/negative test** is this fixed instance of the original claim, not a repaired version:

```text
Let B=A*(∅,{p}) with exactly the frozen D* and E*.
Every t∈B_L(∅ | p ; p) is E*-equal to id_p.
```

The source hom at this atomic boundary has exactly the single axiom class. Thus the displayed proposition is exactly the singleton-boundary fullness obligation; it permits every mixed interior. A negative result refutes frozen SC. A positive result settles only this instance and does not establish all of SC.

**Instructions for a later constructive investigator:** prove the displayed proposition by a sound pure-boundary reduction/recovery or an exactly matching published theorem. Give the full typing and explain why every E* generator used is respected. Do not replace B by modal-free proofs or add normalization assumptions. Stop at this lemma and report its limited reach.

**Instructions for a later adversarial investigator:** construct `t:∅|p;p` in exactly B and prove `t≠id_p`, preferably by a sound separating D* model. All intermediate modalities/units are allowed, but no proof constants, MIX, extra equations, or altered atom map. A failed search or a non-normal representative is insufficient. Stop at a certified witness or report the precise unresolved equality. These instructions commission no agents now.

The named primary-source statements have been checked; their composition does not supply the missing mixed lift. A broader claim that no such theorem exists elsewhere is unwarranted. If a further exact published theorem/comparison covers SC, cite it and stop duplicate work. If a fixed witness refutes it, record that failure without modifying SC. Otherwise attempt only the displayed test and then the general residual obligations after the appropriate research gate, without declaring the claim novel or established to be open.

## 9. Relationship to ProofBasis and completion record

A successful SC result would certify one interacting finite grammar for Cartesian constructive and classical multiplicative linear proof identity, with their different resource permissions. It would not cover arbitrary foundations, dependent telescopes, cyclic validity, universal legitimacy of imported rules, minimality, causal histories, or higher equality. A refutation here would concern this D*, E*, and these canonical maps; it would not refute every finite core.

Repository instructions, the canonical plan, the S2 comparison/integration reports, 017–021, and Tasks 015–016 were read. All original texts in §4 were obtained. Inspected passages include HS's equivariance/cut-permutation proof; Shulman's universal-morphism definitions, cone construction, complete §8 rules/quotient and doctrine-map theorem; the envelope theorem's definition/proof setup and gluing warning; Hughes's net composition/rewiring/freeness statements; van Glabbeek–Hughes's multiplicative commutations and cut-free theorem; and Hasegawa's full-completeness statements, syntax, and translation/equality definitions. No source report, task, charter, plan, dependency declaration, or tracked experiment output was altered. No new mathematical claim is FORMALIZED.

Primary PDFs and extracted text are scratch evidence outside the repository. The seven sources were read directly rather than promoting previous reports' evidence labels. Verification of published statements and a bounded informal comparison proof are distinguished from a mechanically checked or independently refereed new result. The surviving uncertainty is mathematical: full mixed pure-boundary recovery/equality conservativity.

**Decision: UNRESOLVED FROZEN CLAIM.**


## 10. Coordinator review supplement — 2026-10-14

Status: **reviewed as research evidence; pure prerequisite arguments pending independent verification**. This supplement and the status corrections above do not change the frozen SC, D*, E*, source equality, or canonical maps. The independent-check obligation is not a requirement to mechanize every argument. The pure bridge, the unit-extension identification, and finite-schema extraction must retain their INFERENCE status until accepted on their actual arguments.

The next bounded investigation is [Task 017](../../tasks/017-atomic-endomorphism-test.md). Its atomic source hom-set is independently the singleton identity class; testing the mixed target at that boundary does not depend on accepting N≅T₀ or full faithfulness of u. A certified negative instance refutes SC for the fixed doctrine; a positive result settles only the displayed instance, not full SC. No unrestricted universal-existence work or implementation is authorized.
