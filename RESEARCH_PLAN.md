# ProofBasis research program — spine v1 (proposal)

**Status:** proposed plan, not an approved theorem or a commitment to implementation. **Last revision:** 2026-10-09. This file is the **canonical entry point** for research planning. Past reports are evidence; they do not silently replace the plan.

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

## Status and stages

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
