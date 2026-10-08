# Notes [pol]: polarization / continuations / faithful proof-identity semantics

Question tested: the report says that preserving proof identity across classical, intuitionistic and linear logic
forces a fixed framework to contain each foundation's structure as independent primitives. It cites the Joyal/Došen
collapse (CCC + initial ⊥ + natural ¬¬-elimination ⇒ preorder) as the obstruction. We check whether a small core
logic or a fixed semantic universe is known into which several foundations translate faithfully on proof identity.

Downloads: `scratchpad/review/dl/pol/` (pdf + pdftotext -layout .txt). All page numbers refer to the version retrieved.

---------------------------------------------------------------------------------------------------------------------

## S1. Girard, "A new constructive logic: classical logic", MSCS 1(3):255–296, 1991 (LC)
- DOI (from Crossref metadata, not from the document): 10.1017/S0960129500001328.
- Status: **NOT_ACCESSED**. Semantic Scholar marks it CLOSED. It is not on Girard's current homepage
  (girard.perso.math.cnrs.fr; the old URLs return 404, and Wayback returned 403/429).
- SECONDARY_ONLY (Laurent, TLCA'99 "Polarized Proof-Nets: Proof-Nets for LC", lcpn.pdf p.1 §1): "Gentzen's classical
  sequent calculus LK has well known problems, such as the lack of a denotational semantics and the non determinism
  of cut-elimination. J.-Y. Girard proposed in [4] the calculus LC as a refinement of LK to solve these defects. The
  key point is the introduction of polarities for formulas."
  Laurent quotes Girard's open problem: "Find a better syntax (which would be to LC what typed λ-calculus is to LJ)
  for normalization [...] A kind of proof-nets could be the solution".
- SECONDARY_ONLY (Laurent thesis 2002, Prop. 10.1, p.146): through the translation (.)•, LLP reduction simulates LC
  reduction. Corollary 10.2: "Tout modèle dénotationnel de LLP fournit un modèle dénotationnel de LC." Laurent notes that
  LC cut-elimination "n'est pas décrite en détails" in [Gir91a]. Melliès (PRIMS 2016, p.~366) says LC's semantics are
  correlation spaces.
- How the Joyal collapse is avoided (UNVERIFIED-MEMORY plus the secondary sources above): polarities plus a
  non-cartesian (coherence-space / correlation-space) model. The semantics is not a CCC with an initial object and an
  invertible natural ¬¬, so the collapse hypotheses fail. I did not read Girard's own statement.

## S2. Girard, "On the unity of logic", APAL 59:201–217, 1993 (LU)
- DOI (Crossref metadata): 10.1016/0168-0072(93)90093-S.
- Status: **NOT_ACCESSED**. ScienceDirect returned 403 to curl, although Semantic Scholar lists a "BRONZE" open-access
  PDF at sciencedirect…/pii/016800729390093S/pdf. Not cited in any of the texts I retrieved except as a bibliography
  entry (AJ 1994 [Gir91b], Laurent TLCA99 [6]).
- UNVERIFIED-MEMORY: LU is a single sequent calculus whose formulas carry polarities (+, −, neutral). Classical,
  intuitionistic and linear logic sit inside it as *fragments*, with cut between fragments. Its claim is about one
  system containing all three, with a coherence-space-style denotational semantics. As far as I recall it does **not**
  claim faithfulness or injectivity on proof identity.
  **Must be checked against the paper before anyone cites it.**
- Inference: if the memory is right, LU supports the report's characterisation. Unity there is obtained by keeping the
  foundations' structure (polarities and modalities) as separate primitives inside a union system, not by reducing to a
  neutral core.

## S3. Laurent, "Polarized games", APAL 130 (2004) — long version
- Retrieved: https://perso.ens-lyon.fr/olivier.laurent/fullpolgames.pdf. Author's preprint of the long version; the
  homepage labels it "long version - APAL 2004". Status: **VERIFIED_SOURCE**.
- Abstract: "We prove a definability result for this polarized model and this gives complete game models for various
  classical systems: LC, λµ-calculus, . . . for both call-by-name and call-by-value evaluations."
- Thm 2 (Correctness), p.~19: "If π → π′ then σπ = σπ′." Soundness for cut elimination.
- **Thm 3 (Definability)**, p.19: "Let A be a polarized formula without atom, if σ is a finite total strategy on A, σ
  is the interpretation of a proof of ⊢ A in LLP."
- Prop 15 (CBN full completeness), p.~29: "Let A be a type without variable and σ be a finite total strategy on A−,
  there exists a λµ-term u of type A such that σ is the call-by-name interpretation of u."
- Prop 17 is the call-by-value analogue, obtained through Selinger's syntactic duality.
- Scope of the result:
  - "Full completeness" here means **surjectivity/definability only**. **No faithfulness (injectivity) theorem**
    appears in this paper.
  - Restricted to formulas **without atoms**. The text says "the definability result can certainly be extended to
    formulas with atoms", which is conjectural.
  - The AJM variant has only "local definability" (Thm 4).
  - Negative result in the paper (p.~18): "The HO game model we have obtained for MALLP is not fully complete" (a
    pseudo-contraction is not definable).
  - The same polarized games are only a *denotational model* of ILL (Cor 3.1, after McCusker, Prop 3). No ILL full
    completeness or faithfulness is claimed here.
  - Appendix B, Def 19 (Laurent's paraphrase of Selinger): a control category has a CCC (C,&,⊤,→); "(C,`,⊥) is a
    symmetric premonoidal category ... with codiagonals"; ` distributes over &; A→(B`C) ≅ (A→B)`C.

## S4. Laurent, "Syntax vs. semantics: a polarized approach", TCS 2005
- Retrieved: https://perso.ens-lyon.fr/olivier.laurent/synsempol.pdf, a preprint dated January 20, 2005. Venue from
  Laurent's homepage list ("TCS 2005"); no DOI is printed in the preprint. Status: **VERIFIED_SOURCE**.
  **This is the most decisive positive source I found.**
- Abstract: "We present a notion of sliced proof-nets for the polarized fragment of Linear Logic and a corresponding
  game model. We show that the connection between them is very strong through an equivalence of categories (this
  contains soundness, full completeness and faithful completeness)."
- Intro, p.1–2, verbatim:
  - Scope: "the polarized propositional fragment of linear logic LLpol (with all the connectives and the units) and a
    polarized game model".
  - Expressiveness: "our setting is expressive enough to encode propositional classical logic with all connectives
    [23, 20]".
  - The three claims:
    - "Each object of the model is isomorphic to the interpretation of a formula."
    - "Each morphism of the model is the interpretation of a proof."
    - "The interpretations of two proofs are the same iff these proofs are βη-equal (with a canonical representative
      in each class of βη-equivalence given by cut-free sliced proof-nets)."
- Thm 2 (Full completeness): "Let σ be a finite total label-balanced strategy on the arena Γ⋆, there exists a proof π
  of ⊢ Γ in LLpol such that π⋆ = σ."
- **Thm 3 (Faithful completeness)**: "If R1 and R2 are two cut-free sliced proof-nets such that R⋆1 = R⋆2 then
  R1 = R2."
- Thm 4: "There exists an equivalence of categories between the syntactical category of sliced proof-nets and the game
  category."
- Cor 4.2: "There exists an equivalence of control categories between the syntactical category of sliced proof-nets
  and the game category." Prop 10: both are control categories.
- Hypotheses and scope:
  - Propositional only. Second order is named as future work: "not very problematic on the syntactical side but more
    tricky for the game model".
  - LLpol formulas: P ::= !X | 1 | 0 | P⊗P | P⊕P | !N, with dually negative formulas. Atoms occur only under shifts.
  - Proof identity is βη on *sliced* proof-nets, i.e. a chosen equational theory. Laurent says himself that the
    novelty is limited: "We do not claim that this paper contains completely new ideas".
- Inference (F01/F04): a nondegenerate classical proof-identity theory (LLpol βη, which hosts classical logic via
  polarization) has a **fixed semantic universe (polarized HO games) that is fully complete and faithful**. This
  directly refutes using the Joyal collapse as an obstruction to faithful classical proof semantics. It covers one
  family (polarized classical/linear) only, **not intuitionistic + linear + classical simultaneously with faithfulness
  for each**.

## S5. Laurent & Regnier, "About translations of classical logic into polarized linear logic", LICS 2003
- Retrieved: https://perso.ens-lyon.fr/olivier.laurent/clpll.pdf (author version). Status: **VERIFIED_SOURCE**.
- Abstract: "Firstly we build a categorical model of classical logic (a Control Category) from a categorical model of
  Linear Logic by a construction similar to the co-Kleisli category. Secondly we analyse two standard
  Continuation-Passing Style (CPS) translations, the Plotkin and the Krivine's translations, which are shown to
  correspond to two embeddings of LLP into LL."
- Simulation property, p.~2: "all of them are reduction preserving" (t → t′ implies |t| →* |t′|).
- Thm 4.1: "Up to some axiom reductions and some η-expansions the following diagrams commute". This states that
  Plotkin CPS corresponds to the box translation (.)^b and Krivine CPS to the reversing translation.
- Thm 5.1 (Hofmann–Streicher / Selinger): ⟦t⟧_{R^C} = ⟦t*⟧_{(C,R)}. Thm 5.2 is the Krivine analogue.
- **No faithfulness or reflection-of-equality theorem is stated.** The results are preservation, simulation and
  commuting diagrams up to axiom reductions and η.
- Open question in the paper: "whether this game model is related to the first author's one for LLP".
- Inference: this gives evidence that CPS translations factor through a small core (LLP → LL), with derivability and
  reduction preserved. Reflection of proof identity is **not established** by this source.

## S6. Laurent, thesis "Étude de la polarisation en logique", Aix-Marseille II, 2002
- Retrieved: https://perso.ens-lyon.fr/olivier.laurent/these.pdf. Status: **VERIFIED_SOURCE (partial read; French)**.
- Ch.6: control categories (Selinger) are shown to give categorical models of LLP, and correlation spaces from
  [Gir91a] extend to LLP.
- Prop 10.1 (Simulation): LLP reduction simulates LC reduction through (.)•. Cor 10.2: every denotational model of LLP
  gives one of LC. §10.1.4 gives an inverse translation (.)◦ from LLP to LC.
- I found no injectivity/faithfulness claim by grepping (searched "fid", "injectiv"; ligature loss may hide hits).
- "Joyal" does not appear.

## S7. Selinger, "Control categories and duality ...", MSCS 11:207–260 (2001)
- Retrieved: https://www.mathstat.dal.ca/~selinger/papers/control.pdf. Journal version, as printed: "Math. Struct. in
  Comp. Science (2001), vol. 11, pp. 207–260". Status: **VERIFIED_SOURCE**.
- Definition 2.11 (p.~10):
  - Setting: P is "a distributive symmetric premonoidal category with codiagonals" that is "also cartesian-closed".
  - Condition: it is "called a control category if s_{A,B,C} : B^A ` C → (B ` C)^A is a natural isomorphism in A, B,
    and C, satisfying the following coherence conditions" (`` ` `` here is par).
  - **So a control category *is* a CCC.** ⅋ is only premonoidal.
- Lemma 2.7: "In P♯, the object ⊥ is initial, and # is a coproduct". Initiality holds only in the *focus* subcategory,
  not in P.
- §3.4 "A remark on consistency":
  - Lemma 3.7: "There is no central morphism f : 1 → A, unless A ≅ 1."
  - **Cor 3.8**: "A control category in which # is bifunctorial is equivalent to a boolean algebra."
  - Proof: "If # is bifunctorial, then all morphisms are central. ... the category is equivalent to a poset".
  - The text before it compares with Lambek–Scott: "in a bicartesian closed category, there is no arrow A → 0 unless
    A ≅ 0".
  - The name Joyal does not appear.
  - Inference: the collapse is avoided by (i) ⊥ not being initial in P, only in the focus, and (ii) ⅋ being
    non-bifunctorial (premonoidal).
- Thm 3.18 (Structure Theorem): "Any control category P is equivalent to a category of continuations R^C."
- **Prop 6.5 (Soundness and Completeness)**: "The theories induced on the λµ-calculus by the call-by-name categorical
  interpretation are precisely the theories induced by the call-by-name CPS translation." Prop 7.6 is the CBV analogue.
- Thm 6.12: T is a CBN theory iff it is a congruence satisfying Table 6. CBN λµ is an internal language for control
  categories; CBV λµ is the internal language for co-control categories.
- Duality: "syntactic translations ... which are mutually inverse and which preserve the operational semantics".
- Inference: there is a faithful (complete) CPS semantics of classical λµ proof identity in categories of
  continuations over arbitrary C. This is "reflection" at the level of all models / the term model. **But CBN and CBV
  are two different proof-identity theories**, which matters for F04: classical proof identity is a parameter, not
  canonical.

## S8. Melliès & Tabareau, "Resource modalities in tensor logic", APAL 161 (2010)
- Retrieved: http://www.irif.fr/~mellies/papers/resource-modalities-apal.pdf. Version: preprint/author copy with no
  journal header. Status: **VERIFIED_SOURCE**.
- Abstract: "tensor logic, a primitive variant of linear logic where negation is not involutive."
- Intro: "tensor logic is to linear logic what intuitionistic logic is to classical logic"; linear logic is "a
  'depolarized tensor logic'".
- Prop 1 (attributed to Hasegawa): for a dialogue category, the following are equivalent:
  - the continuation monad is commutative;
  - it is idempotent;
  - the Kleisli category with the inherited premonoidal structure is ∗-autonomous.
  "This result demonstrates that linear logic is essentially the same thing as tensor logic where the tensorial
  negation is commutative".
- Thm 1: a model of propositional tensor logic (MAE) with a commutative continuation monad gives a model of LL (Kleisli
  category C_T).
- Prop 3 / Prop 4: "Every proof of the sequent ⊢ A1,...,Ak in linear logic induces a proof of the sequent
  (A1)N,...,(Ak)N ⊢ in tensor logic" and the converse.
  - **These are derivability (preserve + reflect provability), not proof identity.**
  - The converse map "remove[s] all the logical steps introducing a shift operator". There is no round-trip or
    injectivity statement.
- On classical logic and polarized LL: a response category (Selinger) "is the same thing as a model of multiplicative
  additive tensor logic, where the tensor ⊗ is cartesian". LLP "happens to coincide with the multiplicative additive
  fragment of tensor logic, where the tensor product is cartesian".
- Conclusion: "linear logic coincides with tensor logic with the additional axiom that the continuation monad is
  commutative."
- Inference (F03/F04): in this "primitive" core, the foundations differ by **equational/structural axioms**
  (commutativity of ¬¬, cartesianness of ⊗), not by new connectives. That supports a *small core plus a per-foundation
  equational theory*. It also shows that the per-foundation equations do real work: they quotient proofs. No
  faithfulness across foundations is claimed.

## S9. Melliès, "Dialogue categories and chiralities", Publ. RIMS 52 (2016) 359–412, DOI 10.4171/PRIMS/185 (printed)
- Retrieved: https://ems.press/content/serial-article-files/41280 (journal version). Status: **VERIFIED_SOURCE**
  (intro read).
- Main results are coherence theorems (Thm 1, Thm 2, main theorem §7.5): 2-equivalences between dialogue categories
  and dialogue chiralities. These are **not faithfulness or full-completeness theorems for logics**.
- Unifying claim (p.~366): the difference between logics lies in "the algebraic nature of the conjunction and of the
  disjunction connectives ... actions ... in the case of intuitionistic logic, whereas they are tensor and cotensor
  products ... of a ∗-autonomous category C in the case of linear logic, and finite products ∧ and finite sums ∨ of a
  boolean algebra in the case of classical logic."
  - Note: here classical logic is modelled by a *boolean algebra*, i.e. proof-irrelevant, consistent with the
    collapse.
- Also: "polarities are entirely independent of the intuitionistic or classical nature of the underlying logic".
- Inference: this is a conceptual unification (one shape, the chirality), but the foundations are distinguished by
  different algebraic structure. It does not give a faithful common target.

## S10. Abramsky & Jagadeesan, "Games and full completeness for multiplicative linear logic"
- Retrieved: arXiv:1311.6057v1, the Imperial College Technical Report DoC 92/24 (not the JSL 59 (1994) version).
  Status: **VERIFIED_SOURCE** (tech report version).
- Definitions, p.4: "Full Completeness: Any f : A → B is the denotation of a proof of A ⊢ B. (This amounts to asking
  that the unique functor from the relevant free category to C be full ...). One may even ask for there to be a unique
  cut-free such proof, i.e. that the above functor be faithful."
- Thm 1 (§4.5): "If σ is a uniform history-free winning strategy for Γ, then it is the denotation of a unique proof net
  (Γ, φ)."
- Hypotheses:
  - MLL **+ MIX**, **without units** (§2.1 explains why units are omitted).
  - Strategies must be uniform and history-free.
- Inference: the original full and faithful result is for a tiny fragment, and it needs MIX (a non-standard proof
  identity / derivability extension).

## S11. de Carvalho & Tortora de Falco, "The relational model is injective for MELL (without weakenings)"
- Venue: APAL 163(9):1210–1236 (2012), per the citation in de Carvalho 2016.
- Retrieved: arXiv:1002.3131v2. Status: **VERIFIED_SOURCE** (arXiv version).
- Abstract: "for Multiplicative Exponential Linear Logic (without weakenings) the syntactical equivalence relation on
  proofs induced by cut-elimination coincides with the semantic equivalence relation on proofs induced by the multiset
  based relational model ... two cut-free proofs of the full multiplicative and exponential fragment of linear logic
  whose interpretations coincide in the multiset based relational model are the same 'up to the connections between
  the doors of exponential boxes'."
- Corollary 3: "Assume A is infinite. Let R and R′ be two MELL nets without weakening nor ⊥ links. If ⟦R⟧ = ⟦R′⟧, then
  R and R′ have the same (cut-free) normal form."
- Hypotheses:
  - The atom set A is infinite.
  - No weakening and no ⊥.
  - Connected nets (the correctness criterion is acyclic and connected).
  - Untyped framework; holds also for typed nets with atomic axioms (Remark 6).
- Negative result recalled in the paper: the coherence model is **not** injective for MELL [Tortora de Falco 12, 13].
- Follow-up: de Carvalho, "The relational model is injective for MELL", arXiv:1502.02404v4 (VERIFIED_SOURCE, arXiv).
  - Abstract: "the equality between MELL proof-nets in the relational model is exactly axiomatized by cut-elimination."
  - Theorem 9: "Let R and R′ be two PS's s.t. P_f(R) = P_f(R′). If ⟦R⟧ = ⟦R′⟧, then R ≡ R′." The intro states
    ⟦R⟧ = ⟦R′⟧ ⇔ R ≃β R′.
  - Journal venue: not verified.
- Inference: Rel is a **fixed semantic universe** that is injective for MELL proof-nets. Rel is also a model of λ/ILL
  (via Girard's translation) and of LLP/LC (via polarized translations). However:
  - I saw no theorem that the composite translation (e.g. STLC/λµ → MELL → Rel) is injective.
  - Injectivity requires faithfulness of the translation into nets *and* of Rel. The first factor is not established
    in these sources.
  - Rel is **not** fully complete: it has non-definable relations (UNVERIFIED-MEMORY, standard).

## S12. Hasegawa, "Classical linear logic of implications", MSCS 15(2):323–342 (2005)
- DOI 10.1017/S0960129504004621 (Crossref). CSL 2002 version: LNCS, DOI 10.1007/3-540-45793-3_31.
- Retrieved: kurims.kyoto-u.ac.jp/~hassei/papers/clli.pdf, the MSCS preprint "Under consideration ... Received 16
  December 2003; revised 30 June 2004". Also csl02.pdf. Status: **VERIFIED_SOURCE**.
- Direction of translation: it encodes **intuitionistic** linear logic (DILL) **into** classical linear logic (DCLL),
  not the converse.
- Thm 3.1: "All equations derivable in DILL are derivable in DCLL via the encoding." **Soundness only. No conservativity
  or faithfulness claim.**
- Thm 4.1: DCLL is "sound and complete for categorical models given by ∗-autonomous categories with linear exponential
  comonads".
- Prop 6.3: DCLL "is identical to the single conclusion-fragment of µDCLL as a typed equational theory". This is an
  equational isomorphism between two classical-linear presentations.
- Thm 7.1: full completeness of the {→,⊸}-fragment inside the {!,⊸}-fragment of ILL. The text also says (−)◦ is
  "equationally sound and complete (two terms in the source calculus are equal if and only if their translations are
  equal in the target)". This is faithful, but **within intuitionistic linear logic**.
- Thm 7.2: DILL into second-order {→,⊸}: soundness only.
- Author's caveat: "the relationship between the semantic structure of Classical Linear Logic and that of Second-Order
  Intuitionistic Linear Logic is far from obvious; the full story seems yet to be developped."
- Inference: whether ILL → CLL is conservative on proof identity is not settled in this source.
  - UNVERIFIED-MEMORY lead: there are results that free SMCCs embed fully and faithfully into free ∗-autonomous
    categories (Chu/Hasegawa-style). Needs a separate check.

---------------------------------------------------------------------------------------------------------------------

## Synthesis (inference, labelled)

1. **The Joyal collapse is not an obstruction to faithful classical proof semantics in a fixed universe.** It is an
   obstruction only under its hypotheses: a CCC, ⊥ initial in the whole category, and ¬¬ naturally invertible.
   - Selinger's control categories are CCCs that avoid it by a premonoidal ⅋, with ⊥ initial only in the focus.
     Cor 3.8 shows exactly that restoring bifunctoriality re-collapses.
   - Laurent 2005 (S4) gives a fully complete **and faithful** polarized game model (an equivalence of control
     categories) for LLpol, which encodes propositional classical logic.
   - Rel is injective for MELL (S11).
   - So the report overstates if it cites the collapse as an obstruction to *any* faithful common framework. It is an
     obstruction to a common *cartesian-closed, bifunctorial, ⊥-initial* semantics only.
2. **No source I read proves one target that is simultaneously faithful (preserve + reflect proof identity) for
   classical + intuitionistic + linear.** The faithful results found are each for one system:
   - LLpol in games;
   - MELL in Rel;
   - MLL+MIX in AJ games;
   - CBN λµ in categories of continuations (one CBN/CBV choice at a time).
   Polarized games model ILL denotationally only (S3). Tensor logic relates LL to itself by derivability only (S8).
   Laurent–Regnier give simulation, not reflection (S5).
3. **Every unification found achieves unity by fixing per-foundation structure as extra data**: polarity/shift
   connectives (LC, LU, LLP), choice of CBN vs CBV translation (two distinct proof-identity theories, S7), or extra
   equational axioms (commutative or idempotent continuation monad, cartesian ⊗; S8, S9). This partially supports the
   report's claim in a weaker form: foundations differ by *equational theory and structural axioms on a small
   signature*, which is F03/F04 territory. It is not quite "independent primitives". The required axioms then live in
   the environment/theory, so they must be trusted.
4. Girard's own LC/LU texts were NOT accessed. The claims about how they avoid collapse rest on secondary sources and
   memory.
