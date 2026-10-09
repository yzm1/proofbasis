# Report 010: Cross-review A — algebraic fundamentality (Claude on Codex's PR #14)

- **Primary target:** Codex's `reports/009-adversarial-definitions.md`, PR #14, head `e4855a8`.
- **Also read:**
  - AGENTS.md, the charter, `docs/STAGE_0_7_RECONCILIATION.md`;
  - my PR #13 (`reports/008-constructive-definitions.md`) with its notes and critique;
  - reports 002, 005, 006 and 007.
- **Baseline:** main `9c87762`.
- **Not done:**
  - no edits to 008, 009, the charter or the reconciliation;
  - no existence attempt;
  - the source class C is not narrowed.

  Where a proposal would reinterpret the reconciliation's test controls, it is flagged for owner decision (§7).
- **Author / date:** Claude (Claude Code session), 2026-10-09.
- **Supporting files:**
  - `reports/010-source-notes/` (`sources.md`, `fresh-critique.md`);
  - `reports/010-checks/`, two bounded scripts with their outputs.

**Revision note.** A fresh-context referee broke the first draft (2 fatal, 8 major, 9 minor findings). The draft proposed an "ambient, doctrine-relative" criterion, N_amb, as the missing non-vacuity filter. That proposal is **withdrawn**:
- it is not a well-defined predicate on the targets used;
- it accepts a fixed universal rule-table checker.

§10 lists every change. The conclusions below are narrower than the first draft's.

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED (verified)** | Statement read this session in a primary text; location in the notes |
| **ESTABLISHED (secondary)** | Read only as restated in a retrieved secondary text |
| **FOLKLORE (proof reproduced)** | Known result; a complete proof is reproduced here for the project's setting |
| **PROVED HERE** | Argument with a complete informal proof; not machine-checked, not refereed |
| **COUNTEREXAMPLE** | Concrete construction, verified in full |
| **CHECKED (bounded)** | Exhaustive enumeration for the stated cases only |
| **INFERENCE** | Argument with a named gap |
| **OPEN** | Unresolved |
| **UNVERIFIED-MEMORY** | Not checked against a source this session |

---

## 1. Verdict

### 1.1 Report 009's mathematics holds

I re-derived 009's consequential arguments independently (§2):
- N_rep is equivalent to faithfulness, by Yoneda;
- the abelianization obstruction to N_split on a fixed universal group;
- the isomorphism between the checker interface and the typed-path interface;
- the precomposition (Yoneda) calculation behind E8.

I agree with its decision, **DEFINITION UNRESOLVED**, and with its claim that neither N_split nor N_rep can serve as H1's non-vacuity predicate.

### 1.2 Refinements to 009

1. **N_split rejects natural structural embeddings, not only universal groups.** This is 009's own abelianization lemma, applied to cases 009 did not check (§5.3):
   - the free-SMC embedding of C_n (rotation ↦ n-cycle) fails N_split for every n ≥ 3;
   - every faithful embedding into Thompson's V fails it.

   So N_split has false negatives on the controls that reports 005, 006 and 009 call legitimate.
2. **009's indistinguishability lemma generalises.** It extends to any source that has a realization which is an *isomorphism* onto its interface (P5, §5.2).
3. **Scope caveat.** 009 establishes its checker/path isomorphism for sources whose proof equality is flattening (associativity and units). For sources with β/η, a checker must use either conditional equality (reflection) or a normaliser. That changes the trust analysis or the coverage (§2.1).

### 1.3 What existing mathematics says about generating operations (§3–§4)

**There is a canonical presentation-independent "algebra of operations"** in each standard setting:
- clone or Lawvere theory;
- free structured category;
- second-order algebraic theory;
- for equality derivations, polygraphic resolutions up to homotopy.

**Lawvere himself records two limits** (ESTABLISHED, verified, TAC Reprints 5):
- p. 65: two natural presentations of groups give *different* theories, because of the empty model;
- p. 89: one category of models can arise from non-isomorphic theories.

**Folklore result (Tietze; definitional equivalence; proof reproduced, §4).** Passing from a presentation to its generated structure:
- **preserves** exactly the isomorphism-invariant properties of the generated structure. These include every extremal or existential property over presentations: rank, existence of an irredundant basis, finite or finite-convergent presentability (Squier), finite derivation type;
- **loses** the data of the particular presentation: which elements are designated primitive, which equations are designated axioms, the named relation-cells, and provenance.

### 1.4 Does fundamentality need structure beyond the generated algebra?

**Yes.** Neither the generated interface nor the generated algebra suffices (P2, P5, and 009's lemma).

Universal properties are the classical presentation-independent source of "logical" operations. I tested them as the extra structure (§6) and they are **necessary but not sufficient**:
- **For connectives with universal properties.** Doctrine-relative ambient preservation (the source's implication goes to the target's own exponential) is a genuine fidelity condition. It separates realizations with isomorphic interfaces (P6). In proof-irrelevant settings it is *equivalent* to requiring derived operations (P6′, a routine instance of compatibility with congruences).
- **For rules without universal properties.** This covers Hilbert axioms, raw-α or β-only calculi, arbitrary sequent rules, and the reconciliation's graph, group and checker controls. Any faithful realization is just an interpretation of generators (P7), so universal-property criteria are **vacuous** there.
- **Consequence.** A fixed universal rule-table checker, equipped with generic universal-property structure for the connectives, passes every universal-property criterion (§6.3, critique F2). Universal properties therefore do not separate genuine reasoning from interpretation.

**What remains is a sort or fibration discipline** that makes "this realized rule is a template parametric in formula variables and carries no data in types" an *element property* of the generated structure, so that it survives Tietze moves (P1).

- Existing ingredients:
  - comprehension categories / representable map categories with designated type versus term sorts (Uemura; Jacobs);
  - Reynolds parametricity.
- Report 008's genericity criterion with fixed interfaces is one instance.
- **Whether any such discipline rejects the reconciliation's controls without also rejecting legitimate translations is OPEN.** Both 008 and this report end up *accepting* rule-table realizations of sources whose rules are non-logical generators (graph and group calculi), as relative interpretations. That reclassifies part of the reconciliation's controls and **requires an owner decision** (§7, D-1).

---

## 2. Independent checks of Report 009

| 009 claim | Where | Check | Status |
|---|---|---|---|
| N_rep holds for every small faithful compositional interface | §3–4 | The Yoneda embedding y is fully faithful, so y∘F is faithful iff F is; the remaining clauses hold for y. N_rep ⇔ I2 | **Correct** (009's result; restated as P4) |
| H, K are inverse between the checker and path interfaces | §5 | The checker's Hom is boxes quotiented by a fixed box-irrelevance equation, so each class is a path word by construction | **Correct**, for flattening-equality sources (§2.1) |
| Interface invariants cannot separate the two | §5 lemma | Transport of structure | **Correct**; generalised in P5 |
| No fixed finitely generated group U retracts onto every C_p | §6 | Write U^ab ≅ ℤ^r ⊕ T, and choose p with p ∤ \|T\|. A retraction U → C_p factors through U^ab. The image of C_p in U^ab is p-torsion, hence trivial. Contradiction | **Correct** (re-derived) |
| Natural endotransformations of Set(D, –) are precompositions | §6 | Yoneda | **Correct** |
| LF (HHP) passes N_split / N_rep at raw-α identity, fails object β | §7 | Consistent with the verified HHP Theorem 4.1 in reports 007/009. Not re-read here | **Plausible** (relies on 009's citation) |
| Girard (Hasegawa 2000, Theorem 5.6) passes N_split | §7 | Fullness plus faithfulness gives a two-sided inverse. Hasegawa 2000 not retrieved here | **Valid, conditional on 009's verified citation** |
| "Other A with different generated interfaces are not excluded" | §6 | True, but natural compound interfaces are excluded too | **Incomplete** (§5.3) |

### 2.1 Scope caveat (sources with β/η)

In 009's checker, ≈_S is flattening, realised by A's own list-append laws plus box irrelevance. For a source such as NJ(→) with βη, box irrelevance must identify boxes whose serialised terms are βη-equal. That needs one of:
- **(i) a fixed conditional equation** (reflection from a data-level equality derivation), which changes the trust analysis (009 §2.3 permits it only as a fixed reflection rule);
- **(ii) a fixed normaliser to canonical boxes.** This exists only when ≈_S is decidable, so it fails on sources like those in report 006 Proposition A.

009 does not claim more than this, but its §1 headline ("an explicit serialized proof-checker representation … satisfy both") should carry the scope.

---

## 3. Established mathematics of generating operations

Locations and statuses are in `reports/010-source-notes/sources.md`.

| Topic | Statement | Status |
|---|---|---|
| Free algebras | F_K(X) has the universal mapping property for the variety K over X (Birkhoff). Burris–Sankappanavar, Theorem II.10.10, p. 67 | ESTABLISHED (verified) |
| Term functions | Burris–Sankappanavar, Definition II.10.2, p. 63. The book does not use "clone" or "term-equivalent" | ESTABLISHED (verified) |
| Boolean algebras ↔ Boolean rings | Interdefinable by terms. Burris–Sankappanavar, Theorem IV.2.3, p. 123. *Which* operations are basic is not invariant | ESTABLISHED (verified) |
| Mal'cev | Congruence permutability ⇔ a term with m(x,y,y) = x = m(y,y,x). Burris–Sankappanavar, Theorem II.12.2, p. 78. A clone-level (presentation-independent) condition | ESTABLISHED (verified) |
| Clones; Post's lattice | Every clone on {0,1} has a finite basis. {∧,¬}, {NAND} and {→,⊥} are irredundant bases of the full clone, of different sizes (irredundancy checked by hand by the critic). On k ≥ 3 elements there are continuum many clones | ESTABLISHED (secondary: Jeřábek arXiv:1909.12211; Thomas arXiv:1007.2924; Vucaj–Zhuk arXiv:2304.12807) |
| Lawvere theories | Category of theories, p. 62. A presentation determines "the theory presented" as a coequalizer, p. 71. **Remark p. 65:** two group presentations give two theories (empty model). **Remark p. 89:** an algebraic category may be represented by non-isomorphic theories | ESTABLISHED (verified, TAC Reprints 5) |
| Tietze | Finite presentations of isomorphic groups are related by finite sequences of Tietze moves. Finite presentability is independent of the finite generating set | ESTABLISHED (secondary: lecture notes, Touikan Theorem 1.6.2; Druţu slides) |
| Squier, FDT, Kapur–Narendran | Finite convergent presentation ⇒ FP₃ (Squier). FDT is independent of the finite presentation (Squier–Otto–Kobayashi). B₃⁺ has a finite convergent presentation only after adding a generator (Kapur–Narendran) | ESTABLISHED (secondary: Guiraud–Malbos arXiv:1402.2587, pp. 3, 25, 28, 37) |
| Property-like 2-monads | Defined as (IEM)∧(AUM) (Kelly–Lack, TAC 3(9), §§3–4). Finite products and coproducts are examples. **Cartesian closed structure is not given as an example, and monoidal closed structure is not a 2-monad on Cat at all (p. 214).** Lax-idempotent ⇒ property-like (Proposition 6.1) | ESTABLISHED (verified) |
| 2-monads, morphisms | Lax, pseudo and strict T-morphisms: Lack, *A 2-categories companion*, §4.1 | ESTABLISHED (verified) |
| Second-order algebraic theories | Fiore–Mahmoud arXiv:1308.5409, Definition 4.1, Theorems 4.1, 5.1, 5.2 (theories ≃ presentations). Extended abstract, proofs omitted | ESTABLISHED (verified, with that caveat) |
| Linear exponential | "If a linear category has products then the Kleisli category L_! is cartesian closed" (Benton TR-352, Corollary 19, p. 26). The products hypothesis is essential (p. 23) | ESTABLISHED (verified, OCR) |
| Internal categories | Externalisation; small fibrations are externalisations of internal categories (Streicher arXiv:1801.02927, §4) | ESTABLISHED (verified) |
| Derivable vs admissible | Admissible: closure of theorems under the rule. Derivable: via ⊢ A → B (Iemhoff). Assumes a deduction theorem | ESTABLISHED (verified, course notes and Iemhoff p. 1) |
| Logical functor | Preserves finite limits, exponentials and the subobject classifier | ESTABLISHED (secondary: nLab, Streicher gloss) |

**Rules versus derived operations** (corrected from the first draft; critique M5).
- Adding a *derivable* rule *together with its defining proof equation* (r(ξ) = template) is a Tietze move. Without that equation, it adds a new proof constructor and changes the proof structure (009 §2.4).
- Adding an admissible but underivable rule, such as cut, changes the proof structure. Adding it *together with* equations that eliminate it (cut-elimination equations) may leave the hom-sets unchanged.

**Answer to the assignment's question.**
- Existing formalisms give a satisfactory, presentation-independent *algebra of proof operations*: the generated structured category or theory. The caveats are Lawvere's p. 65/p. 89 remarks about signature and Morita choice.
- None of them gives a presentation-independent notion of *fundamental generator*.
- The closest presentation-independent notions are element properties defined by universal properties, together with existential or extremal properties over presentations.

---

## 4. Preserved versus lost information (folklore; proofs reproduced)

**Setting.** A finitary presentational framework, with two Tietze moves and their inverses:
- **T1:** add a generator y with a defining equation y = t;
- **T2:** add an equation that holds in ⟨P⟩.

Here ⟨P⟩ is the structure generated by the presentation P.

**Assumptions** (critique M6), made explicit:
- predicates are invariant under renaming of generator symbols;
- the comparison is up to **isomorphism** of generated structures. Moves that add sorts or atoms (equivalence rather than isomorphism) are not covered.

### P1. Tietze collapse of generator predicates (FOLKLORE; proof reproduced)

**Statement.**
- Let Φ(P, g) be a predicate on (presentation, generator).
- Suppose Φ is invariant under renaming and under every Tietze move that keeps g.
- Then Φ(P, g) = Φ(P′, g′) whenever some isomorphism ⟨P⟩ ≅ ⟨P′⟩ sends g to g′.

**Proof.**
1. Identify the two structures along the isomorphism, and rename g′ to g. Write X = {g} ⊔ X₀ and X′ = {g} ⊔ X′₀.
2. Choose terms: t_{x′} over X equal to x′, and s_x over X′ equal to x.
3. From P:
   - add each x′ with the defining equation x′ = t_{x′} (T1);
   - add R′ and the equations x = s_x (T2; all hold).

   This reaches Q = (X ∪ X′₀, R ∪ R′ ∪ {x′ = t_{x′}} ∪ {x = s_x}). The symmetric moves from P′ reach the same Q. No move removes g. ∎

**Consequence.**
- Every element is a generator of some presentation (by T1).
- So a Tietze-invariant generator predicate is an *element* predicate on ⟨P⟩, and an isomorphism-invariant one is a union of automorphism orbits.
- "Lies in *some* irredundant basis" is such an element predicate. It holds for ∧ and for the constant 0, and fails for projections (critique M4).
- Membership in a *given* basis is not an element predicate.

### P2. Presentation properties (FOLKLORE)

If Ψ(P) is Tietze-invariant, then Ψ(P) = Ψ(P′) whenever ⟨P⟩ ≅ ⟨P′⟩. The proof is P1 without g.

**Preserved:** every isomorphism-invariant property of ⟨P⟩, including the existential and extremal ones over presentations:
- rank;
- existence of an irredundant basis;
- finite, or finite convergent, presentability;
- FDT and the homotopy type of polygraphic resolutions.

**Lost:** the data of a particular presentation:
- which elements are designated as generators;
- which equations are designated as axioms rather than consequences;
- the named relation-cells and the specific derivations of equalities;
- the provenance ledger. 009 §2.4 gives proof-structure isomorphisms that change the ledger.

**Caveat (Lawvere p. 65).** Two signatures that look equivalent can generate non-isomorphic theories, for example when one admits the empty model. The choice of signature, nullary symbols in particular, is not merely presentational.

---

## 5. N_split and N_rep

### 5.1 P4 (009's Yoneda result, restated)

N_rep ⇔ faithfulness (I2). Credit: 009 §3.

### 5.2 P5. Interface collapse, generalised (PROVED HERE; elementary)

**Statement.**
- Let an *interface criterion* be a predicate N(P_S, B_F, F) invariant under isomorphisms of the triple. Such an isomorphism is one of structured categories B_F ≅ B′_F commuting with F and F′.
- Then any two realizations that are **isomorphisms** onto their interfaces (bijective on objects, full and faithful, structure-preserving) get the same verdict.

**Proof.** F′∘F⁻¹ is such an isomorphism. ∎

**Application.**
- 009's lemma is the graph-source instance.
- For a logical source with decidable ≈_S, a canonical-box checker (§2.1(ii)) would be such a realization. Its existence for a fixed A is INFERENCE.

### 5.3 P3. N_split rejects natural embeddings (PROVED HERE, from 009's lemma; CHECKED for n = 3, 5, 7)

**Claim.** A left inverse at the translated boundary restricts to a group homomorphism from the endomorphism unit group G_T to C_n, splitting the embedded C_n. It factors through G_T^ab. For prime p, a splitting exists iff the image of the generator is nonzero in G_T^ab ⊗ ℤ/p (critique minor 1).

**Proof sketch.** The left inverse is a homomorphism into an abelian group, so it factors through the abelianization. The embedded C_n must survive there for the composite to be the identity.

**Cases.**
- **(a) Free SMC.** End(X^{⊗n}) ≅ S_n (by elementary reasoning about the free SMC, as verified by report 006's critic), and S_n^ab = C₂. For n ≥ 3 no homomorphism S_n → C_n is the identity on the n-cycle, because the n-cycle's image in C₂ has order at most 2.
- **(b) Thompson's V.** V is simple (Cannon–Floyd–Parry Theorem 6.9, verified in report 005), so V^ab = 1 and there is no splitting for any n ≥ 2.

**Bounded check.** `reports/010-checks/retraction_check.py` finds only the trivial homomorphism S_n → C_n for n = 3, 5, 7. It confirms S_n^ab = C₂ only.

**Consequence.** N_split has false negatives on embeddings that reports 005, 006 and 009 treat as legitimate. It behaves as a *reversibility* condition, not a non-vacuity condition. This strengthens 009 §6.

---

## 6. Universal properties as the extra structure: what works and what fails

### 6.1 P6. Isomorphic interfaces, different ambient behaviour (COUNTEREXAMPLE; a standard fact, credited)

**Source.** The three-element Heyting chain H₃ = {0 < m < 1}. Here m ⇒ 0 = 0.

**Realization R₁.** The identity.

**Realization R₂.** The order-embedding F(0) = 0, F(m) = a, F(1) = 1 into the Boolean algebra B₄ = {0, a, b, 1}. It preserves meets and top and is full and faithful, so its interface is isomorphic to R₁'s.

**The difference.** F(m ⇒ 0) = 0, but a ⇒ 0 = b in B₄. The probe b ∉ image witnesses failure of the ambient universal property.

**Verification.** All computations are VERIFIED by the critic and by `reports/010-checks/p6check.py`. This is the standard fact that an order-embedding need not be a Heyting homomorphism.

**Caveat.** The table (x, y) ↦ F(x ⇒ y) is not a Boolean term operation, so a "connective images must be derived operations" criterion (002 T1, 008 componentwise) also rejects R₂.

### 6.2 P6′. In proof-irrelevant settings, derivedness equals ambient preservation (PROVED HERE; routine)

**Statement.**
- Let F : H → K be a monotone, meet-preserving map of Heyting algebras.
- Suppose some binary Heyting term t over K satisfies t(Fx, Fy) = F(x ⇒ y).
- Then F(x ⇒ y) = (Fx ⇒ Fy) ∧ F(1).
- In particular, if F(1) = ⊤, then F preserves ⇒.

**Proof.** Put u = Fx, v = Fy, w = F(x ⇒ y).
1. **w ≤ (u ⇒ v) ∧ F(1).** By residuation, as in the first draft: (x⇒y) ∧ x ≤ y gives w ∧ u ≤ v, and w ≤ F(1) by monotonicity.
2. **The congruence.** Take Φ = ↑(u ⇒ v) and its congruence, under which u ≡ u ∧ v.
3. **Applying t.** Term operations respect congruences, so w = t(u, v) ≡ t(u ∧ v, v) = F((x∧y) ⇒ y) = F(1). Hence (w ⇔ F(1)) ∈ Φ. Since w ≤ F(1), that bi-implication equals F(1) ⇒ w, so F(1) ⇒ w ≥ u ⇒ v, i.e. (u ⇒ v) ∧ F(1) ≤ w.
4. **Conclusion.** Combined with step 1, w = (u ⇒ v) ∧ F(1). ∎

**Notes.**
- The critic supplies a counterexample when F(1) ≠ ⊤. It is checked in `p6check.py`.
- In the interface I, F(1) = ⊤ follows from derivability preservation and reflection at the empty context (critique M2).
- This is an instance of known results on functions compatible with congruences (Caicedo–Cignoli; UNVERIFIED-MEMORY).

**Meaning.** For derivability-level fidelity of a connective with a universal property, ambient preservation and "derived operation" coincide. The LF βη case does **not** separate them: it fails I2 and equality preservation already, and `imp` is declared, not derived (critique M1). **No example in this report separates derivedness from ambient universal-property preservation.**

### 6.3 P7 and the failure of universal-property criteria as non-vacuity filters

**P7 (ESTABLISHED in substance).** If P_S is the free structure on a signature Σ of non-logical generators for some doctrine, modulo equations E, then structure-preserving (strict) morphisms P_S → M correspond to interpretations of Σ in M that satisfy E. This is the universal property of free structures (Burris–Sankappanavar II.10.10; Fiore–Mahmoud). For pseudo-morphisms the correspondence needs flexibility results (Blackwell–Kelly–Power; UNVERIFIED-MEMORY).

**Withdrawn proposal N_amb.** The first draft proposed: "F is a pseudo-morphism of the source's doctrine D_S into A or into an admissible construction Φ(A)." The referee showed it fails, for three reasons.

- **Not well-defined (F1).**
  - A is a sorted signature, so the ambient category of probes is unspecified.
  - D_S is not a function of S.
  - Φ(A) ranges over an open class.
  - In 009's opaque-sort checker, data cannot take proof inputs, so the "code-inspecting probes" my case 1′ relied on do not exist.
  - To realise grafting under binders, an opaque Hom sort needs Hom-level abstraction and application. That collapses my rejected case 1′ into my accepted case 1″.
- **Accepts a universal checker (F2).**
  - One fixed A contains a data-level checker for arbitrary rule tables together with generic code-indexed universal-property schemas for the connectives.
  - Such an A passes N_amb for every source whose connectives fit that structure.
  - For sources whose rules have no universal property, N_amb is vacuous. That includes:
    - raw α;
    - β without η;
    - Hilbert systems;
    - arbitrary sequent calculi;
    - the graph, group and checker controls.
- **Kelly–Lack scope (M3).** Property-likeness, which the first draft used to make "preservation" a property, is established for finite (co)products. It is not established for closed structure. Monoidal closed structure is not even a 2-monad on Cat.

**Conclusion (PROVED HERE, from P7).**
- Any criterion that only requires preservation of universal-property structure imposes **nothing** on the realization of rules that are not determined by universal properties.
- Those are exactly the rules a rule-table interpreter handles.
- So universal properties are a fidelity condition for the logical part, and **not** a non-vacuity filter.

---

## 7. Does fundamentality need extra structure, and of what form?

1. **Beyond the generated interface: yes.** By P5 and 009, interface-only criteria cannot separate realizations that are isomorphisms onto their interfaces.
2. **Beyond the generated algebra: yes,** if the distinction is to concern *how* a source rule is realized.
   - By P1/P2, presentation-invariant criteria see only isomorphism-invariant properties of (A, F) and their elements.
   - A rule realised by a fixed core template and a rule realised by a data-indexed lookup can both be elements of the same generated A.
   - To tell them apart by an *element property*, the structure must carry a notion of which sorts are formula or proof sorts and which are data. It must also carry a notion of parametricity in formula variables.
3. **Candidate form, all from existing mathematics.**
   - A comprehension category or representable map category, with designated type and term (proof versus data) sorts (Jacobs; Uemura, verified in report 008's notes).
   - Allowed equivalences: those preserving the designation.
   - Required: realized rules are templates natural or parametric in the formula-variable sorts (Reynolds; report 008's genericity with fixed interfaces).
   - Under this structure, "generic realization" is an element property and so survives P1.
   - **Status: proposal.** Whether it rejects every interpreter and admits every legitimate translation is OPEN. Report 008 records one unresolved attack, A10.
4. **Owner decision D-1 (flagged, not adopted).**
   - Every candidate in 008 and here *accepts* realizations of graph and group calculi by data tables or universal groups. The reasoning is that such sources' rules are non-logical generators (P7) and their realization is a relative interpretation.
   - This reclassifies the reconciliation's controls (a), (b) and (e) **on those sources**.
   - The reconciliation requires N to reject them. Either:
     - the owners accept the reclassification, with explicit reasons; or
     - a criterion must be found that rejects data-table realizations of *non-logical* generators. No such criterion is known that also accepts relative interpretations generally, such as Church encodings (008 A3) or models of theories.
   - **This report does not decide.**
5. **No narrowing of C.** C is unchanged. The limitation in item 4 is a limitation of the criteria, not a removal of sources.

---

## 8. Unresolved questions

| # | Question |
|---|---|
| Q1 | Formalize the sort discipline of §7.3 for report 002's finite schematic presentations with binding. Is "generic realization" then invariant under all designation-preserving equivalences, and stable under adding sorts (equivalence rather than isomorphism; critique M6)? |
| Q2 | Is there an example separating "derived operation" from "ambient universal-property preservation" among realizations that satisfy I1–I3? (None found: P6′ and the LF βη case.) |
| Q3 | Decision D-1 (§7.4) |
| Q4 | 009's checker for sources with β/η (§2.1): must a fixed A use equality reflection or a normaliser, and does either survive the trust interface? |
| Q5 | A Tietze theorem for dependent and binding presentations *up to equivalence* (adding sorts). P1/P2 assume isomorphism |

---

## 9. Recommendation

1. Reject N_split and N_rep as non-vacuity predicates (009; §5).
2. Do not adopt universal-property preservation (N_amb) as non-vacuity. Keep it, or its equivalent "derived connective images", as a *fidelity* clause for connectives with universal properties.
3. The next owner decisions:
   - **D-1:** reclassify or keep the controls on non-logical sources;
   - **the sort discipline of §7.3:** which sorts are proof sorts, which equivalences preserve that, and parametricity.

   009 §9.3's gate test ("do H, K lift to equivalences preserving the extra structure?") then becomes concrete:
   - under the §7.3 discipline, H and K live entirely in data-indexed proof sorts on both sides;
   - so whether they lift depends on D-1.
4. Do not begin existence proofs until D-1 and Q1 are settled.

---

## 10. Changes after the fresh critique

The critique is reproduced in `reports/010-source-notes/fresh-critique.md`.

| Finding | First draft | Action |
|---|---|---|
| F1 (FATAL) | N_amb presented as a well-defined criterion with a verdict table | **Withdrawn**. §6.3 explains why it is ill-defined |
| F2 (FATAL) | "N_amb suffices"; "the form is determined"; "no narrowing" | **Withdrawn**. N_amb accepts a universal checker. The control reclassification is flagged as D-1 |
| M1 | LF βη presented as separating derivedness from ambient preservation | Withdrawn: LF fails I2 and equality anyway |
| M2 | P6′ needed F(1) = ⊤ | Generalized formula; the critic's counterexample is added to checks; F(1) = ⊤ follows from I1; the result is labelled routine |
| M3 | Misparaphrase of Kelly–Lack; D_S undefined | Corrected scope (finite (co)products; closed structure not covered) |
| M4 | "Irredundant basis membership lost"; "two forms preserved" | Corrected: existential and extremal properties are preserved; given-presentation data is lost |
| M5 | Derivable rule = Tietze move; admissible always changes structure | Corrected, with the defining-equation caveat |
| M6 | P1/P2 "PROVED HERE"; hidden assumptions | Relabelled FOLKLORE; assumptions stated; Q5 added |
| M7 | Logical/non-logical split presented as forced | Presented as a choice. Its effect on the controls is flagged (D-1) |
| M8 | Missing notes; unlabelled rows | Notes added; Girard row removed; labels unified |
| Minor 1–9 | P3 scope; P4/P5 credit; P5 needs isomorphism; misattribution of 009 §9.2; Kleisli products; P7 pseudo case; row 1″ non sequitur; P6 standard; garbled row | Applied: P3 restated for n ≥ 3 with the ⊗ℤ/p criterion; P4 credited to 009; P5 requires isomorphism; 009 §9.2's "inspect the whole target" credited; Kleisli rows removed with N_amb; P7 pseudo case marked UNVERIFIED-MEMORY; P6 marked standard |
