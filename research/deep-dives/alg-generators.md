# ALG-01 — Generators, binding-aware algebra and higher proof presentations

**Research status:** bounded mathematical comparison, 2026-10-13. **Task:** [012](../../tasks/012-generators-and-generic-frameworks.md), algebraic track. **Contract:** [CMP-01 v0.1](../reviews/014-comparison-contract.md) (proposed, not yet independently reviewed). **Decision:** NARROW to exact equivalence/finite-coherence comparisons; do not claim a universal algebra exists.

## Executive finding

There is no shortage of **finite generating grammars** for proof constructions. The difficult question is *what structure generation must preserve*. Ordinary clones/Lawvere theories solve substitution-closed first-order finitary operations; second-order algebraic theories and monad/module signatures capture binding; free structured proof categories capture chosen composition and logical equations; polygraphs encode derivations and explicitly separate rewrite cells from higher coherence. These are adjacent but **not interchangeable** without a representation theorem.

The decisive gap is between:
- generation of raw syntax/derivations;
- quotient identity of derivations, including beta/eta and permutation equations;
- certified rule justification and admissibility;
- global checking/causal history.

A finite basis for the first need not be a finite basis for all four. Initial or free semantics guarantees a unique interpretation **within its defined model category**, not that a proof rule is sound in arbitrary mathematics or that an interpreter is ruled out.

## 1. Common-contract mapping

CMP-01 components abbreviated J/Ctx/Sub/Hyp/Der/Comp/Eq/Res/Val/Env/Prov/Event. 'Native' below refers to an established setting, not universal coverage.

| Lens | Native structure | Needs extra declaration or theorem | Characteristic failure |
|---|---|---|---|
| Ordinary clone / Lawvere theory | finitary operations, projections, composition, equations, generator changes | variable binding, scoped hypotheses, typed judgments, noncartesian resource use, proof equality as a distinct sort | cartesian projections/diagonals permit weakening/contraction |
| Second-order algebraic theory (Fiore–Mahmoud) | abstract binding, parameterized metavariables, second-order substitution, equational presentations | justified inference and semantic soundness, resource modes, global cyclic checking | declaring a proof constructor does not derive its mathematical legitimacy |
| Presentable monad/module signatures (Ahrens et al.) | initial syntax when hypotheses hold; binding and substitution; compositional signature building | not all signatures are representable; formal proof-identity adequacy depends on imposed equations | universality of syntax is not universality of justified deductions |
| Free CCC / SMCC / star-autonomous categorical proofs | typed proof morphisms, identities, composition, selected beta/eta and coherence; resource structure varies by doctrine | dependency/binding, cross-doctrine proof equivalence, core derivation of additional source rules | CCC diagonal maps cannot reflect arbitrary linear constraints |
| Multicategories, polycategories, operads/PROPs | multi-input and sometimes multi-output typed composition | explicit binders, modes, theory-specific equality, proof checking | abstract wiring is not proof validity |
| Polygraphs/computads | generators in several dimensions, rewriting cells, interchange/coherence candidates | specific typing/scope and global soundness; source proof equality may not match chosen cells | structural-bureaucracy equality does not imply beta/eta or all proof identities |

These are **comparison lenses**, not six competing complete logical foundations. One may supply the grammar and another the semantics.

## 2. Exact established reference results and interpretation

**Fiore & Mahmoud — second-order algebraic theories.** Their paper establishes categorical equivalences between second-order equational presentations and second-order algebraic theories, and between corresponding algebraic and functorial models; it defines translations for syntax with binding/parameterized metavariables. This supports stable comparison of *presentations in the stated second-order setting*. It does not establish that arbitrary inference-rule presentations are justified or that a universal target with fixed proof equality accepts all logics. [Primary author arXiv](https://arxiv.org/abs/1308.5409). Source evidence: abstract; exact theorem numbering requires full-text verification before use as a proof premise.

**Ahrens, Hirschowitz, Lafont & Maggesi — presentable signatures.** 'Presentable signature' is a sufficient condition for representability/initial syntax; initiality provides recursion/substitution. The article explicitly says syntax existence does not automatically hold for arbitrary signatures. The published article reports UniMath machine-checked main results. [LMCS publisher](https://lmcs.episciences.org/7511), [preprint](https://arxiv.org/abs/1805.03740). Theorem 6.3 ('any presentable signature is representable') is cited from the publisher version as identified in source excerpts; do not generalize it to all signatures or equate source proof validity with initiality.

**Guiraud — The three dimensions of proofs (2006).** This constructs a three-polygraphic translation for **SKS classical propositional logic**. The free three-category describes proofs modulo **structural bureaucracy**. Four-dimensional proof transformation is sketched, not given as a universal completeness theorem. [Author preprint](https://arxiv.org/abs/math/0612089), [journal](https://doi.org/10.1016/j.apal.2005.12.012). It is our closest explicitly higher-dimensional *finite* proof-presentation example, but only for a declared system and equivalence.

**Squier / Guiraud–Malbos — finite derivation type.** Squier's result: a finite convergent presentation implies finite derivation type, and Squier constructed a finitely presented monoid with decidable word problem but without finite derivation type. Thus finite presentation + decidable equality do **not** guarantee finite convergent rewriting or finite coherent completion. FDT is invariant among finite presentations under the appropriate Tietze changes. [Squier original abstract](https://doi.org/10.1016/0304-3975(94)90175-9), [Guiraud–Malbos survey](https://arxiv.org/abs/1402.2587), [2025 book summary](https://doi.org/10.1017/9781009498968.011). This is an obstruction about rewriting presentations/monoids and categories—not a theorem that no finite proof algebra exists.

## 3. Positive worked construction: a finite meaningful proof algebra

Fix propositional intuitionistic natural deduction with implication and conjunction, **modulo the chosen beta/eta equations**.

- Types/propositions: atoms, A⇒B, A∧B.
- Proof generators: hypothesis variable, abstraction and application; pairing and two projections.
- Grafting of a derivation into a hypothesis is typed, capture-avoiding substitution.
- Equations: beta reduction for application/abstraction and pair/projections; eta equations for functions and products; compatible closure.
- Under the Curry–Howard–Lambek correspondence, this is presented by the **free cartesian closed category** on the chosen atomic generators (with products and exponentials, and the usual treatment of context products).

**CMP-01 result:** J/Ctx/Sub/Hyp/Der/Comp/Eq are supplied, with exact beta/eta proof identity; the corresponding category has a universal property relative to cartesian closed structure. The grammar/equation *schemas* are finite although the proofs and proposition types are infinite. No assumption in an environmental signature is silently accepted as an existing theorem.

**Limits:** introducing classical control or linear resources changes the mathematical doctrine/equality, so this does not show a single CCC faithfully captures them. It does not certify object-level axioms by free generation alone. Event/causal time is not supplied.

This is a concrete nontrivial example of finite **logical** generating operations, but not evidence of cross-foundation universality.

## 4. Negative worked construction: cannot preserve linear usage via naive Cartesian embedding

Let S be the multiplicative intuitionistic linear logic fragment with an atomic proposition P, tensor and standard linear context use. In S, the single linear assumption P does **not** entail P⊗P. A resource-count invariant proves this in the atom-only tensor fragment: every proof of P⊗P requires two occurrences of P; one linear hypothesis supplies only one. (A unit/mode extension needs its own lemma.)

Let target T be a cartesian proof category with product × and the diagonal Δ_P : P→P×P. A naive translation that maps linear P to the same cartesian P, tensor to product, and the source sequent to the ordinary target Hom(P,P×P) satisfies target derivability while source derivability fails.

**CMP-01 verdict:** derivability reflection (R) and declared resource integrity (U) both fail; preservation alone can hold. This is an obstruction to **this mapping and chosen doctrine**, not to every translation of linear logic into a cartesian or nonlinear target (CPS/modal embeddings can use different boundaries).

An equally important counterexample against finite *coherence* inference is Squier's monoid: finite rule generators and decidable word problem do not entail a finite convergent presentation. Do not mistake the stronger negative result about convergent rewrites for non-finite algebraic generation.

## 5. Change of generators and what remains fundamental

Take group multiplication/inverse/identity as one presentation; add a named operation for a composite term together with a defining equation as a conservative extension. The **designated primitive list changes**, but the generated algebraic theory (under the applicable definitional/term equivalence) need not.

Thus:
- 'Is primitive in this syntax' is presentation-relative.
- 'Can be generated from a finite signature in a specified algebraic doctrine' is an existential property of the generated mathematical object.
- 'What is justified by the logic' is a *separate* soundness/admissibility question, not recoverable from the generator names.
- 'Which proof identities are retained' requires a fixed quotient/equation doctrine; functors preserving provability need not reflect equalities.

For binding, use second-order or monadic models rather than naive term equivalence with free variables. For linear/multimodal theories, specify which structural maps are available before calling two bases equivalent. A Lawvere-theory equivalence permitting Cartesian projections is not a neutral translation of linear resource behavior.

## 6. Higher cells and event order

In a 3-polygraph, a proof can be encoded by a 3-cell, with structural permutations encoded by interchange. If we wish to distinguish **proofs of equality between proofs**, collapsing to a 1-categorical Hom-set or a single proof quotient may lose precisely the interesting transformations. Further coherence data/cells require a **chosen higher-dimensional presentation**, not automatic claims of infinity or finiteness.

Likewise, a partial order captures required causal dependence but not conflicting branches. Two independent rewrites may commute in the chosen system; overlapping rewrites can branch without a join. Merely assigning them the same generation is not a proof of independence. An explicit event structure or residual/diamond property is a further obligation in CMP-01's Event field.

## 7. Proposed decision for subsequent S2 work

**ALG-01 is complete as a *comparison report*, not as a proof of finite universal generation.**

1. **INST-01** should test whether a fixed generic logical framework realizes our comparison contract across contrasting doctrines, especially equality preservation/reflection and the trust boundary. Investigate the *current* state of LSR Conjecture 8.5; no 2017 open label automatically survives into 2026.
2. **OBS-01** should determine exactly which finiteness properties remain invariant under the accepted presentation equivalence and test whether rewriting obstructions transfer to proof calculi.
3. **S2 synthesis** must compare the outcomes before selecting a universal object; it may conclude that a family of doctrine-indexed finite bases is the scientifically correct target.

**Stop/advance rule:** do not commission a new proof generator implementation. Advance only when a candidate translation has a precise source class, proof identity, context/resource map, trusted premise ledger and a theorem-shaped property *not already supplied by the free construction*.

## Evidence and limits

All new worked examples are informal textbook-level derivations; no formal proof checker executed. Primary source claims were corroborated using publisher/author abstract and available excerpts, not a complete independent audit of every theorem's proof. Prior ProofBasis source notes are reused as leads. In particular source theorem numbering, specific hypotheses on second-order presentation equivalences, and the original categorical correspondence need targeted primary verification before a publication claim. No universal result is claimed.
