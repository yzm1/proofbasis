# ProofBasis research program — spine v1 (proposal)

**Status:** original common-basis direction explicitly approved by the owner; mathematical claims remain unestablished. **Last revision:** 2026-10-14. This file is the **canonical entry point** for research planning. Past reports are evidence; they do not silently replace the plan.

## North star

Investigate whether the structural machinery of mathematical proving admits a **finite, mathematically explanatory generative basis** spanning meaningfully different mathematical foundations, and determine the exact scope, obstructions, costs and alternatives. The goal is not to create another theorem prover, rediscover Turing completeness, or assert a unique minimal list of primitives.

**Separate questions rather than conflating them:**
- **Descriptive:** what mathematical objects capture operations, proofs, derivations, identity, higher transformations, environments and causality?
- **Normative:** what makes an inference rule justified/admissible or a generating operation meaningful?
- **Representational:** which translations preserve and reflect which properties?
- **Existential:** is a fixed finite presentation possible for a declared class and notion of fidelity?
- **Computational:** what are costs of search, checking, equality, translation and normalization?
- **Pragmatic:** what scientific result or useful tooling could emerge even if universality fails?

## Hard invariants of the program

1. Every claim has a **source class, assumptions, quantifiers and epistemic status**. Never slide between "all mathematics", "all effective presentations", and named logics.
2. Keep machinery, environment, trusted rule imports, definitions and evidence provenance separate.
3. Do not confuse encoding, adequacy, derivability reflection, faithful proof identity, fullness, or preservation of causal structure.
4. Compare mathematics **before** proposing new primitives or excluding interpreters through ad hoc syntax.
5. Track both positive and negative evidence, and compare strongest established theorems before novelty claims.
6. Maintain an explicit **bridge to the north star** for every narrower lemma or experiment.
7. No unbounded surveys; no premature survey cutoff either. Breadth first **as a map of relevant directions**, then selective depth by decision value.
8. No software implementation until a mathematical experiment and its falsifiable outcome justify it.

## Historical status and stages

The table below records the earlier sequence. Current direction is given in the final dated override and Task 020; historical labels do not authorize an SC continuation.

| Stage | Gate/question | Status | Deliverable |
|---|---|---|---|
| S0: initial formulation and adversarial review | Is naive universality nontrivial? | Complete as exploratory evidence; flawed conjecture | reports 001 and reviews |
| S0.5: structural fidelity and fundamentality | What did existing frameworks establish? | Complete as evidence, not as universal theorem | reports 002–003 |
| S0.6: existence/obstruction attempts | Could agents attack one identical proposition? | Method failure: divergent targets; valuable cases | reports 004–005 |
| S0.7: definition audits and adversarial controls | Which requirements are incoherent or vacuous? | Evidence complete; universal definition unresolved | reports 006–010 |
| **S1: landscape and research-design reset** | What mature mathematical structures and approaches must be considered? | **Next** | landscape map, option analysis, gap audit |
| **S2: common comparison** | Which existing structure best describes proof machinery across selected test systems? | Planned, dependent on S1 | side-by-side comparison, translations and negative controls |
| **S3: precise conjectures and feasibility** | Which existence, finite generation, equivalence and obstruction claims survive? | Not authorized | theorem-shaped alternatives with scope bridges |
| **S4: selective formal experiments** | Can existing proof tools settle exact disputed lemmas? | Conditional | checked artifacts, minimal experiments |
| **S5: independent peer review and dissemination** | Is result new, sound and useful? | Conditional | independent review, publication or defensible stop |

The stages are not a waterfall: return to S1 whenever a material new theory or overlooked prior art changes S2/S3 conclusions. This must be a logged change, not an informal detour.

## S1 research strategy

**1. Landscape identification (breadth):** Build an organized inventory across logic, proof theory, algebra, category theory, rewriting, type theory, semantics, concurrency and computation. Include mainstream and plausible niche approaches; score relevance and uncertainty. Being uninvestigated means a research backlog item, not an exclusion.

**2. Strategic options:** Compare at least (a) finite algebra of proof generators, (b) universal property / categorical object, (c) a family or hierarchy of bases, (d) institution/fibration indexed by foundations, (e) higher-dimensional proofs and proof transformations, (f) relational graph/multiway operational semantics, (g) impossibility/classification results. Include possibility that no unique universal object is desirable.

**3. Decision-oriented depth:** Select a few promising mathematical structures, not based on popularity, but explanatory reach and exact fidelity. Study decisive theorems and counterexamples.

**4. Synthesis:** State what is known, what must be assumed, what is impossible, and what alternatives to finite universal generators could meet the original intellectual objective.

## Common comparison controls

Use the same suite across theoretical families: intuitionistic natural deduction with βη; classical reasoning with chosen proof identity; linear/resource-sensitive calculus; dependent types and binding; equational rewriting; cyclic/global validity (boundary); proof nets/permutation of independent rules; a group/presentation and generic checker as anti-vacuity controls.

Compare: judgments, contexts, binding, composition, substitution, equality layers, resource rules, causal partial order, soundness/adequacy, environment/trust interface, finitary presentation, decision procedures and known complexity. Mark **N/A**, **unknown**, and **unsupported** separately.

## Research operating model

- **Registry:** see [landscape](research/LANDSCAPE.md), [decision record](research/DECISIONS.md), [backlog](research/BACKLOG.md), and [comparison rubric](research/COMPARISON_RUBRIC.md).
- **One task, one research question, one PR.** Branch-specific deep dives may run independently; integrated synthesis must refer to their exact report/commit.
- **Parallelize independent retrieval/depth.** Serialize shared definitions, cross-theory comparisons and conjecture freezes. Use peer cross-review for decisive claims.
- Agent results must cite exact primary theorems and disclose unverified sources and access limits.
- No new agents should be commissioned merely to produce more pages. See [research governance](research/OPERATING_PROTOCOL.md).

## Gate S1 acceptance

S1 completes only when the landscape has broad coverage and explicit exclusions, the principal alternatives have been compared against the north star and counterexamples, missing technical expertise is identified, and an independent red-team review has challenged *both* the inventory and prioritization. S1 does not require reading every paper. It requires **knowing what is on the map** and why some directions are deferred.

**Owner decisions still required:** desired degree of cross-foundation scope; acceptable notion of justification and equivalence; whether the outcome could be a family of structures rather than one algebra; eventual requirements for effective checking.

## S1 decision update — 2026-10-13

S1 landscape (PR #19) and alternatives (PR #18) are integrated as **research evidence**. [S1 synthesis 013](research/reviews/013-s1-synthesis-and-selection.md) passes the *planning selection gate*, while independent confirmation of decisive mathematics remains outstanding. **S2 is now the active planned research stage.** Start with [CMP-01 Task 011](tasks/011-common-comparison-contract.md); then paired [ALG-01 and INST-01 Task 012](tasks/012-generators-and-generic-frameworks.md); use [OBS-01 Task 013](tasks/013-obstruction-classification.md) as an adversarial classification track. None authorizes the S3 universal existence claim, software implementation, or removal of the north-star alternatives. This dated entry supersedes the historical table's S1 'Next' label without erasing its context.


## Bounded theorem-testing update — 2026-10-14

Tasks 017/018 have yielded one **independently reviewed informal result**: every mixed endomorphism p→p in the exact frozen A*(∅,{p}), with no nonidentity proof generators, equals identity under the full E*. [Synthesis 028](research/reviews/028-atomic-reciprocal-synthesis.md) records the evidence pins, a corrected cross-review typing error and the precise scope. This is not mechanical or external-referee certification, full SC, novelty, or unrestricted universal existence. The general mutual cut/substitution argument supports this atomic acceptance; its possible broader consequences are not silently promoted.

Full SC's all-boundary recovery, source equality preservation/reflection, naturality and finite-schema clauses remain open. The pure bridge/unit-extension comparisons remain separate pending checks if retained as dependencies. The next proposal is a bounded general pure-boundary recovery and equality-reflection gate, not another general definitions round. No broader task or agent is commissioned by this update.


## Next restricted SC gate — 2026-10-14

The reviewed evidence in PRs #34–#39 is now integrated on main. [Task 019](tasks/019-native-pure-fragment-fidelity.md) selects the proposed next gate from synthesis 028: native pure-boundary recovery/equation preservation/structure, independently paired with source equality-reflection and adversarial investigation. It quantifies over the original arbitrary finite X,Y and all source boundaries, retains full mixed interiors and fixes the original D*, E* and canonical maps. No broader definition change, implementation or all-foundations existence task is authorized. Both agents submit independently and decisive arguments receive reciprocal review; none is launched by this planning update.


## Current override — 2026-10-14: programme pause after external review

**This entry supersedes Task 019's selected/ready status and the certification emphasis of the preceding atomic entries.** Task 019 is PAUSED and its launch recommendation withdrawn. Synthesis 028 records an LLM-authored argument with separate-session same-vendor cross-review, not external human or formal certification. The coordinator is also an LLM.

See [external review](docs/EXTERNAL_PROGRAM_REVIEW_2026-10-14.md), [response 031](research/reviews/031-external-review-response.md) and [explicit decision entry](research/DECISIONS.md). Benton 1994's cut-elimination, subformula and semantic-soundness template was missed; simple model closures materially change task sizing. Those closure arguments and the generic/classical comparison must be written and verified, not automatically accepted from either LLM review.

No further paired theorem task is selected. A concise exact lemma/obligation packet, typing-only check and outside proof-theorist assessment are the proposed small pivot. There is no owner decision here to retire the charter, send messages, spend money, impose the review's fourteen-day deadline or archive. External running agents must receive the pause from the owner. The historical chronology is retained.


## Current direction — 2026-10-14: original common basis explicitly reaffirmed

The owner states: “I want to pursue the original common basis question.” This supersedes the pending choice between that goal and an SC-specific note. The charter's meaningful finite cross-foundation basis remains the north star; SC is one local diagnostic, not its definition. Task 019 remains paused. No archive or retirement is selected.

The next investigation is [Task 020](tasks/020-fixed-common-basis-gap.md). Reuse the already specified broad K candidate and existing prior-art/control record; find an exact fixed-core-versus-parameterization gap, theorem correspondence, construction or qualified obstruction. Do not produce another generic definition round or merely extend the pure LNL fragment result. The broad C_fin is a provisional envelope, not an owner-approved characterization of all mathematics; the source scope and omitted explanatory/causal properties remain explicit.

LLM mathematical work remains permitted. Correctness and usefulness depend on the argument, contract, prior-art status and suitable checks; outside human participation is a possible validation method, not a required source of discovery. Same-vendor review remains uncertified evidence. A family of doctrines may be comparative evidence or a demonstrated fallback, not an unapproved replacement objective. See the explicit owner-direction entry in research/DECISIONS.md.
