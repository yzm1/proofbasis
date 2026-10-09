# Report 006: Definition audit of H (Stage 0.7, Phase A) — Claude

## Front matter

**Target audited.** `docs/STAGE_0_7_COMMON_CONJECTURE.md` exactly as in PR #9 at commit `d72ab1f96ebdc0d5125453303a5f946a523ae15f`. It is called **H** below, with clauses H.1–H.7.

**Assignment.** The owner's Stage 0.7 Phase A instruction to Claude (chat assignment; not a file in `tasks/`). It asks for:
- seven focus questions (§4.1–§4.7 below);
- a positive and an adversarial example for every proposed definition;
- the deliverables listed in §9.

**Role.** Constructive but skeptical.

**Phase A only.** The following are out of scope:
- any proof attempt;
- reconciliation with other agents;
- edits to PR #9, the charter or other reports.

Every change proposed below is a *recommendation to the owners*, never a replacement for H.

**Author and date.** Claude (Claude Code session), 2026-10-08.

**Supporting material.**
- `reports/006-source-notes/`: retrieved statements, and the fresh critique of the first draft.
- §10 lists every change made after the critique.

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED (verified)** | A published result whose statement was read in a retrieved primary text this session; location given |
| **ESTABLISHED (secondary)** | A published result read only as restated, verbatim, in a retrieved secondary text, which is named |
| **PROVED HERE (informal)** | A complete pen-and-paper argument in this report. Not machine-checked, not refereed. A fresh critic re-checked it, but that is agreement, not verification |
| **INFERENCE** | An argument with a named gap |
| **OPEN** | Not known |
| **UNVERIFIED-MEMORY** | Not checked against any source this session |

---

## 1. Executive verdict

**Overall status.** H is not yet a coherent, falsifiable proposition. By H's own acceptance rule its status is **definition unresolved**. H already concedes that H.6 (non-vacuity) and H.7 (causal fidelity) are undefined. This audit adds four findings about *how* they can and cannot be closed, and about what H already forces.

1. **Every target satisfying H has an undecidable proof congruence** (Proposition A; PROVED HERE, informal).
   - The proof uses the Novikov–Boone theorem (ESTABLISHED, secondary).
   - H's source class C contains a one-atom calculus whose proof identity is the word problem of a finitely presented group with unsolvable word problem. Faithfulness (H.2) is then a computable reduction to ≈_A.
   - **Corollary.** Under the definitional reading of ≈_A, every framework with decidable definitional equality fails H as a fixed target. This covers intensional Martin-Löf type theory, Church-style System F with βη, the simply-typed λ-calculus, and the unit-free free symmetric monoidal (closed) category.
   - Frameworks with *undecidable* definitional equality (extensional type theory, Lean 4) are not excluded by Proposition A. They raise a separate trust problem (§4.7).
   - Under the propositional reading (HA-3) the corollary does not apply: an internal identity type need not have decidable provability, which is why E6 survives that reading.
2. **No H-target has a uniformly computable, enumerable family of models that separates its proofs** (Proposition B; PROVED HERE, informal).
   - So no non-vacuity criterion for H may *imply* decidable or computably separable proof identity.
   - Whether some other isomorphism-invariant criterion works is **OPEN**. An earlier draft claimed more, and that claim is withdrawn (§10, F1).
3. **The gate's D2 check is answered here (§4.8):**

   > **D2 admits a Higman-type universal construction on the group fragment of C.**

   - The construction is the target A_U, built from a finitely presented group that contains every finitely presented group.
   - It passes D2's T1–T5, and H.1–H.5, for every finitely presented proof-symmetry calculus.
   - It does so by fixed group words alone, with no code, no checker and no environment.
   - It generalises report 005's Thompson-group construction A_V from cyclic groups to all finitely presented groups.
   - So D2 does not by itself exclude algebraically encoded computation. Whether such constructions extend beyond the group fragment is **OPEN**.
4. **H.7 presupposes causal structure that is invariant under the source proof congruence. This is false in C.**
   - The point is already in report 005 §6: rⁿ ~ id. β-reduction is a further instance.
   - H.7 can be stated without a global order only on a separately defined subclass. §4.6 gives the requirements such a subclass must meet. A coherent definition is **OPEN**.

**What is satisfactory or repairable (§4).**
- H.1 and H.2 are mathematically well-defined. Faithfulness without fullness is a meaningful constraint once it is combined with derivability reflection over open judgments.
- H.3 is automatic once translations are morphisms of presentations.
- H.5 can be made precise by tying the environment to translations of the source's own assumptions (M3). The caveat in §4.4 applies.

**Strongest counterexample to my preferred interpretation (§6).**
- My preferred interpretation is a syntactic anti-interpreter package: presentation morphisms, a type-level formula translation, the M3 environment, and no type-case.
- A_U defeats it.
- A semantic strengthening, namely relational parametricity, is defeated by E8: Higman's group at a data sort, acting by precomposition.

**Minimum changes (§7).**
- **M1–M4 are definitional repairs.** They fix the meta-formalism, the source-class reading, the environment and the translation format.
- **M5 (non-vacuity) is an owner choice between two routes**, each with stated open problems:
  - **Route F**, relative fullness;
  - **Route R**, restricting C's proof equations. Route R also reverses H's "decidable equivalence not required".
- **Neither route is shown to exclude every universal-algebraic encoding.**
- **M6 (causality) remains a specification task**, with requirements but no finished definition.

---

## 2. H as audited (restatement, no changes)

- **C.** Report 002 §2.1's finite-schematic presentations with binding, plus finite proof-equation schemas, with these clarifications:
  - effectively checkable local rule applicability;
  - typed compositions;
  - ≈_S generated by the stated equations;
  - no uncertified cyclic or infinitary proofs;
  - target-independent membership.
- **A.** A fixed, finitely presented, typed many-sorted algebra, with:
  - finite generating operation schemas;
  - fixed typing rules;
  - a fixed proof congruence ≈_A.
- **Translations.** For every S ∈ C there is an effective translation F_S satisfying:

| Clause | Requirement |
|---|---|
| H.1 | Derivability preserved and reflected |
| H.2 | d ≈_S e ⇔ F_S(d) ≈_A F_S(e), for d, e of a common judgment |
| H.3 | Identities, composition, substitution and binding preserved modulo equality |
| H.4 | Resource integrity |
| H.5 | Trust separation |
| H.6 | Non-vacuity (open by H's own statement) |
| H.7 | Causal fidelity where defined |

- **Explicitly not required:** fullness, minimality, **decidable proof equivalence**, polynomial translation, proof search, raw chronology.

---

## 3. Running fixtures

| ID | Source S | Judgments and rules | ≈_S |
|---|---|---|---|
| **E1** | NJ(→) | Γ ⊢ M : φ; hyp, →I (binds), →E | β, η |
| **E2** | S_n (report 005 §3.1) | x:P ⊢ d : P; unary rule r | rⁿ(ξ) ~ ξ |
| **E3** | **S_G**, for a finitely presented G = ⟨g₁…g_k ∣ R₁…R_m⟩ with unsolvable word problem | x:P ⊢ d : P; unary rules g_i and g_i⁻¹, as in E2 | g_i g_i⁻¹(ξ) ~ ξ ~ g_i⁻¹ g_i(ξ); R_j(ξ) ~ ξ |
| **E4** | Unit-free MILL (⊗, ⊸) | linear Γ ⊢ M : φ | βη and commuting conversions |
| **E5** | Checker-shaped presentation | "⊢ φ provided check(c, φ)" | — |

### E3 is in C, and its proof classes form exactly G

PROVED HERE (informal). The critic's independent check agrees.

**Membership in C.** E3 has:
- finitely many rule schemas and equation schemas, written over a proof hole ξ;
- one atom sort;
- no side conditions.

**Proof classes at x:P ⊢ P.**
- A proof is a word in the generators and their inverses.
- Applying a rule on the outside multiplies on the left. Grafting into ξ multiplies on the right.
- So ≈_S at this judgment is the Thue congruence generated by g g⁻¹ = 1 = g⁻¹ g and R_j = 1.
- By the standard fact Mon⟨X ∪ X⁻¹ ∣ xx⁻¹ = x⁻¹x = 1, R⟩ ≅ Grp⟨X ∣ R⟩, the classes form G. Composition may come out reversed, giving G^op, which is isomorphic to G via inversion.

**No other judgment is inhabited.**
- No rule has zero premises, so there are no closed proofs.
- No rule relates distinct atoms, so there are no proofs between them.

**Difference from report 005.** This is not report 005's Lemma. That Lemma used normal forms rᵏ; E3 has no normal forms and uses the group-presentation fact instead.

E5 is outside C under report 002 §2.1, which bans side conditions (002 §5 L-d). See §4.3.

---

## 4. Focus-by-focus audit

### 4.1 What kind of object is A? (focus 1)

| Reading | Content | Problem |
|---|---|---|
| (a) Universal algebra | Finitely many sorts and operations | Binding is not expressible. Infinitely many formulas must become *elements* of a sort, i.e. data. This is report 002's B1 shape |
| (b) Finite presentation in a meta-formalism Φ | Φ has binding and generated types, e.g. second-order generalised algebraic theories or an LF signature. A's types and terms are generated by finitely many schemas | **HA-1:** Φ is unstated, and truth depends on it. If Φ = LF, then report 002's fixed signature Σ_univ (B1) is a legitimate fixed finite A |
| (c) Finitely presented categorical structure | Multicategory, polycategory or PROP, possibly with binding | Same dependence on the meta-level |

**Further hidden assumptions:**
- **HA-2.** A "finite schema" indexed by *declarations*, such as an inductive-type schema, lets each source contribute generators.
- **HA-3.** ≈_A may be read as definitional equality (the generated congruence) or as internal propositional equality. The two give different conjectures (E6, §4.4).

| | |
|---|---|
| **Positive example** | E1 into STLC as a Φ-presentation: type former →; term formers lam (binding) and app; equations β and η. F is the identity. H.1–H.3 hold |
| **Adversarial example** | Under reading (a), with formulas as data, a fixed finite *universal* equational theory that identifies codes of ≈_S-equal derivations would pass H.1–H.5. **Such a construction is not given here.** The nearest established tool is Bergstra–Tucker's finite equational specifications with hidden functions. That result is per-algebra, but its Thm 2.4 gives one finitely specified group containing every finitely generated semicomputable group (ESTABLISHED, verified; see source notes). Status of the general claim: OPEN |
| **Verdict** | **Needs correction (M1)** |

### 4.2 Fundamental vs derived vs disguised interpreter (focus 2)

**Definitions.**
- Under M1, a *derived operation* is a term schema of A, i.e. an element of A's clone.
- A *fundamental* operation is a generator. Which operations are generators depends on the presentation, and H does not require minimality, so this is harmless.

**What H lacks.** H has no property that separates a meaningful generator from one that "executes" something.

| | |
|---|---|
| **Positive example** | E1: →I ↦ lam and →E ↦ app. These are fixed templates, parametric in metavariables (report 002's HOM) |
| **Adversarial example 1** | A `step(code, state)` generator of a universal machine. It is visibly an interpreter, and D2's T1 excludes it because formulas become data |
| **Adversarial example 2** | A_U (§4.8). Every source rule maps to a fixed word over A_U's generators. There is no code argument and no type-case, and D2 passes. Yet the source proof identities are realised through a finitely presented group whose existence is proved by encoding recursive enumeration (Higman's theorem) |
| **Verdict** | **Hidden assumption.** "Not an interpreter" is not visible at the level of individual operations or templates. Any criterion must look at global properties of A or F (M5) |

### 4.3 Is C independently and non-circularly specified? (focus 3)

**Non-circularity.** No clause of C mentions A. **Satisfactory.**

**C-1. "Effectively checkable".**
- H imports report 002 §2.1, which already bans side conditions beyond sorts and binding. So E5 is outside C.
- The phrase "local rule applicability must be effectively checkable" could be misread as allowing any decidable side condition. **Recommendation:** state the strict reading explicitly.
- **Cost of the strict reading.** Type theories whose rules carry conversion or positivity side conditions are in C only after being re-presented declaratively (report 002 L-f). That is a real narrowing of "across foundations".

**C-2. Proof-term syntax.** The syntax in which equations are written is implicit. Cite report 002 §2.1's schematic derivations explicitly.

**C-3. Arbitrary proof-symmetry calculi (E2, E3).**
- These are target-independent and legitimately in C.
- They force Propositions A and B.
- Whether "foundations" should include them is a substantive owner question (Route R), not a technicality.

**C-4. Certified cyclic proofs.** A certificate condition is global, not local. Either include cyclic proofs with an explicit global correctness judgment, or exclude them by name.

| | |
|---|---|
| **Positive example** | NJ, MILL and S_n are in C |
| **Adversarial example** | E5 is excluded only by the strict reading. E3 is included, with the consequences of §4.5 |
| **Verdict** | Non-circular. **Needs clarification (M2).** C-3 is an owner choice |

### 4.4 Machinery/environment separation and trust boundary (focus 4)

H.5 permits "signatures, definitions, explicit assumptions, independently justified theorems". Two adversarial examples exploit the permitted categories.

**E6 (definitions as generators).**
- Take A = a type theory with inductive definitions and quotients (Lean 4).
- Define Deriv_S inductively, with one constructor per source rule. Set F(d) := Quot.mk d over EqvGen(≈_S).
- Under *propositional* equality, F(d) = F(e) iff d ≈_S e. This uses `Quot.sound` (a kernel axiom) and Mathlib's `Quot.eq`/`Quot.eqvGen_exact` (ESTABLISHED, verified in Lean 4 core and Mathlib sources; see notes).
- Definitional equality is unchanged.
- E6 also fails D2's T1/T4: it is report 002's B5.

**E7 (assumption as rule).**
- The hypothesis ∀φ. Prf φ → Prf □φ is both an "explicit assumption" and the necessitation rule (report 002 §2.2, `raa`).

**Proposal M3, tied to M1.** Let Φ fix a designated *proof judgment form*: the judgment whose inhabitants are proofs. Then

  E_{F(S)} := F(E_S) ∪ D_S.

- F(E_S) is the source's own assumptions, as hypotheses of the designated proof judgment.
- D_S may contain only:
  - declarations of fresh constants whose type is **not** an instance of the designated proof judgment;
  - δ-eliminable abbreviations.
- D_S may not contain inductive definitions, equations, or proof-judgment constants.

**How M3 escapes report 002 §2.2's critique of item-by-item ledgers.**
- That critique was that classifying items by *logical role* is ill-defined.
- M3 classifies by *Φ-judgment form*, which is a syntactic property fixed once by M1.
- The residual risk is under propositions-as-types targets, where every type is a proof type. There, D_S may declare only fresh *sorts* and term constants of non-proposition sorts, and Φ must distinguish sorts from propositions.
- **Caveat:** if Φ does not make this distinction, M3 is ill-defined (critique M12).

**Cost.** Mathematics that needs genuinely new inductive definitions must supply them as source assumptions (hypotheses) or through A's fixed generators. This is a real restriction.

| | |
|---|---|
| **Positive example** | Group theory over NJ: the axioms are E_S (hypotheses); D_S declares ·, e and ⁻¹ |
| **Adversarial example** | E6 and E7 are both excluded. Report 005's g_P attack (a proof constant plus an equation) is excluded. Targets with **equality reflection** (extensional MLTT, Nuprl) still break M3: a hypothesis p : Id(w, id) becomes a definitional equation (UNVERIFIED-MEMORY for the standard ETT rule). M3 must therefore also require that **hypotheses do not change ≈_A**, which excludes equality reflection |
| **Verdict** | H.5 **needs correction**. M3 plus "no equality reflection" is checkable relative to Φ |

### 4.5 Faithful embedding without fullness (focus 5)

**Definition check.**
- H.2 is well-defined if F_S is defined on raw derivations and respects ≈_S, and ≈_A is a congruence.
- It is then an injective map on proof classes at each translated judgment.
- With fresh atoms for metavariables, the schematic level and the instance level agree. **Satisfactory.**

**Faithfulness alone is weak** (report 004 §5.4). Combined with H.1 over open judgments it is a real constraint:

| | |
|---|---|
| **Positive examples** | E1 into STLC. E2 into the unit-free **free symmetric monoidal category** with atom P ↦ X_P^{⊗n} and r ↦ the n-cycle σ_n. This example is already in report 005 §9 ("End(P^⊗m) is S_m"), credited. By elementary reasoning about the free SMC, End(X^{⊗n}) ≅ S_n and there are no morphisms between different generator multisets, so H.1 and H.2 hold. Cost for H.4: one hypothesis becomes n wires. It fails fullness, which H allows |
| **Adversarial example** | E4 into STLC. x:p ⊢ ⟨x,x⟩ : p⊗p becomes inhabited, so H.1 over open judgments fails |
| **Decisive adversarial example** | E3: see Proposition A |

**Proposition A (undecidable target congruence) — PROVED HERE (informal).** Uses Novikov–Boone (ESTABLISHED, secondary: Bridson–Nyberg-Brodda, arXiv:2512.10800, §3.1).

*Statement.* Under M1's reading, where ≈_A is the congruence generated by finitely many schemas (hence r.e.), if A satisfies H.2 for every S ∈ C, then ≈_A is undecidable and r.e.

*Proof.*
1. Take G finitely presented with undecidable word problem, and S_G ∈ C (§3).
2. w =_G 1 ⇔ w(x) ≈_{S_G} x ⇔ F(w(x)) ≈_A F(x).
3. F is effective, so this is a many-one reduction from G's word problem to ≈_A. ∎

**Remark.** If some finitely presented group has a Σ₁-complete word problem, then ≈_A is Σ₁-complete. That follows from degree preservation under Higman's embedding (Clapham, Valiev), as cited in arXiv:2512.10800 §3.3 (SECONDARY). Not needed here.

**Corollary A1 (scope stated precisely).** Under the definitional reading, each of the following cannot be the fixed A with its fixed equality and no source-specific equations, because its equality is decidable (decidability results UNVERIFIED-MEMORY, standard):
- intensional Martin-Löf type theory (definitional equality);
- Church-style System F with βη;
- STLC with βη;
- the unit-free free symmetric monoidal and symmetric monoidal closed categories.

Under the propositional reading (HA-3), A1 does not apply.

A1 says nothing about targets with undecidable definitional equality, such as extensional type theory or Lean 4 (UNVERIFIED-MEMORY), or Dedukti with non-terminating fixed rules. Those face the M3/equality-reflection issue of §4.4 instead.

**Proposition B (no uniformly computable separating semantics) — PROVED HERE (informal).**

*Statement.* Call a family (M_i)_{i∈ℕ} of models of A **uniformly computable and separating** if:
- (i) given i and a term t, the denotation ⟦t⟧_{M_i} is computable uniformly in i;
- (ii) inequality of denotations is semi-decidable uniformly in i;
- (iii) d ≉_A e implies there is some i with ⟦d⟧_{M_i} ≠ ⟦e⟧_{M_i}.

No A satisfying H for all of C has such a family.

*Proof.*
1. Dovetail over i to semi-decide ≉_A.
2. ≈_A is r.e. (M1).
3. So ≈_A is decidable, which contradicts Proposition A. ∎

**Relation to McKinsey's theorem.** This transposes McKinsey's theorem (finitely presented and residually finite implies solvable word problem; ESTABLISHED, secondary: Rauzy arXiv:2002.02540 and Kharlampovich–Myasnikov–Sapir arXiv:1204.6506). The *uniformity* hypothesis is essential.

**Finite-model separation is excluded only if the finite models form such a family.** That is not automatic for A with infinitely many generated types and equation schemas.

**Verdict.** H.2 is **satisfactory as a definition**. Its consequences are:
- any H-target has undecidable proof identity under the definitional reading;
- no H-target has a uniformly computable separating semantics.

H itself does not require decidability, so these are **conflicts with likely non-vacuity markers**, not with H's text.

### 4.6 Causality without an artificial global order (focus 6)

**HA-4.** H.7 presupposes dependency structure on proof **classes**. In C:
- rⁿ ~ id identifies an n-chain with nothing (report 005 §6, credited);
- β erases or duplicates subproofs.

So H.7 is not definable uniformly on C, which H itself anticipates.

**Requirements a C_causal definition must meet.** These were identified by the fresh critique (M9) and are not yet met by any definition in this report.
1. **Independence is defined on formula occurrences, not rule names.** In sequent calculi, whether two rules permute depends on their active and principal occurrences.
2. **Derivations are trees.** Mazurkiewicz trace theory applies to words over a *static* independence alphabet. Its standard correspondence between traces and labelled partial orders (dependence graphs) is ESTABLISHED (secondary, via arXiv:1011.1030; the primary Book of Traces was not accessed). It does not transfer to trees without an explicit construction.
3. **Equations are permutations.** C_causal's equations must be permutations of adjacent rule instances acting on disjoint active occurrences, including permutations past binary rules. They may not erase, duplicate or cancel.
4. **Class-level order on both sides.** The source dependency order must be an invariant of the ≈_S-class. Causal fidelity then compares it with an order **invariant under ≈_A** on target image classes, not with the raw order of one representative. Under the raw-order reading, even the identity translation fails. A must therefore carry an ≈_A-invariant order on image classes, at least.
5. **Quantifiers.** State whether the conditions hold for all representatives or for canonical ones.
6. **Event maps.** π : Ev(F(d)) ⇀ Ev(d) must handle empty preimages (identity or glue templates). Preservation must be stated pairwise and uniformly ("every event over e precedes every event over e′"), not existentially.
7. **Conflict.** For additive branching, use event structures with conflict (Winskel; UNVERIFIED-MEMORY).

| | |
|---|---|
| **Positive example** | Candidate: unit-free MLL sequent proofs modulo permutations, compared with proof nets. Chaudhuri–Miller–Saurin Thm 16 (ESTABLISHED, verified, author PDF): maximally multi-focused unit-free MLL proofs are equivalent iff they have the same proof net. The *focused* quotient differs from the plain permutation quotient. Whether permutation classes are trace-like (single posets) is **OPEN**; disjunctive dependencies in sequentialisation may prevent it (critique, UNVERIFIED-MEMORY). Units must be excluded |
| **Adversarial example** | A target whose only composition is sequential cut, with no permutation equations. Independent source events receive representative-dependent target orders, which requirement 4 rejects |
| **Cost** | λ-calculi with βη (E1, E4) lie outside any such C_causal. Report 005's freeze already restricted independence to pure permutations (credited) |
| **Verdict** | Definable without a global order **only on a subclass, and that subclass's definition is OPEN**. The requirements above are the specification (M6) |

### 4.7 Do established logical frameworks satisfy H? (focus 7)

| Framework (as fixed target) | Per-source data needed | Status under H |
|---|---|---|
| LF / Twelf / Isabelle-Pure with per-source signature | Rule constants | Violates H.5 (new trusted rules). It is D1 |
| LF with empty signature | — | No base types, so H.1 fails trivially |
| Intensional MLTT, System F βη, STLC βη, unit-free free SMC/SMCC | — | Fails H.2 on E3 (Corollary A1, definitional reading) |
| Dedukti / λΠ-modulo | Per-source rewrite rules | Violates H.2/H.5 (source-specific equations) |
| Extensional MLTT / Nuprl; Lean 4 (undecidable definitional equality) | Inductive definitions, or hypotheses that become equations | Not excluded by A1. Passes H.5 only under the lax reading of "definitions" (E6), or through equality reflection. Excluded by M3 + "no equality reflection" |
| Rewriting logic, universal theory U | Codes | Interpreter by H's intent; H.6 undefined |
| LSR / adjoint logic | Mode theory with equations | Whether mode equations are "source-specific equations" is unclear. LSR Conj 8.5 is open (report 002) |
| Clarke–Scherer–Zeilberger free bifibration | Base functor p per source | Violates H.2/H.5 (report 005 §4.3) |
| A_U (§4.8) | Fixed words per source | **Passes H.1–H.5 and D2 on C_grp.** Not a logical framework |

**Verdict.** No established *logical framework* satisfies H under M1/M3. The only construction found that passes H.1–H.5 on a non-trivial fragment is universal-algebraic (A_U).

### 4.8 The gate's D2 check (required by H's "Required research gate")

D2 is defined in report 002 §2.4:
- T1: componentwise formulas;
- T2: fixed wrapper;
- T3: SN at metavariables + HOM;
- T4: no logical environment items;
- T5: ADQ1.

**Definition of A_U.**
- U is a finitely presented group containing a copy of every finitely presented group. ESTABLISHED (secondary): Bridson–Nyberg-Brodda §3.3, "there exists a finitely presented group containing an isomorphic copy of every finitely presented group". Higman 1961, Thm 1, as restated verbatim in arXiv:1908.10153 and arXiv:2512.10800.
- Bergstra–Tucker Thm 2.4 (ESTABLISHED, verified, scanned report) gives a related finitely specified group containing every semicomputable group.
- For each atom type X_P, A_U has unary generators for U's generators *and their inverses*, with U's relators and the cancellation equations as schemas uniform in X_P. That is a monoid presentation of U.
- A_U has no generators of arity 0, and none between distinct atoms.
- F_G: P ↦ X_P; g_i ↦ the word u_i, where g_i ↦ u_i is an embedding G ↪ U; g_i⁻¹ ↦ u_i⁻¹; grafting ↦ composition.

This generalises report 005 §4.1's A_V (Thompson's V, cyclic groups only).

**Effectiveness.** For each fixed G, F_G is given by finitely many words, so it is effective. H does not require uniform synthesis (report 005).

| Construction | T1 | T2 | T3 | T4 | T5 / H.1 | H.2 | Verdict |
|---|---|---|---|---|---|---|---|
| **A_U on C_grp** | Pass (atom ↦ atom) | Pass | Pass (fixed words; SN trivial) | Pass (empty E) | Pass (only endomorphisms inhabited; no closed terms, since all generators are unary) | Pass (injective embedding) | **D2 admits it** |
| A_V on S_n (report 005) | Pass | Pass | Pass | Pass | Pass | Pass | D2 admits it |
| Free SMC on S_n (P ↦ X^{⊗n}) | **Fail** (atom ↦ compound) | Pass | Pass | Pass | Pass | Pass | Fails T1 only on the literal atom-to-atom reading |
| E8 (§6) | **Fail** (atom ↦ D → X) | Pass | Pass | Pass | Pass | Pass (§6) | Fails T1 (literal reading) |
| B1, universal reflected signature (002) | Fail | Fail | Pass | Pass | Pass | Fails H.2 under definitional ≈_A | Excluded |
| E6, Lean deep embedding | Fail | Pass | — | Fail | Pass | Pass under propositional ≈_A only | Excluded |

**Finding (PROVED HERE, informal, given Higman's universal-group theorem).**
- **D2 admits a Higman-type universal construction on C_grp.**
- D2's T1 read literally (atom ↦ atom) excludes the *natural* free-SMC embedding of S_n, while admitting A_U.
- So on this fragment, D2 discriminates in the wrong direction.

---

## 5. Hidden assumptions and contradictions

| ID | Item | Evidence |
|---|---|---|
| HA-1 | The meta-formalism Φ is unstated | §4.1 |
| HA-2 | Generator schemas indexed by declarations | E6 |
| HA-3 | Definitional or propositional ≈_A | E6; Corollary A1 |
| HA-4 | Causal structure assumed invariant under ≈_S (already in report 005 §6) | E1, E2 |
| HA-5 | "Effectively checkable" invites a lax reading that contradicts 002 §2.1 | E5 |
| HA-6 | Likely non-vacuity markers (decidable or separable proof identity) conflict with H on C. This is not a conflict with H's text, which does not require decidability | Propositions A, B |
| HA-7 | H.4 at the derivability level is subsumed by H.1 over open judgments. Its proof-level content (occurrence and usage tracking) is not stated anywhere else and must be kept | §7 M4 |
| HA-8 | "Independently justified theorems" have no provenance rule | §4.4 |
| HA-9 | D2's T1, read literally, excludes compound atom images, which are needed for natural embeddings (free SMC), while admitting A_U | §4.8 |

**What remains OPEN about non-vacuity.**
- Propositions A and B exclude any H.6 criterion that implies decidable or uniformly computably separable ≈_A.
- They do **not** show that every isomorphism-invariant criterion fails.
  - A_U handles only C_grp, so it is not an H-solution.
  - "Contains a single universal finitely presented group" is not shown to hold for every H-target, which hosts each G at possibly different types.
- H.6's "encoding-invariant" most naturally means invariance under re-encoding of source proofs. This report does not reinterpret it as "isomorphism-invariant property of A". An earlier draft did, and that is withdrawn (§10).

---

## 6. Strongest counterexample to my preferred interpretation

**Preferred interpretation P\***, made up of:
- M1 (fixed Φ; generator schemas indexed by A only; definitional ≈_A);
- M2 (strict C);
- M3 (environment = translated hypotheses + syntax declarations; no equality reflection);
- M4 (presentation morphisms);
- **(T1⁺)**: formulas ↦ A-types built by A's type formers; atoms ↦ type expressions over fresh atomic type variables;
- **(Par-syn)**: A has no type-case and no type-indexed recursion.

**Counterexample 1 (primary): A_U.**
- Its generators are schematic unary constants. They do no type-case, so they satisfy Par-syn.
- Atoms map to atoms, so A_U satisfies T1⁺ (and D2).
- It satisfies M1–M4 and H.1–H.5 on all of C_grp (§4.8).
- **So P\* does not exclude Higman-type universality.**

**Counterexample 2: E8, against the semantic strengthening Par-sem ("A has a relationally parametric model").**

A_U fails Par-sem, since a non-trivial ∀X. X → X is impossible in parametric models (UNVERIFIED-MEMORY, standard). E8 survives it:

- **The target A_D:**
  - STLC with βη;
  - a closed base type D;
  - constants e, mul, inv with the **group axioms**;
  - constants c₁…c_k for U's generators, with U's relators.
- **The translation:**
  - P ↦ D → X_P;
  - g_i ↦ λf.λd. f(mul(c_{u_i}, d)).
  - Composition is reversed (an anti-homomorphism), which is harmless via inverses.
- **H.2.** Soundness in the set model D := U ∗ ⟨d₀⟩, X := D, applied at f := id, shows that mul(c_w, d₀) ≠ d₀ whenever c_w ≠ e. This uses an elementary set-model argument (credit: critique), not the conservativity theorem cited in the first draft.
- **H.1.** There are no terms (D→X_P) → (D→X_Q) for P ≠ Q, and no closed inhabitants of D → X_P.
- **Par-sem.** Plausibly holds: the operations act by precomposition on D. INFERENCE.
- **T1⁺.** Holds only if a data sort may occur in the type image of an atom. It fails the literal reading of D2's T1.

**What blocks each.**

| Blocker | Effect on A_U | Effect on E8 | Notes |
|---|---|---|---|
| Atom-to-atom interface (D2 T1 literal; report 005's interface) | Survives | Blocked | Also blocks the free-SMC embedding (§4.8) |
| "No data sort in atom images" | Survives | Blocked | |
| Par-sem | Blocked | Survives | |
| Fullness (Route F) | Blocked | Blocked | A_U has all of U at each atom; E8 has λf.λd.f(mul(c,d)) for every c. It is *not* shown that every universal construction fails fullness (§7) |
| Removing E3-type sources (Route R) | Blocked | Blocked | Removes these attacks, not universality in general |

**Conclusion.** My preferred syntactic package is defeated by A_U. Its semantic strengthening is defeated by E8. Excluding both together requires fullness, removing E3-type sources, or combining Par-sem with a ban on data sorts in atom images. That last combination would also exclude the natural free-SMC embedding of S_n.

---

## 7. Minimum changes for a falsifiable conjecture

**"Falsifiable"** here means that the statement has a definite truth value, so a candidate A or a counterexample source settles it. It does not mean that it is likely to be refuted.

| # | Change (diff against H; recommendation only) | Fixes | Positive test | Adversarial test |
|---|---|---|---|---|
| **M1** | Fix one meta-formalism Φ, with a designated proof judgment form and a sort/proposition distinction. A is one finite Φ-presentation. Generator schemas are indexed by A's types and terms only. ≈_A is the generated (definitional) congruence | HA-1, HA-2, HA-3 | E1 → STLC | E6 blocked |
| **M2** | State C's strict reading (002 §2.1: no side conditions) and its derivation syntax. Record the cost: type theories with side conditions need declarative re-presentation | HA-5 | NJ, MILL, S_n | E5 excluded |
| **M3** | E_{F(S)} := F(E_S) ∪ {non-proof-sort declarations, δ-abbreviations}. Hypotheses may not change ≈_A (no equality reflection) | HA-2, HA-8, E6, E7 | Group theory as hypotheses | E6; E7; report 005's g_P; ETT reflection |
| **M4** | Translations are Φ-presentation morphisms. H.1 is quantified over open judgments. **Keep a proof-level resource clause**: F preserves the usage count or linearity type of each boundary hypothesis, independently of H.7 | H.3 automatic; HA-7 | E1; E2 → free SMC (usage 1 ↦ n wires is *recorded*, not hidden) | E4 → STLC rejected |
| **M5** | Non-vacuity: owner choice between Route F and Route R (below), **plus** an explicit decision on T1 (atom ↦ atom vs compound) | §5, §6 | — | A_U, E8 |
| **M6** | H.7 on a subclass C_causal satisfying requirements 1–7 of §4.6. The definition itself is **OPEN** | HA-4 | — | E1, E2 outside |

**Recorded costs of M4.**
- Presentation morphisms exclude proof-level negative translations whose RAA template is not uniform at a generic metavariable (002 L-g).
- They need 002's unverified "stable sort" repair or must be excluded.

### Route F: relative fullness on generated interfaces

Requirement: every A-proof of F(J) under F(E_S) is ≈_A to some F(d). Atoms may map to compound types, so report 005's finite-atomic-profile hypothesis is dropped. Proposition A still applies.

- **Excludes:** A_U, A_V, E8, and the free SMC on S_n (n! ≠ n).
- **Makes concrete:** report 005's three-element test.
- **OPEN.**
  - Whether any A meets it on E3-type sources: one needs, for every finitely presented G, a type T with End(T) exactly G.
  - Whether universal constructions can meet it. Algebraically universal categories realise every monoid as a full endomorphism monoid (Hedrlín–Pultr, Pultr–Trnková; UNVERIFIED-MEMORY).
- **Route F is therefore not shown to be an anti-vacuity route by itself.**

### Route R: restrict C's proof equations independently

Restrict proof-equation schemas to a class 𝓔 fixed before and independently of A. For example: β, η and commuting conversions determined by declared connectives' universal properties, plus permutations. Arbitrary relators (E2, E3) are excluded.

- **Effect.** Proposition A's *proof* no longer applies. Requiring a uniformly computable separating semantics (Proposition B's notion) would then be possible in principle.
- **This reverses H's "decidable proof equivalence: not required".** That is a change to H's principal question and must be owner-approved explicitly.
- **OPEN.**
  - Whether 𝓔 can be defined uniformly over Φ-presentations. This is the analogue of a doctrine, which is established per doctrine, not uniformly.
  - Whether equality is even decidable inside 𝓔. η for inductive types, such as ℕ in extensional Gödel T, may be undecidable (UNVERIFIED-MEMORY).

---

## 8. Do the changes preserve the original ProofBasis ambition?

| Charter requirement | M1–M4 | M6 | Route F | Route R |
|---|---|---|---|---|
| (1) Fixed finite primitives | Preserved, made precise | — | Preserved | Preserved |
| (2) Core vs environment | **Strengthened** (M3) | — | — | — |
| (3) Composition and substitution | Automatic (M4). Costs: L-g negative translations; C requires re-presentation of side conditions (M2) | — | — | — |
| (4) Binding and resources | Preserved, provided M4's proof-level resource clause is kept | — | Strengthened | Preserved |
| (5) Explicit proof identity | Preserved (H.2) | — | **Strengthened** to full | **Narrowed** to 𝓔 |
| (6) Causality, not chronology | — | **Narrowed** to a subclass; definition OPEN | — | — |
| (7) Bounded trust | Strengthened | — | — | — |
| "Across foundational traditions" | Narrowed slightly (M2 cost) | — | Keeps maximal C, including non-foundational proof-symmetry calculi | Closer to foundations, but reverses a "Not required" item |

**Assessment.**
- M1–M4 preserve the ambition with stated costs.
- M5 is a real fork, and **neither route is yet shown to secure non-vacuity**.
- Without M5, H has no stated criterion for rejecting A_U-type constructions. Yet the project's intent is to reject them. On C_grp, every counterexample to existence is answered by such a construction (§4.8). Beyond C_grp, whether universal-algebraic constructions extend is OPEN.

---

## 9. Phase A conclusion

| Item | Finding |
|---|---|
| Satisfactory | H.1 and H.2 as definitions; non-circularity of C; the separation of H from H_full; the gate rule "definition unresolved" |
| Needing correction | A's nature (M1); C's reading (M2); H.5 (M3); H.3/H.4 (M4); H.6 (M5); H.7 (M6) |
| Contradictions / hidden assumptions | HA-1 to HA-9. The decisive ones: undecidable ≈_A is forced (Proposition A); no uniformly computable separating semantics (Proposition B); D2 admits A_U on C_grp (§4.8); causal non-invariance (HA-4) |
| Strongest counterexample to the preferred interpretation | A_U (syntactic package); E8 (with semantic parametricity) |
| Minimum changes | M1–M4 (repairs), M5 (an owner fork, with open problems on both routes), M6 (a specification with an open definition) |
| Ambition | Preserved by M1–M4 with stated costs. Causality narrowed. Non-vacuity unresolved under either route |

**Gate status: definition unresolved.** Phase A stops here. No proof attempt was begun.

---

## 10. Changes after the fresh critique (transparency)

The fresh-context referee's critique of the first draft is in `006-source-notes/fresh-critique.md`.

| Critique | First-draft claim | Action |
|---|---|---|
| **F1 (FATAL)** | "H.6 can only be closed by a translation-relative criterion, fullness, or restricting C"; "encoding-invariant" treated as "isomorphism-invariant property of A" | **Withdrawn.** Replaced by the weaker proved claim (Propositions A, B exclude criteria that *imply* decidable or uniformly separable ≈_A). The rest is OPEN. The reinterpretation is withdrawn |
| M1 | ESTABLISHED labels without source notes | Source notes added. Labels split into verified and secondary. Group-theory results are secondary only |
| M2 | Corollary A1 overclaimed (MLTT, System-F-like, SMCC with units, LF) | Restricted to named calculi under the definitional reading. ETT/Lean row added. Equality-reflection loophole added to M3 |
| M3 | Proposition B non-uniform; finite-model corollary | Restated uniformly. The finite-model claim is qualified |
| M4 | "Conflicts with 004's P₃" | **Deleted** (misattribution) |
| M5 | E8 presented as the primary counterexample; Par defined syntactically | A_U is primary (syntactic); E8 is for semantic Par. The T1⁺ reading issue and the full blocker table are added |
| M6 | D2 check not run | §4.8 added: D2 admits A_U |
| M7 | "Every counterexample answered by Higman-type", universal equational theory, "H is consistent" | Restricted to C_grp. Universal equational theory marked OPEN. "Consistent" deleted |
| M8 | Resource row "Preserved" despite dropping proof-level H.4 | Proof-level resource clause kept in M4 |
| M9 | Incoherent C_causal definition; MLL net claim | Replaced by explicit requirements. Definition marked OPEN. MLL example corrected to Chaudhuri–Miller–Saurin's focused statement |
| M10 | Route R "falsifiable", silent on "Not required" | Reversal flagged. Falsifiability defined. η-for-ℕ caveat added |
| M11 | Route F implied to exclude universality | Marked OPEN (algebraically universal categories) |
| M12 | Proof-sort test not intrinsic; reintroduces 002 §2.2's ledger | Tied to Φ's designated judgment. Caveat stated |
| Minor 1–12 | Σ₁ clause; "same as 005 Lemma"; A_U inverses; E8 details; credit 005 for free SMC and HA-4; HA-6 wording; C-1 wording; L-g cost; E4 witness; focus traceability; E6 vs D2 | All applied |

---

## Appendix. Sources

Full statements and locations are in `reports/006-source-notes/sources.md`.

| Status | Sources |
|---|---|
| **ESTABLISHED (verified)** | Chaudhuri–Miller–Saurin 2008, Thms 7 and 16 (author PDF). Lean 4 core (`Quot`, `Quot.sound`, `Quotient.exact`) and Mathlib (`Quot.eq`, `Quot.eqvGen_exact`). Bergstra–Tucker CWI IW 115/79, Thms 2.4, 3.1, 4.1 (scan). Mazurkiewicz DAIMI PB-78 (1977), the trace-equivalence definition only |
| **ESTABLISHED (secondary)** | Novikov–Boone, Higman's embedding theorem, and universal finitely presented groups, via Bridson–Nyberg-Brodda arXiv:2512.10800 and Mikaelian arXiv:1908.10153. McKinsey's theorem, via Rauzy arXiv:2002.02540 and KMS arXiv:1204.6506. The trace/dependence-graph correspondence, via arXiv:1011.1030 |
| **UNVERIFIED-MEMORY** | Decidability of equality for the calculi in Corollary A1. Undecidable definitional equality of ETT and Lean 4. Parametricity facts. Hedrlín–Pultr. Mac Lane coherence (the S_n fact is used only by elementary reasoning) |

**Prior project reports used:**
- 002: §2.1, §2.2, §2.4, §5 B1/B5/L-d/L-f/L-g.
- 003: traces vs proof identity.
- 004: §5.4.
- 005: S_n, A_V, §6 causal non-invariance, §9 free SMC and the three-element test.
