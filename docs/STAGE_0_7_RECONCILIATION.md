# Stage 0.7 — Reconciliation and decision record

**Status: proposed research decision, not a theorem or approved frozen conjecture.** Based on Stage 0.7 Phase A reports [Claude #10](https://github.com/yzm1/proofbasis/pull/10) and [Codex #11](https://github.com/yzm1/proofbasis/pull/11), now retained on main. PR #9 is a *proposal*, not authoritative mathematics.

## Shared findings

1. Both agents audited the same commit of H and returned **DEFINITION UNRESOLVED**.
2. Finite source presentations can express arbitrary effective checkers; syntactic finiteness alone is not an anti-interpreter property.
3. Proof equality matters: one source calculus can have an undecidable word problem through a finitely presented group. Under effective equality-reflecting translations, a target with decidable *definitional* proof equality cannot cover that entire broad class. This is an informal reduction, not an independently machine-checked new theorem.
4. D2 and naturality/homomorphism alone do not establish that a common basis captures fundamental reasoning rather than interpreting a rule table. Universal finitely presented groups and indexed paths are adversarial controls.
5. Context/evidence trust cannot be reduced to names like 'rule' and 'assumption'; the precise introduction, discharge and justification obligations matter.
6. Causal traces are not in general invariant under proof equality; erasure, contraction, cyclic validity, and competing branches create distinct questions.

## Proposed conceptual decisions

**D1 — Core first.** Investigate finite algebra *existence for effective, structurally faithful embeddings*, with explicit composition and equality of proof classes. This is the research aim, not a claim that it exists.

**D2 — Do not require fullness.** It is a distinct stronger problem, with a conditional obstruction in Report 005. Every target inhabitant need not originate from the source.

**D3 — Do not require decidable target proof equality.** It would exclude sources with undecidable finitely presented congruence; if practical checking is required later, adopt a separately named restricted source class or proof-relevant equality certificates.

**D4 — Distinguish core and context by *trusted provenance*.** Imported mathematical assumptions are conditional. An arbitrary source proof checker or unproved inference rule is not a justified primitive merely because it is placed in a signature or environment.

**D5 — Move causal fidelity to an explicit extension H_causal.** This is not dropping causal structure from the research; it prevents an undefined global event notion from blocking a basic existence conjecture. Causality must be scoped to independently specified source systems with compatible events/congruence.

**D6 — Do not declare D2 or any interpreter filter sufficient.** Non-vacuity remains an explicit, testable open design obligation. A 'no encoded interpreter' English prohibition is not itself a mathematical predicate.

## Proposed sequence of formal targets

**H0 (baseline):** Fix source class C of effective finite-schematic proof presentations, including equations on proof classes. Seek a fixed finitely generated typed proof algebra A with an effective, composition/substitution-preserving translation for each S in C, reflecting as well as preserving source proof equality and source derivability under identified context interfaces. Distinguish target judgment inhabitation from source image membership. This **does not claim anti-vacuity**, so H0 alone is a representation baseline and may be satisfied by generic encoding techniques. Do not promote its existence to the project's desired theorem.

**H1 (scientific target):** H0 plus a **formally defined, independently motivated structural/non-interpreter invariant N(A,F_S)**. N must pass test cases for authentic compositional proof translations and reject explicitly constructed universal proof checker and encoded rule-table examples. No such N is approved yet. Therefore H1 is presently a *research schema*, **not a proposition ready for proof**.

**H_full (optional):** H1 plus fullness/surjectivity of target proof classes. Keep the atomic-profile obstruction and finite cyclic-group examples as conditional controls.

**H_causal (optional):** H1 plus a typed event/dependency/conflict structure on a fixed independently selected subclass where those relations are well defined and congruence-compatible. No universal raw construction-history requirement.

## Four unresolved decisions that must be settled in order

1. **C and its equality:** retain all effectively presented finite-schematic calculi with arbitrarily hard congruences, or choose a narrower independently justified class? Compare the consequences explicitly; don't shrink C merely to make a target work.
2. **What counts as a faithful judgment interface?** Define the source/target boundary, whether atomic formulas can map to compound types, and the meaning of derivability reflection when the target has additional inhabitants.
3. **Define N without circularity:** test on (a) typed-path interpreter, (b) finitely presented universal group, (c) LF adequacy for natural deduction, (d) structural linear/categorical translations, (e) explicit checker-as-proof. Report false positives/negatives and why the invariant is meaningful independent of our desired answer.
4. **Choose proof equality and computation interface:** target definitional congruence versus internal propositions/certificates; specify effective proof checking separately from effective equality checking.

## Completion and stop condition

Do not start opposing proof attempts until a *single* well-formed proposition H1, with N specified, is approved. The next work should be a **bounded definition workshop** addressing one invariant and one interface, not another unconstrained survey. Failure to formulate N is an informative outcome: the original concept of fundamental proof operation may not support a non-vacuous theorem under the current ambition.

## Evidence discipline

The group word-problem reduction in Report 006 and the typed-path challenge in Report 007 are substantive arguments with limited, disclosed verification. They are not universal impossibility results. No existing theorem is asserted to settle H1. Preserve both reports and their objections verbatim.
