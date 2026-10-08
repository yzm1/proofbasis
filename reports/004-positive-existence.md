# Report 004: Positive existence — the strongest construction and its exact boundary

**Stage:** 0.6, "Existence vs. Impossibility". This report takes the positive-construction role.

**Author:** Claude (Claude Code session), 2026-10-08.

**Inputs:**
- Reports 001–003.
- `docs/STAGE_0_5_ACCEPTANCE_REVIEW.md`.
- Definitions D1/D2 of report 002 (§2.4).
- Source logs in `reports/004-source-notes/`.
- Machine checks in `reports/004-checks/`.

**This report does not modify:**
- the charter;
- the earlier reports;
- D1/D2 as stated in report 002.

Where this report refines D2, it does so in a new, separately named definition (CRR, §2.2).

**Revision note.** A fresh-context adversarial referee reviewed the first draft (`004-source-notes/fresh-critique.md`). It found:
- one fatal error: the claim that a matrix interpreter passes report 002's D2;
- four major errors, among them a test (§10) that did not discriminate and a decision that pointed at an unfrozen target.

All of these are corrected below. §11 lists every withdrawal and change.

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED** | Published theorem. The passage was read in a retrieved primary or survey text, and the source and location are given |
| **ESTABLISHED (secondary)** | Published theorem seen only as restated by another named author |
| **PROVED HERE (informal)** | A complete pen-and-paper argument written in this report. It is not machine-checked and not refereed. The fresh critic re-derived it, which is agreement and not verification |
| **SOLVER-CHECKED** | One instance checked by Z3 5.1.0 or by finite enumeration (`reports/004-checks/`). This is not a proof of any general statement |
| **INFERENCE** | The author's argument, with a named gap |
| **CONJECTURE** / **OPEN** | Not known to be true or false |
| **REFUTED** | A counterexample is cited |
| **UNVERIFIED-MEMORY** | Recollection that was not checked in this session |

---

## 1. Executive verdict

1. **The frozen conjecture P (§2) is REFUTED.**
   - P asks for a fixed finite core, classical first-order logic (FOL) under its canonical relational translation, that represents every finitely axiomatizable normal modal logic.
   - The representation must:
     - preserve **and** reflect derivability;
     - commute with substitution;
     - map derivations homomorphically;
     - use an environment that cannot constrain valuations.
   - P fails in two independent ways (§5):
     - **Kripke-incomplete logics**, e.g. van Benthem's TMEQ and Thomason's logic;
     - **Kripke-complete logics that no elementary class characterises**, e.g. K+McKinsey and GL.
2. **The exact boundary is a theorem (PROVED HERE, informal; §3.1).**
   - A normal modal logic has such a representation iff it is the logic of an elementary class of Kripke frames.
   - This holds whatever the environment is. That makes it the nontriviality invariant (§6): no environment can make the core represent anything other than the logic of the frames that satisfy it.
   - Two natural relaxations add nothing or fail:
     - **Extra vocabulary in the environment adds nothing.** By the Goldblatt–Hodkinson–Venema form of Fine's theorem (§6.2, D-6).
     - **Arbitrary first-order connective clauses fail for "completely incomplete" logics** (Proposition 6).
3. **The strongest positive construction is ESTABLISHED (Sahlqvist 1975; §4) and not novel.**
   - Every K ⊕ Σ with Σ a finite set of Sahlqvist formulas is represented with a finite, effectively computed environment of first-order frame conditions.
   - The environment is a *frame-equivalent, proposition-free restatement* of the axioms (§2.3). Each axiom *instance* is derived in the core.
   - Analogues:
     - distributive modal logic: ESTABLISHED (GNV Thm 3.8);
     - non-distributive lattice-expansion logics such as the Lambek calculus and MALL: INFERENCE from Conradie–Palmigiano.
4. **What the referee changed** (§6.1, §11).
   - The first draft claimed a Lindenbaum-matrix interpreter passes report 002's D2. **That claim is withdrawn.**
     - The interpreter fails D2's substitution-naturality / homomorphism clause T3 at generic formula metavariables.
     - A finite countermodel confirms this (SOLVER-CHECKED).
   - The smaller finding that survives: **D2's environment clause T4 is vacuous for any first-order core.** D2's anti-importing force there comes entirely from T1 + T3.
5. **No proof-identity (R3) analogue exists in the literature examined (§5.4).**
   - Faithful-completeness theorems exist but are each specific to one structure: Friedman/Statman (CCC), Soloviev (SMCC), HHP (traced), Selinger (dagger compact), de Carvalho (MELL).
   - Faithfulness alone is cheap: a single cartesian model separates proofs. The discriminating proof-level analogue of *reflection* is **fullness**.
6. **Decision: NARROW (§9).**
   - **The R1 line is STOP.** Its positive part is classical (redundant) and its universality is refuted.
   - **The program narrows to P₃**, frozen in §5.5: proof-relevant frame semantics with an anti-Yoneda clause (finite frames) and an anti-collapse clause (fullness). P₃ is OPEN.
   - **The single next test (§10)** is a fixture-level fullness count: for p⊗p ⊢ p⊗p, do the uniform families over finite promonoidal frames number exactly 1 without symmetry and exactly 2 with it? A cartesian model gives 4.

---

## 2. Exact conjecture (frozen before analysis)

### 2.1 Source class C (fixed independently of the answer)

**C** is the class of all **finitely axiomatizable normal modal logics** over a finite similarity type τ, where τ is a finite set of operators ∇ with arities n_∇ ≥ 1.

Each L ∈ C is presented as a finitely schematic Hilbert calculus (report 002 §2.1):
- classical propositional tautology schemas;
- normality axioms for each ∇;
- finitely many extra axiom schemas Σ;
- modus ponens, and necessitation for each dual box.

**Why this class.** It is the standard class of the textbooks, and it was not chosen with reference to FOL. It contains logics with no first-order frame condition (GL, K+M). It is countably infinite, which follows from finite axiomatizability.

**A second tier, used only in §4.3:** logics over distributive and non-distributive lattice expansions. P makes no claim about it.

### 2.2 Canonical relational representation (CRR)

**Core K.** Classical single-sorted first-order logic with equality, with a fixed finite set of inference rules (any standard sequent or natural-deduction system). The core is the same for every L.

**Vocabulary:**
- an (n+1)-ary relation symbol R_∇ for each n-ary ∇; this frame vocabulary depends only on τ;
- a unary predicate letter P_i for each atom p_i.

Operators are taken as diamond-like primitives. If boxes are primitive, the dual clause is used. This convention is fixed once and does not depend on L.

| Clause | Statement |
|---|---|
| **C1 (canonical formulas)** | ST_x(p_i) = P_i(x); ST_x(⊥) = ⊥; ST_x(φ→ψ) = ST_x(φ) → ST_x(ψ); ST_x(∇(φ₁…φₙ)) = ∃y₁…yₙ (R_∇(x,y⃗) ∧ ⋀ᵢ ST_{yᵢ}(φᵢ)). The clause is **stipulated, fixed by arity alone**; it is the Jónsson–Tarski / standard translation |
| **C2 (wrapper)** | W(φ) = ∀x ST_x(φ), independent of L |
| **C3 (derivations)** | **SN:** ST_x(φ[θ/p]) ≡ ST_x(φ)[P := λy.ST_y(θ)], syntactically up to α, including at formula metavariables. **HOM:** each axiom schema and rule of L has a fixed K-derivation template, and F(r(d⃗)) is the template with the F(dᵢ) grafted in |
| **C4 (environment)** | E_L is a set of first-order **sentences in the frame vocabulary {R_∇} only**. It is *atom-free*: no P_i occurs |
| **C5 (adequacy, ADQ1)** | For all φ: L ⊢ φ ⇔ E_L ⊢_K W(φ). Both preservation (⇒) and reflection (⇐) are required |

**Conjecture P (positive existence, frozen).** Every L ∈ C has a CRR, i.e. an E_L satisfying C4 and C5. Given C1–C2, the derivation map of C3 then exists by Theorem 2.

**Not part of P (kept separate on purpose):**
- **Proof identity (R3).** This is P₃, frozen separately in §5.5.
- **Causal order (R4).** No relational-semantics result examined addresses it. HOM preserves the dependency tree of a derivation and says nothing about scheduling.
- **Efficiency.** See §4.4.

### 2.3 The distinctions the task demands

| Distinction | Where it is enforced |
|---|---|
| Preservation vs reflection | C5 requires both, and §3.1 proves them separately. Preservation alone is cheap (§5.3, the one-point-frame row) |
| Finite signature vs finite set of proofs | K has a finite *rule set*. Its vocabulary grows with τ only by non-logical relation symbols |
| Deriving vs importing a rule | An axiom σ is a statement quantified over valuations (second-order: ∀P⃗ ∀x ST_x(σ)). C4 admits only a *proposition-free* sentence, which exists exactly when the second-order quantifier can be eliminated (Corollary 1). So E_L is a frame-equivalent restatement of the axioms, never the axioms themselves. Each axiom *instance* is derived in K from it. This is the precise and limited sense of "derived, not imported". It is not a claim that E_L carries different content |
| Structural translation vs interpreter | C1, C2 and the Boolean base are fixed. The only per-logic datum is E_L, and Theorem 1 determines everything any E_L can do |
| Proof equivalence vs equivalence of conclusions | P concerns conclusions (C5) and derivation shape (C3). Proof equivalence is P₃ |
| Dependency vs execution order | Only dependency, via HOM |
| Existence vs efficiency | §4.4 |

### 2.4 Relation to D2 of report 002

CRR is D2 specialised to a FOL core, with:
1. connective clauses fixed by arity rather than chosen per logic; per-logic clauses are examined in §5.2;
2. T4 replaced by atom-freeness in the frame vocabulary.

Refinement 2 is not motivated by the withdrawn matrix claim (§6.1). It is motivated by the fact that T4 has no force for a FOL core (§6.1), and by being exactly the hypothesis that Theorem 1 needs.

Report 002 §5 L-h already observed that the standard translation fails ADQ1 for logics that are not elementarily determined. This report makes that observation exact (Theorem 1) and supplies the witnesses (§5).

---

## 3. Strongest established theorem

### 3.1 Theorem 1 (characterisation of CRR-representability) — PROVED HERE (informal)

**Statement.** Let E be a set of sentences in {R_∇}, and let Mod(E) be its models, read as Kripke frames. For every τ-formula φ:

  E ⊢_FOL ∀x ST_x(φ)  ⇔  φ is valid on every frame in Mod(E).

**Corollary 1.** A normal τ-logic L has a CRR iff L = Log(K) for some elementary class K of frames, i.e. a class axiomatized by a set of first-order sentences. When this holds, E_L can be any axiomatization of K.

**Standard translation lemma** (ESTABLISHED, BvB Prop. 3): "M, w ⊨ ϕ iff M ⊨ STx(ϕ)[x ← w]". Here a model is a frame together with the interpretation of each P_i as V(p_i).

**Proof.**

*(⇒, from FO-derivability to frame validity: this is the core-to-source direction, i.e. **reflection** of derivability)*
1. Assume E ⊢ ∀x ST_x(φ). Let F ∈ Mod(E) and let V be any valuation.
2. The expansion (F, V) still satisfies E, because E is atom-free.
3. By soundness, ∀x ST_x(φ) holds in (F, V).
4. By the lemma, φ is true at every point. So φ is valid on F.

*(⇐, from frame validity to FO-derivability: combined with L ⊆ Log(Mod E), this is **preservation**)*
1. Assume φ is valid on Mod(E). Let N ⊨ E be any structure for {R_∇} ∪ {P_i}.
2. Its {R_∇}-reduct F lies in Mod(E), because E mentions no P_i.
3. The P_i^N form a valuation on F, so N ⊨ ∀x ST_x(φ) by the lemma.
4. Gödel completeness then gives E ⊢ ∀x ST_x(φ). ∎

The first draft's direction labels were swapped (critique F6); the mathematics is unchanged.

**Corollary 1 from Theorem 1.** ADQ1 says L = {φ : E ⊢ ∀x ST_x(φ)} = Log(Mod E).

**Where atom-freeness is used.** In both directions, E must survive every re-interpretation of the P_i. This is the precise sense in which the environment cannot constrain valuations.

**Provenance.** The central step is printed in Blackburn–van Benthem's proof of Prop. 34 (BvB p. 42, VERIFIED_SOURCE): "as α is first-order, the predicates P1 · · · Pn do not occur in α and hence this is equivalent to α |= ∀xSTx (ψ)". Packaging it as an adequacy criterion is folklore-level. **No novelty is claimed.**

### 3.2 Theorem 2 (the derivation clauses C3) — PROVED HERE (informal)

If L ⊆ Log(Mod(E)), there is a translation F of Hilbert derivations of L into K-derivations from E satisfying SN and HOM.

1. **SN.** By induction on φ, with fresh bound variables in the ∇ clause. A random test in `checks.py` §1 is an *illustration* for a related unary basis. It is not evidence, since SN holds by construction (critique F8).
2. **Axiom templates.**
   - For each axiom schema α, Theorem 1 gives a K-derivation D_α of E ⊢ ∀x ST_x(α).
   - Choose D_α so that no predicate letter other than the P_i of α occurs in it, e.g. cut-free.
   - An instance α[θ⃗/p⃗] goes to D_α[P⃗ := λy.ST_y(θ⃗)], with bound variables renamed to avoid capture.
   - FO derivations are closed under this substitution for predicate letters absent from the hypotheses E (atom-free).
3. **Rule templates.**
   - **MP:** from ∀x(A→B) and ∀xA, infer ∀xB.
   - **Nec** for the dual box Δ_i of ∇ in argument i: from ∀x ST_x(φ), derive ∀x ST_x(¬∇(⊤,…,¬φ,…,⊤)), i.e. ∀x ¬∃y⃗(R_∇(x,y⃗) ∧ ⊤ ∧ … ∧ ¬ST_{yᵢ}(φ) ∧ … ∧ ⊤). This is a fixed derivation of a few steps.
   - The unary case ∀xP(x) ⊢ ∀x∀y(R(x,y)→P(y)) is SOLVER-CHECKED.
4. **HOM** holds by construction: F(r(d⃗)) is the template of r with the F(dᵢ) grafted in. This respects derivation metavariables (report 002 Lemma 1).

**Size.** Preservation is polynomial: |F(d)| ≤ Σ_instances |D_α|·O(|θ⃗|) + O(1) per rule.

### 3.3 Theorem 3 (positive instances) — ESTABLISHED

**Sahlqvist (1975).** K ⊕ Σ, with Σ Sahlqvist, is characterised by the elementary class defined by the effectively computable first-order correspondents.

| Source | Status | What it says |
|---|---|---|
| Goldblatt 2006, p. 52 | VERIFIED_SOURCE | Sahlqvist "proved that the class of frames validating such a formula is definable by an explicit first-order sentence, and that this basic elementary class characterises the normal logic axiomatised by adding the formula to K" |
| BvB Thm 31 (p. 38) | VERIFIED_SOURCE | Correspondence |
| CGV, LMCS 2(1:5) | VERIFIED_SOURCE | "all Sahlqvist formulae are elementary and canonical" |
| de Rijke–Venema 1995, via Goldblatt p. 60 | ESTABLISHED (secondary) | Extension to arbitrary similarity types |

The book numbers BdRV Thms 3.54 and 4.42 are UNVERIFIED-MEMORY.

With Corollary 1: every K_τ ⊕ Σ with Σ Sahlqvist has a CRR, with E_L **finite and computable from Σ**.

### 3.4 Theorem 4 (necessary condition) — ESTABLISHED, Fine 1975

> "If Λ is elementary (i.e. characterised by some elementary class), then Λ is canonical."
> — Goldblatt 2006 §6.6, p. 58, VERIFIED_SOURCE

Hence **CRR-representable ⇒ canonical**.

The converse fails outside C. The bimodal logic EG "is canonical" and "is not sound and complete for any elementary class" (GHV, Lemmas 3.5–3.6, VERIFIED_SOURCE). But EG is axiomatized by the infinite family {α[|Gn|, n] : n < ω} (Def. 3.4).

Whether every *finitely axiomatisable* canonical variety is elementarily generated is GHV's **Problem 4.2** (VERIFIED_SOURCE in the 2003 preprint). Its current status was not determined (§7, O1).

---

## 4. Strongest positive construction

### 4.1 The construction

Input: L = K_τ ⊕ Σ with Σ Sahlqvist.
1. Compute the correspondent c_σ of each σ ∈ Σ, and set E_L = {c_σ}. This set is finite, atom-free and in the frame vocabulary (C4).
2. Translate formulas by ST (C1, C2).
3. Translate derivations by the templates of Theorem 2 (C3).
4. C5 then holds by Theorem 3 and Corollary 1.

### 4.2 Worked instances and machine checks (`reports/004-checks/`, 9 of 9 pass)

| Instance | Check | Status |
|---|---|---|
| K4, with E = {transitivity} | Z3: transitivity ⊢ ∀x ST_x(□p→□□p) | SOLVER-CHECKED |
| KT, with E = {reflexivity} | Z3: reflexivity ⊢ ∀x ST_x(□p→p) | SOLVER-CHECKED |
| Axiom K, with E = ∅ | Z3: ⊢ ∀x ST_x(K) | SOLVER-CHECKED |
| Reflection witness, with E = ∅ | Z3 finds a model refuting ∀x ST_x(□p→□□p) | SOLVER-CHECKED |
| Correspondence for □p→□□p | Over all 530 frames with ≤ 3 worlds: valid ⇔ transitive | Bounded enumeration |
| A fusion connective on ternary frames over a Boolean base, where x ⊨ A∘B iff ∃y,z (R₃(y,z,x) ∧ y ⊨ A ∧ z ⊨ B) | With E = ∅, Z3 finds a countermodel to p ⊢ p∘p. With E = {∀x R₃(x,x,x)}, it is provable | SOLVER-CHECKED, one instance |

The last row is a single instance in a Boolean-based fusion logic. It *illustrates* that at R1 a relational core can reflect the absence of a structural rule. Report 002 §6.2 found the opposite for LF with unrestricted hypotheses. The row is not evidence about full substructural logics, which need the restricted valuations of §4.3.

### 4.3 Second tier: lattice-based logics (outside P)

| Family | Result | Status |
|---|---|---|
| Distributive modal logic | GNV Thm 3.8: "Every Sahlqvist distributive modal logic K.Γ is sound and complete with respect to the elementary class of frames defined by the (set of) first-order correspondents of the axioms Γ" | ESTABLISHED (ILLC preprint 2002, VERIFIED_SOURCE). Heyting implication is excluded as "non-smooth" |
| Non-distributive LE-logics (Lambek, Lambek–Grishin, MALL, orthomodular) | CP (arXiv:1603.08515v2) Thm 7.1: "All LLE-inequalities on which ALBA succeeds pivotally are canonical". Thm 8.8: "ALBA succeeds on all inductive inequalities". Example 2.6 states elementary RS-frame completeness for one axiom only | Statements VERIFIED_SOURCE. The general claim "inductive ⇒ complete for an elementary RS-frame class" is **INFERENCE** |
| Intermediate logics | CPZ, LMCS 2019: correspondence transfer (Thm 6.1). Canonicity transfer only for bi-intuitionistic modal expansions | VERIFIED_SOURCE; partial |
| Lambek calculus, R-models | Kuznetsov, LMCS 2023, reporting Andréka–Mikulás 1994: L∧ strongly complete. With the standard constants, "even weak completeness fails". The semantics "interprets theoremhood and entailment, not proofs" | VERIFIED_SOURCE (Kuznetsov) |
| Linear logic with exponentials | No correspondence theory found. Allwein–Dunn 1993 is "without exponentials" (abstract) | OPEN in this survey |

**What changes in this tier.** Atoms denote up-sets or Galois-stable sets. Keeping C4 requires a first-order closure on atoms, e.g. ⌜p⌝(x) := ∀y(x ≤ y → P(y)). The cost is that **SN then holds only up to E-provable equivalence**, because ⌜θ⌝ is hereditary only provably.

### 4.4 Efficiency, kept separate from existence

- Preservation is constructive and polynomial (Theorem 2).
- Reflection goes through Gödel completeness and canonical models, with no bound.
- Decidability is lost: K4 is decidable, but FOL plus transitivity is not a decision procedure. Ohlbach 1993 notes R-literals duplicated "exponentially often" in clause form.

These are costs, not impossibilities.

---

## 5. Strongest negative obstruction (against the same statement P)

### 5.1 Theorem 5: P is false

There are logics in C with no CRR. Each witness fails Corollary 1.

| Witness | Why no CRR | Status |
|---|---|---|
| **TMEQ** = K + T + M + E + Q | "There is no class of frames that validates precisely the formulas in TMEQ" (BvB Thm 26, p. 34; van Benthem, *Theoria* 44, 1978) | ESTABLISHED (BvB, VERIFIED_SOURCE) |
| **Thomason's logic** L_T, with T ⊆ L_T ⊊ S4, five axioms A–E | Kripke-incomplete (Thomason 1974). Vosmaer, arXiv:1202.3268 Thm 4: "L is completely incomplete", i.e. incomplete for every class of complete BAOs | Vosmaer: VERIFIED_SOURCE, an unrefereed preprint (dated 2006 internally, arXiv 2012). Thomason: secondary |
| **Fine's logic** (above S4) | Kripke-incomplete (Fine 1974). Litak 2003 shows complete incompleteness | ESTABLISHED (secondary, via Vosmaer) |
| **K + M** (□◇p → ◇□p) | Kripke-complete, with the finite model property (Fine 1975a). But "no elementary class can characterise the logic K+M", and any characterising class "must fail to be closed under ultraproducts" (Goldblatt 1974 §17, via Goldblatt 2006 pp. 52–53) | ESTABLISHED (via Goldblatt 2006, VERIFIED_SOURCE) |
| **GL** (Löb) | Kripke-complete but not canonical (Kuznetsov 2017 lecture notes). So by Theorem 4 it is not elementarily determined | ESTABLISHED (secondary) plus Fine's theorem |

**Why the obstruction does not depend on the encoding.** Corollary 1 quantifies over **all** environments. GL is the provability logic of Peano arithmetic, so the boundary excludes a foundationally central logic.

**Is membership in scope decidable? INFERENCE: no.**
- BvB p. 39 (VERIFIED_SOURCE): "Chagrova [19] shows that the problem of determining whether a modal formula expresses a first-order condition on frames is undecidable."
- CP's introduction: canonicity and elementarity are "algorithmically undecidable".
- Both concern single formulas. That *elementary determination of a finitely axiomatized logic* is likewise undecidable is not proved here.

### 5.2 Proposition 6: per-logic first-order connective clauses — PROVED HERE (informal)

Relax C1 to the following family 𝔉:
- each ∇ goes to **any** first-order formula ψ_∇(x; X₁…Xₙ) over any finite relational vocabulary, where the Xᵢ are unary placeholders;
- the Boolean base is classical;
- atoms are unary predicate letters on one sort;
- the wrapper is exactly ∀x;
- E is atom-free;
- ADQ1 is required.

*Claim.* If L has a representation in 𝔉, then L is the logic of a class of complete BAOs.

*Proof.*
1. For each M ⊨ E, let A_M = (P(|M|), f_∇) with f_∇(S⃗) = {m : M ⊨ ψ_∇(m; S⃗)}. This is a complete Boolean algebra with operations.
2. By induction, φ's value under pᵢ ↦ P_i^M is the set defined by ⌜φ⌝.
3. E is atom-free, so every valuation into A_M arises from an expansion of M that is still a model of E.
4. As in Theorem 1, E ⊢ ∀x⌜φ⌝ iff φ = ⊤ in every A_M.
5. L is normal, so its normality and additivity theorems hold in each A_M under all valuations. Hence each f_∇ is a normal operator. ∎

**Consequence.** Completely incomplete logics (Thomason's via Vosmaer; Fine's via Litak) have no representation in 𝔉.

**Reach and caveats** (critique F5, F13):
- The proof uses the wrapper ∀x. Relativised wrappers such as ∀x(D(x) → ⌜φ⌝(x)) are **not covered**: the logic becomes that of matrices, whose quotient algebras need not be complete.
- Vosmaer's definition (with "complete") is the notion step 5 needs. His one-line gloss of Litak omits "complete".
- For the Kripke-complete witnesses GL and K+M, Proposition 6 says nothing. Whether some per-logic first-order clause captures GL is **OPEN** (§7, O2).

### 5.3 Proposition 7 (trilemma, restricted to 𝔉) — PROVED HERE (informal)

Within the family 𝔉 of §5.2, which includes C1 as a special case, no representation scheme has all three of:
- **(U)** universality over C;
- **(N)** an atom-free environment;
- **(A)** ADQ1.

*Proof.* Thomason's logic lies in C, and by Proposition 6 it has no 𝔉-representation satisfying N and A. ∎

Dropping any one property makes the other two achievable, though only by leaving 𝔉 or by an E chosen per logic:

| Keep | Drop | Construction | Status |
|---|---|---|---|
| U + A | N (and T1) | Algebraic semantics: formulas become terms of a Boolean-algebra-with-operators sort, and E_L states each axiom as an equation. Every normal modal logic is complete for its algebras | BvB p. 69 (VERIFIED_SOURCE): "any axiomatic extension of K ... is complete with respect with some class of algebras". This is formulas-as-data plus axioms stated: exactly importing. BvB raise the same "syntax in disguise" worry. A general-frame variant with per-atom admissibility items and closure axioms is UNVERIFIED-MEMORY |
| U + N | A | Preservation only: E_L = the theory of a one-point frame, reflexive or irreflexive depending on L (Makinson). For an inconsistent L, take E = {⊥} | UNVERIFIED-MEMORY for Makinson's theorem and its polyadic form |
| N + A | U | Elementarily determined logics (Corollary 1), e.g. Sahlqvist logics | ESTABLISHED |

### 5.4 What the positive construction does *not* give (R2/R3)

1. **Resources as proof structure.** In translated derivations, world variables are reused freely by K's own contraction and weakening. Resource discipline is reflected only in *which conclusions* are derivable.
2. **Proof identity.** No congruence on K-derivations is known to be preserved and reflected uniformly. Classical proof identity is itself unsettled (reports 001/002). F is injective on raw trees, which is meaningless.
3. **Literature on proof-level completeness.** Every result found is specific to one structure:

| Structure | Result | Single model or family? | Status |
|---|---|---|---|
| CCC / simply typed λ-calculus, βη | Statman–Dowek (arXiv:2309.03602): "If ξ is an infinite cardinal ... Mξ ⊨ t = u if and only if t =βη u". Simpson 1994 announcement: a faithful CC-functor into C exists iff C has an endomorphism with all iterates distinct | **Single** | VERIFIED_SOURCE (Statman–Dowek); Simpson's announcement only |
| SMCC / IMLL with unit | Soloviev (BRICS RS-96-61; APAL 90, 1997) Thm 1: Vect has the "test-property". The proof uses infinite-dimensional V. Earlier published proofs by others were flawed | Collective | VERIFIED_SOURCE |
| Unit-free SMCC | Kelly–Mac Lane, via Petrić–Zekić Prop. 6.5: terms of the same proper type are equal iff they induce the same links | — | Recorded in the source notes (S11); primary not accessed |
| Traced SMC | HHP 2008 Thm 4 (char 0). Whether one interpretation suffices is left open | Collective | VERIFIED_SOURCE |
| Dagger compact closed | Selinger, LMCS 8(3:06) Thm 2.2. Equations only | Collective | VERIFIED_SOURCE |
| MELL proof-nets | de Carvalho (arXiv:1502.02404): "the relational model is injective for MELL proof-nets" | **Single** (Rel) | VERIFIED_SOURCE |
| Full completeness (MLL and variants) | Blute–Hamano–Scott, APAL 131 (2005) | Model-specific | VERIFIED_SOURCE (prf notes) |
| Proof-relevant (profunctor/presheaf) correspondence theory | Not found. Nearest: Kavvos, *Two-dimensional Kripke semantics* (a duality only) | — | Absence of evidence |

**Lesson (INFERENCE).** At the proof level, *faithfulness* is cheap.
- (Set, ×) separates βη-distinct simply-typed terms (Friedman/Statman–Dowek).
- If unit-free IMLL and the Lambek calculus embed faithfully into STLC (UNVERIFIED-MEMORY), one cartesian model already separates their proofs.
- The real analogue of R1's *reflection* is **fullness**: the model must contain no morphisms beyond proofs.

Fox's theorem (via Heunen–Vicary Thm 6.13, secondary) says uniform copy/delete forces cartesianness. A cartesian model therefore adds diagonals and projections, i.e. it fails fullness for linear disciplines.

### 5.5 P₃: the proof-identity conjecture, frozen (proposed; not part of P)

**Setting.**
- **Source:** the free unit-free symmetric monoidal (resp. semigroupal) biclosed category on countably many atoms. This is the proofs of unit-free IMLL (resp. the unit-free Lambek calculus) modulo βη.
- **A frame:** a **finite** promonoidal category P (resp. a finite symmetric promonoidal category), unit-free, with the coherence isomorphisms. Day convolution makes [P, Set] semigroupal biclosed (resp. symmetric).
- **Frame morphisms:** strong promonoidal functors f (symmetry-preserving in the symmetric case). They act on valuations by left Kan extension Lan_f.
- **A valuation:** an assignment of presheaves to atoms.

**Uniform family for A ⊢ B.** A family η_{P,F⃗} : ⟦A⟧ → ⟦B⟧ in [P, Set] such that:
- it is natural in the valuation F⃗;
- it commutes with Lan_f along every frame morphism, up to the canonical strong-monoidal isomorphisms.

**P₃.** Proofs of A ⊢ B correspond **bijectively** to uniform families. That is:
- (faithful) distinct proofs give distinct families;
- (full) every uniform family is the interpretation of a proof.

**P₃⁺ (correspondence).** Adding a categorified frame condition to the frame class adds exactly the matching structural rule's proofs. Examples:
- symmetry ↔ exchange;
- a diagonal structure P(x,x;x) ≠ ∅, with appropriate coherence, ↔ contraction.

**Anti-vacuity clauses.**
- **Anti-Yoneda:** frames must be finite. The syntactic promonoidal category, which would make P₃ trivial via Yoneda and Day, is infinite.
- **Anti-cartesian-collapse:** fullness. The one-point frame alone gives (Set, ×) and fails fullness (§10).

**Caveat (critique F3.4).** "Symmetric" is *structure* (a choice of σ with coherence), not a property. So P₃⁺ correlates structure with rules, unlike R1, where frame conditions are properties.

**Status.** OPEN. No source examined states P₃ or refutes it. Whether frame morphisms are the right uniformity notion is part of the conjecture, and is fixed here so that the next test is well-posed.

---

## 6. Nontriviality analysis

### 6.1 The Lindenbaum-matrix interpreter: the claim is withdrawn, and a smaller finding replaces it

**The construction examined.**
- Every connective c, including →, goes to ⌜c(A,B)⌝(x) := ∃y z (F_c(y,z,x) ∧ ⌜A⌝(y) ∧ ⌜B⌝(z)).
- Atoms go to P_p(x).
- The wrapper is W(φ) = ∀x(⌜φ⌝(x) → D(x)).
- E_S contains totality and functionality of F_c, ∃!x P_p(x) per atom, and Horn restatements of the axioms and rules.
- ADQ1 holds on closed formulas: reflection via the Lindenbaum matrix with D the theorems.

**Why it fails D2 (critique F1).**
- D2's T3 requires F to be defined on *schematic* derivations, with SN at formula metavariables.
- At a generic metavariable X, nothing gives ∃!x ⌜X⌝(x), so the Horn item for X → (Y → X) does not apply.
- **Countermodel (SOLVER-CHECKED, `004-checks/matrix_countermodel.py`, by the critic):** domain {0,1}; F_→(0,1) = 1, otherwise 0; D = {0}; X = {0,1}; Y = {0}.
  - This satisfies the Horn item for all values, functionality, and MP-closure.
  - Yet 1 = F_→(0, F_→(0,1)) is a value of X → (Y → X) and is not in D.
- The MP template fails in the same way: it needs ∃x⌜A⌝(x) at generic A.
- This is the mechanism report 002 identified in L-g and I-C. **The first draft's claim that the matrix interpreter passes D2 is withdrawn.**

**What survives (INFERENCE).**
- **T4 is vacuous for any first-order core.** Under T1, source formulas go to FO formulas, and no FO sentence quantifies over formulas or over "the core's propositions".
- So for FOL cores, D2's anti-importing force comes entirely from T1 + T3, not T4.
- **Open:** whether an interpreter passing T1 + T3 could be built by sending metavariables to a "stable sort" that carries uniqueness (002's L-g repair, which 002 itself marked as needing checking). If so, the stable-sort repair would reopen the matrix loophole. Any adoption of that repair must be tested against this construction.

### 6.2 Attack catalogue against CRR

| # | Attack | Result | Reason |
|---|---|---|---|
| D-1 | A universal interpreter in E: arithmetic, or a Turing machine checking S-proofs, encoded in the frame vocabulary | **Fails universality; harmless where it works** | By Theorem 1 the represented logic is Log(Mod E) whatever E encodes. Where it works, it is a genuine frame-completeness theorem |
| D-2 | The matrix interpreter (§6.1) | **Excluded** | It violates C1 (→ becomes a relation) and C2 (designation predicate). Independently, it fails SN at metavariables (§6.1) |
| D-3 | Environment-supplied machinery: algebraic or general-frame semantics (§5.3, row 1) | **Excluded by C1/C4; the exclusion is exactly importing** | Universality is recovered only by formulas-as-data with the axioms stated |
| D-4 | Per-logic FO connective clauses (family 𝔉) | **Fails for completely incomplete logics** (Proposition 6). **OPEN for GL** | §5.2 |
| D-5 | Preservation-only (one-point frame) | **Excluded by C5** | §5.3 |
| D-6 | Extra symbols or sorts in E, so that the frame class is the reducts of models of E (a PC class) | **Adds nothing (INFERENCE from an ESTABLISHED theorem)** | PC classes are closed under ultraproducts, because reducts commute with ultraproducts. GHV statement (3) (VERIFIED_SOURCE, erdos.txt p. 4–5): "if a variety V is generated by some ultraproducts-closed class of structures, then it is generated by an elementary class". So every D-6-representable logic already has a plain CRR. GL, K+M and the incomplete logics remain excluded |

**Invariant.** The represented logic equals the logic of the environment's frame class (Theorem 1). It is semantic, environment-independent, and proved. Every attack either respects it, and is then a frame-completeness theorem, or leaves CRR.

**Disclosed loopholes:**
1. D-4 for GL (Kripke-complete but not elementary).
2. Relativised wrappers inside 𝔉 (§5.2 caveat).
3. CRR excludes frameworks (LF, Dedukti) *as cores*; they remain D1 media (report 002 §5).
4. The LE tier has only SN up to equivalence (§4.3).
5. The stable-sort repair (§6.1, open).

---

## 7. Open obligations and failed approaches

### Open obligations

| # | Obligation | Status |
|---|---|---|
| **O1** | GHV Problem 4.2: is every finitely axiomatizable canonical logic elementarily determined? If not, there is a canonical witness against P inside C | OPEN as of the 2003 preprint; the current status was not checked |
| **O2** | Does GL have a representation in 𝔉 (per-logic FO clauses)? | OPEN. D-6 is closed (§6.2) |
| **O3** | LE tier: inductive ⇒ complete for an elementary RS-frame class? Is the closure translation SN up to equivalence? | INFERENCE. Needs the APAL 2019 version and a check of RS-frame compatibility conditions |
| **O4** | P₃ / P₃⁺ (§5.5) | OPEN. Next test in §10 |
| **O5** | Mechanising Theorems 1 and 2 | Not done; feasible in Lean or Isabelle. Do it only if a gate requires it (the result is folklore-level) |
| **O6** | Primary sources: Sahlqvist 1975, van Benthem 1978, Thomason 1974, Fine 1974/75, Litak 2003, BdRV, Chagrova | Seen only through surveys or Vosmaer. Thomason 1974 pages conflict: BvB give 150–158, Goldblatt and Vosmaer give 30–34 |
| **O7** | The stable-sort repair of report 002 versus the matrix interpreter (§6.1) | OPEN |

### Failed approaches (recorded as findings)

1. "Canonical ST is universal for normal modal logics." Refuted (Theorem 5).
2. "Per-logic FO clauses rescue universality." Refuted for completely incomplete logics (Proposition 6).
3. "Extra vocabulary rescues GL." Refuted by GHV (3) (§6.2, D-6).
4. "The matrix interpreter shows D2 admits importing." **Withdrawn**: it fails T3 (§6.1).
5. "A proof-relevant frame test of *faithfulness* discriminates." **Withdrawn** (first-draft §10): the one-point frame already separates proofs (critique F3).
6. A uniform proof-identity completeness theorem across structural disciplines. None found.

---

## 8. What the findings establish for ProofBasis (task item F)

| Claim | Status |
|---|---|
| A fixed finite core (FOL) represents an infinite, effectively presented class of logics. It preserves and reflects derivability, uses an environment that cannot constrain valuations, and satisfies SN and HOM | ESTABLISHED (Sahlqvist) plus PROVED HERE (packaging). **Not novel** |
| The construction is not an interpreter: what any environment can do is fixed by Theorem 1 | PROVED HERE (informal) |
| Exact reach: the elementarily determined logics. It excludes GL and K+M, and extra vocabulary does not help | Theorem 1, ESTABLISHED witnesses, and GHV (3) |
| Universality over C without importing is impossible within 𝔉 | PROVED HERE (Proposition 7), given Vosmaer's preprint |
| "Deriving vs importing" made precise: E_L is a proposition-free, frame-equivalent restatement of the axioms, available exactly when the second-order quantifier can be eliminated | PROVED HERE (Corollary 1). The content is equivalent, not different |
| No R3 proof identity, no proof-level resource discipline, no R4 causal order | §5.4 |
| Cross-foundation scope (first-order theories, HOL, dependent type theory, cyclic proofs) | **Not addressed by P.** First-order theories put their non-logical axioms in the environment legitimately. HOL comprehension is logical and would be imported. Cyclic-proof trace conditions are not first-order (F05). All UNVERIFIED as theorems |

**Relationship to the original ambition.**
- The original ambition is a finite algebra of *proof* operations, faithful to proof *structure*, across *foundations*.
- The strongest positive result is *derivability-level* and *one-family*, with an exact negative boundary inside that family. It **separates** the ambition into two parts:
  - **(i) The R1 question.** Answered, classically and not novelly, with a sharp boundary.
  - **(ii) The R3 question.** No positive construction exists even in the most favourable family, and faithfulness alone is too cheap to test it.
- P₃ (§5.5) is the bridge between them. It is the one formulation found here that could be both true and new.

---

## 9. Decision: **NARROW**

- **The R1 line is STOP.**
  - Its positive part is classical (redundant), and its universality is refuted (Theorem 5, Proposition 7).
  - No further R1 work is recommended except O1–O3, which only refine the boundary.
- **The program narrows to P₃ (§5.5)**, frozen with both anti-vacuity clauses.

**Why not the critic's "UNRESOLVED for R3".** The critic objected (F4) that P₃ was not frozen. It is now frozen, with an explicit source, frame class, uniformity notion, and anti-Yoneda and anti-collapse clauses. Its truth value is unknown. NARROW records that the program should continue only on this target.

**Why not STOP overall.** Nothing examined refutes P₃.

**Why not PROCEED.** P is refuted, and P₃ has no positive evidence yet.

**The single missing lemma:** P₃ for the fixture of §10, the base case of P₃⁺ for exchange.

---

## 10. The single most valuable next test

**Fixture.** The sequent p⊗p ⊢ p⊗p, in unit-free IMLL and in the unit-free Lambek calculus.

| Calculus | βη-distinct proofs |
|---|---|
| IMLL | Exactly 2: identity and swap (link graphs; Kelly–Mac Lane via Petrić–Zekić) |
| Lambek | Exactly 1: identity. No exchange |

**Test.** Determine the uniform families (§5.5) for p⊗p ⊢ p⊗p:
- **(T-a)** over finite promonoidal frames: is the count exactly 1?
- **(T-b)** over finite symmetric promonoidal frames: is the count exactly 2?
- **(T-c)** for p ⊢ p⊗p over finite promonoidal frames: is the count exactly 0?

**Why it discriminates, unlike the withdrawn draft test.**
- **The cartesian frame gives the wrong count.** In (Set, ×), the transformations F×F → F×F natural in F are the four maps (a,b) ↦ (a,b), (b,a), (a,a), (b,b). For p ⊢ p⊗p, the diagonal exists.
  - So the one-point frame **fails** fullness on the fixture.
  - The test is anti-monotone in the frame class: more frames means fewer uniform families. This is the opposite of the faithfulness test, which the one-point frame trivialised (critique F3).
- **Why counts 1 and 2 are plausible (INFERENCE).**
  - A diagonal component needs a map from the summand P(x,y;z)×F(x)×F(y) into a summand P(x',x';z)×F(x')×F(x'). Naturality in F forces x' ∈ {x,y}. Frames with P(x,x;z) = ∅ for x ≠ z block this.
  - Compatibility with the morphism P → 1 should propagate the block to all frames, so the diagonals should not be uniform. The swap requires σ, so it should exist only in the symmetric class.
  - Nothing here is checked.
- **Both outcomes are informative.**
  - **Counts 1 / 2 / 0 confirmed:** the first evidence that proof-relevant frames reflect a structural rule at the proof level (P₃⁺ base case).
  - **Extra uniform families found:** finite proof-relevant frames do not reflect linearity even on the smallest fixture. The relational route to R3 is blocked, which supports STOP for R3 along this route.
- **The anti-vacuity clauses do real work.** Anti-Yoneda excludes the syntactic frame, which would make the count trivially correct. Anti-collapse is the test itself.

**Method (no implementation).**
1. Pen-and-paper coend calculus on the fixture: (F⊗F)(z) = ∫^{x,y} P(x,y;z) × F(x) × F(y).
2. Literature check: Day 1970; dinatural/parametric full-completeness methods (Blute–Scott; BHS 2005); Kavvos.
3. **Implementation gate.** If step 1 reduces T-a/T-b to a search over promonoidal categories with ≤ 3 objects, a bounded enumeration script (not a prover) would settle the fixture. That is the only implementation this report would support, and only after step 1.

---

## 11. Changes after the fresh critique (transparency)

| Critique | First-draft claim | Action |
|---|---|---|
| **F1 (FATAL)** | The matrix interpreter passes D2, so D2 admits importing | **Withdrawn.** It fails T3 at metavariables (countermodel added). Replaced by the smaller finding "T4 is vacuous for FOL cores" (§6.1) |
| **F2 (MAJOR)** | D-6 (extra vocabulary) is OPEN | **Corrected:** closed by GHV (3) (§6.2) |
| **F3 (MAJOR)** | §10 test asked about collective *faithfulness* over finite promonoidal frames | **Withdrawn:** the one-point frame trivialises it, and unit-free IMLL proof identity is link identity. Replaced by a *fullness* count on a fixture (§10) |
| **F4 (MAJOR)** | NARROW toward an unfrozen P₃ | P₃ now frozen with explicit clauses (§5.5). The decision is split: R1 STOP, program NARROW (§9). The critic's alternative is recorded |
| **F5 (MAJOR)** | Trilemma over unquantified "schemes"; U+A row mis-specified | Restricted to family 𝔉. The U+A row is rewritten as algebraic semantics. The relativised-wrapper gap is disclosed (§5.2–5.3) |
| **F6** | Theorem 1 direction labels | Swapped to the correct labels |
| **F7** | Hidden hypotheses (cut-free D_α, the Nec target, diamond primitives, "forced", many-sorted core) | Stated (§2.2, §3.2). Core made single-sorted. "Forced" replaced by "stipulated" |
| **F8** | SN random check presented as evidence | Relabelled as an illustration (`checks.py` §1) |
| **F9** | "Continuum-many" logics in C | Corrected to countably many |
| **F10** | "Reflects resource discipline" in the verdict | Reduced to one illustrative instance |
| **F11** | Credit to report 002; misquoted T4 | L-h credited (§2.4). T4 is discussed with its full wording, "or over the core's propositions" (§6.1) |
| **F12** | Undecidability of the boundary asserted before it was labelled | Labelled INFERENCE (§5.1) |
| **F13** | Citation details | Vosmaer dating, Goldblatt pp. 52–53, and Vosmaer's gloss of Litak noted |
| **F14** | "Never stated in the environment" | Replaced by "frame-equivalent, proposition-free restatement" (§2.3) |

---

## Appendix A. Machine checks (`reports/004-checks/`)

| File | What it does |
|---|---|
| `checks.py` and `checks-output.txt` | Z3 5.1.0 entailments and countermodels, plus a bounded frame enumeration. 9 of 9 pass. §1 is an illustration only |
| `matrix_countermodel.py` and its output file | The critic's bounded search refuting the matrix interpreter at a generic metavariable |

Run each with `python3 -I <file>`.

A Z3 `unsat` on a negated entailment is a solver proof of that one first-order entailment. Nothing here proves Theorems 1–2 or any general claim.

## Appendix B. Sources (as retrieved; page numbers refer to the retrieved version)

Full logs are in `reports/004-source-notes/`.

**Modal correspondence and incompleteness**
- **[BvB]** P. Blackburn, J. van Benthem, "Modal Logic: A Semantic Perspective", ILLC PP-2006-30 (Handbook of Modal Logic, ch. 1, 2007): Prop. 3; Thm 26 (p. 34); Thm 31 (p. 38); Chagrova remark (p. 39); Prop. 34 (p. 42); p. 69. VERIFIED_SOURCE.
- **[GOL]** R. Goldblatt, "Mathematical Modal Logic: A View of its Evolution" (2006), author's copy: pp. 52–53, 58 (§6.6), 60. VERIFIED_SOURCE.
- **[GHV]** R. Goldblatt, I. Hodkinson, Y. Venema, "Erdős graphs resolve Fine's canonicity problem", ILLC PP-2003-26; BSL 10(2), 2004: statement (3); Def. 3.4; Lemmas 3.5–3.7; Prop. 4.1; Problem 4.2. VERIFIED_SOURCE.
- **[CGV]** W. Conradie, V. Goranko, D. Vakarelov, LMCS 2(1:5), 2006 (SQEMA). VERIFIED_SOURCE.
- **[Vos]** J. Vosmaer, "A new version of an old modal incompleteness theorem", arXiv:1202.3268v1, Thm 4. VERIFIED_SOURCE (preprint).
- **[Kuz17]** S. Kuznetsov, Logic II lecture notes, University of Pennsylvania 2017 (GL is not canonical). Secondary.
- **[Ohl]** H. J. Ohlbach, AAAI 1993 overview. VERIFIED_SOURCE (garbled extraction).

**Lattice-based families**
- **[GNV]** M. Gehrke, H. Nagahashi, Y. Venema, "A Sahlqvist theorem for distributive modal logic", ILLC preprint 2002 (APAL 131, 2005): Thms 3.6–3.8. VERIFIED_SOURCE.
- **[CP]** W. Conradie, A. Palmigiano, arXiv:1603.08515v2 (APAL 2019): Thms 7.1, 8.8; Example 2.6. VERIFIED_SOURCE (preprint).
- **[CPZ]** W. Conradie, A. Palmigiano, Z. Zhao, "Sahlqvist via translation", LMCS 2019. VERIFIED_SOURCE.
- **[Kuz23]** S. Kuznetsov, LMCS 2023 (R-models of the Lambek calculus). VERIFIED_SOURCE.

**Proof identity**
- **[SD]** R. Statman, G. Dowek, arXiv:2309.03602. VERIFIED_SOURCE.
- **[Sol]** S. Soloviev, BRICS RS-96-61 (APAL 90, 1997). VERIFIED_SOURCE.
- **[HHP]** M. Hasegawa, M. Hofmann, G. Plotkin, LNCS 4800 (2008). VERIFIED_SOURCE.
- **[Sel]** P. Selinger, LMCS 8(3:06), 2012. VERIFIED_SOURCE.
- **[dC]** D. de Carvalho, arXiv:1502.02404 (CSL 2016). VERIFIED_SOURCE.
- **[BHS]** R. Blute, M. Hamano, P. Scott, APAL 131 (2005). VERIFIED_SOURCE (prf notes).
- **[PZ]** Petrić–Zekić, Prop. 6.5 (Kelly–Mac Lane). As recorded in the prf notes.
- **[Sim]** A. Simpson, categories mailing list, 4 July 1994. The TLCA 1995 paper was NOT_ACCESSED.
- **[HV]** C. Heunen, J. Vicary, *Categories for Quantum Theory*: Thms 6.6 and 6.13 (Fox). Secondary.

**Not accessed:** BdRV 2001; Sahlqvist 1975; Fine 1974/1975; Thomason 1974; van Benthem 1978; Litak 2003; Chagrova 1991; Friedman 1975; Fox 1976; Day 1970; Andréka–Mikulás 1994; Allwein–Dunn 1993 (full text); Kelly–Mac Lane 1971.
