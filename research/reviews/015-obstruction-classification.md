# OBS-01 — Conditional obstructions and classification under CMP-01

**Status:** bounded adversarial research report, 2026-10-13. **Task:** 013. **Comparison baseline:** CMP-01 v0.1, PR #21 (still provisional); no S3 universal conjecture frozen. **Verdict:** several strong *conditional* impossibility/limitation results; no unconditional refutation of finite explanatory proof machinery.

## 1. The critical distinction: what is finite?

Separate F0 finite logical rule *schemas*; F1 finite presentation by generators and equations; F2 finite convergent rewriting presentation; F3 finite homotopy/coherence basis; F4 finite basis of all admissible rules; F5 finite native context/interface menu; and F6 finite search/checking cost. None is interchangeable. A single rule schema can have infinitely many instances. Likewise finite equational presentations can have undecidable word problems; proof checking can be decidable while equality of proof classes is not.

CMP-01 obligations: P proof existence preservation; R derivability reflection; EP equality preservation; ER equality reflection; F fullness; U resources; TR trust provenance; CF causality; HC higher coherence. Below each negative theorem is explicitly matched to its hypothesis rather than extrapolated to all targets.

## 2. Main results and quantifier audit

| Result | Actual class/hypotheses | Exact conclusion | Which CMP-01 goal it can obstruct | What it does **not** show |
|---|---|---|---|---|
| Squier 1994 / Guiraud–Malbos | A finitely presented monoid; finite convergent string presentation | Finite convergent implies finite derivation type (FDT), a finite homotopy-basis condition; FDT invariant under relevant finite Tietze changes; S1 decidable word problem but lacks FDT | F2 and F3 if a proposed universal representation must maintain the *specific rewriting/coherence structure* | Not a contradiction to F0/F1 or to arbitrary faithful embeddings of monoids into proof theories |
| Higher-dimensional convergence/coherence | Finite higher polygraphic presentations, dimensions and hypotheses must be specified | Higher-dimensional analogues may fail to inherit low-dimensional FDT implications; check exact theorem independently before using | HC/F3 in a selected higher category | Not that all proof systems have infinitely generated higher cells |
| Rybakov, admissible IPC rules | Intuitionistic propositional logic and its admissibility closure under substitutions | No finite basis of **all admissible rules** in stated sense | F4 if demanded by a universal core with no extra admissibility certificates | Does not block finite ordinary inference rules for IPC, finite proof grammars or decidable rule admissibility |
| Cyclic proofs / global trace | Finite derivation graph plus trace condition along infinite paths | Local correct rules and a finite pre-proof graph alone do not imply acceptance as cyclic proof | Val, TR, sometimes compositionality of proof graphs | Does not block finite certificates, reset systems or decidable soundness checking |
| Resource-sensitive typing | Linear logic without contraction, target unrestricted Cartesian diagonal | A naive atomic/tensor-to-product translation can create target derivations that do not exist in source | R and U for that translation | Not all linear–nonlinear adjunctions, CPS or modal encodings |
| Proof net equality versus raw LF | MLL quotient by proof-net commuting conversions, LF with uninterpreted rule constructors | Two source-equivalent proofs may translate to unequal target terms | EP for that encoding and equality pair | Not generic impossibility of reflecting net identity in a richer target |
| Undecidable group word problem | Source proofs equated by relators of a finitely presented group, effective translation with EP+ER into target *decidable* equality | Source equality would be decidable: contradiction | EP+ER jointly, **only** if target Eq and translation are effective and source class contains the hard group calculus | Not an obstruction if target equality undecidable or source class narrower; equality and type checking must not be conflated |
| Categorical collapse | Additional assumptions such as Cartesian classical negation and natural elimination, or bifunctoriality conditions on classical connectives | Distinct proof arrows can collapse under these precise laws | ER for this specific categorical target/equality | Not that classical proof identity cannot be represented categorically |
| Finite native interfaces/fullness | Fixed finitely many native profiles, **full** embedding of cyclic endomorphism classes | Finite-profile obstructions in earlier report 005; group abelianization against uniformly retracting cyclic p-groups | F and native profile requirements | Not merely EP+ER / faithful embedding; do not silently demand fullness |
| Process algebra finite axiomatisation | Specific process equivalences, action alphabets and auxiliary operator signatures | Known signature-sensitive non-finite axiomatisability (must inspect individual theorem) | F1 under a fixed signature and chosen behavioral Eq | Not signature-independent non-finite proof-operation presentation |

### Primary sources checked in this pass

- Craig C. Squier, *A finiteness condition for rewriting systems*, Theoretical Computer Science 131(2), 1994, pp. 271–294, DOI [10.1016/0304-3975(94)90175-9](https://doi.org/10.1016/0304-3975(94)90175-9). Abstract confirms 'finite canonical ⇒ every finite presentation FDT', and S1 not FDT despite FP-infinity and decidable word problem.
- Guiraud & Malbos, *Polygraphs of finite derivation type*, [arXiv:1402.2587](https://arxiv.org/abs/1402.2587), published MSCS 2016. Abstract verifies FDT invariant of finite presentations and constructive critical branching analysis.
- V. V. Rybakov, *Bases of admissible rules of the modal system Grz and of intuitionistic logic*, Math. USSR-Sb. 56(2), 1987, pp. 311–331, DOI [10.1070/SM1987v056n02ABEH003038](https://doi.org/10.1070/SM1987v056n02ABEH003038). Abstract supplies IPC's non-finite admissible-rule basis.
- *Abstract cyclic proofs*, Mathematical Structures in Computer Science 2024, [Cambridge article](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/abstract-cyclic-proofs/8734FB325CF465FAA88EC18663EE090A). Abstract: finite derivation graphs, global trace, and PSPACE-completeness of checking specified abstract cyclic conditions.
- *From GTC to reset: generating reset proof systems from cyclic proof systems*, Annals of Pure and Applied Logic 175(10), 2024, [publisher](https://www.sciencedirect.com/science/article/pii/S0168007224000897). Explicitly constructs reset conditions from trace systems; crucial counterweight to claiming that global conditions inherently defy finitely presented local machinery.
- Additional reports in repo: 003 proof-net versus LF; 005 restricted profile obstruction; 006 group/equality reductions; 008–010 checker/path/presentation counterexamples. Their novel informal proofs remain unmechanized.

**Access/verification disclaimer:** Abstracts and repo source extracts were inspected; complete original proofs, exact higher-dimensional theorem numbering and process-algebra negative theorems were not freshly independently verified. Entries relying only on repository reports are provisional controls, not newly proven results.

## 3. Concrete elementary negative controls

**Linear resource failure (R/U).** In a tensor-only intuitionistic linear calculus with atom P and no extra axioms, `P ⊬ P ⊗ P`. A counting invariant tracks that every tensor proof consumes two P occurrences while hypothesis provides one. In Cartesian closed semantics `P → P × P` exists by the diagonal. Sending tensor to product and linear context to ordinary Cartesian context therefore fails derivability reflection and resource discipline. *This attacks that morphism, not the existence of stronger modal translations.*

**Proof identity mismatch (EP).** Select MLL proof-net equality quotient identifying independent rule permutations. An LF encoding which records each sequent rule as a distinct constructor can map the two derivations to distinct normal forms. Thus equality preservation fails. To repair, choose an equality-respecting translation or a target quotient; do not claim proof identity is 'obviously preserved' by adequacy of raw derivations.

**Infinite admissibility vs finite deduction (F4 only).** IPC has finite standard deductive presentations and decidable admissibility for certain versions while admitting no finite basis of its *entire set* of admissible rules. Hence any proposed basis whose 'fundamentality' criterion requires all admissible inferences as derived rule schemata faces a genuinely different finiteness question. This is a useful **counterexample to conflating legitimacy with being an element of a finite primitive list**.

**Cyclic correctness (Val).** A finite directed cycle through locally well-formed rule instances is merely a cyclic *pre-proof*. Proofhood may depend on a trace that progresses along every infinite branch. A core built solely from local rule checking is incomplete as a proof validator unless a global witness/checker or equivalent reset construction is included. The 2024 reset construction demonstrates an alternate representation of global validity, so the observation alone cannot rule out generic finite mechanisms.

## 4. Transfer risks: monoids to proof calculi

For any proposed transfer of a finite-presentation obstruction, demand **one of**:

1. A full/faithful structure-preserving functor and a theorem that transports the exact obstruction, **including** its homotopy/coherence data, along that functor; or
2. A direct proof-theoretic construction whose generated proof category has the required obstruction and whose allowed target morphisms preserve it.

A syntactic embedding of a monoid's word problem into proof terms is **not enough** to transfer failure of finite homotopy basis, finite convergence or native finite generators. Likewise a proof calculus can have finite inference schemas but no finite admissible-rule basis without contradiction.

No such universally valid transfer theorem was verified in this investigation. Therefore **Squier does not refute universal finite explanatory proof operations**. The correct use is a discriminating test once an HC/finiteness preservation condition is fixed.

## 5. Invariance and presentation changes

- Squier FDT: invariant under finite presentation changes in the specified monoid setting.
- Existence of a finite list of named primitives: **not invariant** under adding a definable operator and its defining law.
- Existence of a finite presentation: can be an invariant *of the algebraic object under specified category/equivalence*, but not of arbitrary representation methods.
- EP/ER: relative to selected equality on source and target; a stronger target congruence can break reflection.
- Decidable equality: preservation plus reflection and computable translations into decidable target equality makes source equality decidable, by direct algorithmic reduction. If target equality is undecidable, no contradiction follows.
- Proof coherence and causality: neither follows from shared derivability; separately present cells or event/residual structure.

## 6. CMP-01 obligation matrix

'Fail' means an **explicit construction fails the obligation**, not the entire lens. 'Boundary' means a conditional theorem restricting what can be asked. 'Unresolved' means no compatible obstruction yet.

| Control | P | R | EP | ER | F | U | TR / Val | HC / CF | Overall |
|---|---|---|---|---|---|---|---|---|---|
| Linear→Cartesian naïve tensor map | not attacked | **Fail** | unknown | unknown | unknown | **Fail** | no inferred defect | n/a | Specific translation rejected |
| Raw LF for MLL net equality | plausible for derivations | source-specific | **Fail** | unknown | unknown | source-specific | extra source constants must be trusted | n/a | Must repair Eq translation |
| Group source into decidable-Eq target | if effective | may hold | incompatible with ER in general | **Cannot coexist with EP** | not needed | n/a | source group laws must be accounted | n/a | Universal effective EP+ER ruled out **under decidable target Eq** |
| IPC admissibility all-rules basis | standard proof system exists | n/a | n/a | n/a | n/a | n/a | **F4 fails** for entire admissible closure | n/a | Finite ordinary proof grammar survives |
| Cyclic pre-proof graph | graph representable | validity reflection fails if checking only local rules | chosen | chosen | n/a | n/a | **Val fails without trace/reset condition** | event graph insufficient | Global validity must be represented |
| Monoid S1 FDT/convergent | finite presentation | n/a | n/a | n/a | n/a | n/a | n/a | **F2/F3 boundary** | No general proof-algebra no-go follows |
| Classical categorical collapse | can preserve provability | depends | may hold | **Fail under specified collapse equations** | not evaluated | mode-specific | n/a | n/a | Specific doctrine/equality rejected |

## 7. Strongest conclusions we can defend

1. *There is no theorem in the checked evidence refuting the original ProofBasis north star in every mathematically meaningful interpretation.* Whether such a theorem exists elsewhere remains a literature question.
2. We **can** refute ambitious but overconstrained variants: a finite convergent rewriting representation of every finitely presented monoid preserving their homotopy data; a fixed decidable proof-congruence target faithful and effectively uniform over all finitely presented group word problems; a finite basis containing all admissible rules of IPC under the stated admissibility scheme; and the naïve linear→Cartesian embedding preserving derivability reflection.
3. Strong 'finite universal' statements must parameterize **what is finite** and **which morphisms preserve it**. A finite operation *grammar* is not a finite coherence, admissibility, or certified validity basis.
4. Generic doctrinal frameworks remain a plausible best-known explanatory direction but must be checked for equality reflection and trust provenance. An interpreter-only result is not an answer by itself.

## 8. Required review before S2 synthesis

- Verify selected original theorem statements and examples in full text (not only abstracts).
- Independently test whether CMP-01's proposed fields allow a translation to hide checker state in type images; do not invent a magical anti-interpreter invariant.
- Cross-review the exact ALG-01 / INST-01 / OBS-01 claim cards using common Eq, context and trust obligations.
- Check literature for finite basis results that directly concern *proof identity/coherence*, not monoids alone.
- Decide whether an S3 target should describe an indexed family of finite proof theories, a classification boundary, or a stronger existence proposition. Record the decision; do not silently narrow the source class.

**Decision:** OBS-01 submitted as an adversarial boundary map. No unqualified no-go result; no S3 theorem authorized.
