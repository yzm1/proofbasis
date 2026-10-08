# Falsification register and test plan

These are *attempted refutations*, not claims that the project has already failed. Record exact mathematical evidence and the version of the conjecture affected.

| ID | Threat | What would defeat the claim | First action |
|---|---|---|---|
| F01 | Already solved | Existing representation theorem satisfies all our defined properties | Recover strongest general-logics/LF/rewrite theorem with exact hypotheses |
| F02 | Trivial encoding | Any computable proof checker suffices under definitions | Try interpreter-in-a-primitive construction and see whether constraints exclude it |
| F03 | Hidden inference rules | Environment includes arbitrary trusted rules | Audit core/environment interface and trust obligations |
| F04 | Incompatible proof identities | No translation both preserves and reflects chosen proof congruences | Study classical/constructive and resource-sensitive examples |
| F05 | False graph locality | Cyclic/global correctness cannot be captured by specified local operators | Test cyclic derivations and trace criteria |
| F06 | False order invariance | Independent-looking rewrites change proof identity or result | Test non-confluent rewrite and resource-sensitive examples |
| F07 | Infinite/effective boundary | Important valid proof forms require infinitely many premises or non-effective validity | Examine omega-rule and semantic second-order consequence |
| F08 | Minimality ambiguity | 'Fundamental' disappears under arbitrary encodings | Compare competing bases and translation costs |
| F09 | False equivalence of efficiency | Derived/eliminated rule has severe size or search blow-up | Locate cut elimination and resolution tree-vs-DAG separation results |
| F10 | Weak universal quantifier | Target class C is chosen so narrowly the result is tautological | Require independent motivations and negative controls for C |

## Record template

For every investigated threat record: date; exact claim version; source and precise theorem location; relevant assumptions; proof sketch/counterexample; status (verified primary / secondary / conjecture / unresolved); result (fatal / requires scope change / not fatal / unknown); follow-up.

## Acceptance gate

Do not proceed to operation enumeration or implementation before F01–F04 and F08 have a source-grounded written assessment and a revised formal conjecture exists. Do not hand-wave around known counterexamples by redefining preservation after the fact.
