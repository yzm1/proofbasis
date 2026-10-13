# S2-R1 — From definitions to falsifiable mathematics

**Status:** Approved operating protocol for the current two-agent research round; NOT approval of any universal-algebra conjecture. Recorded 2026-10-13. This document supplements [Task 014](../tasks/014-s2-contract-repair.md), the [S2 critical review](reviews/016-s2-critical-integration.md), and [the research plan](../RESEARCH_PLAN.md).

## Research trajectory and hard exit

1. Map established mathematical theories and existing results (S1, completed as a selection gate).
2. Specify *a finite portfolio of definite statements* about fundamental proof machinery, not one vague claim. Declare source classes, sorts, contexts, substitutions, proof equality, translations, trusted parameters and **separate** finiteness properties.
3. Attempt construction **and** falsification against the same frozen statements (S3 only after decision).
4. Verify decisive proofs, improve or reject statements, and communicate precisely what is new and what remains open.

**S2-R1 is the terminal bounded definition-repair round by default.** The task must deliver candidate conjectures plus proof/refutation entry points. It cannot end merely by requesting another general definitions survey. A new definition round would require a documented, bounded and independently reviewed mathematical reason why no candidate can yet be tested.

## What must be explicitly quantified

For each candidate C:
- Order of quantifiers, e.g. exists fixed target A for every S in explicitly specified class C, exists comparison F, or a *family* A(d) indexed by declared doctrines d.
- Mathematical sorts, contexts, assumptions, operations and substitution/composition laws.
- Source and target congruence / chosen proof identity; P, R, EP, ER, optional fullness F, resource U, trust TR, causal/higher obligations if claimed.
- **Intrinsic target-boundary reflection** versus **relative or image-restricted reflection**, with restrictions and target ambient operations made explicit.
- Finiteness vector: finite operation schemas, generators, equations, coherence, admissibility rules, native interfaces, decidability/effective checking; never conflate.
- Exact role of source-specific information: allowed environment axioms, interpreted rule tables, doctrine parameters and imported trusted inference.
- Presentation invariance: conservative defined generators/sorts, changes of notation and accepted equivalences.
- **Scientific meaning:** the result is not satisfied merely because an interpreter executes each source rule unless this is explicitly the weaker result under investigation.

## Common controls

Both independent agents must use the same tests: intuitionistic natural deduction with implication/products and beta-eta equality; cut-free unit-free MLL with proof-net/permutation equality; checker/typed-path/rule-table and finitely presented group encodings. Dependent substitution and cyclic global proof validity remain declared boundary tests, not silently dropped from the ultimate ambition. Test conservatively defined generators and hidden interpreter data in formula/type images.

## Agent round and independence

**Two Codex agents are running, user-started.** They replace the originally suggested Claude/Codex split because Claude tokens were exhausted. We neither assume these agents have completed nor that they are independent merely because each is Codex.

- **Codex A (structural / constructive)**: independently formulate and test 2–3 candidates, including one fixed finite-core conjecture and one indexed-family alternative. Target `research/reviews/017-structural-contract-repair.md`.
- **Codex B (adversarial / falsification)**: independently formulate the **same categories** of candidates, attempt counterexamples and expose interpreter/presentation loopholes. Target `research/reviews/018-adversarial-contract-repair.md`.
- Freeze the same baseline main commit `f1ce6b9bcf205b440d109bb82b888fd9acc262d5`, Task 014 and this protocol as common instructions. This protocol was added after agents started: send its link to each if feasible; **do not claim they already read it**. If branches started at the earlier SHA, do not rebase before Phase A submission; evaluate against the frozen task and reconcile protocol differences later.
- Separate working contexts, branches, report files and PRs; do not read the other agent's ongoing branch/report before each initial submission. No shared feedback loop or coordinated conjecture changes in Phase A.
- **Same model is not independent validation**: require later fresh-context cross-review, primary-source checks and (for decisive claims) outside mathematical expertise or mechanized checking.
- If the agents' submitted quantifiers or source classes differ, do not pretend they refuted the same conjecture. Normalize and freeze the common statements **before** comparing proof attempts.

## Deliverable: claim cards

Each agent must produce at least two, ideally three, compact claim cards:

1. Precise proposition and quantifier scope.
2. Existing mathematics / strongest related primary theorem.
3. Constructive witness or proposed route.
4. Strongest genuine refutation approach, and what a counterexample would and would not refute.
5. Finiteness and trust/equality/translation contracts.
6. Bridge from restricted test systems to the original mathematical ambition.
7. Verdict: **PROCEED / PIVOT / STOP / EXISTING THEOREM / DEFINITON FAILED**, with reasons.

**Reject:** unstructured surveys, coding tricks relabeled universal algebra, replacing equality by derivability, hidden source-specific rules, and proofs that attack different propositions.

## Decision gate after submissions

Review each report first as evidence, not as mathematical truth. Cross-examine the other report only after independent submission. Produce one reviewable synthesis PR recording:

- Are candidate statements well-formed and independently falsifiable (in the mathematical sense)?
- Are the positive/negative tracks truly addressing the *same* frozen claim?
- Which statements are already known theorems, plausible new statements, conditional obstructions or incoherent definitions?
- Are there decisive presentation/trust loopholes?
- Which of these actions follows: (a) freeze a non-vacuous candidate and launch construction + obstruction; (b) investigate a bounded portfolio; (c) pivot to family/classification; (d) stop claiming an algebra of fundamental operations; or (e) record rigorous reasons for one exceptional further definitions task.

**S3 remains blocked until this gate is passed.** Do not create implementation work as a substitute for an existence/obstruction investigation.

## Coordination record

2026-10-13: User started **two Codex agents** (not a Claude agent) because Claude tokens were exhausted. No completion status or agent branch identifiers were supplied in chat. Task 014 defines the originally allocated structural and adversarial roles. On receipt of PRs, verify which actual agent/report fulfills each role; do not infer role from author identity.
