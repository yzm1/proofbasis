# Task 016 — Pure MLL bridge and mixed-core conservativity

**2026-10-14. Baseline:** main `bb2dd041a7c68acb175b6591721cbd282eeb8d9c`. The frozen proposition is [017 §6/Card SC](017-structural-contract-repair.md), critically restated in [020 §8](020-cross-review-by-adversarial-agent.md) and selected in [021](021-s2-r2-selection.md). This report changes none of those documents. No additional agents, implementation, or unrestricted S3 investigation were launched.

**Evidence convention:** VERIFIED_SOURCE means the primary passage was inspected in this task. INFERENCE means an informal mathematical argument given here, not a mechanically checked result. REPOSITORY_EVIDENCE means an earlier report's source assessment, not fresh verification. UNKNOWN marks an undischarged obligation. In particular, a blocked download is not evidence that a theorem does not exist.

## 1. Executive mathematical verdict

**The frozen SC conjunction is unresolved by this investigation.** No well-typed counterexample was established, and no verified composition of published theorems closes it. There is a concrete pure-net comparison argument: tensor/par factorization is root-par insertion/removal, and dual factorization rotates an unchanged labeled forest. This removes the need to posit a physical unit or forget occurrence labels in the proposed pure bridge. Its identification with the *entire* specified Shulman quotient still needs the primary-presentation audit stated below.

The mixed assertion remains separate. Neither the net factorization argument nor virtual-unit freeness supplies recovery of all mixed-target proofs or invariance under all mixed equations. An adjunction triangle cancels one actual modal/unit detour; a finite-vector-space LNL model separates two actual axiom matchings. These are proved instances, not a conservativity theorem.

**Access limitation affecting completion of the gate:** the Heijltjes–Straßburger original author PDF was obtained and read. The running environment denied arXiv HTTPS with HTTP 403 at the proxy. The other original papers listed below were not freshly inspected. Their theorem correspondence entries are explicitly provisional. This is a partial gate result awaiting source access, not a completed primary-literature audit or a claim of mathematical novelty.

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

Only the first row below is freshly VERIFIED_SOURCE. Remaining rows record the exact leads in 019–020; none is used as a freshly verified theorem premise in this report.

| Primary source and location | Mathematical content and hypotheses | Correspondence and remaining mismatch |
|---|---|---|
| Heijltjes–Straßburger, *Proof nets and semi-star-autonomous categories*, MSCS 26(5), 789–828 (2016), author PDF: Defs. 2.1–2.5, Props. 2.3/2.6, Defs. 3.1/5.1/5.8, Prop. 5.7, Thm. 5.10 (PDF p. 19), proof on pp. 22–23 | Annotated, unit-free forests; connected and acyclic switchings; LM has axiom/tensor/par and no MIX. Cut is admissible and preserves the net. The free net category extends an atom functor into a **∂-strict** semi-star-autonomous category uniquely up to natural isomorphism. An ssa functor is a pair `(G,γ)` preserving virtual-unit data and λ, not just an ordinary functor. | Strong original freeness input for nonempty profiles. Its unary category and virtual-unit functor must be compared with the chosen polycategory. It is not a theorem about F/U, nonlinear CCC structure, or SC. The paper explicitly excludes an empty-conclusion case from its cut-cut permutation discussion (Lemma 8.1, PDF p. 29). |
| Shulman, *LNL polycategories and doctrines of linear logic*, LMCS 19(2:1) (2023), Defs. 2.1/2.10/2.14, Thm. 7.4, §8/Figure 2/Prop. 8.3 and quotient paragraph; [original PDF](https://arxiv.org/pdf/2106.15042) | REPOSITORY_EVIDENCE: free completion and its quotient syntax, with context-parametric universal operations; §8 restricts the general doctrine setting. | Must audit every pure/mixed equation and the chosen cones. A free-completion universal property alone does not establish either source adequacy or doctrine-change conservativity. Finite-schema extraction and exact quotient matching remain unverified here. |
| Shulman, *Star-Autonomous Envelopes and Conservativity*, EPTCS 353 (2021), Thm. 10.1, Cor. 10.6, Remarks 7.7/10.7; [original PDF](https://arxiv.org/pdf/2004.08487) | REPOSITORY_EVIDENCE: full/faithful universal star-autonomous extension of a small symmetric polycategory preserving designated existing tensors/cotensors; a separate SMCC consequence. | The proposed application is u, after checking its universal-property identification. No nonlinear zone, F/U, or added nonlinear atom set is in this reported theorem. The older internal-hom-preservation gap flagged in Remark 10.7 must not be ignored in a gluing argument. |
| Hughes, *Simple free star-autonomous categories and full coherence*, Thm. 3 and unit-rewiring definition; [original PDF](https://arxiv.org/pdf/math/0506521) | REPOSITORY_EVIDENCE: free star-autonomous category via linkings modulo unit rewiring. | Relevant to T₁ and labeled matching at unit-free boundaries. Its target is not A*. No absolute label-equality algorithm is inferred for arbitrary base categories. |
| van Glabbeek–Hughes, *MALL proof nets identify proofs modulo rule commutation*, §2, Tables 2–4, Thm. 1; [original PDF](https://arxiv.org/pdf/1609.04693) | REPOSITORY_EVIDENCE: cut-free unit-free MALL net equality iff rule commutations, with or without MIX, tracking occurrences. | The no-MIX multiplicative restriction is the frozen source comparison. It is not a statement about E₀ or E*. Cut compatibility requires a further argument. |
| Hasegawa, *Categorical glueing and logical predicates for models of linear logic*, reported Thms. 5.2/5.3/5.6; [author PDF](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/full.pdf) | REPOSITORY_EVIDENCE: specified MILL→MLL, relatively free classical extension, and MILL→DILL full-completeness results. | Cannot compose two extensions from a common source into a theorem about their common mixed extension. Check the classical gluing proof against Shulman's Remark 10.7 and verify modal/internal-hom preservation. |
| Hasegawa, *Girard translation and logical predicates*, JFP 10(1) (2000), Props. 3.1/3.3/3.4, Lem. 3.2, Thm. 5.6; [primary article](https://doi.org/10.1017/S0956796899003615) | REPOSITORY_EVIDENCE: arrow-STLC βη, substitution, equality reflection, and fullness at its specific dual-context translated boundaries. | A genuine full-completeness lead, but neither the native nonlinear product/implication boundary map nor classical MLL in full D*. |

The HS source was obtained from the [author's website repository](https://github.com/willemheijltjes/willemheijltjes.github.io/blob/25044f45477b9a2fdf0d4fb09de5b6d4400b8640/pdf/2016-heijltjes-strassburger.pdf), whose publication entry identifies the article and DOI `10.1017/S0960129514000395`. PDF SHA-256: `f26b991401baf30a72d6da0c7724b4e4766a0b9150d2c674f3426be03264d3fe`. Use this version's **Theorem 5.10**, rather than the earlier manuscript's Theorem 5.21 cited in 020. This is a version distinction, not a different theorem claim.

## 5. Explicit pure-net bridge argument

**INFERENCE; the following is a direct comparison argument for the structural/universal presentation described in the frozen reports. Its certification for the complete published E₀ requires the source audit in §8.** It does not invoke a blanket equivalence between arbitrary semi-star-autonomous categories and all empty-profile polycategories.

### 5.1 Factorization maps

Represent `N(Γ;Δ)` by the forest `Γ^⊥,Δ` with its labeled axiom matching. The following are explicit inverse maps, retaining every old leaf label:

```text
N(Γ,A,B;Δ)  ≅ N(Γ,A⊗B;Δ)
N(Γ;Δ,A,B)  ≅ N(Γ;Δ,A⅋B)
N(Γ,A;Δ)    ≅ N(Γ;Δ,A^⊥).
```

For the first bijection the new input tensor is a **par root in the negative forest**. For the second it is a positive par root. Insert/remove that root. In each switching it has exactly one retained edge, so it is a pendant vertex. Adding it to a tree preserves connectedness/acyclicity; removing it leaves the same old tree. The atomic matching is unchanged, so the maps are inverse on proof classes, not just on inhabitation. Dual rotation leaves the normalized one-sided forest unchanged. These maps apply at every remaining linear context, not only unary homs.

The tensor universal morphism `A,B→A⊗B` is the tensor of the two expanded identities. The par universal morphism `A⅋B→A,B` is its dual counterpart. Cutting with them performs the displayed root-removal operation: path composition through their identity links joins precisely the original corresponding leaves. Dual evaluation and coevaluation are the rotations of the expanded identity. Thus the factorization β/η equations hold by the actual inverse maps.

Cut naturality follows directly: on an unrelated port, root insertion/removal changes no alternating linking path. Identity, associativity, exchange, and interchange have the same path description. HS Def. 2.5 and Prop. 2.6 supply the verified linking-composition/cut-admissibility input. This accounts for each *kind* of base and tensor/par/dual universal equation described in the frozen E₀; it is not an assertion that an unread presentation contains no additional generator.

### 5.2 Empty and virtual-unit profiles

The frozen source has `N(;)=∅`: no axiom or final MLL rule proves the empty sequent. Do not deduce a contrary inhabitant from a convention declaring the empty graph connected. Sequentialization (HS Prop. 2.3) connects correctness to LM proofs, and cut admissibility preserves that source restriction.

The factorization operations above always replace a nonempty formula occurrence or pair by another nonempty occurrence. None turns a nonempty profile into the empty profile. The generating universal arrows themselves have nonempty profiles. N with this empty hom-set is therefore a candidate model of the stated pure structural/universal operations; it does not install an empty proof constant.

Its virtual unit is **the set** `I_v(A)=N(;A)`. The canonical map `I_v(A^⊥⅋B)→N(A;B)` removes the root par; this is exactly the λ described in HS Prop. 5.7. It does not introduce a physical linear unit object. Arbitrary nonempty multiport profiles can likewise be bundled by par-root insertion with specified bracketing. The empty profile is handled separately rather than hidden in such bundling.

### 5.3 Candidate two-sided inverse

If the audited E₀ has precisely these structural and universal operations, the net model gives a structure-preserving interpretation `R:T₀→N` fixing atoms. The canonical constructor interpretation i sends atomic axiom to dual coevaluation, tensor to composition with its universal morphism, par to factorization, and cut to typed composition.

For independent par/tensor commutations, naturality of inverse factorization on the untouched port and interchange give the equation in T₀. Par/par commutations commute two root insertions. Tensor/tensor commutations are interchange together with the derived associativity/symmetry maps, always tracking the original ports. A principal tensor/par cut cancels the matching factorization and reduces to its constituent cuts; atomic cuts use the identity law. These calculations give the proposed interpretation of the frozen source equations and cut reductions, rather than interpreting raw sequent trees as inert constructors.

On source nets `Ri=id`: all leaf links are retained, and sequentialization supplies the constructors. On generated target proofs the proposed proof of `iR=id` is induction on the **full** audited generator list: universal morphisms are fixed; factorization is fixed because it is the unique inverse to the same cut map; structural operations/cuts are preserved. For raw dual expressions this is equality after the canonical boundary isomorphisms, not a new strict double-dual equation. At the translated, De-Morgan-normalized source formulas the chosen comparison uses those frozen isomorphisms.

This is a concrete way to discharge the pure bridge **once the complete E₀/cone comparison is checked**. It would give equality preservation/reflection, intrinsic fullness, and substitution/cut compatibility at the original boundaries, including the empty profile. It contains no F/U recovery and consequently proves nothing about j by cancellation.

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

with the usual empty products and linear units. The nonlinear homs are the corresponding FinSet maps. These universal properties supply the stipulated D* operations. Additional equalities in this model are allowed; no equation requiring compact closure is added to the free target.

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

Their types are those of the displayed bijections; `cut_N` substitutes into a nonlinear slot. Thus these cancellation/reconstruction tests quantify over admissible ambient contexts, and do not restrict their proofs to modal-free interiors. They still do not eliminate arbitrary interleavings with the other universal operations. Checking every published equation, including nonlinear terminal/product/hom and linear unit/counit reconstruction, is the unresolved audit/recovery requirement rather than an assumed consequence of these four equations.

Let `f:I_L≅F1_N` be the canonical strong-monoidal unit isomorphism, η the adjunction unit, and ε its counit. Then

```text
s = f⁻¹ ∘ ε_(F1_N) ∘ Fη_(1_N) ∘ f : I_L→I_L,
h = ρ_p ∘ (id_p⊗s) ∘ ρ_p⁻¹        : p→p.
```

All arrows type; the intermediate object is `FUF1_N`. The F⊣U triangle gives `s=id_I`, hence `h=id_p`. Naturality of the unitors makes this equality stable when inserted into any appropriate larger proof. This is an equation in the full mixed congruence; it neither assumes `FU=id` nor forbids mixed interiors.

In contrast, promoting the linear identity `p→p` directly to a nonlinear proof of Up is ill typed: U factorization requires an empty linear input and a single linear output. The hypothetical diagonal `p→Up→FUp→FUp⊗FUp` therefore is not an SC witness. The actual diagonal on FX is well typed, but substituting `p↦FX` changes SC's frozen atom map.

For a nonlinear identity control, the same FinSet/vector-space D* model distinguishes the two projections `p×p→p` when p is a two-element set. Product β and function η hold by their universal properties. This excludes collapse of this specific source pair under E*, without classifying all target selectors or proving the native NJ clause.

### Units and MIX

The source forests `⊢p^⊥,p⊗p` (unbalanced leaves) and `⊢p^⊥,p,q^⊥,q` (disconnected switching) have no source class. A well-typed mixed proof at either original boundary would refute SC. No such proof is exhibited here. Identifying `I_L` with its dual/counit would add an unlicensed equation; the compact-closed model above is not evidence that this identification holds in A*.

## 7. Strongest positive argument and strongest obstruction

The strongest positive argument is the explicit net model with inverse universal factorizations in §5, supported by the original sequentialization and cut statements. It exposes what an exact N→T₀ proof would check, including named occurrences, full pure cut/dual detours, virtual units, and the empty boundary. For A*, the genuine modal triangle and separating model are the strongest verified instances in this task.

The strongest obstruction is **an unproved mixed recovery/equality-conservativity step**, not a counterexample. An arbitrary target representative can alternate nonlinear hom/product factorization, F/U, duality, and unit operations. The triangle calculation covers one family of detours. Neither that calculation nor the pure net model reduces every such representative or checks every ambient equation relating representatives.

Red-team checks reject the following proposed shortcuts:

* Free initiality constructs j but gives no inverse on its old-boundary homs.
* Pure linear unit conservativity, even if its cited theorem is verified, establishes u rather than v_X.
* A faithful separating interpretation does not recover target-only inhabitants.
* No-MIX proof-net coherence does not describe mixed modal equations.
* Syntactic mixed detours are not necessarily nonimage classes: s and h above cancel.
* Strictifying the source's duality does not authorize changing the target congruence; the canonical boundary comparisons still matter.
* An added proof constant, copied linear input, MIX rule, or imported source equality changes the frozen ledger/doctrine.
* A finite list of ordinary equations is not a finite higher-coherence or normalization theorem.

## 8. Exact remaining obligations and next test

There are three separate outstanding obligations:

1. **Primary E₀ audit:** read Shulman §8 and the selected pure cones in full; check that every generator/equality is interpreted by §5, including the duality/coherence comparisons. This is a source-access/presentation obligation. It is not an assertion that unit-free MLL freeness is a new open problem.
2. **Mixed linear conservativity:** for every original X,Y and pure MLL boundary b, prove that `j_X:T₀(i b)→A*(i b)` is bijective, with cut/substitution naturality, under E₀/E*. Alternatively refute it by a typed nonimage class or equality witness. The pure argument alone does not discharge this.
3. **Mixed nonlinear conservativity and finite presentation:** prove the frozen native NJ bijection against all E* interiors, and verify the stated finite-schema extraction. A theorem for the implicational Girard translation is insufficient without an exact comparison preserving products and the complete ambient doctrine.

The **smallest immediate positive/negative test** is this fixed instance of the original claim, not a repaired version:

```text
Let B=A*(∅,{p}) with exactly the frozen D* and E*.
Every t∈B_L(∅ | p ; p) is E*-equal to id_p.
```

The source hom at this atomic boundary has exactly the single axiom class. Thus the displayed proposition is exactly the singleton-boundary fullness obligation; it permits every mixed interior. A negative result refutes frozen SC. A positive result settles only this instance and does not establish all of SC.

**Instructions for a later constructive investigator:** prove the displayed proposition by a sound pure-boundary reduction/recovery or an exactly matching published theorem. Give the full typing and explain why every E* generator used is respected. Do not replace B by modal-free proofs or add normalization assumptions. Stop at this lemma and report its limited reach.

**Instructions for a later adversarial investigator:** construct `t:∅|p;p` in exactly B and prove `t≠id_p`, preferably by a sound separating D* model. All intermediate modalities/units are allowed, but no proof constants, MIX, extra equations, or altered atom map. A failed search or a non-normal representative is insufficient. Stop at a certified witness or report the precise unresolved equality. These instructions commission no agents now.

Before deciding that a new proof attempt is warranted, unblock and complete the named primary-source audit. If an exact published theorem/comparison covers SC, cite it and stop duplicate work. If a fixed witness refutes it, record that failure without modifying SC. Otherwise retain the displayed test and the general residual obligations, without declaring the claim novel or established to be open.

## 9. Relationship to ProofBasis and completion record

A successful SC result would certify one interacting finite grammar for Cartesian constructive and classical multiplicative linear proof identity, with their different resource permissions. It would not cover arbitrary foundations, dependent telescopes, cyclic validity, universal legitimacy of imported rules, minimality, causal histories, or higher equality. A refutation here would concern this D*, E*, and these canonical maps; it would not refute every finite core.

Repository instructions, the canonical plan, the S2 comparison/integration reports, 017–021, and Tasks 015–016 were read. The original HS passages identified in §4 were read, including the proof's equivariance/cut-permutation discussion. No source report, task, charter, plan, dependency declaration, or tracked experiment output was altered. No new mathematical claim is FORMALIZED.

The arXiv access check returned proxy HTTP 403; GitHub Git reads succeeded. The prepared environment draft adds the primary-source hosts and `api.github.com`, but a draft save does not apply runtime networking or publish the environment. The source-dependent entries remain unverified until access is applied and those texts are read. This operational limitation must not be recast as mathematical evidence against SC.

**Decision: UNRESOLVED FROZEN CLAIM.**
