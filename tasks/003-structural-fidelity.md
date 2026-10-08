# Task 003 — Proof identity, resources, and partial-order fidelity

**Suggested owner:** Codex. **Stage:** 0.5. **Output:** `reports/003-structural-fidelity.md` in its own PR.

## Mission

Independent adversarial audit of what a cross-foundation finite proof algebra would have to preserve *beyond derivability*. Start from a concrete minimal proof-net example, then compare existing frameworks. Do not invent a prover.

Read AGENTS.md, the charter, definitions, falsification plan and Stage-0 synthesis; inspect PR #1 and PR #2 plus the newer PR #2 self-review. Validate decisive sources independently.

## Problems to solve

1. **Verify or refute PR #1's MLL example.** Fix the precise fragment, contexts, occurrence labels, rule order, net-equivalence criterion, and target LF signature/conversion. Explicitly derive the two source proofs, show whether the proof nets are equivalent, and show whether target LF proof terms are equal. Do not assume the report's witness is correct.
2. Determine which conclusion this example supports: failure of the *specific raw LF encoding*, failure of an entire class of encodings, or something stronger. Do not generalize without a theorem.
3. Examine the strongest existing faithful or fully complete representations of the selected quotient in proof nets, CLF/LLF, generic modal or linear frameworks, categorical presentations and other relevant primary research. Analyze proofs modulo beta/eta, net permutations, resource-use and composition.
4. Address PR #2's correction of the vacuity–identity lemma: formally distinguish equality preservation from equality reflection and identify which constructions break each.
5. Model *causal precedence versus execution ordering versus proof equivalence*. Investigate whether a fixed independence congruence, event structure, or proof-net quotient preserves the intended behavior, and exhibit one conflict/nonconfluent example.
6. Specify trust boundaries, global validity conditions (cyclic cases as a boundary), and complexity costs separately. PSPACE-hard equality is not by itself impossibility.

## Optional mechanization

Only use an existing installed checker **if** it can settle a specific named dispute and is feasible in the assignment budget. Otherwise give explicit hand-checkable derivations and exact references. Never claim 'FORMALIZED' without checked artifacts.

## Required outputs

A precise test fixture described in mathematical prose (no software implementation required), theorem/evidence ledger, preserved/reflected properties table, strongest known faithful encoding or clearly bounded obstruction, identified unresolved lemma, STOP/NARROW/PROCEED recommendation.

Do not update the shared original report or charter. Work only in your report and supporting task-specific source notes. Prefer small, auditable PR.

## Completion test

State at least one verified structural non-equivalence/equivalence pair and what it does **not** imply about universality.
