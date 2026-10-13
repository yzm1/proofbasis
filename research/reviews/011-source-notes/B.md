# Cluster B: algebraic theories, operads, binding and type-theoretic structure (source notes)

Session date: 2026-10-09. Downloads: `t011/dl/B/` (PDF/HTML). Text extracts: `t011/dl/Btxt/`. Nothing was executed.
The Fiore–Plotkin–Turi PostScript (`fpt_abstractsyn.ps`) was downloaded but **not** rendered, because PostScript is executable code. FPT therefore stays SECONDARY_ONLY.
Labels: VS = VERIFIED_SOURCE (text retrieved this session; location given) · SEC = SECONDARY_ONLY · MEM = UNVERIFIED-MEMORY · NA = NOT_ACCESSED.
Prior work, not repeated here: Report 010 §3 (clones, Post, Lawvere p.65/p.89, Tietze, Squier, Kelly–Lack, Fiore–Mahmoud).

---
## B1 Operads, PROPs, polycategories, generalized multicategories
1. **Objects.**
   - A PROP is a symmetric strict monoidal category whose objects are ℕ.
   - A T-multicategory is a monad in the bicategory E_(T) of T-spans, for a cartesian monad T on a cartesian category E.
   - A T-operad is a T-multicategory with C0 = 1.
2. **Results.**
   - (VS) Leinster, *Higher Operads, Higher Categories*, arXiv:math/0305049, Def. 4.2.1–4.2.3. Quote: "A T-multicategory is a monad in the bicategory E_(T)."
   - (VS) Leinster Ex. 2.2.5, p.45: plain operads describe exactly the **strongly regular** finitary theories. These are equations in which "the same variables appear in the same order, without repetition, on each side". Commutative monoids and groups are not strongly regular, and §4.1.6 gives a method that rules out any "devious selection" of generators. Ex. 4.1.8: some cartesian monads (monoids with anti-involution) have no strongly regular presentation.
   - (VS) Lack, "Composing PROPs", TAC 13(9) 2004, pp.147–163, Thm 4.6. Let S and T be sub-PROPs of R. Suppose every map of R factors as σ∘τ uniquely up to a permutation. Then R is the composite S ⊗_P T via a distributive law. Example: the bialgebra PROP is the composite of the comonoid and monoid PROPs (Prop 4.8, §4).
   - (VS) Cruttwell–Shulman, arXiv:0907.2460, abstract: generalized multicategories are "lax algebras"/"Kleisli monoids" relative to a monad on a double category or virtual equipment. This unifies symmetric multicategories, globular operads, Lawvere theories and topological spaces.
3. **Represents / cannot.**
   - Represents multi-input composition with a typed "profile" of operations, through the choice of T.
   - **Plain or non-symmetric operads cannot express duplication or erasure of variables** (contraction and weakening). For that you need symmetric or cartesian (clone/Lawvere) structure.
   - No binding natively.
   - Polycategories (multi-output; the classical sequent calculus) were NA this session (MEM: Szabo 1975; Cockett–Seely 1997).
4. **Limitation.** The choice of T (the "shape of composition") is a **parameter, not derived**. A "finite basis" claim relative to an operad is relative to that chosen shape. Strong regularity is a non-trivial presentation-invariant obstruction.
5. **ProofBasis relevance.** Adjacent, and provides essential vocabulary. The structural rules of a logic (contraction, weakening, exchange) correspond exactly to the choice of operad/PROP/clone level. That makes "foundational neutrality" here a choice of T. A deep dive could change the framing: it would make "which composition doctrine" an explicit axis rather than a hidden assumption.
6. **Neighbours.**
   - Polynomial monads give a model of T-operads (GK Cor 5.17, B5).
   - Monads with arities (B6).
   - Lack's composition is the method behind IH (B2).

## B2 Finite complete presentations of PROPs (the direct "finite basis" analogue)
1. **Objects.** A finite set of generators and equations in a symmetric monoidal theory, together with a semantic functor into a concrete PROP. Two properties matter:
   - universality: the functor is full;
   - completeness: the functor is faithful on the quotient.
2. **Results.**
   - (VS) **Lafont 2003**, "Towards an algebraic theory of Boolean circuits" (author preprint 12 Feb 2003; JPAA 184 (2003) 257–310, SEC citation).
     - **Thm 10**, p.29: 7 generators (exchange, duplication, erasing, xor, false, and, true) with the relations of figs 13 and 40 "form a presentation of F[2]". F[2] is the monoidal category of all maps Z₂^p→Z₂^q.
     - Further presentations, all theorems with canonical forms and rewriting: S (Thm 1), M (Thm 2), F (Thm 3), A (Thm 4), L(Z₂) (Thm 5), GL(Z₂) (Thm 6).
     - **Negative result, §4.2:** the monoidal subcategory S[2] of permutations (reversible circuits) "is not finitely generated". By Lemma 14, every gate of arity ≤m generates only even permutations for n>m, so T_{m+1} is undefinable. S[k] is not finitely generated for even k. The alternating part A[2] is finitely generated (Cor 1), but Lafont says "other relations are needed" for a presentation, and gives none.
     - Linear injections that are monotone are "not finitely generated" (p.~27).
   - (VS) **Bonchi–Sobociński–Zanasi**, "Interacting Hopf Algebras", arXiv:1403.7048v4, JPAA preprint.
     - Thm 6.4: IH_R ≅ SV_k, the PROP of linear relations (subspaces) over the field of fractions k of a PID R.
     - The general signature has one scalar generator per r∈R. For R=Z, §7 gives a presentation "based on the finite signature of HA + HA^op", so linear relations over Q have a **finite** complete presentation.
     - The axioms are derived via Lack's distributive laws: "two Hopf algebra and two Frobenius algebra structures".
   - (VS) **ZX-calculus**:
     - Backens arXiv:1307.7025, Thm 21: complete for stabilizer QM.
     - Jeandel–Perdrix–Vilmart arXiv:1705.11151, Thm 1: the π/4 fragment is complete for Clifford+T, i.e. ⟦D1⟧=⟦D2⟧ iff ZX_{π/4} ⊢ D1=D2. The proof goes through completeness of ZW (integer matrices) and back-and-forth translations. This is a finite generator set.
     - Vilmart arXiv:1812.09114, Thm 1: complete for all pure-qubit QM. Generators carry angles α∈ℝ, so the presentation is **finite schemas, not finite generators**. Vilmart notes "a non-linear axiom is necessary" for the general calculus (citing [24]).
     - Hadzihasanovic–Ng–Wang, LICS 2018 pp.502–511: SEC (search listing only; no arXiv copy confirmed).
   - (VS, *recent preprints, unrefereed status unknown*) **Minimality.**
     - Backens–Perdrix–Wang arXiv:1709.08903 (LMCS 16:4 version) proves that 8 of 9 stabilizer rules are necessary. The bialgebra rule was left open. Necessity is proved via alternative ("non-standard") interpretations.
     - Stoltz arXiv:2606.12383v3 (Aug 2026) claims both remaining rules are necessary: the "first complete, minimal ruleset" for stabilizer ZX, "assuming the usual connectivity-only meta-rule".
     - Stoltz–Vilmart arXiv:2608.14872v3 (Sep 2026) claims two complete **and** minimal pure-qubit rulesets.
   - (SEC) Baez–Coya–Rebro arXiv:1707.08321 was downloaded but not inspected in detail.
3. **Represents / cannot.**
   - Represents a semantic category, with **equality of diagrams = equality of denotation** (completeness).
   - Variable-free; no binding; the semantics is fixed in advance.
   - A complete presentation axiomatizes the equational theory of ONE model. It does not give a basis of "inference".
4. **Strongest limitations.**
   - (a) Finite generation can fail outright: Lafont's reversible circuits, by a parity invariant.
   - (b) Completeness sometimes needs schemas over a continuum of parameters, and non-linear axioms.
   - (c) "Minimality" means irredundancy relative to a fixed generator set plus a meta-rule ("only connectivity matters", compact or braided ambient). This is NOT presentation-invariant. Compare the Tietze collapse in Report 010 P1.
5. **ProofBasis relevance.** **Direct methodological prior art for "finite complete generating basis"**: generators + equations + a completeness theorem + independence via non-standard interpretations. It exists only where a fixed target semantics is given.
   - A deep dive could change the framing. It suggests ProofBasis must name the target model (a "PROP of proofs modulo X"). Without one, "complete" has no meaning.
   - Lafont's parity obstruction is a template for **negative** results: an invariant preserved by all bounded-arity generators.
6. **Neighbours.**
   - Lack composition (B1).
   - Rewriting/polygraphs (Lafont uses Burroni polygraphs; Report 010 Squier).
   - Post's lattice: Lafont's F[2] is the PROP analogue of the full Boolean clone, but with explicit copy/discard generators.

## B3 Algebraic theories with variable binding
1. **Objects.**
   - Binding signatures and their initial algebras in presheaves on finite contexts (FPT).
   - Second-order equational presentations with metavariables (Fiore–Hur; Fiore–Mahmoud).
   - Modules over monads (Hirschowitz–Maggesi).
   - Abstract clones with second-order structure (Arkor–McDermott).
   - Presentable signatures (Ahrens–Hirschowitz–Lafont–Maggesi).
2. **Results.**
   - (VS) Fiore–Hur, "Second-Order Equational Logic (Extended Abstract)", CSL 2010, LNCS 6247, author PDF, abstract items 4–5:
     - SOEL is a conservative extension of Birkhoff equational logic;
     - "semantic completeness of equational derivability";
     - "derivability completeness of (bidirectional) Second-Order Term Rewriting".
     - The logic is "synthesised from the model theory. Hence it is necessarily sound." This is an extended abstract; proofs not checked.
   - (VS) Hirschowitz–Maggesi, arXiv:cs/0608051v2:
     - Thm 2: "For any signature Σ, the category of Σ-representations has an initial object."
     - Thm 3: "The monad Λ is initial in the category of exponential monads."
   - (VS) Ahrens–Hirschowitz–Lafont–Maggesi, "Presentable signatures and initial semantics", LMCS 17(2):17 (2021), arXiv:1805.03740.
     - Thm 6.3: "Any presentable signature is representable" (initial model exists).
     - Thm 6.4 uses AC.
     - **Non-example 5.5:** a signature (power-set-like) that is NOT representable.
     - Modularity: Thm 5.9.
     - Claimed computer-checked in UniMath. Labelled "formally checked (reported)": we did not run or inspect the code.
     - Successor: "Reduction monads and their signatures", arXiv:1911.06391, downloaded, not inspected.
   - (VS) Arkor–McDermott, "Abstract clones for abstract syntax", arXiv:2105.00969 (FSCD 2021).
     - Prop 24: for every S-sorted second-order presentation Σ and clone X, the free Σ-algebra exists, and the forgetful functor is monadic.
     - Thm 26: induction principle.
     - λ-calculus with βη is a second-order presentation.
   - (SEC) Fiore–Plotkin–Turi LICS'99 pp.193–202, via Turi's page and search abstract: syntax is the initial model; the substitution lemma is automatic. LICS Test-of-Time 2019. Primary text NA.
3. **Represents / cannot.**
   - Represents: binding, capture-avoiding substitution as a monoid/monad structure, metavariables (rule schemas!), and equations βη.
   - Cannot (by itself): dependent typing; side conditions (eigenvariable, freshness beyond scoping); proof identity beyond the stated equations; resource/linearity unless the base is changed.
   - Non-representable signatures exist.
4. **Limitation.** "Finite second-order presentation" is easy for λβη. **The generator set (e.g. abs/app) is again a presentation choice** (cf. Fiore–Mahmoud: theories ≃ presentations up to Morita-type equivalence, Report 010). The initial-semantics guarantee needs a representability hypothesis that can fail (Non-example 5.5).
5. **ProofBasis relevance.** **Direct prior art for "finite, explanatory basis for binding and substitution".** The meta-level (metavariables, substitution as monad multiplication) is already a finitely generated algebraic structure. Novelty must lie elsewhere.
6. **Neighbours.**
   - Lawvere/clones (Report 010).
   - B4 (dependent generalization).
   - B6 (monads with arities).
   - B7 (bracket abstraction eliminates binding but loses ξ; see below).

## B4 Dependent type theories as algebraic objects; initiality
1. **Objects.**
   - Cartmell GATs/contextual categories.
   - Dybjer CwFs.
   - Awodey natural models (representable natural transformations).
   - Isaev essentially-algebraic presentations.
   - Uemura representable map categories.
   - BHL raw/acceptable/well-presented type theories.
2. **Results.**
   - (VS) Awodey arXiv:1406.3219, Def. 1 and p.~4: "a category with families is the same thing as a representable natural transformation".
   - (VS) Castellan–Clairambault–Dybjer arXiv:1904.00827: the cwf definition "can be unfolded to yield a generalized algebraic theory in Cartmell's sense"; "the syntax of Martin-Löf type theory may be defined as the initial cwf in a precise sense".
   - (VS) Isaev arXiv:1602.08504v3, abstract: type theories as essentially algebraic theories. The category of them supports combination and equivalence. Models are "contextual categories with additional structure".
   - (VS) Uemura arXiv:1904.04097v3 (2023), abstract and Thm 6.10: "every type theory has a bi-initial model". The internal-language 2-functor has a left bi-adjoint (Thm 7.20), and democratic models ≃ theories (Thm 7.31). Syntax is via a logical framework.
   - (VS) Bauer–Haselwarter–Lumsdaine arXiv:2009.05539v1:
     - Defines raw → acceptable → well-presented type theories.
     - Meta-theorems: presuppositions (Thm 5.15), elimination of substitution (Thm 5.22), inversion (Thm 5.27).
     - "Much of the present work has been formalised in Coq."
     - Related work (pp.~56–58): Uemura "essentially subsumes ours". LF-based approaches need "adequacy or initiality theorems". Categorical semantics of BHL theories is left to "future work".
   - (VS) Brunerie (with de Boer, Lumsdaine, Mörtberg), HoTTEST slides, 10 Sep 2020: "Initiality for Martin-Löf type theory with Π, Σ, Id, N, +, ⊥, ⊤, U_i, El".
     - Fully annotated syntax.
     - Models are contextual categories as an essentially algebraic theory, with "ℕ ⊔ ℕ² sorts", "seven new operations", "nineteen new equations", plus one operation and one equation per type former.
     - Agda 2.6.1 with Prop, funext, propext and quotients (github tag v2.0, not inspected).
   - (SEC) nLab and the de Boer licentiate (KTH) page say initiality for full MLTT was long "treated as established" but never written up. Streicher 1991 is NA.
3. **Represents / cannot.**
   - Represents: dependent contexts, substitution, type formers, all as **finitely many operation schemas** of an essentially algebraic theory. They are indexed by context length, so there are infinitely many sorts.
   - Initiality connects the syntax to every model.
   - Cannot: proof identity beyond judgmental equality. Propositional equality and the higher structure need HoTT models. These frameworks are about **definitions of type theories**, not about "fundamentality" of rules.
4. **Limitation.**
   - Initiality is theory-by-theory, or requires an adequacy bridge from naïve syntax to the framework (BHL explicit).
   - Finiteness is at the level of schemas over ℕ-indexed sorts.
   - Choice of judgement forms is a parameter. Uemura generalizes this, but via an LF.
5. **ProofBasis relevance.** **Direct prior art and possibly framing-changing.** "Type theories are presented by finite rule schemas, and the syntax is initial" is established, with partial formal checks. A ProofBasis claim at this level would be redundant. The open part is invariance under change of presentation, and cross-foundation translation (Isaev's category of theories and Uemura's ThT are the existing answers).
6. **Neighbours.**
   - B3 (the simple case).
   - B5 (W-types/containers for inductive types).
   - Logical frameworks (LF), in another cluster.

## B5 Polynomial functors / containers
1. **Objects.** A polynomial functor P(X)_j = Σ_{b∈B_j} Π_{e∈E_b} X_{s(e)}, given by a diagram I←E→B→J in an lcc category. A container is a pair (S ▷ P).
2. **Results.**
   - (VS) Gambino–Kock arXiv:0906.4931v2:
     - Thm 4.5: "The free monad on a polynomial endofunctor is a polynomial monad", assuming E has W-types (§4.3).
     - Cor 5.17: P-Multicat ≃ PolyMnd/P, PlainOperad ≃ PolyMnd(1)/M, Cat ≃ PolyMnd/Id.
     - Prop 1.22: P:Set→Set is polynomial iff every slice of el(P) has an initial object.
     - Prop 1.16: polynomial functors preserve connected limits.
   - (VS) Abbott–Altenkirch–Ghani, "Containers: constructing strictly positive types", TCS 342(1) 2005 (author PDF):
     - Thm 3.4: container extension ⟦−⟧ is full and faithful.
     - Abstract: all strictly positive types exist in any Martin-Löf category.
3. **Represents / cannot.**
   - Represents: signatures of first-order operations with arities given by sets/types, inductive (W) types, and operads.
   - Not directly binding: needs presheaf/second-order structure as in B3. A not-strictly-positive type is not a container.
   - Polynomial functors are cartesian, so they do not capture all quotient (e.g. commutative) structure without symmetries or analytic functors (MEM: Joyal species).
4. **Limitation.** Representation of *signatures*, not of equations or proof equality. Existence depends on W-types in the ambient category.
5. **ProofBasis relevance.** Adjacent. It is a canonical *format* for "generators with arities", including infinitary ones. A deep dive is unlikely to change framing.
6. **Neighbours.** B1 (operads = polynomial monads over M), B3, B4.

## B6 Monads, Lawvere theories with arities, 2-monads
- (VS) Berger–Melliès–Weber arXiv:1101.3064v2, Thm 3.4: for a category E with dense generator A, T ↦ (Θ_T, j_T) "induces an adjoint equivalence between the category of monads with arities A and the category of theories with arities A". This extends finitary monads ↔ Lawvere theories. Monads induced by Leinster T-operads have canonical arities.
- (NA) Hyland–Power ENTCS 2007; Kelly–Street 1974. Report 010 already verified Lawvere's p.65/p.89 remarks and Kelly–Lack property-like 2-monads.
- **Represents:** a theory-level object independent of presentation. **Cannot:** single out generators.
- **Limitation:** the arities (A) are again a parameter.
- **Relevance:** adjacent. This is the "presentation-free" counterpart of everything in B1–B5, consistent with Report 010's conclusion that algebra gives invariant theories but no invariant "fundamental generators".

## B7 Combinatory logic and combinatory completeness; illative CL
1. **Objects.**
   - An applicative structure (A,·) with s,k.
   - Combinatory algebras, lambda algebras, partial combinatory algebras (PCA; NA, MEM: van Oosten).
2. **Results.**
   - (VS) Selinger, *Lecture Notes on the Lambda Calculus*, arXiv:0804.3434v2:
     - **Thm 5.1**: (A,·) is combinatorially complete iff ∃ s,k with sxyz = xz(yz), kxy = x. This is a finite basis (2 elements, 2 equations) for all "polynomial" functions.
     - **§5.4**, "The failure of soundness": the naive interpretation of λ-terms in a combinatory algebra is not sound. λx.x and λx.(λy.y)x are interpreted as i and s(ki)i, which are distinct in C/=_c (Cor 5.7).
     - **Thm 5.14**: A is a lambda algebra iff it absolutely satisfies **nine** axioms (Table 3). So λβ-equality is captured by finitely many extra combinatory equations (Curry's axioms), "required to hold absolutely" (Rem 5.16).
     - Prop 5.19: every extensional combinatory algebra is a lambda algebra.
   - (VS, secondary-authoritative) SEP "Combinatory Logic" (Bimbó; rev. 5 Nov 2024):
     - §2.3 Theorem (combinatorial completeness) for {S,K}.
     - The relevant base {B,C,W,I} gives λI-functions (no cancellator).
     - Bracket-abstraction algorithms "differ ... whether they commute with either of the reductions or equalities".
     - §1: "if we consider the language of FOL expanded with combinators, then the resulting system is inconsistent, because CL is powerful enough to define the fixed point of any function".
     - Basic logic (Fitch): "Curry's paradox is positive"; consistent such systems "cannot contain full abstraction"; Fitch's JE′ was "shown to be inconsistent by Myhill".
   - (VS-bibliographic) SEP "Curry's Paradox" (rev. 20 Jun 2026): Curry 1942b, "The Inconsistency of Certain Formal Logics", JSL 7(3):115–117, doi:10.2307/2269292; Curry 1942a, JSL 7(2):49–64.
   - (MEM) Kleene–Rosser 1935, Annals of Math. 36, inconsistency of Church's/Curry's systems. Barendregt–Bunder–Dekkers JSL 1993, illative systems complete for propositional/predicate logic. Barendregt 1984 Ch. 7 (combinatory axioms A_β, A_βη). All NA.
3. **Represents / cannot.**
   - Represents: every λ-definable function via 2 combinators. Binding is eliminated by an algorithm.
   - **Cannot**, without extra axioms: λ-equality. Weak CL equality is strictly finer, and ξ fails.
   - Adding logical constants (illative CL) with unrestricted combinatory completeness yields **triviality** (Curry's paradox needs only positive implication).
4. **Strongest negative.** A finite basis for *computation/substitution* does not give a finite basis for *logic*. Combining full combinatory completeness with implication/equality yields inconsistency unless restricted. The restrictions are typing, or the illative restrictions of the BBD kind (MEM).
5. **ProofBasis relevance.** **The closest historical precedent and a cautionary one.**
   - Universality of {S,K} is exactly the "universal computation presented as proof-theoretic universality" trap (AGENTS.md rule 6).
   - The finite basis exists, but it is *intensional*. It needs a finitely axiomatized correction (nine axioms) to match λβ, and it collapses when logic is added.
   - A deep dive could sharpen the falsification criteria.
6. **Neighbours.**
   - B3: bracket abstraction is a translation from second-order to first-order syntax that fails to preserve the congruence ξ.
   - B9: Tarski also eliminates variables, via pairing.

## B8 Abstract algebraic logic
1. **Object.** A logic is a substitution-invariant consequence relation ⊢ on a formula algebra. The main tools are matrices, Leibniz congruence Ω_A(D), and algebraizability via translations τ (formulas→equations) and Δ (equations→formulas).
2. **Results.** (VS, secondary-authoritative) SEP "Algebraic Propositional Logic" (Jansana; rev. 20 May 2022):
   - Definition (BP 1989): conditions (1)–(3), "both translations are inverses of each other ... modulo logical equivalence".
   - **Theorem 4**: L is algebraizable iff for all A∈Alg L the Leibniz operator commutes with inverse homomorphisms and is an isomorphism between L-filters and the congruences θ with A/θ ∈ Alg L.
   - **Theorem 5**: the same on Fm_L.
   - **Non-algebraizable examples:** the local consequence of normal modal logics (l. ~2303), lS4 (l. ~2363). Non-protoalgebraic logics: the {∧,∨} fragment, PML, and others (§10).
   - Primary sources: Blok–Pigozzi Memoirs AMS 396 (1989), Font 2016 book, and Font–Jansana–Pigozzi 2003 are NA. Béziau's universal logic is NA.
3. **Represents / cannot.**
   - Represents: derivability (consequence) and the translation-invariant algebraic counterparts. The Leibniz hierarchy classifies logics *invariantly*.
   - **Cannot: proofs, proof identity, rules-as-operations**. It is proof-irrelevant by construction (only ⊢).
4. **Limitation.** Many logics are not algebraizable. Even when one is, the equivalence is at the level of consequence, not derivations. Equivalence of logics is "deductive equivalence", not isomorphism of proof structures.
5. **ProofBasis relevance.** Adjacent; it is a useful **control**. It shows the mature, invariant theory of "logics and translations" exists *at the consequence level*. ProofBasis must say what it adds beyond this, namely proof-relevance. Report 010 P6′ is consistent with this: in proof-irrelevant settings derivedness collapses to preservation. A deep dive would not change framing, but it would provide the invariant comparison notion (Leibniz hierarchy).
6. **Neighbours.** B9 (algebraic logic of FOL); institutions and general logics (other clusters).

## B9 Other algebraic families
- **Relation algebras and cylindric algebras; Tarski–Givant.** (VS) Andréka–Németi, arXiv:1111.0995v1, "Formalizing set theory in weak logics...".
  - Abstract: FOL translates into the equational theory of Df₃ (Boolean algebras with three commuting complemented closure operators), equivalently [S5,S5,S5]. These are "strong improvements of the main result of" Tarski–Givant 1987.
  - Intro: Tarski (1953) formalized set theory in RA. This proved the equational theory of RA undecidable.
  - **Thm 2.1**: there is a recursive Tr with ZF ⊨ φ iff Tr(ZF) ⊢_d Tr(φ). This preserves and reflects **derivability**, via the pairing-function "bridge" Δ.
  - **Thm 2.2**: completeness only on a recursive subset K.
  - Negatives: "no finite Hilbert-style inference system which would be complete and sound" for L^d_3, because the quasi-equational theory of RDf₃ is not finitely axiomatizable. **Monk's result:** for every n there is a valid 3-variable formula needing more than n variables in any proof. For example, associativity of relation composition needs 4.
  - Two variables do not suffice (decidable).
  - Tarski–Givant book NA. (MEM) Monk 1964/1969: RRA and RCA_n (n≥3) are not finitely axiomatizable. Not re-verified beyond the quoted secondary statement.
  - **Relevance: strongest "finite equational basis for all of mathematics" precedent**, but at the derivability level only, via a coding (pairing) assumption. It shows that a finite basis for *provability* is cheap (with undecidability). It also shows that finite axiomatizability of the *intended semantics* fails. This is direct prior art against any derivability-only reading of ProofBasis.
- **Hopf algebras of proofs / renormalization.** The search found only physics renormalization (Connes–Kreimer; arXiv:1505.04765, hep-th/0301015). No proof-theoretic Hopf algebra was found (search-level only; not exhaustive). Hopf and Frobenius structure does appear in B2 (IH, ZX) as the algebra of copy/discard/add.
- **Not covered (NA):** polyadic algebras (Halmos), Boolean categories (Lamarche–Straßburger, a proof-identity candidate; recommend another cluster check), Rota-style algebras.
