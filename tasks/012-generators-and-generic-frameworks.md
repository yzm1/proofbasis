# Task 012 — paired S2 investigations: ALG-01 and INST-01

**Dependency:** CMP-01 must fix the comparison contract before findings are interpreted jointly. Independent source retrieval may begin earlier, but do not silently choose a different contract.

## ALG-01: mathematical generators and higher proof presentations

Compare clones, Lawvere/second-order binding-aware theories, free structured categories, multicategories/polygraphs (including Guiraud 2006) using the CMP-01 contract. Identify what counts as finite generation, change of generators, derivability and proof identity. Determine exactly when categorical universal properties or higher cells carry more than a generic proof interpreter. Recover strongest known finiteness/coherence results and their hypotheses; do not infer they apply to arbitrary mathematical proofs.

**Output:** research/deep-dives/alg-generators.md; one positive and one negative construction under the contract.

## INST-01: indexed and generic proof frameworks

Compare LF/LLF/CLF, Licata–Shulman–Riley, adjoint logic/mode theories, Shulman doctrines, MMT/institution-style translations, and binding-aware context categories. Resolve the *current verified status* of LSR Conjecture 8.5 or state exactly what could not be verified. Separate object rule parameters from core-derived inference, and distinguish raw adequacy from proof-equality preservation and reflection.

**Output:** research/deep-dives/generic-frameworks.md; exact theorem applicability matrix, strong negative control, and one missing lemma that matters to the shared contract.

**Both tracks:** source-grounded, no novel tool implementation, no conjecture substitution, no source-class narrowing without owner approval. Deliver separate PRs. Cross-review before S2 synthesis.
