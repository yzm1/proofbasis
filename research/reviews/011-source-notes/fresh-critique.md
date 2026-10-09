# Adversarial critique of review 011 (landscape audit draft)

Reviewer: independent red-team subagent, 2026-10-09. Target: `research/reviews/011-landscape-audit.md` (branch `research/011-landscape-audit`, commit 94db652) and `research/reviews/011-source-notes/{A..E}.md`. No repo files edited.

**What I checked myself this session**
- I re-fetched and grepped four primary texts:
  - Avron–Zamansky arXiv:0806.0081 (Thm 4.7, §4 and the conclusion);
  - Andréka–Németi arXiv:1111.0995 (Thm 2.1 and the introduction);
  - Guiraud arXiv:math/0612089 (abstract, outline, §3);
  - Ciabattoni–Galatos–Terui LICS'08 author PDF (Thm 4.2, Cor 7.2, §7 preamble).
- I confirmed through the arXiv API that 15 cited arXiv IDs resolve to the stated titles and authors. These include every 2025–2026 preprint the report relies on: 2609.37815, 2606.12383, 2608.14872, 2602.15081, 2506.01028 and 2508.02764.
- I grepped reports 001–010, the charter and the task files for the "absent / never engaged" claims.

Items marked **(M)** below come from my memory and were not verified this session.

---

## BLOCKING

### B1. The "not already answered / never engaged" claims are false. Task 009 item 6 is unmet.

Task 009 item 6 requires each deep dive to say *why it is not already answered by the older reports*. The report's answers to that question are contradicted by the repository.

**DD1 (§8, line 387).** The report says: "Reports 001–010 never engaged polygraphs or Squier-type invariants." The repository shows otherwise:
- `reports/001-source-notes/adequacy-levels-translations.md` S6a (l.165–177) is VERIFIED_SOURCE on the Polygraphs book. It covers Thm 8.2.4 (S₁), §10.4 (infinitely many critical branchings) and Lafont. Its inference reads: "Squier-type results show finite presentation ≠ finite convergent presentation, so decidable proof identity via rewriting in a finite basis can fail even when a finite presentation exists (F04/F09)."
- `reports/010-cross-review-algebraic-fundamentality.md` l.79 and l.137 cover finite derivation type (FDT), Squier, invariance of FDT under change of finite presentation (Squier–Otto–Kobayashi) and Kapur–Narendran. It also mentions "polygraphic resolutions up to homotopy" (l.72, l.199).

**§1 item 4 (line 64).** The report says: "Decisive negative results the project had not engaged". Several of the listed results were already engaged:
- the Joyal collapse is 001 CX4 and appears in 001-review, row 6;
- Heijltjes–Houston Thm 9.1 is 001 CX5;
- Lafont's parity argument is 001 CX12, and 001-review l.64 downgraded it to "an analogy only";
- S₁ is in the 001 notes and in 010.

**Q2 "Absent from the seed registry or prior reports" (l.238–252).** This list includes items that the prior reports already covered:
- Lafont's finite PROP presentations (001 CX12);
- admissible-rule bases: Rybakov and Iemhoff in `002-source-notes/bnd-binding-derived-rules.md` l.301–308, and derivable vs admissible in 010 l.143;
- initiality and type-theory frameworks: Uemura and Kaposi–Xie in 001-review l.125–127, Uemura in 008 l.521;
- Jeřábek (002, extensively);
- Thiele / Hilbert's 24th problem (002; 001 notes).

**Effect.** The novelty and priority argument for DD1 is "nobody looked at this". That argument is invalid, and the earlier reports' *conclusion* on Squier (F04/F09 in 001) is never confronted. The report also does not engage 001-review's verdict that Lafont's argument is "an analogy only". 011 promotes the same argument back to a "negative template" (§6 item 6, F5) without answering that objection.

**Minimal fix.**
- Replace each "never engaged / absent" with an exact delta, of the form: "001 S6a cited Thm 8.2.4 as a non-finiteness caveat. 011 adds: Guiraud 2006, FDT as a classification tool, dimension-≥3 failure."
- Remove from Q2 the items that the prior reports already covered.
- Answer 001-review's "analogy only" verdict on Lafont before using it in F5.

### B2. The closest prior programme, identified by the project's own reviews, is missing from the map, the ranking and the deep-dive list

**What the prior reviews established.** `reports/001-review.md` (l.17, 38–41, 97–121, 216–232) and `reports/002-fundamentality.md` (l.189–202, 297, 424, 454–478) identify the following as the narrowed question's home and principal redundancy threat:
- Licata–Shulman–Riley's fibrational framework (FSCD 2017);
- Licata–Shulman adjoint logic;
- Shulman's LNL polycategories and MATT (2023);
- Pruiksma–Pfenning adjoint logic;
- MTT.

They also name a concrete open conjecture: LSR Conj 8.5, "Completeness of Permutative Equality". 001-review l.226 records "Single discriminating next test (pen and paper)".

**What 011 does with it.**
- 011 mentions LSR exactly once, in a parenthesis inside F2 (l.300).
- LSR and the related frameworks appear in no §3 table and no §5 matrix row.
- They are absent from Q3 ("closest structures"), from DD1–DD6 and from Q4.

**Effect.** Q3 ranks polygraphs first without comparing them with the one programme that already pursues "fixed generic machinery + per-foundation mode theory + equational adequacy (proof identity)". DD3 and DD5 duplicate questions that the earlier reviews had already sharpened into LSR Conj 8.5. The prioritisation cannot be accepted as written.

**Minimal fix.**
- Add an L3/L5 row for "generic substructural/modal frameworks (LSR, adjoint logic, MTT, Shulman)", using the status recorded in 001-review and 002.
- Put it in the Q3 ranking.
- Either make LSR Conj 8.5 a deep dive, or explicitly argue why DD1–DD5 supersede it.

---

## MAJOR

### M1. Avron–Zamansky Thm 4.7 is misstated in a claim labelled V and "re-checked myself" (§1 item 5, l.80)

**The report's claim.** "Avron–Lev canonical Gentzen systems (coherence ⇔ cut-elimination ⇔ 2Nmatrix semantics; coherence is decidable; Avron–Zamansky Thm 4.7, V)".

**What the paper says** (arXiv:0806.0081, which I checked):
- Thm 4.7 states the three-way equivalence: coherent ⇔ strongly characteristic 2Nmatrix ⇔ **strong** cut-elimination.
- The introduction and conclusion restrict this to **k ∈ {0,1}**.
- The paper then states (l.~768–772 of the extracted text) that a calculus G₀ "admits standard cut-elimination, although it is not coherent. Hence coherence is not a necessary condition for cut-elimination in general". Only the subclass of *simple* calculi (Def 4.12) recovers the equivalence.
- Decidability of coherence is Prop 2.10, not Thm 4.7.

The §3.1 row (l.159) is correct. The executive summary and the LANDSCAPE row ("Decidable 'finite rule set is justified' criteria") are not.

**Also unflagged.** Equating "justified" with coherence or cut-elimination is the author's own inference (INF), not a result. The theorem also fixes LK structural rules and two-valued Nmatrix semantics.

**Fix.**
- Restate §1 item 5 as: "coherent ⇔ strong cut-elimination ⇔ strongly characteristic 2Nmatrix, for k∈{0,1} (Thm 4.7). Standard cut-elimination does not imply coherence (AZ08 §4, counterexample G₀). Coherence decidable (Prop 2.10)."
- Mark "justified = coherent" as INF.

### M2. Guiraud 2006 is over-read as "proofs with proof identity", and the dimension bookkeeping is wrong (§1 item 3; §2 L3 row; Q3 rank 1; F1; DD1)

**What Guiraud actually identifies** (abstract and §3, which I checked):
- The identity is **structural bureaucracy only**: types A and B, i.e. reordering independent rule applications. It is realised by the exchange (interchange) law of the free 3-category.
- Formulas are 2-cells and **inference rules are 3-cells**.
- Proof *transformations* (normalisation, cut elimination) would be 4-cells, and the paper only gives them in an "informal discussion" (§5).

**Where the report goes wrong.**
- Bureaucracy-identity is far finer than normalisation-based (βη) or generality-based identity. So "finite presentations of proofs *with* proof identity exist" (§1.3) and "Per logic, yes (… Guiraud 2006)" (§2 L3) conflate permutation-of-independent-rules with Došen-style proof identity.
- Q3 rank 1 assigns "rules (dimension 2), proof identifications (dimension 3), coherence (dimension 4)". That contradicts Guiraud, where rules are 3-cells.
- F1's "FDT / finite polygraphic resolution to dimension 3" therefore points at the wrong dimension.
- The relevant dimension is exactly where FDT pathologies hold, by the report's own §3.4: Guiraud–Malbos Thm 4.3.9 and infinitely many critical branchings for finite 3-polygraphs.
- Squier's theorem (Thm 7.3.5), FDT invariance (Thm 8.1.2) and S₁ (Thm 8.2.4), which the report makes central, are theorems about **categories/monoids presented by 2-polygraphs**. Their transfer to a 3- or 4-dimensional proof setting is unproved.

**Fix.**
- Say "proofs modulo bureaucracy (interchange)". Do not say "with proof identity".
- Correct the dimensions.
- State that the FDT machinery the report relies on applies to the 2-polygraph level, and that at the proof level Guiraud–Malbos Thm 4.3.9 shows finite convergence does not imply FDT.
- Make "does any finiteness invariant survive at the level of proofs?" an explicit open question in DD1, not an assumption.

### M3. "Free CCC ↔ NJ βη" is mislabelled and over-scoped (§1 item 3 "A6, V/M"; §3.1 row l.154 ends "(Selinger Cor 3.8, V)")

**Status.** In note A6, Lambek–Scott and Seely are **NA**. A's cross-cutting item 1 says "VS for the cited theorems", which contradicts A6. The CCC ↔ NJ and *-autonomous ↔ MLL correspondences are therefore **M**, and only Selinger's control-category result is V.

**Scope.** CCC corresponds to the {→, ∧, ⊤} fragment. Full NJ with ∨ and ⊥ corresponds to bicartesian closed categories, where η for sums and the empty type is a separate, harder theory (M: Ghani 1995; Altenkirch–Dybjer–Hofmann–Scott 2001; Scherer 2017). The control suite says "intuitionistic natural deduction with βη" without restricting the fragment.

**Fix.** Label the correspondences M. Write "NJ(→,∧,⊤) βη", and flag sums and ⊥ as a separate open item for DD3.

### M4. "L1 is settled / pre-empted" over-reaches the sources (§1 item 2, l.58–59; §2 L1 row)

- **BHL.** The report cites Bauer–Haselwarter–Lumsdaine for "initiality theorems". Note B4 records that BHL leave categorical semantics to "future work", and that "LF-based approaches need adequacy or initiality theorems". BHL is a *definition* paper with metatheorems, not an initiality result.
- **Uemura Thm 6.10.** The theorem holds for type theories in Uemura's own (logical-framework) sense. 001-review l.127 records Kaposi–Xie: "substructural (e.g. linear or modal) type theories are not definable as SOGATs" by their method. "Syntax generation is pre-empted" is therefore false for the linear control that the report's own suite requires.
- **Fix.** Restrict the claim: "for structural, non-modal dependent type theories in Uemura's sense". Remove BHL from "initiality". Add the Kaposi–Xie limit.

### M5. "No binding in the Polygraphs book (V by text search)" is an inference, and the binding gap is overstated (§1 item 8, l.99; §3.4)

**Label.** A negative grep result is INF, not V.

**Evidence the notes already contain.** The source notes themselves include binding-aware two-dimensional work that the report never connects to DD1:
- **Hirschowitz 2013** (LMCS 9(3:10), note E1, VERIFIED_SOURCE Thm 4.2): a sound and complete *cartesian-closed 2-categorical* semantics of permutation equivalence for **higher-order** rewriting.
- **Ahrens–Hirschowitz–Lafont–Maggesi**, "Reduction monads and their signatures" (B3, downloaded, not inspected): two-dimensional (reduction) initial semantics with binding.

**Other literature (M).**
- Seely 1987, "Modelling computations: a 2-categorical framework";
- Hilken 1996, a 2-categorical proof theory of simply-typed reduction;
- Hamana, second-order rewriting;
- explicit-substitution calculi (λσ, Abadi–Cardelli–Curien–Lévy), which give a *finite first-order* presentation of binding. A known negative template applies: Melliès 1995, failure of preservation of strong normalisation for λσ.

**Fix.**
- Relabel the claim INF.
- Recast the "binding gap" as: "binding-aware 2-dimensional rewriting exists (Hirschowitz 2013; reduction monads); whether FDT-type invariants exist for it is the open question."

### M6. "No surveyed framework preserves proof identity" / "Unsupported by any established theory" (Q4 row 5, l.276; §1 item 7)

This contradicts the repository's own evidence:
- 001 (l.366) records faithful proof-identity translations between specific foundations: Selinger's cbn/cbv λμ duality and CPS (Prop 8.1, up to type isomorphism).
- 001 R2 records the LF/HHP compositional bijection on derivations.
- Dedukti Lemma 32 gives βηΣ-convertibility (note C3).
- MMT Def 3.39 defines proof-conservativity (reflection of proof *existence*).

What is true is narrower: no *general cross-foundation framework* (institutions, general logics, interpretability) imposes proof-identity preservation on its morphisms.

**Fix.** Scope the claim to framework-level morphism notions, and cite the specific translations that do preserve identity.

### M7. Charter strawmen and a misquotation (§1 item 6, l.91; Q4 rows 2 and 4)

- **Misquotation.** §1 item 6 quotes "The charter's 'preserve proof identity across foundations'". That phrase does not occur in `docs/RESEARCH_CHARTER.md`, `RESEARCH_PLAN.md` or any task file (grep). AGENTS.md rule 4 forbids this kind of paraphrase-as-quotation.
- **Proof identity.** Charter requirement 5 already reads "Explicitly chosen notion(s) of proof equivalence/identity". Q4 row 2 ("proof identity is a given relation") attacks a position the charter does not hold.
- **Finiteness.** The charter defines "Finite basis: finite number of generators/rule *schemas*". Q4 row 4 ("'Finite' is an intrinsic property — Weakened") attacks a position the charter already rejects.
- **Novelty.** Q4 row 1 ("would be a new kind of result — Contradicted") is equally a strawman: the charter says not to claim novelty, and 001/002 already concluded this.
- **Fix.** Either cite the exact report text that made each assumption, or delete the row. Remove the fabricated quotation.

### M8. The coverage matrix does not meet Task 009 item 4 or the rubric (§5)

**Seed families silently dropped.** These seed rows have no matrix row:
- "Model theory, descriptive proof semantics, proof-relevant semantics";
- "Type theory and logical relations, parametricity, effect modalities" (never discussed anywhere in 011);
- "Computability" (in §3.5 but absent from §5);
- polycategories and double categories (B1 says polycategories were NA, and the report omits them);
- fibrations, equipments and doctrines (part of the general-logics seed row);
- term-graph rewriting;
- LLF/CLF.

The task says "don't silently declare the seed map complete". These rows are dropped without a deferral reason.

**Families in §3 but not in §5:** combinatorial proofs, complexity of cut elimination, session types, polynomial functors, and monads with arities / 2-monads.

**No evidence rows.** The rubric says: "Evidence row required for any decisive claim: precise source URL/DOI and inspected theorem location, status, assumptions, result, scope limitation, and strongest objection." The report contains no URLs or DOIs and no assumptions or objection columns. The §5 "Evidence" column holds author surnames only. Delegating to the notes is acceptable only if each decisive §1 and §6 claim links to a specific note entry, and none does.

**Vocabulary.** The matrix uses "investigated enough to deprioritise", which is neither the task's vocabulary (investigated / partial / unknown / deferred) nor LANDSCAPE.md's (seed / scoped / investigated / ruled out with argument / deferred with reason).

**Priority labels.** Three different rows are "**Highest**" (Identity of proofs DD3, Canonical systems DD2, Polygraphs DD1), while §8 imposes the strict order DD1 > DD2 > DD3.

**Fix.**
- Add every seed row, with a state and a reason.
- Add an evidence table for the roughly 11 decisive claims in §1.4 and §6: note ID, URL/DOI, theorem location, hypotheses, scope and strongest objection.
- Harmonise the vocabulary.
- Make the priority labels consistent with §8.

### M9. Sequencing contradiction: DD1 depends on DD3 (§8, l.394–397)

- DD1's bounded question is "finite polygraphic presentation of the proof category **modulo the declared identity**". Which identity to declare is exactly DD3's question. So "DD1, DD2 and DD3 are independent" is false.
- Given B2 and M2, DD1 as framed can only test bureaucracy-identity (Guiraud) or βη.
- **Fix, either:**
  - run DD3 first in a narrow form ("which identities are well-defined for the controls"), then DD1 parametrised by the result; or
  - restate DD1 as "for identity ∈ {bureaucracy, βη}" and drop the independence claim.

### M10. The "open territory" conclusion contradicts the report's own gap (§2, l.133)

- "The open territory is the conjunction L2 ∧ L3/L4 ∧ L5". This drops **L1 binding**, which is the declared decisive gap of the top-ranked DD1 (§1.8), and **L6 causality**, which is charter requirement 6.
- Deferring L6 to H_causal is defensible (STAGE_0_7_RECONCILIATION D5), but then the conclusion should say "excluding L6 by prior decision D5".
- **Fix.** State the conjunction as L1(binding) ∧ L2 ∧ L3/L4 ∧ L5, with L6 deferred under D5.

### M11. CGT08 hypotheses are omitted, and Q3 rank 4 over-generalises

I checked the CGT08 PDF:
- Thm 4.2 ("Every axiom in N₂ is equivalent to a finite set of structural rules") is stated over **FLe** (full Lambek with exchange).
- The rules are *analytic*, i.e. preserve cut-elimination, only after completion. Completion requires an **acyclicity** condition unless weakening is present (§7 preamble; Thm 7.1(a)).

Problems in the report:
- The report's "N₂ axioms ≡ finite structural rules" omits both the base and the analyticity condition.
- Q3 rank 4 and the LANDSCAPE row present canonical systems *and* the hierarchy as "Finite rule set is justified iff a decidable condition holds". CGT provides a sufficient transformation for the classes N₂ and P₃, not an iff-decidable criterion. Only the Avron–Zamansky coherence result is decidable, and that one is strong-cut-elimination only (M1).

**Fix.** Add "over FLe; analytic under acyclicity or with weakening", and split the rank-4 claim into its two parts.

### M12. The negative-evidence list mixes theorems, remarks and unbridged transfers (§6)

- **#11 Krivine.** "Computational content grows with axioms" is a remark in an introduction (note C6), not a theorem, yet it is labelled V like the theorems.
- **#1 and #2.** These state monoid-level results (S₁; undecidability of finite convergent presentability, §4.2.7) as implications for "finite basis for proof identity". §4.2.7 is uniform undecidability over *all* finite 2-polygraphs. It says nothing about a *fixed* proof calculus. The bridge is INF and should be labelled so.
- **#9.** This drops the coNP ≠ NP condition on Das–Straßburger, and the result itself is about "polynomial-time decidable linear TRS", not a "complete basis".
- **Fix.** Add a "type" column (theorem / remark / analogy) and an "INF bridge" column. Restore the conditions.

### M13. The north-star red-team required by Task 009 item 5 is thin

Q4 red-teams the *earlier reports*, and several of its rows are strawmen (M7). It does not red-team the north star itself. Missing items:
- **(a) Is "foundation" the right index?** Proofs in ZF, NBG or Mizar-style set theory are first-order derivations plus axioms in the environment. For FOL-based foundations, "across foundations" may then collapse to a logic plus environment, and the cross-foundation content would live only in genuinely different logics (type theories, linear/modal). This could radically shrink L5.
- **(b) Kill or stop criteria.** What S2 outcome would end the programme? There is no bridge to RESEARCH_PLAN's "defensible stop".
- **(c) Is "explanatory" a mathematical notion at all?** The report silently equates it with L2 (cut-elimination / coherence), an INF identification that it never defends.
- **(d) Should finiteness be dropped?** McGee's infinitary completeness (C7) and the schema-indexed results (ZX with angles; Uemura's ℕ-indexed sorts) suggest that "finite modulo schemas" might be trivial or the wrong invariant. The report records these but never asks whether "finite" should be abandoned.
- **(e) Missing expertise.** The S1 gate requires identifying missing technical expertise: higher-dimensional rewriting, structural proof theory of substructural logics, and type-theory semantics. 011 does not.

**Fix.** Add a §4.Q8 "North-star red team" covering (a)–(e).

### M14. Several F1–F6 reformulations are vacuous, already solved or ill-posed (§4 Q7)

- **F1.** Ill-posed as stated.
  - FDT is defined for categories presented by polygraphs, so it is undefined where binding lacks a polygraph theory (M5).
  - The free CCC on a set of base types has infinitely many objects and schema-indexed generators. It is not a finite polygraph in the book's sense, so FDT is either trivially false or needs a new "finite modulo schemas" notion that does not yet exist.
  - Guiraud's finiteness works only because propositional formulas are themselves finitely generated 2-cells.
  - Wrong dimension (M2).
  - "Decide whether": FDT is presumably undecidable in general (M; analogous to §4.2.7). Say "determine for the controls", not "decide".
- **F2.** Two problems.
  - *Vacuity risk*: if the "finite stock" may grow per foundation it is vacuous. If it is fixed, it is the LSR / adjoint / MTT programme (B2), which is prior art in progress.
  - "Every foundation's proof doctrine" is undefined for set-theoretic foundations.
  - Finitary 2-monads with finite presentations exist for any doctrine with finitely many type formers (M: Kelly–Power presentations), so the positive answer may be trivial.
- **F3.** Partly answered already.
  - "Universality = expressive completeness of the justified class" is already *negative* for natural classes: CGT Cor 7.2 over LJ, Ex 7.4 for Łukasiewicz, and Kracht's restriction to primitive axioms (NA).
  - What remains is the existing Ciabattoni et al. classification programme. F3 is ProofBasis-specific only if linked to L3/L5.
- **F4.** Vacuous as worded.
  - In categories of logics or institutions with comorphisms, the initial object is the trivial/empty logic.
  - Colimits are the *known* construction for combining logics: note C3 quotes Rabe, "combinations are colimits"; cocompleteness of institution categories is M.
  - "Universality = existence of initial or colimit objects" is therefore either trivial or already established. The content must lie in the *morphism notion*, which is DD5.
  - **Fix.** Restate F4 as "a morphism notion preserving and reflecting declared proof identity, closed under composition, with the controls as objects".
- **F5.** Mixes things up.
  - p-simulation (Frege robustness) is a positive *invariance* result, not an obstruction.
  - Lafont parity was ruled "an analogy only" by 001-review.
  - It omits the canonical obstruction theory for finite equational bases (see gap #3 below).
- **F6.** Ill-posed.
  - "The maximal coherent identity" presupposes uniqueness. Maximality (Post-completeness) is a property of a given theory: βη is maximal for CCC.
  - For a logic whose free structure is not Post-complete, maximal consistent extensions need not be unique (non-canonical by Zorn-type arguments, M). For classical logic, non-uniqueness is exactly what Straßburger reports.
  - **Fix.** "Determine whether the standard identity is maximal, and the set of maximal extensions".
- **Claim about Task 010.** "F1, F5 and F6 are not on that list" (l.306) is false for F5/F1. Task 010 explicitly lists "an obstruction/classification programme without a universal object" and "an equivalence class / hierarchy of generating presentations".

---

## MINOR

1. **Malformed table (§1 item 4, l.66–76).** The Joyal, Heijltjes–Houston, Das–Straßburger, CGT and Rybakov rows have two cells instead of three, so the Content and Status columns are shifted or empty.
2. **§1 table, Heijltjes–Houston row.** It omits "**with units**". Without units, proof nets are canonical, as the report's own A3 note says.
3. **Andréka–Németi Thm 2.1** (checked). It is stated for the 3-variable logic L³_d with a finite Hilbert-style ⊢_d, with **Tr(ZF) as an infinite recursive premise set**. "Finite equational calculus" comes from the abstract's Df₃ equivalence and should be phrased that way.
   - It adds nothing decision-relevant beyond Craig, the universal Turing machine and Kleene normal form, which already settle L0. It is listed among "decisive passages re-checked", but it is not decisive for any choice.
   - The Monk attribution for "no finite Hilbert system" is correct per AN's introduction (for Lₙ).
4. **Došen maximality "proved for CCC (V)".** The proof rests on Statman's and Simpson's typed Böhm theorem, which are NA. "BCC open (2004)" needs a current-status check before DD3 relies on it.
5. **"Wolfram multiway … Contradicted" (Q4).** This is a category error: deprioritising a direction is not contradicting an assumption. "Subsumed by polygraphs" is INF and should be labelled so. The dismissal itself is sound.
6. **Proof complexity rated "Low-medium" (§5) while F5 relies on p-simulation classes.** These are inconsistent.
7. **E-graphs dismissed for "no built-in binding".** Binding-aware e-graph variants exist (M; e.g. "slotted e-graphs", 2024–25). The low priority is still defensible.
8. **§11 "(Filled in after review.)"** is a placeholder, so the PR is not review-complete.
9. **Doubrovinski 2508.02764.** The real title is "When are two algorithms the same? Towards addressing Hilbert's 24th problem". It concerns *algorithms*, not proofs, and the A2 note should say so.
10. **Guiraud 2006 venue** (APAL 141, 266–295) is known only via a citation in Guiraud–Malbos and should be marked as such.
11. **References.** No fabricated references were detected in the IDs I checked. All 15 arXiv IDs tested resolve with matching titles and authors, including the unrefereed 2026 preprints. Venues marked UM in the notes remain unverified.

---

## Inventory gaps, ranked by decision value

| # | Missing family | Why it can change decisions | Where it bears |
|---|---|---|---|
| 1 | **LSR fibrational framework / adjoint logic / MTT / Shulman LNL polycategories** (in prior reports; omitted here) | Closest active programme with an explicit open proof-identity conjecture (Conj 8.5). Redundancy threat to F2, DD3 and DD5 | B2 |
| 2 | **Higher-order rewriting in 2-categories and binding-aware reduction semantics**: Seely 1987, Hilken 1996, Hirschowitz 2013 (already in note E1), reduction monads (AHLM 2020), Hamana second-order rewriting; explicit substitutions and categorical combinators (λσ; Curien), with Melliès's preservation-of-SN counterexample as a negative template; nominal rewriting (Fernández–Gabbay) | Directly decides DD1's "binding gap": whether two-dimensional binding-aware theories exist and whether finite first-order encodings of binding break normalisation properties | DD1 |
| 3 | **Tarski's finite basis problem**: McKenzie 1996 (undecidability of the finite basis property for finite algebras); Lyndon, Murskiĭ and Perkins non-finitely-based finite algebras and semigroups (M) | The canonical theory of obstructions to finite equational bases and their undecidability. It is the natural base for F5 and for the existential question, and it is absent while the polygraph analogue is featured | F5, existential layer |
| 4 | **Quantifiers: hyperdoctrines and fibrations** (Lawvere 1969, Seely 1983, Jacobs 1999); **first-order proof identity**: expansion trees (Miller), Heijltjes's proof forests, McKinley, Hughes's first-order combinatorial proofs (abstract only), Chaudhuri–Hetzl–Miller 2012 | Every L3 "per-logic yes" in 011 is propositional. The control suite includes binding, and Brünnler shows locality breaks at quantifiers | DD3, DD1 |
| 5 | **Polycategories, Lambek deductive systems and multicategories, Cockett–Seely weakly distributive categories** (a seed row, silently dropped) | Multi-conclusion classical sequent calculus is the natural carrier of classical proof identity | DD3 classical |
| 6 | **Classical Curry–Howard beyond Selinger**: Parigot λμ, Curien–Herbelin λμμ̃, Laurent's polarised linear logic (001-review: the collapse is *avoidable*), Melliès–Tabareau, Führmann–Pym | 011 §6 #3 states classical identity "requires non-canonical structure" without the polarised positive results recorded in 001-review | DD3 |
| 7 | **Geometry of interaction, ludics, transcendental syntax**; relational-semantics injectivity (de Carvalho et al., in 001-review) | Semantic invariants of cut-elimination, and therefore candidate identity criteria | DD3 |
| 8 | **Proof-relevant semantics and model theory; logical relations and parametricity** (seed rows dropped) | Fidelity criteria (full abstraction, parametricity as a "naturality = identity" criterion; cf. Pistone in note A2) | DD3, rubric item 4 |
| 9 | **Theory of logic translations**: Mossakowski–Diaconescu–Tarlecki, "What is a logic translation?" (2009, M); proof-theoretic and Grothendieck institutions (NA); Meseguer maps of logics | DD5's core question has a direct prior answer attempt | DD5 |
| 10 | **Presentations of 2-monads and the theory of doctrines** (Kelly–Power, Hyland–Power, Lack; B6 NA) | Vacuity test for F2 | F2 |
| 11 | **Deep inference with quantifiers and binding** (Brünnler first-order; Tiu; Ralph, M) | Needed to extend Guiraud beyond propositional logic | DD1 |
| 12 | **Termination of proof transformations**: Gentzen/Buchholz ordinal assignments; cut-elimination as term rewriting (Dershowitz–Moser, M) | Termination is a hypothesis of Squier's theorem for the proof-transformation polygraph | DD1 (L4) |
| 13 | Hilbert's 24th problem (Thiele) | Already in 002 and the 001 notes; low marginal value | DD3 background |
| 14 | Implicit complexity and light logics; quantitative/graded proof theory; proof mining | Resource layer; low | Backlog |

---

## Prioritisation verdict

- **Polygraphs first is not justified as written.** It rests on three things this critique undermines: a false novelty premise (B1), an identity conflation and dimension error (M2), and an ignored competitor (B2). Its top question also depends on DD3 (M9).
- **Recommended order:**
  1. **DD0.** Reconcile with LSR Conj 8.5 and generic frameworks. This is short, and it decides whether DD3/DD5 are redundant.
  2. **DD3-narrow.** Which identities are well-defined for the controls, including first-order and classical (gaps 4–6).
  3. **DD1, parametrised by those identities**, and including the binding literature (gap 2).
  4. **DD2**, after its originals (Avron–Lev, Belnap, Kracht) are accessed. They are all NA now, so ranking DD2 "Highest" rests on M-status sources.
- **DD4 is near-redundant.** Report 001-review already recorded Uemura and Kaposi–Xie. B4's verdict is "a ProofBasis claim at this level would be redundant". Fold DD4 into a one-paragraph scope note, plus the substructural limit.
- **DD6 should be promoted and re-based** on gap 3 (McKenzie / Tarski's finite basis problem). It currently leans on Lafont's parity argument, which 001-review rated an analogy.
- **Dismissals.** Wolfram, Langlands, e-graphs and L0 surveys are dismissed correctly. Realizability and ordinal analysis are dismissed acceptably, but gap 12 is a narrow exception. HoTT "narrow only" is acceptable. Concurrency deferred under D5 is acceptable if stated as such (M10).
