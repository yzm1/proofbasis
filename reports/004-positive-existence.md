# Report 004: Positive existence — the strongest construction and its exact boundary

**Stage:** 0.6, "Existence vs. Impossibility". This report takes the positive-construction role.

**Author:** Claude (Claude Code session), 2026-10-08.

**Inputs:**
- Reports 001–003, `docs/STAGE_0_5_ACCEPTANCE_REVIEW.md`, and the definitions D1/D2 of report 002 (§2.4).
- Source logs in `reports/004-source-notes/`.
- Machine checks in `reports/004-checks/`.

**This report does not modify:** the charter, the earlier reports, or D1/D2 as stated in report 002. Where this report refines D2, it does so in a new, separately named definition (CRR, §2.2) and records why plain D2 is inadequate (§6.1).

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED** | Published theorem. The passage was read in a retrieved primary or survey text; the exact source and location are given |
| **ESTABLISHED (secondary)** | Published theorem seen only as restated by another author; that author is named |
| **PROVED HERE (informal)** | A complete pen-and-paper argument written in this report. It is not machine-checked and has not been refereed |
| **SOLVER-CHECKED** | One instance checked by Z3 5.1.0 or by finite enumeration (`reports/004-checks/checks.py`). This is not a proof of the general statement |
| **INFERENCE** | The author's argument, with a gap that is named |
| **CONJECTURE** / **OPEN** | Not known to be true or false |
| **REFUTED** | A counterexample is cited |
| **UNVERIFIED-MEMORY** | Recollection that was not checked against a source in this session |

---

## 1. Executive verdict

1. **A frozen conjecture, P (§2), is REFUTED as stated.**
   - P asks for a fixed finite core, namely classical first-order logic (FOL) under its canonical relational translation, that represents every finitely axiomatizable normal modal logic.
   - The representation must:
     - preserve **and** reflect derivability;
     - commute with substitution;
     - map derivations homomorphically;
     - keep the environment free of logical content.
   - Two independent obstructions refute it (§5):
     - **Kripke-incomplete logics**: van Benthem's TMEQ and Thomason's logic.
     - **Kripke-complete logics that no elementary class characterises**: K+McKinsey.
2. **The exact boundary is a theorem (PROVED HERE, informal; §3.1).** A normal modal logic is representable in this sense iff it is the logic of an elementary class of Kripke frames.
   - This holds for any environment whatsoever. Nothing an agent puts in the environment can make the core represent a logic other than the logic of the frames satisfying that environment.
   - This is the nontriviality invariant (§6). It is a theorem, not a terminological exclusion.
3. **The strongest positive construction (ESTABLISHED, Sahlqvist 1975; §4).** It is classical, so it is not novel.
   - Every logic K ⊕ Σ, with Σ a finite set of Sahlqvist formulas, is represented with a finite, effectively computed environment of first-order frame conditions.
   - Each axiom of S is *derived* in the core from a proposition-free sentence. It is never stated in the environment.
   - Analogues exist for distributive modal logic (ESTABLISHED: Gehrke–Nagahashi–Venema Thm 3.8). For non-distributive lattice-expansion logics such as the Lambek calculus and MALL, the analogue is INFERENCE from Conradie–Palmigiano's ALBA theorems.
   - At the level of derivability (R1), the construction reflects resource discipline. A ternary-frame example is SOLVER-CHECKED.
4. **A loophole in report 002's D2 (§6.1).** A Lindenbaum-matrix interpreter that imports every axiom passes D2's syntactic tests. The refined definition CRR closes this loophole by an invariant, not by fiat.
   - Allowing *arbitrary* first-order clauses for the connectives does not rescue universality either. This is PROVED HERE (informal) for "completely incomplete" logics (§5.2).
5. **No proof-identity (R3) lift exists in the literature examined (§5.4, §7).**
   - Faithful-completeness theorems exist, but each covers one structure and most are collective (a family of models, not one): Friedman/Statman (CCC), Soloviev (SMCC), Hasegawa–Hofmann–Plotkin (traced), Selinger (dagger compact), de Carvalho (MELL in Rel).
   - None is a correspondence theory across structural rules. The FOL core itself carries no proof identity that is preserved and reflected.
6. **Decision: NARROW (§9).** Existence at R1 with an honest environment is *established* for an infinite, sharply delimited class. Universality over the independently defined class is *refuted*. R3 is *open*, with no candidate construction.
   - The single most valuable next test (§10): does Kripke/ternary-frame correspondence lift to proof identity for one Sahlqvist condition, exchange? The question is posed via Day convolution over finite promonoidal "frames".

---

## 2. Exact conjecture (frozen before analysis)

### 2.1 Source class C (fixed independently of the answer)

**C** is the class of all **finitely axiomatizable normal modal logics** over a finite similarity type τ, where τ is a finite set of operators ∇ with arities n_∇ ≥ 1.

Each L ∈ C is presented as a finitely schematic Hilbert calculus (report 002 §2.1) consisting of:
- classical propositional tautology schemas;
- normality axioms for each ∇;
- finitely many extra axiom schemas Σ;
- the rules modus ponens and necessitation for each dual box.

**Why this class.** It is the standard class in modal logic texts. It was not chosen with reference to first-order logic: it contains logics with no first-order frame condition at all, such as GL and K+M. It also does not consist of a restricted example, since it is infinite, with continuum-many members up to equivalence (UNVERIFIED-MEMORY; not needed below).

**A second tier, used only in §4.3:** logics over distributive and non-distributive lattice expansions (DLE/LE), as in Conradie–Palmigiano. P makes no claim about this tier.

### 2.2 Canonical relational representation (CRR)

- **Core K.** Classical many-sorted first-order logic with equality, with a fixed finite set of inference rules (any standard sequent or natural-deduction system). The core is the same for every L.
- **Vocabulary.**
  - For each n-ary operator ∇ there is an (n+1)-ary relation symbol R_∇. This frame vocabulary depends only on τ.
  - For each propositional atom p_i there is a unary predicate letter P_i.

The representation consists of five components.

| Clause | Statement |
|---|---|
| **C1 (canonical formulas)** | ST_x(p_i) = P_i(x); ST_x(⊥) = ⊥; ST_x(φ→ψ) = ST_x(φ) → ST_x(ψ); ST_x(∇(φ₁…φₙ)) = ∃y₁…yₙ (R_∇(x,y⃗) ∧ ⋀ᵢ ST_{yᵢ}(φᵢ)). The clause for each connective is **fixed by its arity alone**; it is the Jónsson–Tarski / standard translation |
| **C2 (wrapper)** | W(φ) = ∀x ST_x(φ). It is independent of L |
| **C3 (derivations)** | SN: ST_x(φ[θ/p]) ≡ ST_x(φ)[P := λy.ST_y(θ)], syntactically up to α. HOM: each axiom schema and rule of L has a fixed core derivation template, and F(r(d⃗)) is the template with F(dᵢ) grafted in |
| **C4 (environment)** | E_L is a set of first-order **sentences in the frame vocabulary {R_∇} only**. It is *atom-free*: no P_i occurs, and there is no sort of propositions |
| **C5 (adequacy, ADQ1)** | For all φ: L ⊢ φ ⇔ E_L ⊢_K W(φ). Both directions are required: preservation (⇒) and reflection (⇐) |

**Conjecture P (positive existence, frozen).** Every L ∈ C has a CRR, that is, an environment E_L satisfying C4 and C5. The translation is then *forced* by C1–C3.

**Not part of P (kept separate on purpose).**
- **Proof identity (R3).** P speaks of derivability and of the *shape* of the derivation map (SN, HOM), not of proof equivalence. The proof-identity analogue is stated as P₃ in §5.4 and is OPEN.
- **Causal order (R4).** Excluded, because no relational-semantics result examined addresses it. The CRR translation is static: it maps each derivation tree to a derivation tree and says nothing about scheduling.
- **Efficiency.** Excluded. Existence of E_L says nothing about proof size or search; see §4.4.

### 2.3 How each distinction demanded by the task is respected

| Distinction | Where it is enforced |
|---|---|
| Preservation vs reflection | C5 requires both, and §3.1 proves them separately. Preservation alone is trivial (§6.2, D-5) |
| Finite signature vs finite set of proofs | K has a finite *rule set*. Its vocabulary grows with τ, but only by relation symbols, which are non-logical. No finite set of proofs is involved |
| Deriving vs importing a rule | C4 forbids stating any axiom of L: an axiom quantifies over valuations (second order) and cannot be written in the atom-free frame vocabulary. Each axiom instance must be *derived* in K from E_L. §6 shows that relaxing C4 is exactly what permits importing |
| Structural translation vs interpreter | C1 is fixed by arity, the Boolean base is fixed, and the wrapper is fixed. The only per-logic datum is E_L, and the invariant of §3.1 determines what any E_L can achieve |
| Proof equivalence vs equivalence of conclusions | P is about conclusions (ADQ1) plus derivation shape. Proof equivalence is P₃, kept separate |
| Dependency vs execution order | HOM preserves the derivation tree's dependency structure. Nothing is claimed about execution order |
| Existence vs efficiency | Separated in §4.4 |

### 2.4 Relation to D2 of report 002

CRR is D2 with three refinements:
1. C1 replaces "each connective goes to a fixed A-formula context" with "the context is fixed by arity". Per-logic contexts are examined separately in §5.2.
2. C4 replaces D2's syntactic "logical item" test with atom-freeness in the frame vocabulary.
3. The core is fixed to FOL.

§6.1 shows that refinement 2 is needed.

---

## 3. Strongest established theorem

### 3.1 Theorem 1 (characterisation of CRR-representability) — PROVED HERE (informal)

**Statement.** Let τ be a similarity type, E a set of sentences in the frame vocabulary {R_∇}, and Mod(E) its class of models, regarded as Kripke frames. For every τ-formula φ:

  E ⊢_FOL ∀x ST_x(φ)  ⇔  φ is valid on every frame in Mod(E).

**Corollary 1.** A normal τ-logic L has a CRR iff L = Log(K) for some elementary class K of frames, where "elementary" means axiomatized by a set of first-order sentences. When this holds, E_L can be taken to be any axiomatization of K.

**Proof.**

*Standard translation lemma* (ESTABLISHED: BvB Prop. 3, "M, w ⊨ ϕ iff M ⊨ STx(ϕ)[x ← w]"). Here a model is a frame together with the interpretation of each P_i as V(p_i).

(⇐, reflection) Suppose φ is valid on every frame in Mod(E). Let N be any first-order structure for {R_∇} ∪ {P_i} with N ⊨ E.
- Because E mentions no P_i, the {R_∇}-reduct F of N lies in Mod(E).
- The interpretations of the P_i form a valuation on F.
- φ is valid on F, so by the standard translation lemma N ⊨ ∀x ST_x(φ).
- Hence E ⊨ ∀x ST_x(φ), and Gödel completeness gives E ⊢ ∀x ST_x(φ).

(⇒, preservation) Suppose E ⊢ ∀x ST_x(φ). Let F ∈ Mod(E) and let V be any valuation.
- The expansion (F, V) still satisfies E, because E is atom-free.
- By soundness, (F, V) ⊨ ∀x ST_x(φ).
- By the lemma, φ is true at every point of (F, V). Hence φ is valid on F. ∎

**Corollary 1** follows by taking L = {φ : E ⊢ ∀x ST_x(φ)}.

**Where atom-freeness is used.** It is used in **both** directions: E must survive every re-interpretation of the P_i. This is the precise sense in which the environment cannot constrain valuations.

**Provenance.**
- The central step is printed in Blackburn–van Benthem's proof of their Prop. 34 (BvB p. 42, VERIFIED_SOURCE): "as α is first-order, the predicates P1 · · · Pn do not occur in α and hence this is equivalent to α |= ∀xSTx (ψ)". Their use is r.e.-ness of a frame theory.
- Packaging it as a two-sided adequacy criterion for an environment is this report's contribution. The contribution is elementary and almost certainly folklore. **No novelty is claimed.**

### 3.2 Theorem 2 (derivation-level clauses C3) — PROVED HERE (informal); SN SOLVER-CHECKED on 500 random instances

If L ⊆ Log(Mod(E)), there is a translation F of Hilbert derivations of L into K-derivations from E that satisfies SN and HOM.

1. **SN.** ST_x(φ[θ/p]) = ST_x(φ)[P := λy.ST_y(θ)] up to renaming of bound variables, by induction on φ. The ∇ clause uses fresh variables. This was checked syntactically on 500 random formula/substitution pairs (`checks.py` §1).
2. **Axiom templates.** For each axiom schema α of L, Theorem 1 gives a fixed K-derivation D_α of E ⊢ ∀x ST_x(α).
   - An instance α[θ⃗/p⃗] is translated as D_α[P⃗ := λy.ST_y(θ⃗)].
   - First-order derivations are closed under substituting formulas for predicate letters that do not occur in the hypotheses. Since E is atom-free, this applies.
3. **Rule templates.**
   - MP: from ∀x(A→B) and ∀xA, infer ∀xB.
   - Nec for □_∇ in argument i: from ∀x A, infer ∀x∀y⃗(R_∇ x y⃗ → A(yᵢ)).
   - The unary case is SOLVER-CHECKED (`checks.py` §2, "template Nec").
4. **HOM.** F(r(d⃗)) is the template of r with F(dᵢ) grafted in. Derivation metavariables are therefore respected (report 002 Lemma 1).

**Size.** |F(d)| is at most the sum over the axiom instances in d of |D_α|·O(|θ⃗|), plus O(1) per rule application. That is polynomial in |d|. See §4.4 for the reverse direction.

### 3.3 Theorem 3 (positive instances) — ESTABLISHED

**Sahlqvist (1975).** For each Sahlqvist formula there is an effectively computable first-order frame condition. K ⊕ Σ, with Σ Sahlqvist, is characterised by the elementary class those conditions define.

| Source | Status | What it says |
|---|---|---|
| Goldblatt, *Mathematical Modal Logic: A View of its Evolution* (2006), p. 52 | VERIFIED_SOURCE | Sahlqvist "proved that the class of frames validating such a formula is definable by an explicit first-order sentence, and that this basic elementary class characterises the normal logic axiomatised by adding the formula to K" |
| BvB Thm 31 | VERIFIED_SOURCE | Correspondence, with an effective method |
| Conradie–Goranko–Vakarelov, LMCS 2(1:5), 2006 | VERIFIED_SOURCE | "all Sahlqvist formulae are elementary and canonical" |
| de Rijke–Venema (1995), via Goldblatt p. 60 | ESTABLISHED (secondary) | Extension to arbitrary similarity types |

The book numbers BdRV Thms 3.54 and 4.42 are UNVERIFIED-MEMORY.

**Combined with Corollary 1**, every K_τ ⊕ Σ with Σ Sahlqvist has a CRR whose E_L is **finite and computable from Σ**.

### 3.4 Theorem 4 (necessary condition) — ESTABLISHED, Fine 1975

> "If Λ is elementary (i.e. characterised by some elementary class), then Λ is canonical."
> — Goldblatt 2006, §6.6, VERIFIED_SOURCE; also restated as (1) by Goldblatt–Hodkinson–Venema

Hence **CRR-representable ⇒ canonical**. The converse fails:
- Goldblatt–Hodkinson–Venema (ILLC PP-2003-26; BSL 10(2), 2004), Lemmas 3.5–3.6, VERIFIED_SOURCE: the bimodal logic EG "is canonical" and "is not sound and complete for any elementary class".
- However, EG is axiomatized by the infinite family {α[|Gn|, n] : n < ω} (Def. 3.4). It therefore lies **outside** C.
- Whether every *finitely axiomatisable* canonical variety is elementarily generated is the authors' **Problem 4.2** (VERIFIED_SOURCE in the 2003 preprint). Its current status was not determined; see §7, O1.

---

## 4. Strongest positive construction

### 4.1 The construction

Input: L = K_τ ⊕ Σ with Σ Sahlqvist. Steps:
1. Compute the first-order correspondent c_σ of each σ ∈ Σ (Sahlqvist–van Benthem algorithm). Set E_L = {c_σ : σ ∈ Σ}. This set is finite, atom-free and in the frame vocabulary, so C4 holds.
2. Translate formulas by ST (C1) and wrap them with ∀x (C2).
3. Translate derivations by the templates of Theorem 2 (C3).
4. C5 holds by Theorem 3 combined with Corollary 1.

### 4.2 Worked instances and machine checks

All of the following are in `reports/004-checks/checks.py`; the output is in `checks-output.txt`. Result: 9 of 9 checks pass.

| Instance | Check | Status |
|---|---|---|
| SN for ST | 500 random (φ, θ) pairs, syntactic equality modulo α | SOLVER-CHECKED (bounded) |
| K4: E = {transitivity} | Z3 proves transitivity ⊢ ∀x ST_x(□p→□□p) | SOLVER-CHECKED |
| KT: E = {reflexivity} | Z3 proves reflexivity ⊢ ∀x ST_x(□p→p) | SOLVER-CHECKED |
| Axiom K | Z3 proves ⊢ ∀x ST_x(K) with E = ∅ | SOLVER-CHECKED |
| Reflection witness | With E = ∅, Z3 finds a model refuting ∀x ST_x(□p→□□p) | SOLVER-CHECKED |
| Correspondence (frame level, second order) | For all 530 frames with ≤ 3 worlds: □p→□□p valid ⇔ transitive | Exhaustive, bounded |
| Resource discipline (ternary frames) | Read x ⊨ A∘B as ∃y,z (R₃(y,z,x) ∧ y ⊨ A ∧ z ⊨ B). With E = ∅, Z3 finds a countermodel to p ⊢ p∘p. With E = {∀x R₃(x,x,x)}, it is provable | SOLVER-CHECKED |

The last row shows that at R1 the relational core **reflects** the absence of contraction: p ⊢ p∘p is underivable unless the environment contains the contraction frame condition. Report 002 §6.2 found the opposite for LF with unrestricted hypotheses.

**Caveat.** The ternary clause shown is for a fusion connective over a Boolean base. A full substructural logic needs the LE-tier semantics of §4.3, where valuations are restricted.

### 4.3 Second tier: lattice-based logics (outside P; recorded for scope)

| Family | Result | Status |
|---|---|---|
| Distributive modal logic | GNV Thm 3.8: "Every Sahlqvist distributive modal logic K.Γ is sound and complete with respect to the elementary class of frames defined by the (set of) first-order correspondents of the axioms Γ" | ESTABLISHED (Gehrke–Nagahashi–Venema, ILLC preprint 2002, VERIFIED_SOURCE). Heyting implication is excluded there as "non-smooth" |
| Non-distributive LE-logics (Lambek calculus and extensions, Lambek–Grishin, MALL, orthomodular) | Conradie–Palmigiano, arXiv:1603.08515v2: Thm 7.1, "All LLE-inequalities on which ALBA succeeds pivotally are canonical"; Thm 8.8, "ALBA succeeds on all inductive inequalities". Example 2.6 states completeness with respect to an elementary class of RS-frames for one axiom | VERIFIED_SOURCE for these statements. The general claim "inductive LE-logic ⇒ complete for an elementary RS-frame class" is **INFERENCE**, from canonicity plus correspondence plus perfect LEs being complex algebras of RS-frames |
| Intermediate logics via DLE | Conradie–Palmigiano–Zhao, "Sahlqvist via translation", LMCS 2019: correspondence transfer (Thm 6.1). Canonicity transfer only for bi-intuitionistic modal expansions | VERIFIED_SOURCE; partial |
| Lambek calculus, binary-relation (R-)models | Kuznetsov, LMCS 2023, reporting Andréka–Mikulás 1994: L∧ strongly complete for R-models. With the constants interpreted in the standard way, "even weak completeness fails". The semantics "interprets theoremhood and entailment, not proofs" | VERIFIED_SOURCE (Kuznetsov). Andréka–Mikulás are seen secondary only |
| Linear logic with exponentials | No source examined gives a correspondence theory. Allwein–Dunn 1993 is explicitly "without exponentials" (abstract) | OPEN in this survey |

**What changes in this tier.** Atoms denote up-sets or Galois-stable sets, not arbitrary sets. To keep C4, the canonical translation must apply a first-order closure to the atom: for example ⌜p⌝(x) := ∀y(x ≤ y → P(y)) in the intuitionistic case.
- **Cost:** SN then holds only **up to E-provable equivalence**, not syntactically. ⌜θ⌝ is hereditary only provably.
- This weakening of C3 was flagged in report 002 §5 L-h. Here it is pinned to its exact source.

### 4.4 Efficiency, kept separate from existence

- **Preservation** (Theorem 2) is constructive and polynomial.
- **Reflection** is not constructive. It goes through Gödel completeness and Sahlqvist canonicity (canonical models), and gives no bound on recovering an L-derivation from a K-derivation.
- **Decidability is lost.** For example, K4 is decidable but FOL plus transitivity is not a decision procedure. Ohlbach (1993, VERIFIED_SOURCE, extraction partly garbled) notes that the relational translation's R-literals can be duplicated "exponentially often" in clause form.

These are costs, not impossibilities.

---

## 5. Strongest negative obstruction (against the same statement P)

### 5.1 Theorem 5: P is false — ESTABLISHED components plus Corollary 1

There are finitely axiomatizable normal modal logics in C with **no** CRR.

| Witness | Why no CRR | Status |
|---|---|---|
| **TMEQ** = K + T + M + E + Q (four schemas, unimodal) | "There is no class of frames that validates precisely the formulas in TMEQ" (BvB Thm 26; van Benthem, *Theoria* 44, 1978). So TMEQ is not Log(K) for any frame class, let alone an elementary one | ESTABLISHED (BvB, VERIFIED_SOURCE) |
| **Thomason's logic** L_T, with T ⊆ L_T ⊊ S4, axiomatized by five formulas A–E | Kripke-incomplete (Thomason, *Theoria* 40, 1974). Vosmaer, arXiv:1202.3268 Thm 4: "L is completely incomplete", i.e. incomplete with respect to every class of *complete* BAOs | Vosmaer: VERIFIED_SOURCE, **preprint (refereeing unknown)**. Thomason: secondary |
| **Fine's logic** (above S4) | Kripke-incomplete (Fine, *Theoria* 40, 1974). Litak 2003 calls it "completely incomplete" | ESTABLISHED (secondary, via Vosmaer's introduction) |
| **K + M** (McKinsey, □◇p → ◇□p) | *Kripke-complete*: it has the finite model property (Fine 1975a). But "no elementary class can characterise the logic K+M" (Goldblatt 1974 §17, as reported in Goldblatt 2006, p. 52) | ESTABLISHED (via Goldblatt 2006, VERIFIED_SOURCE) |
| **GL** (Löb) | Kripke-complete, but not canonical (Kuznetsov's lecture notes, 2017, secondary). By Theorem 4 it is therefore not elementarily determined | ESTABLISHED (secondary) plus Fine's theorem. Primary sources not accessed |

**Why the obstruction is not an artefact of a particular encoding.**
- Corollary 1 quantifies over **all** environments E. The argument uses only Gödel completeness and atom-freeness.
- GL is the provability logic of Peano arithmetic, so the boundary excludes a foundationally central logic, not an exotic one.

**The boundary itself is undecidable.** BvB p. 39 reports (VERIFIED_SOURCE): "Chagrova [19] shows that the problem of determining whether a modal formula expresses a first-order condition on frames is undecidable." Conradie–Palmigiano's introduction states that canonicity and elementarity, separately and together, "are algorithmically undecidable".
- So no algorithm decides, given S ∈ C, whether S is in scope.
- This is a statement about frame-definability of one formula, which is related to but distinct from elementary determination of a logic. **INFERENCE:** the undecidability transfers. It is not proved here.

### 5.2 Proposition 6: arbitrary first-order connective clauses do not rescue P for completely incomplete logics — PROVED HERE (informal)

Relax C1 as follows:
- Each ∇ may go to **any** first-order formula ψ_∇(x; X₁…Xₙ) over **any** finite relational vocabulary, with the Xᵢ unary predicate placeholders. This is report 002's T1 with per-logic contexts.
- The Boolean base stays classical.
- Atoms remain unary predicate letters on one sort.
- E remains atom-free (C4), and ADQ1 is still required.

*Claim.* Then L is complete with respect to a class of complete BAOs. Hence a completely incomplete L, such as Thomason's logic per Vosmaer, has no such representation.

*Proof.*
1. For each M ⊨ E, let A_M be the powerset algebra P(|M|) with operations f_∇(S⃗) = {m : M ⊨ ψ_∇(m; S⃗)}. A_M is a complete Boolean algebra.
2. By induction on φ, the value of φ in A_M under the valuation pᵢ ↦ P_i^M is the set defined by ⌜φ⌝. Since E is atom-free, every valuation into A_M arises from an expansion of M that is still a model of E.
3. Exactly as in Theorem 1, E ⊢ ∀x⌜φ⌝ iff φ = ⊤ in every A_M.
4. L is normal, so its normality and additivity axioms hold in each A_M under all valuations. Each f_∇ is therefore a normal operator, and each A_M is a complete BAO.
5. Hence L is the logic of the class {A_M : M ⊨ E}, which consists of complete BAOs. ∎

**Reach.** This closes the per-logic-clause loophole for the witnesses Thomason (via Vosmaer) and Fine (via Litak). It does **not** close it for GL or K+M, which are Kripke-complete and hence complete for complete BAOs. Whether some non-canonical first-order clause plus an elementary environment captures GL is **OPEN** (§7, O2).

### 5.3 Proposition 7 (trilemma for C) — PROVED HERE (informal), from Theorem 5 and Proposition 6

Consider schemes in which the Boolean base is fixed and atoms are unrestricted unary predicates. No such scheme has all three of the following:
- **(U)** universality over C;
- **(N)** a non-importing environment, i.e. atom-free C4;
- **(A)** reflection, i.e. ADQ1.

Each pair is achievable:

| Keep | Drop | Construction | Status |
|---|---|---|---|
| U + A | N | Two-sorted general-frame or algebraic semantics. A sort of admissible propositions is added; E_L states, for every admissible X⃗, ∀x ST_x(σ)[X⃗] for each axiom σ. Every normal modal logic is complete for its algebras or general frames | BvB p. 69 (VERIFIED_SOURCE): "any axiomatic extension of K ... is complete with respect with some class of algebras". General-frame completeness is UNVERIFIED-MEMORY; the mod agent did not find it verbatim. BvB themselves ask whether this is "really just syntax in disguise" |
| U + N | A | Preservation only. For example, E = the theory of a one-point frame: every consistent normal logic is valid on a one-point frame (Makinson) | UNVERIFIED-MEMORY (Makinson's theorem). Illustrates that preservation without reflection is cheap |
| N + A | U | Restrict to elementarily determined logics (Corollary 1), e.g. Sahlqvist | ESTABLISHED (§3.3) |

### 5.4 Negative at R2/R3: what the positive construction does *not* give

1. **Resources as proof structure.** In the K-derivation of a translated linear or relevant derivation, worlds are reused freely: the core's own contraction and weakening act on world variables. The resource discipline is reflected only in *which conclusions* are derivable, via frame conditions, and not in the *shape* of K-proofs.
2. **Proof identity.**
   - K is classical FOL. No congruence on K-derivations is known to be preserved and reflected for every L, and classical proof identity is itself unsettled (reports 001/002 on the Joyal/Lafont collapse).
   - F is injective on raw derivation trees, trivially, because templates are tagged by rule. That is not a meaningful identity result.
3. **The proof-identity analogue P₃ is OPEN.** P₃ asks for a fixed non-syntactic semantic core (one model, or one collectively faithful family) whose **proof-relevant** relational semantics is faithful for the free proof category of every logic in an infinite, independently defined class, with the correspondence uniform in the frame condition. What the literature offers:

| Structure (one discipline each) | Faithful-completeness result | Single model or family? | Status |
|---|---|---|---|
| CCC / simply typed λ-calculus, βη | Statman–Dowek (arXiv:2309.03602): "If ξ is an infinite cardinal ... Mξ ⊨ t = u if and only if t =βη u". Simpson 1994 announcement: faithful CC-functor into C iff C has an endomorphism with all iterates distinct | **Single** (full type hierarchy over an infinite set) | VERIFIED_SOURCE (Statman–Dowek); Simpson's announcement only |
| SMCC / IMLL with unit | Soloviev (BRICS RS-96-61; APAL 90, 1997) Thm 1: "the category of vector spaces over a field I has the test-property". Needs infinite-dimensional V. Earlier published proofs by others were flawed | Collective | VERIFIED_SOURCE |
| Traced SMC | Hasegawa–Hofmann–Plotkin 2008, Thm 4 (char 0). A single interpretation is left open | Collective | VERIFIED_SOURCE |
| Dagger compact closed | Selinger, LMCS 8(3:06), Thm 2.2. Equations only; dimension 2 insufficient | Collective (faithful into a power FinHilb^X) | VERIFIED_SOURCE |
| MELL proof-nets | de Carvalho (arXiv:1502.02404): "the relational model is injective for MELL proof-nets". The coherence model is not | **Single** (Rel) | VERIFIED_SOURCE |
| Proof-relevant (profunctor/presheaf) Sahlqvist theory | Not found. Nearest: Kavvos, *Two-dimensional Kripke semantics* (a duality, no correspondence theory) | — | Absence of evidence from search only |

   - Each row is a separate, discipline-specific coherence analysis. Several have a history of flawed proofs.
   - Fox's theorem (via Heunen–Vicary Thm 6.13, secondary) says that uniform copy and delete make a symmetric monoidal category cartesian. Uniform structural rules therefore cannot simply be added to one core without changing its proof identity. This is the F04 risk, specialised.

---

## 6. Nontriviality analysis

### 6.1 Report 002's D2 admits an importing interpreter

**Construction (Lindenbaum-matrix interpreter).** For any finitely axiomatized Hilbert calculus S whose rules are MP-like (Horn):
- Every connective c, including →, goes to the first-order context ⌜c(A,B)⌝(x) := ∃y z (F_c(y,z,x) ∧ ⌜A⌝(y) ∧ ⌜B⌝(z)).
- Atoms go to P_p(x).
- The wrapper is W(φ) = ∀x(⌜φ⌝(x) → D(x)), which is fixed and independent of S.
- E_S contains:
  - totality and functionality of each F_c;
  - ∃!x P_p(x) for each atom p;
  - the Horn restatement of each axiom schema, e.g. ∀a b c d (F_→(b,a,c) ∧ F_→(a,c,d) → D(d)) for p → (q → p);
  - each rule, e.g. MP: ∀a b c (D(a) ∧ F_→(a,b,c) ∧ D(c) → D(b)).

**ADQ1 holds.**
- Preservation is by induction on derivations.
- Reflection: interpret the domain as the Lindenbaum algebra, D as the set of theorems, and P_p as {[p]}.
- This works for *every* such S, whether or not it is algebraizable, since the Lindenbaum matrix with D the set of theorems is a model of S.

**SN holds** syntactically. The substituted environment items ∃!x ⌜θ⌝(x) are E-provable.

**D2's syntactic logical-item test (002 §2.2)** counts an item as logical iff it "quantifies over ... the sort or type that interprets source formulas".
- Here the single individual sort is literally the same sort as the world sort of the standard translation. Whether it "interprets formulas" is a fact about the *intended model*, not about syntax.
- So the test either admits this interpreter, which imports every axiom verbatim as a Horn clause, or excludes ST as well.

**Finding (INFERENCE, recorded as a negative result against 002's D2).** D2's T4 does not separate deriving from importing at R1.

### 6.2 Attack catalogue against CRR

The test applied to each attack: if any of them passes C1–C5, CRR is inadequate.

| # | Attack | Result | Reason |
|---|---|---|---|
| D-1 | Universal interpreter: E encodes arithmetic, or a Turing machine checking S-proofs, inside the frame vocabulary (graphs interpret arithmetic) | **Fails universality; harmless where it succeeds** | By Theorem 1, whatever E encodes, the represented logic is Log(Mod(E)), the frame logic of its models. A checker cannot add theorems that the frames do not validate, and it cannot remove theorems the frames do validate. Where such an E works, it is a genuine frame-completeness theorem |
| D-2 | Disguised checker: the matrix interpreter of §6.1 | **Excluded** | It needs (i) → sent to a relation, violating C1 (Boolean base fixed), (ii) a designation predicate in the wrapper, violating C2, and (iii) ∃!x P_p(x), violating C4. Point (iii) is load-bearing and not terminological: per-atom constraints are exactly what breaks the expansion step of Theorem 1. Without them, the occurrences of p in p→(q→p) are translated independently and the interpreter loses soundness |
| D-3 | Environment-supplied machinery: two-sorted general frames or algebras (§5.3, row 1) | **Excluded by C4, and the exclusion is forced** | Universality is recovered exactly by placing ∀X⃗ ∀x ST_x(σ)[X⃗] for each axiom σ in E. This is importing: the axiom is stated, not derived. BvB raise the same "syntax in disguise" objection independently |
| D-4 | Per-logic first-order connective clauses | **Fails for completely incomplete logics** (Proposition 6); **OPEN for GL and K+M** | See §5.2 and §7, O2 |
| D-5 | Preservation-only representation (E = one-point frame) | **Excluded by C5** | §5.3, row 2 |
| D-6 | Extra vocabulary in E: symbols beyond {R_∇}, so that Mod(E) projects to a pseudo-elementary (PC) class | **OPEN** | Theorem 1 then gives L = Log(PC class). Whether this captures GL or K+M was not determined. Goldblatt (via Goldblatt 2006) shows any class characterising K+M "must fail to be closed under ultraproducts". PC classes *are* closed under ultraproducts (standard), so **INFERENCE:** K+M remains excluded even under D-6 |

**Invariant.** The nontriviality invariant is Theorem 1 itself: *the represented logic equals the logic of the environment's frame class*. It is semantic and environment-independent, and it is a theorem. Every attack either respects it, in which case it is a frame-completeness theorem and not vacuous, or violates C4. Violating C4 is equivalent to stating second-order (valuation-quantified) content in the environment.

**Disclosed loopholes.**
1. D-4 for Kripke-complete but non-elementary logics.
2. D-6 for logics other than K+M.
3. CRR's exclusion of "frameworks" (LF, Dedukti) *as cores* is inherited from D2; they remain D1 media (002 §5).
4. The LE tier weakens SN to "up to provable equivalence" (§4.3).

---

## 7. Open obligations and failed approaches

### Open obligations (ordered by decisiveness)

| # | Obligation | Current status |
|---|---|---|
| **O1** | Is every finitely axiomatizable canonical normal modal logic elementarily determined? (GHV Problem 4.2.) If not, a canonical but non-representable logic exists in C, which is a third kind of witness | OPEN as of the 2003 preprint. The current literature status was not checked |
| **O2** | Does GL, or K+M, have a representation with per-logic first-order clauses (D-4) or extra vocabulary (D-6)? | OPEN for GL. For K+M under D-6: INFERENCE, excluded (§6.2) |
| **O3** | LE tier: does "inductive LE-logic ⇒ complete for an elementary RS-frame class" hold in general, and is the closure translation SN up to equivalence in every case? | INFERENCE. Needs the APAL 2019 version of Conradie–Palmigiano and a check of the RS-frame compatibility conditions, which the authors themselves "do not discuss" |
| **O4** | Proof-identity analogue P₃ | OPEN; no candidate. §10 poses the cheapest discriminating test |
| **O5** | Mechanisation of Theorems 1 and 2 | Not done. The proofs are short, and a Lean/Isabelle formalisation of ST plus Gödel completeness is feasible. Do this only if a gate demands it, since the result is folklore-level |
| **O6** | Primary-source checks: Sahlqvist 1975, van Benthem 1978, Thomason 1974, Fine 1974/1975, Litak 2003, BdRV | Seen only through surveys (BvB, Goldblatt) or Vosmaer. Citation conflict: BvB gives Thomason 1974 as *Theoria* 40:150–158, while Goldblatt and Vosmaer give 40:30–34 |

### Failed approaches (recorded as findings)

1. **D2 as an R1 anti-vacuity criterion** fails, because the matrix interpreter passes it (§6.1).
2. **"Canonical ST is universal for normal modal logics"** fails by Theorem 5. This was the most natural strong form of P.
3. **"Per-logic first-order clauses rescue universality"** fails for completely incomplete logics (Proposition 6).
4. **A uniform proof-identity completeness theorem across structural disciplines:** none found. Each known result is discipline-specific, and Fox's theorem limits naive uniformity (§5.4).
5. **The literature search for a "proof-relevant Sahlqvist theorem"** found nothing (absence of evidence only).

---

## 8. What the findings establish for ProofBasis (task item F)

| Claim | Status |
|---|---|
| A fixed finite core (FOL) represents an **infinite, effectively presented** class of logics with derivability preserved and reflected, an atom-free environment, substitution naturality and homomorphic derivations | ESTABLISHED (Sahlqvist) plus PROVED HERE (packaging). **Not novel** |
| This positive construction is *not* an interpreter: what the environment can do is pinned down by Theorem 1 | PROVED HERE (informal) |
| The exact reach of this core is "elementarily determined logics"; the reach is undecidable to test; it excludes GL and K+M | Theorem 1 plus ESTABLISHED witnesses |
| Universality over finitely axiomatizable normal modal logics, without importing axioms, is impossible for this core | ESTABLISHED / PROVED HERE (Theorem 5, Proposition 7) |
| "Deriving vs importing" has a precise meaning here: the axiom's second-order (valuation) quantifier is eliminable into the frame language | PROVED HERE, as the content of Corollary 1 |
| The positive construction does **not** give R3 proof identity, does **not** represent resources at proof level, and does **not** address R4 causal order | §5.4 |
| Cross-foundation scope (first-order theories, HOL, dependent type theory, cyclic proofs) | **Not addressed by P.** Notes: for first-order theories the environment *is* the theory, which is legitimate because their axioms are non-logical. For HOL, comprehension is logical and would have to be imported. For dependent type theories, only soundness-style translations are known in this survey. For cyclic proofs, the trace condition is not first-order (F05). All are UNVERIFIED as theorems |

**Relationship to the original ambition.**
- The original ambition is a finite algebra of *proof* operations, faithful to proof *structure* across *foundations*.
- The strongest positive result found is *derivability-level* and *one-family* (modal and lattice-based propositional logics). It has an exact negative boundary inside that family.
- This **separates** the ambition into:
  - **(i)** an R1 question that is answered, classically and not novelly, with a sharp boundary;
  - **(ii)** an R3 question for which no positive construction exists even in the most favourable family.
- The bridge from (i) to (ii) is P₃. It is OPEN, and it is the only place where ProofBasis could still be both true and new.

---

## 9. Decision: **NARROW**

- **Not PROCEED.** P is refuted, and the positive part is classical.
- **Not STOP.** The negative results are confined to R1 universality. Nothing found refutes P₃, and P₃ is not settled by any theorem examined.
- **Not UNRESOLVED.** At R1 the status is fully resolved: existence on an exact class, impossibility beyond it.

**Narrowed target.** Replace "universal finite proof algebra" by P₃ restricted to one structural correspondence:

> Does the Kripke/ternary-frame correspondence for a single Sahlqvist structural condition lift to a *proof-relevant* correspondence that is faithful for proof identity?

**The single missing lemma** is P₃ for exchange (§10).

---

## 10. The single most valuable next test

**Question T (exchange, proof-relevant).**
- Let **M** be the free monoidal biclosed category, without units, on countably many atoms; equivalently, the non-commutative Lambek calculus with proofs modulo βη.
- Let **S** be the free symmetric monoidal closed category, without units, on the same atoms; equivalently, IMLL without units.
- A *proof-relevant ternary frame* is a small promonoidal category P. This is the categorification of a ternary relation R(x,y,z): a set-valued P(x,y;z) with associativity isomorphisms. Its presheaf category with Day convolution is monoidal biclosed.
- A *symmetric* promonoidal structure is the categorified version of the commutativity correspondent R(x,y,z) → R(y,x,z).

T asks:
- **(a)** Is the class of Day-convolution interpretations over **finite** promonoidal categories collectively faithful for M?
- **(b)** Is the class over finite **symmetric** promonoidal categories collectively faithful for S?

**Why this is the right test.**
1. **It is the proof-level analogue of the positive construction.** It replaces the relation R by the profunctor P and validity by natural transformations. It keeps C4's spirit: finite frames, not syntax.
2. **The vacuous version is known and excluded by construction.** Yoneda into Day convolution over the syntactic category is fully faithful and closed. This is an informal argument recorded in the prf notes §S14, not from a source. It is the proof-level analogue of the Lindenbaum interpreter of §6.1. T forbids it by requiring finite frames, just as C4 forbids stating axioms.
3. **It discriminates.**
   - **(a) and (b) both true.** This is the first instance of a proof-relevant Sahlqvist correspondence, and a concrete route to P₃ for a family of structural rules.
   - **(a) or (b) false.** This is a fixture-level obstruction: two distinct proofs that every finite proof-relevant frame identifies. The relational route to P₃ is then blocked even in the most favourable case, which supports STOP for R3 along this route.
4. **Known anchors bound the difficulty.**
   - Soloviev's theorem gives (b)-type completeness for *Vect*-valued interpretations with an infinite-dimensional space. Whether *finite Set-valued* frames suffice is not known to this report.
   - HHP explicitly leave single-model and bounded-dimension questions open in the traced case.

**Method (no implementation).**
1. Run a literature check for promonoidal or Day-convolution completeness: Day 1970, Kavvos, and "Day algebras" (Robinson–Wrigley, seen as an abstract only).
2. Do a pen-and-paper analysis of the smallest fixtures:
   - in S: identity versus symmetry on p⊗p ⊢ p⊗p;
   - in M: the first sequent with two βη-distinct proofs, which must first be identified.
3. **Implementation gate.** Implementation would be justified only if the pen-and-paper analysis reduces (a)/(b) to a finite search over small promonoidal categories. Even then it would be a bounded enumeration script, not a prover.

---

## Appendix A. Machine checks

- `reports/004-checks/checks.py`: Python 3 with z3-solver 5.1.0. Run with `python3 -I reports/004-checks/checks.py`.
- `reports/004-checks/checks-output.txt`: the recorded output, 9 of 9 checks passed.
- Z3 `unsat` on a negated entailment counts as a solver proof of that one first-order entailment. Finite enumerations are bounded checks.
- Neither kind is a proof of Theorems 1–2 or of any general claim.

## Appendix B. Sources (as retrieved; page numbers refer to the retrieved version)

Full extraction logs, with verbatim quotes and locations, are in `reports/004-source-notes/`.

**Modal correspondence and incompleteness**
- **[BvB]** P. Blackburn, J. van Benthem, "Modal Logic: A Semantic Perspective", ILLC preprint PP-2006-30 (Handbook of Modal Logic, ch. 1, Elsevier 2007). Locations: Prop. 3; Thm 13; Thm 26; Thm 31; Prop. 34; Thm 55 and p. 69. VERIFIED_SOURCE.
- **[GOL]** R. Goldblatt, "Mathematical Modal Logic: A View of its Evolution", Handbook of the History of Logic vol. 7 (2006), author's copy. Locations: pp. 52, 58 (§6.6), 60. VERIFIED_SOURCE.
- **[GHV]** R. Goldblatt, I. Hodkinson, Y. Venema, "Erdős graphs resolve Fine's canonicity problem", ILLC PP-2003-26; Bull. Symb. Logic 10(2), 2004. Locations: Def. 3.4; Lemmas 3.5–3.7; Problem 4.2. VERIFIED_SOURCE.
- **[CGV]** W. Conradie, V. Goranko, D. Vakarelov, "Algorithmic correspondence and completeness in modal logic I: the core algorithm SQEMA", LMCS 2(1:5), 2006. VERIFIED_SOURCE.
- **[Vos]** J. Vosmaer, "A new version of an old modal incompleteness theorem", arXiv:1202.3268v1. Thm 4. VERIFIED_SOURCE (preprint).
- **[Kuz17]** S. Kuznetsov, lecture notes, Logic II, University of Pennsylvania, 2017: GL non-canonical. Secondary.
- **[Ohl]** H. J. Ohlbach, AAAI 1993 overview of translation methods. VERIFIED_SOURCE (garbled extraction).

**Lattice-based families**
- **[GNV]** M. Gehrke, H. Nagahashi, Y. Venema, "A Sahlqvist theorem for distributive modal logic", ILLC preprint 2002 (APAL 131, 2005). Thms 3.6–3.8. VERIFIED_SOURCE.
- **[CP]** W. Conradie, A. Palmigiano, "Algorithmic correspondence and canonicity for non-distributive logics", arXiv:1603.08515v2 (APAL 2019). Thms 7.1, 8.8; Example 2.6. VERIFIED_SOURCE (preprint).
- **[CPZ]** W. Conradie, A. Palmigiano, Z. Zhao, "Sahlqvist via translation", LMCS 2019. VERIFIED_SOURCE.
- **[Kuz23]** S. Kuznetsov, on R-model completeness of the Lambek calculus, LMCS 2023. VERIFIED_SOURCE.

**Proof identity**
- **[SD]** R. Statman, G. Dowek, "On Statman's finite completeness theorem", arXiv:2309.03602. VERIFIED_SOURCE.
- **[Sol]** S. Soloviev, "Proof of a conjecture of S. Mac Lane", BRICS RS-96-61 (APAL 90, 1997). VERIFIED_SOURCE.
- **[HHP]** M. Hasegawa, M. Hofmann, G. Plotkin, "Finite dimensional vector spaces are complete for traced symmetric monoidal categories", LNCS 4800 (2008). VERIFIED_SOURCE.
- **[Sel]** P. Selinger, "Finite dimensional Hilbert spaces are complete for dagger compact closed categories", LMCS 8(3:06), 2012. VERIFIED_SOURCE.
- **[dC]** D. de Carvalho, "The relational model is injective for multiplicative exponential linear logic", arXiv:1502.02404 (CSL 2016). VERIFIED_SOURCE.
- **[Sim]** A. Simpson, announcement on the categories mailing list, 4 July 1994; the TLCA 1995 paper itself was NOT_ACCESSED.
- **[HV]** C. Heunen, J. Vicary, *Categories for Quantum Theory*: Thms 6.6 and 6.13 (Fox). Secondary for Fox 1976.

**Not accessed**
- BdRV, *Modal Logic* (2001).
- Sahlqvist 1975.
- Fine 1974/1975.
- Thomason 1974.
- van Benthem 1978.
- Litak 2003.
- Chagrova 1991.
- Friedman 1975.
- Fox 1976.
- Day 1970.
- Andréka–Mikulás 1994.
- Allwein–Dunn 1993 (full text).
