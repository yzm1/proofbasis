# Stage 0.7, Phase A — Independent definition audit (Codex)

## 1. Verdict and immutable target

**DEFINITION UNRESOLVED — the Phase A gate does not pass.** The pinned H expresses an ambitious universal quantifier, and correctly separates faithfulness from fullness. I find no established contradiction between its derivability and proof-equality clauses. But H does not yet specify a predicate whose existence can be tested: its non-vacuity criterion is an explicit open obligation, and its event objects, maps, and compatibility with proof equality are unspecified.

This verdict is supported by concrete tests, not just those missing labels:

- Finite schematic source syntax already admits arbitrary effective certificate checkers, presented by explicit computation derivations (§3).
- An indexed finite-list/path representation interprets a source rule table while preserving derivability, proof classes, and composition on an independently specified family (§4). Its classification depends on the missing non-vacuity/trust predicate.
- Replacing a primitive rule by an assumed function has inverse proof translations. A derivation from that assumption certifies a macro without resolving whether the rule has been imported (§5).
- A raw-event interpretation and a proof-class interpretation of causal fidelity give different answers on β-erasure and cyclic graphs (§7).

**No claim that H is false, true, or vacuous is established.** The successful attacks target missing definitions and overstrong interpretations; failed attacks are recorded. In particular, PR #7's full/finite-profile obstruction does not apply to H. No prover, prototype, algebra implementation, or class-wide existence/impossibility attempt is made here.

**Exact target:** [PR #9](https://github.com/yzm1/proofbasis/pull/9), [docs/STAGE_0_7_COMMON_CONJECTURE.md at d72ab1f96ebdc0d5125453303a5f946a523ae15f](https://github.com/yzm1/proofbasis/blob/d72ab1f96ebdc0d5125453303a5f946a523ae15f/docs/STAGE_0_7_COMMON_CONJECTURE.md).

- Git blob: `71f79bcf08717cc9e46d06843dfbe267cc1d5d9c`.
- SHA-256 of the inspected file bytes: `a2e25da0244e91a343f5aa7c1d801cdbc2dd71fe659dbd691d25575abdbc47e3`.
- Research baseline: integrated main `40868e8`; Reports 001–005, their corrections, Stage-0 synthesis/acceptance review, AGENTS.md, charter, definitions, falsification plan, and protocol.

The conjecture remains untouched. Proposed repairs appear only in §9; none is adopted. **INFERENCE** denotes informal mathematical arguments, **VERIFIED_SOURCE** an inspected primary passage, and **UNKNOWN** an unresolved claim. Nothing here is **FORMALIZED**. Earlier agent findings, including my Report 005, are not independent mathematical verification.

## 2. What H actually quantifies over

H asks for **one** fixed finitely presented typed many-sorted A, with fixed typing/equality, such that **every** S in the target-independent class C has an effective translation of expressions, judgments, contexts, and proofs satisfying clauses 1–7. It does not require full maps on proof classes, finitely many atom profiles, or a uniform algorithm that discovers translations from source presentations.

Writing its existing obligations schematically, without filling them in:

```text
∃ A. FinitePresentation(A) ∧
  ∀ S ∈ C. ∃ effective F_S.
    DerivabilityIff(S,A,F_S) ∧ EqualityIff(S,A,F_S)
    ∧ CompositionSubstitution(S,A,F_S)
    ∧ ResourceIntegrity(S,A,F_S) ∧ Trust(S,A,F_S)
    ∧ NonVacuity_?(S,A,F_S) ∧ Causality_?(S,A,F_S).
```

The question marks identify obligations left open by the pinned file; they are not replacements for H. Environment translation is also implicit: “under the translated assumptions” does not yet define a map on source environments or say exactly what source-dependent declarations may accompany it. For example, the trust test in §5 has different outcomes depending on whether an empty source environment must remain empty or may acquire assumptions representing its fixed logical principles.

**Assessment of the universal ambition.** The order `∃A ∀S ∃F_S` is the correct strong order for the stated class. It is not `∀S ∃A_S`, and no source class may be chosen after selecting A. The absence of uniform synthesis is not a contradiction: each translation can be effective even if there is no common procedure producing them. A finite signature does not bound the number of generated types, indexed interfaces, or proofs. Therefore cardinality arguments that require a finite atom/interface menu cannot be imported from Report 005.

**Remaining quantifier decisions (UNKNOWN until fixed).** A completed statement needs the domains of F on open/schematic derivations; all source environments and typed boundary judgments over which clause 1 ranges; the componentwise substitutions in clause 3; and the structures/maps in clause 7. If substitution is native, the intended law would include

```text
F(d[e/u]) ≈A F(d)[F(e)/F(u)],
```

with an explicit context map making both sides well-typed. A translation of whole proof codes has a different target substitution operation. H currently permits neither side to be chosen silently. Likewise “finite generating operation schemas” needs a formal grammar of schemas, indices, and typing premises. Ordinary finite presentations are meaningful mathematical objects; allowing an arbitrary semantic side condition inside a purported schema would be a different definition.

## 3. Source membership and what finite presentation restricts

### 3.1 An explicit checker inside C

**INFERENCE — definition test.** Fix any deterministic machine M deciding a certificate predicate V_M(q,w). Encode configurations by finite terms for state, symbol, and tape/list constructors. There are finitely many states/symbols and transition patterns. Introduce these schematic judgments and rules:

```text
Run(c,c)                                      identity
Run(l_r[σ],u_r[σ])                             one rule per transition r
Run(c,d), Run(d,e)  ⇒  Run(c,e)                composition
Run(start(q,w), accepting_configuration(t)) ⇒  Proof(q)
```

The transition patterns, their sorted substitutions σ, and the start/accept configuration constructors are explicit finite syntax. No rule has an external “M accepts” side condition. Give Run composition its finite associativity/unit equations; leave other proof identity syntactic, modulo binding renaming where applicable. Local instances and finite derivations are effectively checkable. First-order signatures are the binding-arity-zero cases of Report 002's second-order signatures.

Induction on Run derivations shows that they compose actual machine transitions; conversely each finite accepting execution yields a derivation. Consequently

```text
Proof(q) is derivable  iff  ∃w. V_M(q,w)=1.
```

Thus even the **strict** Report 002 reading of finite schematic syntax includes deductive presentations of arbitrary effective proof checkers, once their computation is made declarative. The result does not assert that their target representations satisfy all of H. It establishes that the class definition cannot supply the missing non-vacuity criterion by itself. A universal machine can itself be a source calculus in C. A translation-relative criterion must distinguish interpreting another calculus's rule table from faithfully representing a source that genuinely contains computation; a blanket prohibition on computational derivations would exclude ordinary reasoning about programs.

### 3.2 Finiteness has real limits, but is not an anti-interpreter invariant

**INFERENCE.** For effectively enumerable finite syntax with checkable finite derivations/certificates, under a fixed finite or effectively enumerable assumption supply, enumerate candidate finite proofs with assumption evidence, check them, and output their conclusions. Derivability is recursively enumerable. Similarly, finite effective proof-equation schemas generate an enumerable relation of equality derivations; this does not make equality decidable. An arbitrary non-effective set of environmental axioms would invalidate the assumption-supply hypothesis; it must not silently be treated as an effective empty-environment foundation.

This excludes an effective empty-environment calculus whose intended consequence is all true first-order arithmetic. If those truths could be enumerated, for each machine e one could await either its arithmetical halting sentence or its negation; exactly one is true, giving a halting decision procedure. Such a procedure is impossible by the usual diagonal program that loops exactly when the supposed decider predicts it halts. These elementary arguments are informal, not new results or a refutation of H. They locate the effective-proof boundary of C. Full semantic second-order consequence and unrestricted infinitary proofs are not automatically covered by the ambition merely because their syntax is finite.

Finite presentation therefore restricts effectivity/presentation, while the checker construction shows it does not enforce mathematically native operations. Unlimited finite translations, numerical indices, and mathematical signatures can contain arbitrarily large source descriptions. This is compatible with a fixed finite core and with H's deliberate absence of efficiency bounds.

### 3.3 Presentation dependence can hide legitimate systems

Report 002 §2.1 forbids side conditions beyond sorting/binding unless they are re-presented declaratively. H adds effective local applicability but does not expressly say that this earlier prohibition is removed.

**Concrete example (INFERENCE).** A standard conversion rule in a typed lambda calculus has premise `Γ⊢t:A` and computational side condition `A≡B`, yielding `Γ⊢t:B`. On the strict Report 002 reading, this presentation is outside C. A version with an explicit finite equality derivation `c:A≡B` as a second premise may be inside C. But its proofs now include c, and can distinguish two certificates for the same conversion. Forgetting those certificates is not faithful for raw proof identity unless an appropriate congruence identifies them. Selecting canonical certificates also need not commute with composition/substitution without a coherence argument.

This exposes a real admission obligation for dependent/conversion-based foundations, not a proof that all their representations are impossible. On a broader “any effectively checkable side condition” reading, admission is easier but rule schemas immediately include arbitrary validators. The owner must choose which interpretation of **the existing class definition** governs; this audit does not choose a new C.

## 4. Explicit non-vacuity test: typed paths versus rule-table interpretation

**INFERENCE — bounded test of the definition, not an existence attempt for H.** Let G be any finite directed multigraph with uniquely identified edges. Define S_G by atomic objects Q_v, one unary inference operation `e:Q_u→Q_v` for each edge, identity/cut, and only the category unit/associativity proof equations. Empty boundaries have no proofs. It is a finite schematic source; its proof classes from Q_u to Q_v are exactly finite edge paths from u to v. G is specified independently of any target.

Now describe the standard indexed path/list construction. This test uses a data-indexed reading of typed operation schemas; H does not yet specify whether such indexed families are admissible. A conventional fixed first-order-sort reading would require reassessing the example, rather than assuming it qualifies. Its fixed syntax has finite list/numeral/edge-record constructors, a typed empty path, a typed edge-cons constructor, concatenation, and finite recursive lookup equations. The graph is **a literal data argument**, not a new primitive rule. Edge lookup has finite computation evidence. At a closed duplicate-free edge table, its canonical membership witness for each edge is unique; auxiliary lookup proofs need not introduce arbitrary certificate choices. The judgment and derivation translations are

```text
F_G(Q_u ⊢ Q_v) = Path(G,u,v)
F_G(id_u) = the empty path at u
F_G(e) = the singleton list [edge-id(e)]
F_G(d₂ ∘ d₁) = F_G(d₁) ++ F_G(d₂).
```

Here Path is the typed path family; inhabitance requires the encoded edges to exist in G and endpoints to match. This is a description of existing typed finite-list/free-category machinery, not a new implemented proof algebra.

The audit calculation is exact:

1. Inhabitants are precisely valid paths, so derivability is preserved and reflected, including absence of paths between disconnected vertices and absence of closed source proofs.
2. Associativity/units flatten source composites into edge words; unique typed edge words distinguish their classes. The map preserves and reflects the specified equality without installing per-G equations.
3. Grafting inserts/concatenates paths. Identity, composition, and sorted renaming of vertex/edge names are preserved. There is no binding operation in this source to omit.
4. Each arrow has one input/output boundary. No resource can be cloned to obtain an additional translated judgment: the path type checks the exact boundary transition sequence.
5. No new target primitive rule, equality axiom, or oracle is supplied; G sits in the translated judgment. On the literal no-new-trusted-primitive reading, the environment is empty and each singleton macro includes the finite lookup evidence. On a role-based reading that rejects interpreted source-rule tables wherever stored, this step is disallowed. That reading needs the missing mathematical criterion, not just a change in the table's address.

This is also a rule-table interpreter for finite unary calculi: a serialized source derivation is checked against G by fixed generic machinery. Calling the same constructor “edge composition” or “interpret rule” changes no typing or equations. Clause 6 says such serialization must not be the source of universality, but supplies no predicate deciding this case. An adequate translation-relative criterion must explain whether this ordinary free-category representation is admitted and what makes a general reflected rule-table interpretation different.

**Limit:** this is not a verified interpreter for all C, and it is not asserted to satisfy undefined clause 6 or every possible causal structure. If events are edge occurrences ordered by path traversal, their map preserves that chain. This is a semantic path order, not the execution order of constructing or checking the list. A requirement about native proof-construction dependencies could classify the same representation differently. That distinction is part of clause 7's unresolved definition, not a causal correspondence theorem claimed here.

Report 002's B1 reflected-signature proposal supplies a more ambitious checker lead (`Prf code_S code_J`, generic membership/instantiation/use). Its general adequacy and selected proof-equation reflection were not independently verified here; they remain **UNKNOWN**, not a theorem establishing clauses 1–5 for all C. Conversely, the withdrawn matrix-interpreter claim in Report 004 does not prove D2 vacuous: its failure at schematic metavariables is expressly preserved.

**Finding:** no construction has been established to satisfy H's non-vacuity requirement, because that requirement is not yet a formal predicate. The path test establishes why finite generation, compositionality, and a syntactically empty environment cannot fill the gap automatically. It does not establish that no suitable criterion exists.

## 5. Environment restrictions: rule/assumption equivalence is concrete

**INFERENCE — trust-boundary test.** Let N be the usual simply typed natural-deduction calculus for implication and absurdity, with βη proof equality. Fix an opaque atom p and K=((p→⊥)→⊥)→p. Form source N_r by adding the monomorphic rule

```text
Γ ⊢ f:(p→⊥)→⊥
----------------- r
Γ ⊢ r(f):p.
```

Give r no computation equation; source equality is the ordinary λ βη congruence extended to this constructor. This remains a finite schematic presentation. Compare the same core N under the **explicit assumption** `k:K`:

```text
F(r(f)) = k F(f);                  F preserves variables/λ/application.
G(k) = λz. r(z);                   G preserves the other constructors.
```

Substitution of k by the displayed closed source term gives a reverse proof translation. `G(F(r(f))) ≈ r(G(F(f)))` by β; `F(G(k)) = λz.k z ≈ k` by η. Induction extends these inverse laws to all typed terms and ordinary substitutions. Thus, under exactly corresponding contexts, the primitive-rule presentation and assumed-function presentation preserve and reflect derivability and proof equality, with composition/binding intact.

The assumption has genuine deductive content. In a two-world intuitionistic Kripke frame w₀≤w₁, let p hold only at w₁ and absurdity nowhere. No world forces ¬p, so w₀ forces ¬¬p but not p. The ordinary rules of N preserve forcing, by induction on derivations. Hence N cannot derive K from an empty context. “The macro `r(f)=k f` is certified from the core and declared assumptions” does not mean k's content was derived in the core.

H's classification of this example is unresolved:

- If “translated assumptions” means only the image of the source mathematical environment and that environment is empty, adding k is prohibited. The test does not then pass that requirement.
- If a per-S environment may include its logical principle as an explicit foundation assumption, the assumed-function presentation supplies no new **syntactic inference rule** and the macro has a core derivation. But it has transported precisely the primitive rule's content.

The distinction must be specified by source/environment provenance, not by whether k is written as an axiom, function, or tactic. It also cannot be based solely on quantification over formulas: this k is monomorphic. Nor should every induction, choice, extensionality, or set-theoretic schema be automatically called an illicit rule; assumptions of legitimate mathematical foundations were explicitly permitted. A rule/axiom policy that changes under the inverse translations above is carefully presentation-relative, not encoding-invariant. This is a definition obligation, not proof that H forbids every classical foundation or that every assumption-based translation fails.

“Independently justified theorems” also needs a stated checking foundation and dependencies. It cannot silently mean “true in whichever stronger foundation validates the source.” Clause 1 must continue to reflect derivability in the stated source under the corresponding assumptions, not in an unnamed extension.

## 6. Equality and resources: coexistence, counterexamples, and redundancy

### 6.1 Equality faithfulness can coexist with derivability reflection

There is no conflict between clauses 1 and 2 just because they compare different foundations. Hasegawa's linear CPS result is a verified positive control (§8). Identity translation of a finite λ-calculus with the same selected βη equality is another elementary control, though it is not universal.

There is also a direct counterexample to treating fullness as necessary for derivability reflection: Report 005's cyclic unary sources have End(p)=C_n and no other populated atomic boundaries; their faithful embeddings into the fixed group-word presentation of Thompson's V preserve those populated/empty boundaries while leaving infinitely many extra target endomorphisms at p. Source rotations become words of exact order n. The group theorem was checked from Cannon–Floyd–Parry in that report; its proof-category application remains **INFERENCE**. Extra proofs of an already derivable translated judgment do not violate clause 1. H correctly excludes fullness from its requirements.

A declared-rule LF encoding can fail to preserve a chosen object β equation: the terms headed by primitive `imp-e`/`imp-i` do not β-reduce like the corresponding source λ redex. This is a failure of that encoding/equality comparison, not of all permitted representations. LF's raw-proof adequacy theorem does not claim otherwise.

### 6.2 A resource failure of a specific representation

**INFERENCE.** In unit-free intuitionistic multiplicative linear logic set

```text
w(p)=1;  w(A⊗B)=w(A)+w(B);  w(A⊸B)=w(B)−w(A).
```

Each identity, tensor, implication, exchange, and cut rule preserves `w(Γ)=w(B)` for `Γ⊢B`. Therefore `p⊢p⊗p` is not derivable: 1≠2. A direct Cartesian interpretation of tensor as product with unrestricted p admits `x↦(x,x)`, giving that translated judgment a proof. It fails clause 1 and the “additional translated judgments” part of clause 4. This excludes the direct Cartesian interpretation, not targets with modalities, indexed contexts, other formula translations, or all possible A.

### 6.3 Clause 4 needs its independent content specified

The part of clause 4 forbidding **additional translated judgments** already follows from clause 1, if both quantify over the same contexts/judgments. Its remaining phrase “Track boundary occurrences and relevant modalities” needs a preservation relation distinct from that non-derivability condition.

A small test illustrates the distinction. Take the atomic one-input/one-output calculus with only identity proofs, permitting no closed proof, weakening, or contraction. Map its atom to a fresh object in the free Cartesian category. On the permitted zero/one-input atomic boundaries, empty/nonempty hom-sets still agree, and identity's single proof class remains faithful. Yet

```text
id_p = π₁ ∘ Δ_p : p→p
```

is a target representative that copies then deletes an occurrence. Translating identity by this representative preserves composition modulo Cartesian equality and introduces no additional **translated** atomic judgment. The underlying free Cartesian hom-set calculation is elementary: a variable-only output p must select an available p input, and no closed p exists.

If clause 4 forbids that representative on occurrence grounds, it is stronger than its derivability test and must define whether it examines F's chosen representatives, their equality classes, or all target proofs at a translated boundary. If it permits the representative because it equals identity, resource usage is observed modulo target equations, not by raw occurrence count. Neither answer is silently adopted here. Counting raw copies in every βη-equivalent representative would also reject harmless expansions in ordinary unrestricted calculi.

## 7. Cyclic validity and causal fidelity

### 7.1 Checkable cyclic graphs need an admission and annotation argument

**VERIFIED_SOURCE.** Brotherston's thesis Definition 5.1.6 requires every infinite path of a finite cyclic pre-proof graph to have an infinitely progressing trace on a tail. Proposition 5.1.10 says deciding this is decidable, via Büchi-automaton emptiness; the complete construction is in Appendix A. Thus a global check need not be an oracle. H has no polynomial-size/checking requirement, so neither globality nor complexity establishes impossibility of a finite core.

But the native graph's global validity condition is not a conjunction of the displayed local inference-rule instances. Under strict Report 002 membership, a checker derivation or other explicit validity certificate must be incorporated. H excludes graphs without certificates; it does not specify which annotated graph presentations are actually members, their proof congruences, or their valid composition operations.

**Explicit certificate-identity problem (INFERENCE).** For a valid graph g, a checker execution certificate c and the same certificate with administrative identity steps c′ may both verify validity. If the annotated proofs `(g,c)` and `(g,c′)` retain raw certificate identity, forgetting certificates maps two distinct proofs to one graph proof. Choosing a canonical certificate does not by itself prove compositionality. Identifying all checking evidence with a finite equation schema may be a reasonable separately proposed presentation, but its translation must derive that equality in the fixed core; it cannot be imported as a new target equation. Annotation is not automatically neutral for clauses 2–3.

**VERIFIED_SOURCE — a limit on a specific replacement.** Berardi–Tatsuta (2019), Theorem 8.3, give their 2-Hydra formula H from Definition 3.5 a proof in `CLKIDω(Σ_N,Φ_N)`, but no proof in `LKID(Σ_N,Φ_N)+(0,s)-axioms`. This rules out a conclusion-preserving identity-on-formulas replacement of that cyclic system by that explicit-induction system under those assumptions. It does not exclude other formula translations, richer fixed cores, or every representation allowed by common conjecture H. The paper's formula H is unrelated to the name of the conjecture audited here.

### 7.2 Raw events and proof-class events cannot be conflated

**INFERENCE — conditional counterexample.** In simply typed λ-calculus, with x,y:p, let

```text
d = (λz:p.x) ((λu:p.u) y) : p;      e = x : p.
```

They are β-equivalent. The displayed d has application/abstraction occurrences and the proof of its argument; e has none of those. Consequently an exact occurrence-poset invariant of the βη class cannot recover both raw event structures. A quotient-level definition requiring a bijection of all such occurrences is contradictory for this source. H does **not** explicitly require that bijection or exact chronology, so this is not a contradiction of literal H.

A raw-derivation event map can instead send events of d to events of the chosen raw F(d), while F(d)≈F(e) and their event structures differ. It must then say how maps change under equality: β-erasure has no residual for some events; duplication can give several residuals. A total single-valued map on proof classes is not interchangeable with a partial or relational residual map. Clause 7 currently does not select the level, preservation versus reflection, injectivity, or representative/equality coherence.

**Cyclic instance.** A finite cyclic graph has a dependency loop. Mapping each graph node to a distinct point of a strict partial order and preserving every edge would give `a<a` around a loop, impossible. The unfolding has instead infinitely many distinct event occurrences with an acyclic ancestor order. A finite presentation can represent that unfolding; H does not demand finitely many represented events. Thus “cyclic proofs have no partial-order semantics” is an invalid general conclusion. Graph nodes, unfolded occurrences, and operational executions must be distinguished before specifying the event map.

### 7.3 Conflict requires comparisons between alternatives

**INFERENCE — concrete test.** Start a labeled Petri marking with one token x:p. Let a and b each consume x and produce a q token. The one-event traces [a] and [b] are valid alternatives; they cannot both consume the same x in a joint execution. Each individual trace has an empty internal conflict relation. Preserving only its event poset and within-trace relations therefore says nothing about the conflict **between** a and b. A family of compatible event maps, or another explicitly chosen structure comparing alternatives, is needed to express that requirement.

CLF's labeled-token trace theorem handles a precise version of independence and consumption (§8); it does not automatically supply a uniform conflict structure for all proof calculi. A rule-commutation quotient, operational redex independence, and independence of mathematical assumptions also need not coincide. The issue is missing typed structures/quantifiers, not an established universal obstruction. This audit does not choose C_causal; that owner decision, if needed, must precede testing clause 7 as required by the pinned file.

## 8. Do existing representation theorems settle H?

**No theorem has been established to settle this identical target.** Without predicates for clauses 6–7, no theorem comparison can certify all seven clauses. The strongest relevant verified controls have exact, narrower scopes:

| Primary result | Checked statement and hypotheses | Relevance and remaining limit |
|---|---|---|
| Harper–Honsell–Plotkin, Theorem 4.1 | For every first-order formula and specified term/hypothesis context, valid raw proof expressions biject canonical LF inhabitants in the **specified Σ_FOL**; simultaneous term/proof substitution commutes with encoding | Strong syntax/binding adequacy. Object inference constants are declared in the signature; arbitrary selected mathematical proof equations are not covered. |
| Hasegawa, Proposition 5 and Theorem 1 | In the specified computational λ-calculus, `Γ⊢M=N:σ` iff `Γ°;∅⊢M°=N°:(σ°→o)⊸o`; every target inhabitant at that translated type/context is equal to a source image. o is absent from source base types | Equality reflection and fullness coexist across a change of discipline. Not arbitrary foundations, source equations, or causal structures. Proposition 5 attributes its equality result to Sabry–Felleisen. |
| CLF II, Lemma 5.19 and Theorem 5.23 | For the fixed net signature, individually labeled token traces correspond to expression classes under concurrent equality; the lemma reflects that equality into allowed exchanges | A real causal/resource correspondence. One constant per source transition is declared; no universal core-derived-rule theorem. |
| LSR extended version, §9.1 | Equational adequacy requires derived rule templates, equation preservation, normal-form back-translation and inverse laws, and permutation reflection | A serious generic route, not a proved theorem for all C. Its Conjecture 8.5 remains labeled a conjecture in the inspected version; the later “Theorem 8.5” reference does not certify it. Current resolution UNKNOWN here. |

**D2 is a candidate, not H.** Under Report 002's literal D2, ordinary LF/LLF declared-rule encodings fail the native-formula/imported-rule restrictions; CLF's Petri signature similarly declares transition constants. This is not a claim that the frameworks are deficient for their stated purpose. Generic F/U or mode-theoretic translations may derive rules for particular fixed modes; arbitrary base arrows, transformations, or equations supplied per source need their own trust audit. No verified theorem says every such input is admissible D2 machinery. Conversely, D2's stricter atom/sort/wrapper requirements can exclude genuine compound CPS or indexed representations. H expressly requires these admissions/exclusions to be tested, not assumed.

**Prior corrections remain in force.** Report 004's modal obstruction concerns its fixed relational/atom-free representation family. It does not exclude every H translation. Its matrix interpreter claim was withdrawn because of failure at schematic metavariables. Report 005's obstruction requires fullness and finite native atomic profiles, neither required by H. Declaring either report a refutation of H would change the question. Known free/category/framework universal properties quantify over specified structures and generators; they do not erase the input trust/equality obligations.

## 9. Minimal repair proposals — separate, not adopted

These are proposals for an explicit versioned owner decision. They do not amend the pinned file or authorize Phase B.

| Issue | Minimal proposed decision | What it sacrifices or adds |
|---|---|---|
| Scope and open contexts | Specify C's syntax/typing/equation/certificate grammar; quantify clause 1 over source environments and typed boundaries; define F on schematic proof holes with context/substitution laws | Removes presentation ambiguity. Requiring native hypotheses or fixed wrappers would additionally exclude some coded/indexed representations; those strengthenings must be acknowledged. |
| Non-vacuity | Supply a translation-relative predicate and apply it to the path/rule-table test and the reflected-signature checker. A candidate is fixed binding-aware judgment interfaces, componentwise syntax translation, and core-derived schematic rule templates with an explicit ban on source-rule codes in those interfaces | May exclude LF-style adequate encodings and legitimate parameterized categorical/CPS representations. No proof that this candidate excludes every interpreter is supplied. Strict D2 cannot be declared correct by fiat. |
| Trust separation | Fix which source axioms/signatures/hypotheses may enter E, and require theorem/macro certificates over their translated images with dependency provenance. Decide explicitly how the rule/assumption inverse translation in §5 is classified | Loses automatic invariance under changing a logical rule into a mathematical axiom. A presentation-relative ledger may be necessary; excluding all schematic axioms could exclude intended foundations. |
| Resource integrity | Specify the boundary-occurrence/modal maps and whether checking is on images, classes, or all target inhabitants; retain clause 1's quantification over all translated resource judgments | Gives clause 4 content beyond clause 1. A raw-representative ban sacrifices otherwise equal administrative copy/delete expansions; class-level observation needs an invariant. It need not introduce fullness. |
| Causal coherence | Choose raw derivations/configurations with typed event maps and stated residual coherence, or a specified quotient-level invariant. Decide how unfolding and inter-proof conflict are represented | Raw semantics are not invariants of every proof class. Exact quotient occurrence preservation excludes β-erasure; finite-node strict-poset preservation excludes native cyclic graphs. Restricting C_causal changes only the stated causal scope if clauses 1–6 still range over all C. |
| Certified re-presentations | Require an explicit judgment/proof equivalence between a native calculus and its annotated presentation, including certificate identity and composition, before counting it as the intended foundation | Adds a real admission lemma; mere decidability of a checker is insufficient. Does not require a new prover or efficient certificates. |

## 10. Phase A outcome and next definition test

The audit establishes a bounded but material result: **the existing finite-schematic restriction does not exclude arbitrary effective checker calculi**, and the indexed path example shows how rule-table interpretation can preserve substantial declared structure without new primitive target rules or equations. H's undefined clause 6 is therefore an essential condition, not optional wording. The environment inverse translations and β/cyclic examples likewise identify decisions that change which representations are admissible.

It does not establish global vacuity or internal inconsistency of every permitted interpretation, and it does not establish a universal positive construction. Proof equality and derivability reflection have verified compatible instances. Failures of Cartesian, declared-rule LF, or explicit-induction representations remain failures of those specified representations.

**The cheapest next definition test:** the owner must state the proposed non-vacuity predicate and apply it, without renaming operations or changing assumptions, to the two readings of the exact typed-path representation in §4. Record whether ordinary free-category generation and interpretation of the supplied rule table are admitted, and why the classification survives inlining its finite lookup definitions. This directly tests the missing gate. Causal/annotation decisions must also be fixed before the gate can pass; a successful path classification alone does not resolve them.

The pinned contract says: “If non-vacuity or causal fidelity remains undefined, the gate cannot be marked passed.” Both remain undefined. **Decision: DEFINITION UNRESOLVED. Stop after Phase A; no proof attempt, reconciliation, or replacement conjecture is authorized by this report.**

## Appendix — source passages and reading limits

Access/recheck date: 2026-10-08. Primary reading here is selected theorem/definition passages and their necessary context, not full reading of every publication. The repository reports and corrections were read as research evidence. No earlier agent's extraction is silently promoted to primary verification.

- **Harper, Honsell, Plotkin**, *A Framework for Defining Logics*, [Edinburgh manuscript](https://era.ed.ac.uk/bitstreams/f02739c7-c52e-4764-9229-a1fcb46daad6/download), Theorem 4.1, pp. 21–22; introduction's signature/adequacy definitions. Rechecked the displayed bijection, contexts, substitution equation, and proof-constant heads. **VERIFIED_SOURCE.** The source's main LF conversion is β; object-logic reductions are not inferred from that theorem.
- **Masahito Hasegawa**, *Linearly Used Effects: Monadic and CPS Transformations into the Linear Lambda Calculus*, FLOPS 2002, LNCS 2441, 167–182, [author copy](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/flops02.pdf), §§4–5, Proposition 5 p. 176 and Theorem 1 p. 177. **VERIFIED_SOURCE** for Hasegawa's statements; the attributed original Sabry–Felleisen proof was not newly extracted. No recursion/fullness extension is asserted.
- **Cervesato, Pfenning, Walker, Watkins**, *A Concurrent Logical Framework II: Examples and Applications*, [CMU-CS-02-102](https://www.cs.cmu.edu/~fp/papers/CMU-CS-02-102.pdf), March 2002, revised May 2003, §§5.2–5.4; Lemma 5.19 pp. 44–45 and Theorem 5.23 p. 46 (PDF pp. 46–48). **VERIFIED_SOURCE.** The isolated theorem sentence suppresses quotient notation; the preceding equality-reflection and inversion lemmas control its interpretation, as recorded in [Report 003 source notes](003-source-notes.md).
- **Licata, Shulman, Riley**, *A Fibrational Framework for Substructural and Modal Logics*, [2017 extended author version](https://dlicata.wescreates.wesleyan.edu/pubs/lsr17multi/lsr17multi-ex.pdf), Conjecture 8.5 p. 59 and §9.1 pp. 59–61. **VERIFIED_SOURCE** for the label and adequacy obligations; general resolution today **UNKNOWN**.
- **James Brotherston**, *Sequent calculus proof systems for inductive definitions*, Edinburgh PhD thesis, 2006, [official copy](https://era.ed.ac.uk/bitstreams/de6ecd6d-65fc-4b72-a0a1-f383b1748f5a/download), Definition 4.2.5 p. 81; Definition 5.1.6 p. 97; Proposition 5.1.10 pp. 98–99. **VERIFIED_SOURCE** for global validity and decidability. The inspected proof sketch constructs Trace, its complement, and an automaton for bad graph paths; Appendix A is the stated full proof, not mechanically checked here. Download SHA-256: `a643e2fa22d25cb9ac387d4d9fb22725bfcaffeb690310a92272ae17cadd06c1`.
- **Stefano Berardi, Makoto Tatsuta**, *Explicit induction is not equivalent to cyclic proofs for classical logic with inductive definitions*, LMCS 15(3:10), 2019, DOI [10.23638/LMCS-15(3:10)2019](https://doi.org/10.23638/LMCS-15(3:10)2019), [journal-formatted arXiv version](https://arxiv.org/pdf/1712.09603v5), Definitions 4.3–4.6 pp. 10:11 and Theorem 8.3 p. 10:23. **VERIFIED_SOURCE** for the exact compared systems and counterexample statement. Neither an arbitrary logical translation impossibility nor universal causal nonrepresentability follows.

The source-checker presentation, path test, rule/assumption inverse translations, Kripke countermodel, linear weight invariant, atomic Cartesian example, and conditional causal counterexamples are **INFERENCE / informal arguments**, not checker artifacts. They are bounded definition tests expressly requested for Phase A. No novelty is claimed.
