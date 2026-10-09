# Report 010: Cross-review A — algebraic fundamentality (Claude on Codex's PR #14)

**Primary target:** Codex's `reports/009-adversarial-definitions.md`, in PR #14 at head `e4855a8`.

**Also read:**
- `AGENTS.md`, the charter, `docs/STAGE_0_7_RECONCILIATION.md`;
- my own PR #13 (`reports/008-constructive-definitions.md`) with its source notes and critique;
- reports 002, 005, 006 and 007.

**Baseline:** main at `9c87762`.

**Restrictions observed:**
- No edits to reports 008/009, the charter or the reconciliation.
- No universal existence attempt.
- The source class C is **not** narrowed.

**Author and date:** Claude (Claude Code session), 2026-10-09.

**Supporting material:**
- `reports/010-source-notes/`: source extractions and the fresh critique;
- `reports/010-checks/`: one bounded brute-force check.

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED (verified)** | Statement read this session, or in an earlier verified project log, in a primary text; location given |
| **ESTABLISHED (secondary)** | Read only as restated in a retrieved secondary text |
| **PROVED HERE** | New argument with a complete informal proof in this report. Not machine-checked; not refereed |
| **COUNTEREXAMPLE** | A concrete construction whose verification is given in full |
| **CHECKED (bounded)** | Verified by exhaustive enumeration in `reports/010-checks/` for the stated cases only |
| **INFERENCE** | Argument with a named gap |
| **OPEN** | Unresolved |
| **UNVERIFIED-MEMORY** | Not checked against a source this session |

---

## 1. Verdict

### 1.1 On Report 009

I checked report 009's mathematics independently (§2). Its consequential claims hold:

- N_rep is automatic by Yoneda.
- The abelianization obstruction to N_split on a fixed universal group is correct.
- The checker and the typed-path interfaces are isomorphic.
- The set-level naturality calculation for precomposition actions is correct.

I found three substantive problems.

1. **N_split is worse than 009 says.**
   - The same abelianization argument shows that N_split also rejects the *natural* structural embeddings that reports 005, 006 and 009 itself treat as legitimate controls:
     - the free-symmetric-monoidal embedding of C_p (rotation ↦ p-cycle), for every odd prime p;
     - Thompson's V embedding, for every p.
   - So N_split rejects good translations as well as the universal group (§5.3; PROVED HERE, with a bounded check for p = 3, 5, 7).
2. **009's decisive controls 1–2 contain no logical operations.**
   - The graph calculi S_G consist only of non-logical edge generators. By the universal property of free categories (§3.6), every faithful functor out of S_G is fixed by where it sends the edges. There is therefore *no* logical structure for a fundamentality criterion to preserve or detect.
   - Hence 009's indistinguishability result, although correct, cannot show that interface criteria fail to separate interpretation of **logical** rules from genuine derivation.
   - §5.4 supplies the missing logical-source case: Proposition P6 is a separating example that interface invariants provably cannot see.
3. **009 frames its next test around the restricted interface.** Its recommendation ("identify extra structure beyond the quotient interface") is correct. The missing separating lemma does exist in its simplest form (P6). The extra structure it needs is the **ambient category together with a doctrine**: universal properties tested against *all* objects of the target, not just translated ones. This is established mathematics (structure-preserving functors; property-like structure), not a new theory.

### 1.2 On the mathematics of fundamental operations

**Existing formalisms already give a presentation-independent "algebra of proof operations":**
- the generated structure: the clone, the Lawvere theory, or the free structured category;
- for equality derivations, the polygraphic/rewriting structure, up to homotopy.

**By design, none of them gives a presentation-independent notion of "fundamental generator".**
- **Proposition P1 (PROVED HERE).** Any predicate on generators that is invariant under Tietze moves is a predicate on *elements* of the generated structure.
- **Proposition P2 (PROVED HERE).** Any presentation property invariant under Tietze moves is a property of the generated structure.

So information is **preserved** by passing from a presentation to the generated structure only in two forms:
- the structure up to isomorphism;
- properties of the form "some or every presentation has property X". Examples: finite presentability, finite convergent presentability (Squier), finite derivation type.

Information is **necessarily lost**:
- which operations are primitive;
- irredundancy and basis size;
- the relations as named 2-cells and their syzygies;
- provenance (rule versus assumption);
- the derivation history of equalities.

### 1.3 Fundamentality needs additional structure — and existing mathematics supplies it

An acceptable notion **must** depend on more than the generated interface:
- by P1 and P2;
- by 009's isomorphism lemma, generalised in §5.2 (P5).

The minimal sufficient extra structure found here is:

- **(a) A doctrine D.** This is a structure whose operations are determined *up to unique isomorphism* by universal properties (Kelly–Lack property-like structure; Lawvere's adjoint characterization of logical operations). Operations given this way are element properties in P1's sense, so they survive every Tietze move. **Fundamental operation := structure map of a D-universal property.**
- **(b) The ambient target with probes over all of its objects.** A realization is *fundamental for S's logic* iff it is a D_S-structure-preserving functor into A, or into a D-construction on A such as a (co-)Kleisli category. Universal properties must hold against every ambient object, not only translated ones.
  - **Proposition P6 (COUNTEREXAMPLE, complete).** Two realizations of the same intuitionistic implication have *isomorphic* interfaces (both fully faithful). One preserves the ambient implication; the other realizes the source's implication by a fixed table while the target's own implication disagrees.
  - **Proposition P6′ (PROVED HERE).** In proof-irrelevant Heyting settings, requiring connective images to be *derived term operations* already forces ambient preservation, provided top and meets are preserved.
  - **Where the two notions diverge.** Only with proof relevance do "derived operation" and "ambient universal property" come apart. The LF-with-βη case (§5.4″, INFERENCE) is the example.
- **(c) A provenance ledger for non-logical generators.**
  - **Proposition P7 (PROVED HERE, from the established universal property of free D-structures).** For a source presented as a D-structure on a signature Σ, a D-structure-preserving realization is determined *exactly* by its values on Σ.
  - So, once logical structure is required to be preserved, the **only** remaining interpretive freedom is the interpretation of non-logical generators. That is precisely what a ledger must record.

**What remains OPEN (§7):**
- which constructions on A count as admissible "derived ambient structure" (Q1);
- whether a fixed A with code-inspecting data can make a deep (data-indexed) realization of a logical source satisfy the ambient universal property (Q2). This is the decisive next test;
- whether one fixed doctrine can host every source doctrine through admissible constructions (Q3). Q3 is the ProofBasis question at the level of doctrines. It narrows nothing.

---

## 2. Independent checks of Report 009

| 009 claim | Where | My check | Status |
|---|---|---|---|
| N_rep holds for every small faithful compositional interface | §3, §4 | Yoneda: y : B → [B^op, Set] is fully faithful, so y∘F is faithful iff F is faithful. N_rep is equivalent to I2 (faithfulness) and adds nothing | **Correct** (P4) |
| A_check and A_path have isomorphic structured interfaces (H, K) | §5 | The construction defines Hom_check as boxes quotiented by a *fixed* box-irrelevance equation, so each Hom_check class is a path word by design. H, K are inverse. The isomorphism is essentially built in | **Correct**; see §2.1 for the scope caveat |
| Invariants of the structured interface cannot separate the two | §5 lemma | Transport of structure along an isomorphism. This is an instance of P5 | **Correct, and tautological once stated**. The content is in *which* data the criteria read (B_F only) |
| No fixed f.g. group U retracts onto every C_p | §6 | Let U^ab ≅ ℤ^r ⊕ T with T finite, and p ∤ \|T\|. A retraction r : U → C_p factors through U^ab because C_p is abelian. Then C_p → U^ab → C_p is the identity. But the image of C_p in U^ab is a p-torsion subgroup, hence trivial, which is a contradiction | **Correct** (independently re-derived) |
| Natural transformations K_D ⇒ K_D are precompositions | §6 | Yoneda for the representable Set(D, –) | **Correct** |
| LF (HHP) passes N_split / N_rep at raw α-identity; it fails β-preservation for the object β-redex | §7 | Consistent with HHP Theorem 4.1 as verified in reports 007/009. The β failure is the standard "constants do not compute" | **Plausible**; I did not re-read HHP this session |
| The Girard translation passes N_split via Hasegawa 2000, Theorem 5.6 (fullness) | §7 | I did not retrieve Hasegawa 2000. The argument (a fullness-plus-faithfulness bijection gives a two-sided inverse) is valid given the cited theorem | **Valid conditional on 009's verified citation** |
| "Other A with different generated interfaces are not excluded" by the obstruction | §6 | True as stated, but it understates the defect: the natural compound interfaces are excluded too | **Incomplete** (P3) |

### 2.1 Scope caveat on 009 §4–5: equality for sources with β/η

- **What 009's checker does.** Its source class is graph calculi, where ≈_S is flattening. The checker realises that equality with A's **own** list-append monoid laws plus a box-irrelevance equation.
- **What a logical source would need.** For S = NJ(→) with βη, box irrelevance must identify boxes whose serialized terms are βη-equal. That needs either:
  - (i) a fixed *conditional* equation (equality reflection from a data-level equality derivation), or
  - (ii) a fixed normaliser that sends boxes to canonical forms. This exists only where ≈_S is decidable, and a universal one exists only uniformly over decidable presentations.
- **Consequences.** In case (i) the target has equality reflection. Report 009 §2.3 allows this only if the reflection rule is fixed, but this changes the trust analysis. In case (ii) the construction does not cover sources with undecidable ≈_S (report 006 Proposition A).
- **Scope.** 009's indistinguishability is therefore **established only for flattening-equality sources**. For logical sources, P5 (§5.2) recovers it, with the same caveat.

---

## 3. Established mathematics of generating and fundamental operations

All statuses and locations are in `reports/010-source-notes/sources.md`.

### 3.1 Clones and term operations

- **Clone of an algebra.** The clone of an algebra **A** is the set of its term operations. It is the smallest set of finitary operations that contains the projections and the basic operations and is closed under composition.
- **Term equivalence.** Two algebras on the same carrier are *term-equivalent* if their clones coincide, and two varieties are term-equivalent if their classes of algebras are interdefinable by terms.
- **The standard example (Stone).** Boolean algebras (∧, ∨, ¬, 0, 1) and Boolean rings with identity (+, ·, 0, 1) are term-equivalent: x + y := (x ∧ ¬y) ∨ (¬x ∧ y), and x ∨ y := x + y + xy.
- **Consequence.** *Which* operations are basic is not an invariant of the clone.

### 3.2 Generation, independence and irredundant bases

- **Post's lattice.** Every clone on {0,1} is finitely generated, and the clone of all Boolean functions has bases of different sizes:
  - {NAND} (Sheffer);
  - {∧, ¬};
  - {→, ⊥}.

  Each of these is irredundant. **Irredundant bases are neither unique nor of fixed size.**
- **Three-element set.** There are continuum many clones, so some are not finitely generated (Janov–Mučnik).
- **Consequence.** "The fundamental operations of a clone" has no canonical meaning in general.

### 3.3 Lawvere theories (presentation independence)

- An algebraic theory is a category with finite products, generated by one object, in which the morphisms n → 1 are the n-ary term operations. Lawvere, *Functorial semantics of algebraic theories*.
- A presentation (signature plus equations) determines its theory. Different presentations of the same variety give isomorphic theories.
- Models of the theory are product-preserving functors into Set.
- **This is the standard presentation-independent "algebra of operations".**

### 3.4 Presentations and Tietze moves

- **Tietze's theorem.** Any two finite presentations of isomorphic groups are connected by a finite sequence of Tietze transformations:
  - add or remove a generator together with a defining relation;
  - add or remove a relation that is a consequence of the others.
- **B. H. Neumann.** Finite presentability does not depend on the finite generating set.
- **Generality.** The same proof pattern works for monoids and for any finitary equational presentations. P1/P2 below re-prove what is needed.

### 3.5 What survives presentation change

- **Mal'tsev conditions.** Example: the existence of a term m(x,y,z) with m(x,y,y) = x = m(y,y,x), which is equivalent to congruence permutability. Such conditions are stated purely in terms of the clone, so they are invariant under term-equivalence. They are the classical presentation-independent invariants of a variety.
- **Squier.**
  - A monoid with a finite complete (convergent) rewriting system is of homological type FP₃.
  - Some finitely presented monoids with decidable word problem have no finite complete rewriting system on *any* finite generating set.
  - Squier–Otto–Kobayashi: finite derivation type (FDT), a property of the 2-dimensional structure of derivations between equal words, is independent of the finite presentation.
- **The pattern.** Properties of *presentations* (convergence, derivation type) become invariants of the *presented structure* by quantifying over presentations. A property of a given presentation need not survive a change of generators (Kapur–Narendran).

### 3.6 Free constructions and universal properties

- **Free structures.** For any algebraic, or many-sorted, or second-order (Fiore–Mahmoud) theory T and signature Σ, the free T-structure Free_T(Σ)/E has this universal property: T-morphisms Free_T(Σ)/E → M correspond bijectively to interpretations of Σ in M satisfying E.
- **Uniqueness.** Operations given by universal properties, such as products, exponentials and adjoints, are determined **up to unique isomorphism**. Lawvere: "structure of a cartesian closed category is entirely given by adjointness" (ESTABLISHED, verified, TAC Reprints 16, p. 3; report 008 notes).
- **Property-like structure (Kelly–Lack).** A 2-monad is property-like when an algebra structure, if it exists, is unique up to unique isomorphism, and every morphism automatically preserves it up to coherent isomorphism. Finite products are an example.
- **Generalised frameworks.**
  - Generalised algebraic theories ↔ contextual categories (Cartmell);
  - essentially algebraic theories ↔ locally finitely presentable categories (Gabriel–Ulmer);
  - type theories as representable map categories (Uemura, verified in report 008);
  - PROPs, operads and polygraphs (computads) for multi-input / multi-output structure;
  - polygraphic resolutions for equality derivations (Lafont–Métayer).

### 3.7 Inference rules versus derived operations

- **Derivable rule.** The conclusion is obtained from the premises by a fixed derivation schema with holes. This is an element of the clone of the proof structure (a derived operation).
- **Admissible rule.** The set of theorems is closed under the rule, but no such schema need exist. Example: cut in a cut-free sequent calculus.
- **Effect of adding rules.**
  - Adding a derivable rule is a Tietze move: the clone and the proof structure are unchanged up to isomorphism.
  - Adding an admissible but underivable rule leaves *provability* unchanged but changes the proof structure. It is **not** a Tietze move.
- **Consequence.** The generated proof algebra correctly distinguishes derivable from merely admissible rules.

### 3.8 Answer to "does an existing formalism already provide a satisfactory, presentation-independent algebra of proof operations?"

**For the algebra: yes.**
- For proof systems as typed, binding-aware structures, the free structured category (or Lawvere-style theory, or second-order algebraic theory) generated by the rules modulo the proof equations is the canonical presentation-independent object.
- Its elements are exactly the derived proof operations (§3.7).
- Invariance under Tietze moves is built in.

**For "fundamental operation": no, and none can be (P1).** The only presentation-independent notions of fundamentality are:
- properties of individual derived operations within the generated structure, such as "is the counit of an adjunction";
- existence statements over presentations.

---

## 4. Information preserved and lost: new results

### 4.1 Setting

Fix a finitary presentational framework 𝔉. Examples: groups, monoids, many-sorted algebraic theories, finite-product theories, second-order algebraic theories.

A **presentation** P = (X, R) consists of:
- a finite set X of generators (typed operation symbols);
- a finite set R of equations between 𝔉-terms over X.

⟨P⟩ is the generated structure (the free 𝔉-structure on X modulo R).

The two **Tietze moves** and their inverses are:
- **(T1)** Add a generator y with a defining equation y = t, where t is a term over the other generators.
- **(T2)** Add an equation that holds in ⟨P⟩.

### 4.2 Proposition P1 (Tietze collapse of generator predicates) — PROVED HERE

**Statement.** Let Φ(P, g) be a predicate on pairs (presentation, generator of that presentation). Suppose Φ is invariant under every Tietze move that keeps g as a generator. Then for any two presentations P, P′ of isomorphic structures, and generators g ∈ P and g′ ∈ P′ that correspond to the same element under some isomorphism θ : ⟨P⟩ ≅ ⟨P′⟩:

  Φ(P, g) = Φ(P′, g′).

So Φ(P, g) depends only on the pair (⟨P⟩, [g]) up to isomorphism.

**Proof.**
1. Identify ⟨P′⟩ with ⟨P⟩ via θ, so that g and g′ denote the same element e. Rename g′ to g in P′.
2. Write X = {g} ⊔ X₀ and X′ = {g} ⊔ X′₀.
3. Every x′ ∈ X′₀ is equal in ⟨P⟩ to some term t_{x′} over X. Every x ∈ X₀ is equal to some term s_x over X′.
4. Starting from P:
   - add each x′ ∈ X′₀ with defining equation x′ = t_{x′} (moves of type T1);
   - add each equation of R′ (type T2: each holds in ⟨P⟩, since ⟨P′⟩ ≅ ⟨P⟩ with g ↦ g);
   - add each equation x = s_x (type T2).

   The result is Q = (X ∪ X′₀, R ∪ R′ ∪ {x′ = t_{x′}} ∪ {x = s_x}). The generator g is never removed.
5. Starting from P′, the symmetric moves reach the same Q, again keeping g.
6. Therefore Φ(P, g) = Φ(Q, g) = Φ(P′, g). ∎

**Corollary P1′.**
- Every element e of a finitely presented ⟨P⟩ is a generator of some finite presentation: apply T1 with y = e.
- So a Tietze-invariant Φ defines a predicate on all elements of ⟨P⟩. If Φ is also invariant under isomorphism, it is a union of Aut(⟨P⟩)-orbits.
- In particular, "being a basic operation" is not Tietze-invariant, because every element is basic in some presentation.
- "Belonging to an irredundant basis" is not an element property either. For example, ∧ belongs to the irredundant basis {∧, ¬}, but in {NAND} it is a derived operation, so it is basic in one presentation and derived in another.

### 4.3 Proposition P2 (presentation properties) — PROVED HERE

**Statement.** If Ψ(P) is invariant under Tietze moves, then Ψ(P) = Ψ(P′) whenever ⟨P⟩ ≅ ⟨P′⟩.

**Proof.** Steps 4–6 of P1, without the generator g. ∎

**What survives (the positive content).** Any presentational property X yields two invariants of the generated structure:
- "∃ P presenting M with X";
- "∀ P presenting M, X".

Squier's finite-convergence property and FDT are of the first form. The project's "has a pure presentation" (report 008, N_log) is also of this form, and so it is presentation-independent.

**What is lost (forced by P1/P2).** Anything not expressible either as a property of M up to isomorphism or as a quantification over presentations of M. That includes:
- the identity of the primitive operations;
- basis size;
- names and roles of relations, i.e. the 2-cells and the derivations of equalities;
- the rule-versus-assumption ledger. Report 009 §2.4 exhibits structurally inverse translations that change the ledger.

---

## 5. Application to N_split and N_rep, and to the checker problem

### 5.1 Proposition P4 (N_rep is faithfulness) — PROVED HERE (via the established Yoneda lemma)

For any small category B and functor F : P → B, the composite y∘F : P → [B^op, Set] is faithful iff F is faithful, because the Yoneda embedding y is fully faithful.

N_rep's remaining clauses (identity, composition, naturality on all probes of B) hold for y automatically.

Hence **N_rep ⇔ I2**. This makes 009's finding exact.

### 5.2 Proposition P5 (interface collapse, generalised) — PROVED HERE

**Setting.**
- An *interface criterion* is a predicate N(P_S, B_F, F) that is invariant under isomorphisms of the triple. Such an isomorphism is an isomorphism of structured categories B_F ≅ B′_F commuting with F and F′.
- A realization is *full and faithful at the interface* when F : P_S → B_F is an isomorphism of structured categories.

**Statement.**
- For any source S, all full and faithful realizations of S receive the same verdict under every interface criterion.
- For any two faithful realizations F, F′ with an isomorphism B_F ≅ B_{F′} over P_S, they also receive the same verdict.

**Proof.** If F and F′ are isomorphisms onto their interfaces, then F′ ∘ F⁻¹ : B_F ≅ B_{F′} commutes with F and F′. Invariance does the rest. ∎

**Scope.**
- P5 extends 009's lemma from graph calculi to any S. The premise is the existence of a full and faithful realization of the kind considered.
- **For logical sources** (for example NJ(→) with βη), a deep realization with canonical-form boxes (§2.1(ii)) is full and faithful at its interface whenever ≈_S is decidable. That such a fixed construction exists is INFERENCE.
- Conclusion: **no interface criterion can separate genuine from interpretive realizations, even for logical sources**, wherever full and faithful deep realizations exist.

### 5.3 Proposition P3 (N_split rejects natural embeddings) — PROVED HERE; CHECKED (bounded)

**Statement.** N_split fails for every faithful translation of the cyclic source S_p (unary rule r, equation rᵖ = id; reports 005 and 009) into:
- **(a)** the free symmetric monoidal category, via P ↦ X^{⊗p} and r ↦ the p-cycle, for every odd prime p;
- **(b)** Thompson's group V acting on a single object, via any embedding C_p ↪ V, for every prime p;
- **(c)** any target in which the translated object's endomorphism group G_T has |G_T^ab| coprime to p, or more generally G_T^ab has no p-torsion summand that the embedded C_p can map onto.

**Proof.**
1. N_split asks for a monoid homomorphism End(T) → C_p that is left inverse to the embedding at the translated boundary.
2. Restricted to the unit group, it is a group homomorphism G_T → C_p that is the identity on the embedded C_p. Any homomorphism to an abelian group factors through G_T^ab.
3. **(a)** By Mac Lane's coherence theorem for symmetric monoidal categories (ESTABLISHED, secondary/memory; the critic of report 006 verified the S_n fact by elementary reasoning), End(X^{⊗p}) = S_p. Here S_p^ab = C_2, so for odd p every homomorphism S_p → C_p is trivial.
4. **(b)** V is simple (Cannon–Floyd–Parry Theorem 6.9; ESTABLISHED, verified in report 005), so every homomorphism V → C_p is trivial.
5. **(c)** The same factorisation argument. ∎

**Bounded check.** `reports/010-checks/retraction_check.py` enumerates all homomorphisms S_p → C_p for p = 3, 5, 7. It finds only the trivial one, and so no splitting.

**Consequence.** N_split rejects translations that reports 005, 006 and 009 all count as legitimate structural embeddings. N_split is therefore a fullness-like *reversibility* condition, not a non-vacuity filter. 009's own §6 conclusion ("reversibility … has not become an interpreter filter") is strengthened: it also produces false negatives on natural structures.

### 5.4 Proposition P6 (ambient universal properties separate realizations with isomorphic interfaces) — COUNTEREXAMPLE, complete

This is the simplest case of logical structure: proof-irrelevant (thin) cartesian closed categories, i.e. Heyting algebras.

**Source S.** The three-element chain H₃ = {0 < m < 1} as a Heyting algebra.
- **Judgments:** x ⊢ y iff x ≤ y.
- **Connectives:** ∧ = meet and ⇒ = Heyting implication. In H₃, m ⇒ 0 = 0, because the largest z with z ∧ m ≤ 0 is 0.

**Realization R₁ (native).**
- A₁ = H₃, F₁ = id.
- F₁ preserves ⇒ and ∧ *in the ambient* A₁.

**Realization R₂ (tabulated).**
- A₂ = the four-element Boolean algebra B₄ = {0, a, b, 1} with a ∧ b = 0 and a ∨ b = 1.
- F₂(0) = 0, F₂(m) = a, F₂(1) = 1.
- Implication is realised by the *table* F₂(x ⇒ y) := F₂(x ⇒_{H₃} y).

**Verification.**
1. **F₂ is an order-embedding.** It preserves and reflects ≤ on {0 < a < 1}. As a functor between thin categories it is therefore full and faithful. Derivability is preserved and reflected (I1), and faithfulness (I2) is trivial in thin categories.
2. **F₂ preserves the ambient meets:** F₂(x ∧ y) = F₂(x) ∧_{B₄} F₂(y) on the chain.
3. **The interfaces are isomorphic.** B_{F₂} = {0, a, 1} with the induced order is a three-element chain, isomorphic to H₃ = B_{F₁} over the source. Every interface criterion (P5) assigns R₁ and R₂ the same verdict.
4. **F₂ does not preserve the ambient implication.**
   - F₂(m ⇒ 0) = F₂(0) = 0.
   - But in B₄, F₂(m) ⇒ F₂(0) = a ⇒ 0 = ¬a = b ≠ 0.
   - The source's implication is realised by a value that is **not** the target's own implication of the realised arguments. The target has an implication, and F₂ does not use it.
   - Equivalently, the ambient universal property fails. For the probe b ∈ B₄ (not in the image): b ∧ F₂(m) = b ∧ a = 0 ≤ F₂(0), but b ≰ F₂(m ⇒ 0) = 0. So F₂(m ⇒ 0) is not the exponential in B₄.
5. **R₁ satisfies the ambient universal property by construction.** ∎

**Caveat: what P6 does and does not separate.**
- In R₂ the table x, y ↦ F₂(x ⇒ y) is **not** a term operation of B₄.
  - Boolean term functions act coordinatewise on B₄ ≅ 2².
  - Any binary term t with t(1,0) = 0 and t(0,0) = 1 on the coordinates gives t(a,0) = b.
- So a criterion that requires connective images to be *derived operations of A* (report 002's T1 / report 008's componentwise clause) also rejects R₂.
- P6 thus separates **interface criteria** from **ambient criteria** in general. It does not by itself separate "derived operation" from "ambient universal property". That is the job of P6′ and the LF case below.

### 5.4′ Proposition P6′ (in proof-irrelevant settings, derivedness already forces ambient preservation) — PROVED HERE

**Statement.**
- Let K be a Heyting algebra and H a Heyting algebra (the source).
- Let F : H → K be monotone, preserve binary meets, and preserve top (F(1) = ⊤).
- Suppose there is a binary Heyting term t over K such that t(Fx, Fy) = F(x ⇒ y) for all x, y ∈ H.
- Then F(x ⇒ y) = Fx ⇒_K Fy for all x, y.

**Proof.** Fix x, y and put u = Fx, v = Fy, w = F(x ⇒ y).

1. *(w ≤ u ⇒ v.)* (x ⇒ y) ∧ x ≤ y in H. Applying F (meets and order) gives w ∧ u ≤ v, so w ≤ u ⇒ v by residuation in K.
2. *(w ≥ u ⇒ v.)*
   - Let Φ = ↑(u ⇒ v), a filter of K, and let ≡_Φ be its Heyting congruence (a ≡ b iff (a ⇔ b) ∈ Φ; standard).
   - Modulo Φ, u ⇒ v ≡ ⊤. Therefore u ≡ u ∧ v, since u ⇔ (u ∧ v) = u ⇒ v.
   - Every term operation respects every congruence, so w = t(u, v) ≡ t(u ∧ v, v).
   - Since F preserves meets, u ∧ v = F(x ∧ y), so t(u ∧ v, v) = F((x ∧ y) ⇒ y) = F(1) = ⊤.
   - Hence w ≡ ⊤, i.e. w ∈ Φ, i.e. w ≥ u ⇒ v. ∎

**Meaning.**
- In thin (proof-irrelevant) cartesian closed settings, a connective image that is a term operation of the ambient Heyting algebra *must be* the ambient implication, once meets and top are preserved.
- So for derivability-level fidelity, "derived operation" and "ambient universal property" coincide.
- The hypothesis F(1) = ⊤ is used essentially. Whether a counterexample exists without it was not determined: a bounded search over small Heyting algebras timed out.

### 5.4″ The proof-relevant separation: LF with βη (INFERENCE)

In proof-relevant settings the two notions come apart.

- In report 009's HHP encoding with source βη, the object implication goes to the LF type true(imp φ ψ). That is a *derived* type: a fixed type family applied to the derived term imp φ ψ.
- The canonical candidate currying maps are imp-i and imp-e. Their composite imp-e(imp-i f) does not reduce to f (009 §7: constants do not compute). So these maps are not mutually inverse up to ≈_A, and the canonical exponential comparison fails.
- **Gap:** that *no* other natural isomorphism exists is not proved here.

This is the case where "derived operation" (T1-style) holds but "ambient universal property" (N_amb) fails. It is why N_amb, not derivedness, is proposed in §5.6.

**Interpretation of P6.**
- R₂ is a minimal "rule-table interpretation". It reproduces the source's *consequence relation and proof structure* exactly, through the table F₂(x ⇒ y), while ignoring the target's own logical operation.
- No criterion that reads only (P_S, B_F, F) can detect this (step 3).
- A criterion that tests universal properties against **ambient probes** can (step 4).
- The probe b lies outside the image, which is exactly the information 009's B_F discards.

### 5.5 Proposition P7 (forced logical part, free non-logical part) — PROVED HERE from §3.6

**Statement.** Let D be a doctrine (a 2-monad or theory of structure on categories) whose algebras have their D-operations specified by universal properties. Let S be presented as a D-structure P_S = Free_D(Σ)/E, where Σ consists of non-logical generators such as atoms, edges or group generators, and E are the non-logical equations. Let M be a D-structure. Then strict D-morphisms P_S → M correspond bijectively to Σ-interpretations in M satisfying E. For pseudo-morphisms the correspondence is up to equivalence.

**Proof.** This is the universal property of the free D-structure (§3.6), together with the quotient's universal property for E. ∎

**Reading.**
- Once realizations are required to be D_S-morphisms into an ambient D_S-structure, the logical rules are **forced**: their images are determined by the universal properties.
- The only per-source freedom is the interpretation of Σ.
- Interpreting Σ is *legitimate representation of non-logical data*. Whether it is trusted is a ledger question: assumption, defined object, or relative interpretation.
- This splits the "interpreter worry" into a mathematically decided part (logic, forced) and an accounting part (non-logical generators, recorded).
- **Applied to 009's controls 1–2.** S_G = Free_Cat(G) has D = Cat and Σ = the edges. Every faithful realization is just an interpretation of edges. Checker and path are therefore *both* admissible as representations of S_G. They differ only in **where the edge interpretations come from**: a data table in a type family (internal), or ambient morphisms (external). That difference is ledger and ambient information, not logical information.

### 5.6 The repaired criterion and its tests

**N_amb (doctrine-relative ambient preservation).** Let D_S be the doctrine whose universal properties S's connectives satisfy. N_amb(A, F_S) holds iff F_S is a pseudo-morphism of D_S-structures into some D_S-structure Φ(A) obtained from A by an admissible construction. "Admissible" means at least the identity, and Kleisli or co-Kleisli categories of a (co)monad definable in A. The exact admissible class is Q1.

**Grounds (existing concepts):**
- cartesian closed functors, logical functors (topos theory) and monoidal closed functors (morphisms preserving structure given by universal properties);
- Kelly–Lack property-like structure, which makes preservation a property;
- Lawvere's thesis that logical operations are adjoints.

**Presentation independence (PROVED HERE, from P1 and §3.6).**
- N_amb is invariant under Tietze moves of A's presentation, because it depends only on the generated A.
- It is invariant under D_S-equivalences of A.
- It is **not** invariant under isomorphisms of B_F alone (P6). That non-invariance is the point.

| Required case | Source used | N_amb verdict | Reason |
|---|---|---|---|
| 1. Explicit checker | 009's S_G (graph) | ✔ | D = Cat; no logical structure; P7 |
| 1′. Explicit checker | **a logical source**, e.g. NJ(→) with βη, deep boxes in an A with code-inspecting data | ✘ (INFERENCE; Q2) | Ambient probes Γ = data types admit non-parametric maps Γ × F(φ) → F(ψ) that inspect codes. These have no counterpart in Γ → F(φ ⇒ ψ), so F(φ ⇒ ψ) is not an ambient exponential. The gap: a complete proof needs a specific A |
| 1″. Explicit checker | logical source in an *opaque-sort* A that adds ambient currying (box(λ…) ↔ ambient λ) | ✔ | Then F(φ ⇒ ψ) **is** an ambient exponential. By uniqueness of universal properties (§3.6) it is the target's implication up to unique isomorphism, presented with checker vocabulary. By P1 this is a re-presentation of a genuine cartesian closed structure, not an interpreter |
| 2. Typed paths | 009's S_G | ✔ | As case 1 |
| 2′. Typed paths | a logical source's rule table (report 008 C2a) | ✘ (INFERENCE) | As case 1′ |
| 3. Universal f.p. group | S_G for groups | ✔ | No logical structure (D = groupoids or Cat). Universality is not disqualifying (agrees with 009) |
| 4. Standard LF (HHP) | first-order ND with **raw α** identity | ✔ (vacuous: with raw identity ⊃ has no universal property) | — |
| 4. Standard LF (HHP) | first-order ND with **βη** identity | ✘ | ⊃ ↦ declared constant `imp`. true(imp φ ψ) is not the LF exponential true φ → true ψ up to the required isomorphism, because imp-e ∘ imp-i does not reduce. Matches 009 §7 |
| 4′. Shallow LF / judgments-as-types | NJ(→) | ✔ | → ↦ Π |
| 5. Girard (Hasegawa 2000) | STLC → dual-context linear λ-calculus | ✔ | F is a cartesian closed functor into the co-Kleisli category of ! (Seely/Benton; see notes), an admissible construction |

**Attacks on N_amb:**

| Attack | Result |
|---|---|
| **Reader / Cayley state wrappers** (report 008 critique) | These are Kleisli categories of a reader or state monad, so admissible. Under N_amb they are acceptable **only** for interpreting non-logical Σ (edges, group generators), where P7 says interpretation is legitimate and ledger-tracked. A reader environment carrying a *logical* rule would have to make F(φ⇒ψ) an ambient exponential in Kleisli(Reader_E). Kleisli(Reader_E) is cartesian closed when A is, and its exponential does not use E. So a rule table in E cannot alter the logical part |
| **Universes / internal syntax externalized by representables** (u ↦ Tm(s,u)) | The objects are ambient types, so they are admissible in form. Logical connectives must still be ambient exponentials, so case 1′ applies |
| **Higman / A_U** | Accepted for group sources (no logic), rejected for nothing else. Correct by P7 |
| **Thin tabulation (P6)** | Rejected. This is the defining test |

---

## 6. Does fundamentality need additional structure? (answer to the core question)

**Yes, and the form is determined.**

1. **The generated algebra alone does not suffice.**
   - By P1/P2, any notion invariant under presentation change is a property of the generated algebra.
   - By P5 and 009's lemma, any notion that reads only the generated *interface* cannot separate full and faithful realizations.
   - By P6, isomorphic interfaces can hide a tabulated connective.
2. **Three pieces of additional structure suffice in every case tested.**
   - **A doctrine D_S.** It specifies which operations are logical, via universal properties. It is presentation-independent by property-likeness: the operations are elements characterised up to unique isomorphism, so they survive P1.
   - **The ambient target.** Universal properties are tested against all of A's objects, or those of an admissible construction Φ(A).
   - **A provenance ledger for the non-logical signature Σ.** By P7 this is the only remaining freedom.
3. **Mathematical form.**
   - Pseudo-morphisms of 2-monad algebras (Kelly–Street, Lack).
   - Equivalently, for type theories, morphisms of representable map categories (Uemura) that preserve the relevant type-former structure.
   - Plus annotated presentations for the ledger. Report 009 §9.2 independently suggests "a chosen judgment fibration/logical doctrine"; this report supplies the separating lemma (P6) and the forced/free decomposition (P7).
4. **No new theory is introduced.**
   - Every ingredient is established: clones, Lawvere theories, Tietze, universal properties, property-like 2-monads, (co-)Kleisli constructions.
   - The new parts are the arguments P1–P7 and the observation that they fit the ProofBasis question.
5. **No narrowing.**
   - C is unchanged.
   - Sources without logical structure are fully covered: N_amb is vacuous there, and they are represented by interpreting Σ.
   - The universal ambition is restated at the doctrine level (Q3), not shrunk.

---

## 7. Unresolved questions

| # | Question | Why it matters |
|---|---|---|
| **Q1** | Which constructions Φ(A) are admissible: identity, (co)Kleisli, Eilenberg–Moore, slices, glueing? Externalizations of *internal* categories, whose objects are global elements of a data object, must be excluded, or must still face ambient probes | Without a principled class, N_amb could be satisfied vacuously by Φ(A) := the source's own term model built internally |
| **Q2** | **Decisive next test.** Fix a concrete A with natural numbers and case analysis, and the deep (box) realization of NJ(→) with βη. Prove or refute that F(φ⇒ψ) is not an ambient exponential, i.e. that some ambient probe breaks the currying bijection. Also determine the minimal ambient features (code inspection versus opaque sorts) that decide the case | It turns 1′ / 2′ from INFERENCE into a theorem, or exposes an interpreter that survives N_amb |
| **Q3** | Is there one fixed doctrine D_A and admissible constructions Φ_D such that every source doctrine D_S maps into Φ_D(A)? Covers cartesian, linear, modal and classical: control categories, with the caveat that parametricity is inconsistent with λμ (Hasegawa 2006, report 008 notes) | This is the ProofBasis universality question at the level of doctrines. It is not narrowed |
| **Q4** | A Tietze theorem for dependently typed and binding presentations (generalised algebraic theories, second-order theories). P1 needs only T1 and T2 together with "every element is term-definable", which holds there (INFERENCE) | P1's scope |
| **Q5** | How to classify *conditional* equations and equality reflection in deep realizations of sources with undecidable ≈_S (§2.1) | Trust and equality interface |

---

## 8. Recommendation

1. **Do not adopt N_split or N_rep.**
   - N_rep is equivalent to faithfulness (P4).
   - N_split rejects natural embeddings (P3) and accepts checkers (009).
2. **Adopt the conclusion that fundamentality is doctrine-relative and ambient.**
   - Make N_amb the candidate non-vacuity component.
   - It still needs Q1 (admissible constructions) and Q2 (the deep-realization test) before any H1 is frozen.
3. **Use a logical source for the next control.** 009's graph and group controls cannot test fundamentality of *logical* operations. The decisive control is Q2.
4. **Relation to report 008 (my PR #13).**
   - N_amb refines 008's N_log ∧ N_gen.
   - 008's "fixed interface menu" becomes "admissible constructions Φ(A)".
   - 008's genericity becomes "logical part forced by universal properties" (P7).
   - 008's restriction to C_harm^prop is **not** needed for N_amb: non-logical sources are covered by P7. That restriction should be reconsidered.

---

## 9. Source discipline and limits

- P1–P7 are informal. P3 has a bounded mechanical check.
- Statuses of the established results in §3 are in the source notes. Several are secondary or memory:
  - Mac Lane coherence for the S_p fact;
  - Kapur–Narendran;
  - Seely/Benton co-Kleisli cartesian closure;
  - Kelly–Lack examples.
- Hasegawa 2000 and HHP were not re-read here. I rely on report 009's verified citations and say so.
- No novelty is claimed.

## 10. Changes after the fresh critique

(Filled in after review.)
