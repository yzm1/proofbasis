# Review 011: S1 landscape audit and missing prior art (Task 009)

**Assignment:** `tasks/009-landscape-audit.md` (MAP-01). Baseline: main `22dd02fc4f320b3d93d0e44b1d705c042f3fa626`.

**Author / date:** Claude (Claude Code session), 2026-10-09.

**Role:** landscape agent (`research/OPERATING_PROTOCOL.md`). This review does not:
- design an algebra;
- freeze a conjecture;
- declare the map complete;
- edit the canonical plan.

Proposed changes to `research/LANDSCAPE.md` appear in a separate, clearly marked appendix of that file (§10).

### Method

- Five parallel source passes (clusters A–E), each using the comparison rubric.
- Primary texts retrieved this session wherever possible.
- Per-family notes are in `research/reviews/011-source-notes/{A,B,C,D,E}.md`. Each claim there carries a status and location.
- I re-checked the decisive passages myself against the retrieved text:
  - Guiraud 2006 abstract;
  - Andréka–Németi Thm 2.1;
  - Polygraphs book Thm 8.2.4;
  - Avron–Zamansky Thm 4.7;
  - Došen's Joyal-collapse passage;
  - Heijltjes–Houston Thm 9.1;
  - Lafont Thm 10.

### Status labels

| Label | Meaning |
|---|---|
| **V** | Statement read in a primary text this session |
| **S** | Read only in a secondary source |
| **M** | Unverified memory |
| **NA** | Not accessed |
| **INF** | My inference |

Prior ProofBasis reports are used as evidence, not authority.

---

## 1. Executive summary

1. **The landscape splits into seven layers, and the project's original question spans several of them** (§2):
   - L0: computation / derivability;
   - L1: generation of syntax with binding;
   - L2: justification of rules;
   - L3: identity of proofs;
   - L4: higher-dimensional transformations;
   - L5: cross-foundation translation;
   - L6: causality.

   Earlier work narrowed onto L0/L1 and translation-interface questions.
2. **At L0 and L1 a finite basis is already known, and is cheap.**
   - All of ZF provability is captured by a recursive translation into a *finite equational calculus* (Tarski–Givant; Andréka–Németi Thm 2.1, V).
   - Logical frameworks with a single substitution rule (Metamath), or a fixed meta-logic (Isabelle/Pure, Dedukti), adequately encode many foundations at the provability level (C3 notes, V).
   - Dependent type theories are finite rule-schema presentations with initiality theorems (Uemura Thm 6.10; Bauer–Haselwarter–Lumsdaine; V).
   - **Any reading of ProofBasis that concerns derivability or syntax generation alone is pre-empted.**
3. **At L3, finite presentations of proofs *with* proof identity exist, one logic at a time.**
   - Free cartesian closed categories for NJ βη; free *-autonomous categories for MLL; control categories for λμ (A6, V/M).
   - A finite 3-polygraph whose free 3-category gives classical propositional proofs modulo "structural bureaucracy": **Guiraud, *The three dimensions of proofs*, 2006** (V). This is direct prior art the project never cited.
   - **Remaining candidate novelty:** cross-foundation uniformity, or a precise "explanatory" criterion. A finite basis per logic is not new.
4. **Decisive negative results the project had not engaged:**

   | Result | Content | Status |
   |---|---|---|
   | Squier's monoid S₁ | finitely presented with decidable word problem, yet without finite derivation type (FDT) or any finite convergent presentation | Polygraphs book Thm 8.2.4, V |
   | FDT is presentation-invariant | Thm 8.1.2 | V |
   | Existence of a finite convergent presentation is undecidable | §4.2.7 | V |
   | Joyal collapse | Došen 2003, §5, V |
   | MLL proof equivalence is PSPACE-complete | Heijltjes–Houston Thm 9.1, V |
   | No polynomial-time complete linear basis for Boolean logic unless coNP = NP | Das–Straßburger, V |
   | The analytic-rule hierarchy has provable limits | Ciabattoni–Galatos–Terui Cor 7.2, Ex 7.4, V |
   | Admissible rules of IPC have no finite basis | Rybakov via Jeřábek, S |
   | No finite equational basis for bisimilarity on a CCS fragment | Moller, S; Aceto et al. Thms 1–2, V |

   These are templates for *presentation-invariant obstructions to finite bases*. That kind of result is what the project's existence question needs.
5. **Justification of rules has a mature, partly decidable theory the registry missed:**
   - Avron–Lev canonical Gentzen systems (coherence ⇔ cut-elimination ⇔ 2Nmatrix semantics; coherence is decidable; Avron–Zamansky Thm 4.7, V);
   - the Ciabattoni–Galatos–Terui hierarchy (axioms ↔ finite structural rules, Thms 4.2 and 5.6, V);
   - Belnap's display-logic cut-elimination theorem (M, to verify).

   Harmony / proof-theoretic semantics is *not* a settled or safe criterion (C1 notes, V/S).
6. **Proof identity is not one fixed thing:**
   - normalization-based and generality-based identity agree only on small fragments (Došen §4, V);
   - there is no canonical axiomatisation of Boolean categories (Straßburger, V);
   - in HoTT, identity is a tower whose shape depends on the foundation (D1, V);
   - concurrent-game identity has several inequivalent forms once symmetry is added (E1; one unrefereed 2026 preprint).

   **The charter's "preserve proof identity across foundations" presupposes a notion that the literature shows is non-canonical.**
7. **Cross-foundation comparison in the literature preserves theorems, not proofs:**
   - institutions and general logics leave proof structure a free parameter (Meseguer 1989 Def 12, V);
   - proof-theoretic reduction maps proofs only primitive-recursively;
   - interpretability and "sameness of theories" form a hierarchy whose levels separate (Barrett–Halvorson; Friedman–Visser);
   - fibring of logics is not modular (Caleiro–Marcelino–Marcos Thm 4.1, V).
8. **The structure closest to the actual objective is higher-dimensional rewriting (polygraphs).**
   - It has finite generators in each dimension, composition, higher cells for identifications of proofs, *presentation-invariant* finiteness invariants (FDT, homological FPₙ), and known negative instances.
   - Its known gap is **variable binding**: there is no treatment in the Polygraphs book (D3, V by text search).
   - Second closest: free structured categories over doctrines, combined with Došen's "maximality" criterion for equations.
9. **Recommended portfolio (§8).** Five deep dives, in priority order:
   - **DD1** polygraphs and proof identity (Guiraud 2006; FDT for the control suite; the binding gap);
   - **DD2** justification theory (canonical systems, analytic hierarchy, display logic);
   - **DD3** identity-of-proofs theory (normalization vs generality, maximality, the classical case);
   - **DD4** type theories as finite presentations (initiality) versus what they leave out;
   - **DD5** cross-foundation morphisms that preserve proof structure.

   Wolfram multiway systems and Langlands do **not** warrant dedicated investigation (§7).

---

## 2. The landscape as a layered map

Each layer is a distinct mathematical question. A family can sit in several layers. The arrows (→) mark established bridges.

| Layer | Question | Families (status in this review) | What is settled |
|---|---|---|---|
| **L0** computation / derivability | Is there a finite device that verifies or derives exactly the theorems? | Universal machines, Kleene normal form, Craig; Cook–Reckhow proof systems; rewriting-logic universal theory; Tarski–Givant / relation and cylindric algebra; logical frameworks at the provability level | **Yes, trivially, for r.e. theories** (E6, B9, C3). **Not a research target** except as a negative control |
| **L1** generation of syntax with binding | What finite data present the syntax and judgments of a foundation? | Clones / Lawvere theories, operads / PROPs / generalized multicategories, second-order algebra (Fiore et al., Hirschowitz–Maggesi, Arkor–McDermott), GATs / CwF / natural models / Uemura / BHL, polynomial functors, combinatory logic | **Yes, at the level of finite schemas, with initiality** (B3, B4). Choosing the composition doctrine (operad vs PROP vs clone) is a *parameter* that encodes structural rules (Leinster Ex. 2.2.5, V) |
| **L2** justification | When does a finite rule set define a meaningful operation? | Proof-theoretic semantics / harmony; canonical Gentzen systems (Avron–Lev); analytic hierarchy (CGT08); display logic (Belnap); admissible rules (Rybakov, Jeřábek, Iemhoff); logicality (Tarski–Sher–McGee); abstract algebraic logic | **Partially, with decidable criteria in restricted settings** (A8, V). Negative results: harmony is incomplete or unsafe; IPC admissible rules have no finite basis; the analytic hierarchy is bounded |
| **L3** proof identity | When are two proofs the same, and is there a finite presentation of proofs modulo identity? | General proof theory (Prawitz, Došen); categorical proof theory (CCC, *-autonomous, control categories, Boolean categories); proof nets; combinatorial proofs; focusing / multifocusing; full completeness / game semantics | **Per logic, yes** (free structures; Guiraud 2006). **Across logics, identity is not canonical**: Joyal collapse, normalization ≠ generality, no canonical Boolean categories; complexity barriers (PSPACE for MLL; Das–Straßburger) |
| **L4** higher transformations | How are proof transformations (rewrites, permutations, normalisation) and their coherence presented finitely? | Polygraphs / higher-dimensional rewriting, Squier / FDT / homology, coherence theorems, string diagrams, HoTT / cubical, directed type theory | **Exact invariants with negative instances**: FDT is invariant; S₁; undecidable; dimension ≥ 3 has infinitely many critical branchings. Bridges: L3 → L4 (Guiraud 2006); L4 → HoTT (Kraus–von Raumer) |
| **L5** cross-foundation | How are different foundations related while preserving something? | Institutions, general logics, MMT / LATIN, Dedukti / Logipedia, fibring / combination, interpretability / bi-interpretability / tightness, reverse mathematics, ordinal analysis, realizability | **Theorem-level relations are mature; proof-level relations are absent** (C4, C5). Combination is not modular |
| **L6** causality / time | Dependency, independence and conflict of proof steps | Event structures, traces, Petri nets, Lévy residuals and optimal reduction, concurrent games, session types, process algebra | **Rich, but identity of strategies or processes is non-canonical**. Finite axiomatisability fails for some process calculi (Moller) |
| Analogies | — | Wolfram multiway / ruliad; Langlands functoriality | Multiway is subsumed by L4 and has few theorems. Langlands has no technical link (E3, E7, V) |

**Reading of the map.** The north star asks for a *finite, explanatory generative basis* across foundations.
- L0 and L1 give finiteness for free.
- L2 decides "explanatory" (justified).
- L3 and L4 decide "of proofs", not merely theorems.
- L5 decides "across foundations".

Every layer has mature mathematics. **The open territory is the conjunction L2 ∧ L3/L4 ∧ L5.** The literature treats each conjunct separately; it does not combine all three.

---

## 3. Family-by-family assessment (comparison rubric, condensed)

Columns:
- **Obj**: mathematical object.
- **Key result**: the strongest relevant result, with its status.
- **Represents / cannot.**
- **Rel**: relation to ProofBasis. **P** = direct prior art; **Adj** = useful adjacent structure; **An** = methodological analogy; **Sp** = speculative.
- **DD?**: would a deep dive change the framing?

Full rubric blocks are in the notes.

### 3.1 Proof theory (cluster A)

| Family | Obj | Key result | Represents / cannot | Rel | DD? |
|---|---|---|---|---|---|
| Deep inference / atomic flows | Derivations inside formulas, with local rules | SKS: every rule is *local*, with atomic identity, cut, weakening and contraction (Brünnler, V). Locality depends on the representation: switch is local on trees, not on strings (Brünnler §3.5, V) | Classical/linear propositional logic; quantifiers lose locality | P | Via DD1 (Guiraud builds on SKS) |
| Identity of proofs | Equivalences on derivations | Normalization vs generality identities agree only on limited fragments (Došen 2003 §4, V). Joyal collapse: a CCC with ⊥ and natural ¬¬A→A is a preorder (§5, V). Maximality (Post-completeness of the equations) is proved for CCC (V); for BCC it was open in 2004 | — | **P** | **Yes, DD3** |
| Categorical proof theory | Free structured categories | Free CCC ↔ NJ βη; *-autonomous ↔ MLL; control categories ↔ λμ, and a bifunctorial ∨ collapses them to Boolean algebras (Selinger Cor 3.8, V). No canonical Boolean categories (Straßburger, V) | Per-logic identity; classical identity requires choices | **P** | DD3 |
| Proof nets / complexity | Graphs of links with correctness criteria | MLL with units: equivalence is PSPACE-complete (Heijltjes–Houston Thm 9.1, V) | Canonical forms only where tractable | P | DD3 (as a limit) |
| Focusing | Normal forms modulo permutation | Multifocusing: maximal multifocused proofs ↔ MLL proof nets (Chaudhuri–Miller–Saurin Thm 16, V) | Canonical representatives of permutation classes | Adj | Supports L6 |
| Cut-elimination complexity | Size of normal forms | Non-elementary blow-up (Statman / Orevkov, S); quasipolynomial in deep inference (S) | "Admissible" ≠ "cheaply derivable" | Adj | No |
| Game semantics / full completeness | Models in which every morphism is a proof | Full completeness for MLL + MIX (Abramsky–Jagadeesan Thm 1, V) | Fullness criterion per logic | Adj | Part of DD3 |
| **Canonical systems (missing)** | Finite sets of canonical introduction rules | Coherence is decidable; for k ∈ {0,1}, coherent ⇔ strongly characteristic 2Nmatrix ⇔ strong cut-elimination (Avron–Zamansky Thm 4.7, V; Avron–Lev original NA) | Justification of connectives over *fixed* LK structure; no proof identity | **P** | **Yes, DD2** |
| **Analytic hierarchy (missing)** | Axioms ↔ (hyper)structural rules | N₂ axioms ≡ finite structural rules (CGT08 Thm 4.2, V); P₃ ≡ hyperstructural rules (Thm 5.6, V). **Negative:** any structural rule is derivable in LJ or trivialises it (Cor 7.2); no rule captures Łukasiewicz (Ex 7.4) | Which axioms become finite analytic rules, with proved limits | **P** | DD2 |
| **Display logic (missing)** | Display calculi | Belnap's general cut-elimination (conditions C1–C8) (M; verify); Kracht's characterisation (NA) | Family-level cut-elimination | P | DD2 |
| **Complete linear bases (missing)** | Linear inference rules of Boolean logic | Sound linear rules are coNP-complete; no polynomial-time complete linear TRS unless coNP = NP (Das–Straßburger, V), which poses a "complete basis" question | Negative finite-basis template | **P** (negative) | DD1/DD2 |
| Combinatorial proofs | Syntax-free proof objects | Sound and complete; polynomial-time checkable (Hughes; first-order version arXiv:1906.11236, V) | Identity *candidate*, not a theorem | Adj | DD3 |

### 3.2 Algebra and type-theoretic structure (cluster B)

| Family | Obj | Key result | Represents / cannot | Rel | DD? |
|---|---|---|---|---|---|
| Clones / Lawvere (prior work: reports 010) | Term operations | Presentation-independent structure; Tietze; Mal'cev (report 010) | No binding; generators not invariant | Adj | Done |
| Operads / PROPs / generalized multicategories | Multi-input composition | Plain operads ↔ "strongly regular" theories (no duplication or deletion) (Leinster Ex 2.2.5, V); composing PROPs via distributive laws (Lack Thm 4.6, V); Cruttwell–Shulman | The **choice of composition doctrine encodes the structural rules** | Adj | Inside DD1 / DD4 |
| **Finite complete PROP presentations (missing)** | Generators and relations, complete for a semantics | Boolean circuits F[2]: 7 generators plus finitely many relations (Lafont Thm 10, V). **Reversible circuits are not finitely generated** (parity invariant, §4.2, V). Interacting Hopf algebras ≅ linear relations (Bonchi–Sobociński–Zanasi Thm 6.4, V). ZX completeness (Jeandel–Perdrix–Vilmart Thm 1, V; Vilmart Thm 1, with schematic angles) | "Complete" is relative to a *fixed target semantics* | **P** (methodology) | Template for DD1 |
| Algebra with binding | Second-order syntax and equations | Second-order equational logic (Fiore–Hur, V abstract); initial representations (Hirschowitz–Maggesi Thms 2–3, V); presentable ⇒ representable, with a stated non-example (Ahrens–Hirschowitz–Lafont–Maggesi Thm 6.3, Non-ex 5.5, V; claimed UniMath, not inspected); Arkor–McDermott Prop 24 (V) | Finite schemas for binding syntax and reductions; not proof identity in general | **P** (L1) | DD4 |
| Dependent type theories as algebra | GAT / CwF / natural models / representable map categories | Bi-initial model for every type theory (Uemura Thm 6.10, V); general definition (BHL, V, partly Coq-checked); MLTT initiality formalised in Agda (Brunerie et al., V slides) | **A foundation = a finite schema presentation with initial semantics** | **P** | **DD4** |
| Polynomial functors | Signatures, inductive types | Gambino–Kock Thm 4.5 / Cor 5.17 (V) | Shapes of operations | Adj | No |
| Monads with arities / 2-monads | Abstract theories | Berger–Melliès–Weber Thm 3.4 (V) | Doctrines as parameters | Adj | Inside DD4 |
| **Combinatory logic (missing as a precedent)** | Finite bases {S, K} | Combinatory completeness ⇔ s, k exist (Selinger Thm 5.1, V). Naive λ→CL translation is unsound for β; extra axioms are needed (§5.4, Thm 5.14, V). Illative CL: Curry paradox, inconsistency (SEP, S) | Finite basis for *computation*; failure as a basis for *logic* | **P** (historical precedent and warning) | No (lesson recorded) |
| **Tarski–Givant / algebraic logic (missing)** | Relation, cylindric and polyadic algebras; AAL | ZF provability ↔ derivability of translations in a finite equational calculus (Andréka–Németi Thm 2.1, V). No finite Hilbert system is complete for the semantics (Monk) | Derivability only | **P** (pre-empts L0) | No |
| Abstract algebraic logic | Logics ↔ algebra classes | Blok–Pigozzi algebraizability via the Leibniz operator (S) | Consequence relations, not proofs | Adj | No |

### 3.3 Justification, frameworks, cross-foundation (cluster C)

| Family | Obj | Key result | Represents / cannot | Rel | DD? |
|---|---|---|---|---|---|
| Proof-theoretic semantics / harmony | Validity from rules | IPC incomplete for PTS variants: Harrop's admissible rule comes out valid (Piecha–Schroeder-Heister, S). Sandqvist completeness requires a nonstandard ∨ clause (S). Prawitz's conjecture is open. Naive comprehension is harmonious yet paradoxical (SEP, V) | Not a safe or complete criterion | P | DD2 |
| Admissible rules | Closure under rules | IPC: no finite basis (Rybakov, S); Visser rules form a basis (S). Admissibility is coNEXP-complete versus PSPACE for derivability (Jeřábek 2007, V) | "Generated" must say derivable vs admissible | P | DD2 |
| Logical frameworks | Meta-logics with signatures | Dedukti adequacy Thms 21, 23, 33 (V), conservativity only up to βηΣ (Lemma 32). Isabelle/Pure "faithful" = sound and complete (V). Metamath has a single substitution rule (V) | **Provability-level**; logic-specific rules are *declared and trusted* | P | No (covered) |
| MMT | Theories and morphisms | Logics as theories; morphisms preserve judgments (Thm 2.31, V); "no single conceptualization" (Rabe, V) | Proof identity not addressed | P | DD5 |
| General logics / institutions | Entailment and proof calculi | Meseguer: proof structure is a free parameter (Def 12, V) | Shape of a cross-foundation object | **P** | DD5 |
| **Combination / fibring (missing)** | Combined logics | Non-modular except under narrow conditions (Caleiro–Marcelino–Marcos Thm 4.1, V) | Limits on "generate a logic by combining parts" | Adj (negative) | DD5 |
| **Interpretability / sameness of theories (missing)** | Theories up to interpretation | Hierarchy of equivalences separates (Barrett–Halvorson Thm 5.2, V; Friedman–Visser 2025, V). PA / ZF / Z₂ are tight (Visser; Enayat, with a 2026 corrigendum, V) | Theorem-level comparison of foundations | Adj | DD5 |
| **Reverse mathematics / ordinal analysis (missing)** | Strength of subsystems | Big Five (Simpson, S); proof-theoretic reduction maps proofs primitive-recursively (SEP, V) | Strength, not proof structure | An | No |
| **Realizability (missing)** | Programs realizing proofs | Krivine: each new axiom needs new instructions (V) | No fixed computational basis across axioms | An (negative) | No |
| **Logicality (missing)** | Invariance criteria | McGee: permutation-invariant operations = those definable in infinitary logic (S) | Infinitary "logical basis", not finite | An | No |

### 3.4 Higher-dimensional structure (cluster D)

| Family | Obj | Key result | Represents / cannot | Rel | DD? |
|---|---|---|---|---|---|
| **Polygraphs / higher-dimensional rewriting** | Free (n,1)-categories on cells | Squier coherence (Thm 7.3.5); FDT is invariant (8.1.2); finite convergent ⇒ FDT (8.2.1); **S₁ is decidable with no FDT** (8.2.4); existence of a finite convergent presentation is undecidable (§4.2.7); TRS ↔ finite 3-polygraphs (13.4.8). All from the Polygraphs book, V | Finite generators + composition + identity cells, with *invariant* finiteness tests. **No binding** | **P (closest to the objective)** | **DD1** |
| **Guiraud 2006 (missing, crucial)** | SKS → 3-polygraph | "the free 3-category generated by this 3-polygraph describes the proofs of classical propositional logic modulo structural bureaucracy" (abstract, V). Thm 2.4.3: provability correspondence; Thm 3.3.1: bureaucracy ↔ exchange relations (V) | Propositional; linear logic only sketched | **P** | **DD1** |
| Dimension ≥ 3 limits | — | Finite convergent n-polygraphs can have infinitely many critical branchings (Guiraud–Malbos §4.3; Mimram, V); FDT fails in higher dimensions (Guiraud–Malbos Thm 4.3.9, V) | Squier does not lift naively | P (negative) | DD1 |
| Coherence theorems | "All diagrams commute" up to an invariant | Joyal–Street: equal iff planar-isotopic (Selinger survey Thm 3.1, V); coherence via convergent rewriting (Guiraud–Malbos, V) | Identity of *structural* proofs | Adj | DD1 / DD3 |
| HoTT | Types as ∞-groupoids | Judgmental equality is not internal; UIP and K are optional; reflection contradicts univalence; the universe is not a set (HoTT book, V). Contractible globular operad on identity types (Lumsdaine, V) | **Proof identity as a foundation-dependent tower** | Adj (decisive for L3 framing) | Narrow DD only |
| Cubical type theory | Computational univalence | Homotopy canonicity (Coquand–Huber–Sattler, V); normalisation and decidable conversion for Cartesian cubical type theory without universes (Sterling–Angiuli, V). De Morgan and Cartesian variants are both viable | No unique presentation | Adj | No (unless DD3 needs it) |
| Directed type theory | Non-invertible transformations | 2DTT (Licata–Harper, V); Riehl–Shulman (V) | Rewrites as morphisms | Adj | Later |
| Homological invariants | Homology of monoids and categories | FDT ⇒ FP₃; S₁ is FP∞ but not FDT (Thms 9.3.4, 9.3.15, V) | Detects but does not construct | Adj | Inside DD1 |

### 3.5 Computation, causality, deduction, analogies (cluster E)

| Family | Obj | Key result | Represents / cannot | Rel | DD? |
|---|---|---|---|---|---|
| Event structures / traces / Petri nets | Causality, conflict | Copycat-as-identity forces receptive and innocent strategies (Winskel notes Thms 4.12, 4.18, V); identity choices multiply with symmetry (preprint, unrefereed) | Causal structure; identity not canonical | Adj | Deferred (H_causal) |
| Lévy residuals / optimal reduction | Permutation equivalence | NA this session | — | Adj | Later |
| Session types (Caires–Pfenning, Wadler) | Cut = communication | V, for the linear logics each paper uses | Concurrency ↔ linear proofs | Adj | No |
| Rewriting logic / Maude | Concurrent rewriting | Reflective "universal theory, like universal Turing machines" (arXiv:1910.08416 §1, V; Clavel–Meseguer theorem NA) | **Vacuous universality**, as a negative control | Adj | No |
| E-graphs | Congruence closure data structure | No built-in binding; saturation "or timeout" (egg, V) | Engineering | An | No |
| Automated deduction | Inference systems with redundancy | Saturation framework mechanised in Isabelle (AFP "Saturation_Framework", V); "inference system" = arbitrary set of inferences | Procedures as generators; finiteness not intrinsic | Adj | No |
| Proof complexity | Cook–Reckhow systems | Frege systems are p-equivalent; extended Frege likewise (Buss notes citing Cook–Reckhow / Reckhow, S). Existence of a p-optimal system is open | **Presentation invariance at the level of size**: a model for invariance theorems | An | No |
| Computability | Universal machines | Kleene normal form, Rice (SEP, V); Craig (S); Craig–Vaught (M) | L0 trivial | — | No |
| **Process-algebra axiomatisability (missing)** | Equational bases for bisimilarity | No finite basis for a CCS fragment (Moller, S). Auxiliary operators under Assumptions 1–3 do not help (Aceto et al. Thms 1–2, V) | **Negative finite-basis theorems that depend on the signature** | P (negative template) | Inside DD1 |
| Wolfram multiway / ruliad | Multiway rewriting graphs | Arsiwalla–Gorard–Elshatlawy: Prop 3.1 concerns an example; Prop 3.3 assumes the homotopy hypothesis. The ZX paper has no theorems. Metamathematics "posits" (V) | Subsumed by polygraphs; does not engage Squier | Sp | **No** |
| Langlands | Functoriality | Langlands' 2011 lectures, informal (V) | No technical link | An | **No** |

---

## 4. Answers to the seven required questions

### Q1. Which traditions are indispensable?

1. **Structural and general proof theory (L2/L3).** The only traditions that define proof identity and justification precisely: Došen; categorical proof theory; canonical systems; the analytic hierarchy.
2. **Higher-dimensional rewriting / polygraphs (L4).** The only tradition with presentation-invariant finiteness theorems for *identities between derivations*. It contains Guiraud's proof-theoretic instance.
3. **Algebraic theories with binding and type-theoretic semantics (L1).** Needed to state *what* is being presented, including binding: Fiore et al.; Hirschowitz–Maggesi; Uemura; BHL.
4. **General logics / institutions (L5).** Needed to state "across foundations" at all.
5. **Computability (L0)** only as a boundary and negative control. It is already decisive and needs no further investment.

### Q2. Which important traditions were overlooked?

**Absent from the seed registry or prior reports:**
- Canonical Gentzen systems (Avron–Lev), the Ciabattoni–Galatos–Terui analytic hierarchy, and display logic.
- Finite complete presentations of PROPs: Lafont circuits, ZX, interacting Hopf algebras. This includes Lafont's *non-finite-generation* parity argument.
- Guiraud's polygraphic presentation of classical proofs.
- Squier / FDT used as an *obstruction theory*. Polygraphs were listed, but their negative theorems were not engaged.
- Tarski–Givant and algebraic logic, which pre-empt finite bases for derivability.
- Combinatory logic and illative combinatory logic, as precedent and warning.
- Finite axiomatisability in process algebra (Moller; Aceto et al.).
- Das–Straßburger's complete-linear-basis question.
- Interpretability, bi-interpretability and tightness of foundations; reverse mathematics and ordinal analysis.
- Combination / fibring of logics and its collapse.
- Realizability's growth of instruction sets.
- Logicality (Tarski–Sher–McGee).
- Initiality theorems for type theories.
- Admissible-rule bases (Rybakov, Jeřábek, Iemhoff).

**Listed but thin in the seed:** HoTT and cubical type theory, operads, concurrency.

### Q3. Which existing structures most closely express the actual objective?

| Rank | Structure | Why | Gap |
|---|---|---|---|
| 1 | **(n,1)-categories presented by polygraphs.** The "proof category of a foundation" with cells for rules (dimension 2), proof identifications (dimension 3), and coherence (dimension 4) | Finite generators, composition, identity as cells; FDT and FPₙ are *presentation-invariant* finiteness properties; there are negative instances; Guiraud 2006 already instantiates it for classical propositional proofs | Binding and dependent types; cross-foundation morphisms; justification is absent |
| 2 | **Free structured categories over doctrines** (CCC, *-autonomous, control, LNL / adjoint), with **Došen's maximality** as the criterion that the identity equations are "complete" | Per-logic proof identity with universal properties | Classical identity is non-canonical; the doctrine is a parameter |
| 3 | **Type theories as finite schema presentations with initiality** (Uemura, BHL) | Exactly "foundation = finite presentation generating syntax and models" | Identity = judgmental equality; no justification criterion; no cross-foundation fidelity beyond derivability |
| 4 | **Canonical systems and the analytic hierarchy** | "Finite rule set is justified iff a decidable condition holds" | Fixed structural layer; no proof identity |
| 5 | **Institutions / general logics / MMT** | Indexing by foundations with morphisms | Proof structure left as a parameter |

The literature suggests the objective is best expressed as a **combination**: a polygraphic or doctrinal presentation (1–2) of each foundation's proofs, justified by an L2 criterion (4), and related across foundations by morphisms of an institution-like indexed structure (5).

### Q4. Which ProofBasis assumptions are contradicted or weakened?

| Assumption (charter or earlier reports) | Evidence | Effect |
|---|---|---|
| A finite universal basis would be a new kind of result | Finite bases exist at L0 (Tarski–Givant, frameworks), L1 (Uemura, BHL), and per logic at L3 (free categories, Guiraud) | **Contradicted** for those levels. Novelty is possible only for cross-foundation uniformity with justification and identity |
| "Proof identity" is a given relation that translations should preserve | Došen §4; Joyal collapse; no canonical Boolean categories; HoTT identity tower; concurrent games | **Weakened.** Identity must be a declared parameter, possibly per foundation, and its invariance across foundations is itself a question |
| Harmony / proof-theoretic semantics can serve as the justification criterion | PTS incompleteness; naive comprehension; presentation-sensitivity | **Weakened.** Canonical-system coherence and the analytic hierarchy are better-developed candidates |
| "Finite" is an intrinsic property | Brünnler §3.5 (locality depends on the representation); Aceto et al. (depends on the signature); ZX and type theories (schema-level); IPC admissible rules (no finite basis) | **Weakened.** Finiteness must be stated relative to a representation, signature and schema discipline. **Strengthened** where invariants exist (FDT, p-simulation) |
| Cross-foundation translations should preserve proof identity | No surveyed framework does; institutions leave proof structure free; reductions preserve proofs only primitive-recursively | **Unsupported** by any established theory. An open question, not a background assumption |
| The difficult part is excluding interpreters (Stage 0.7 focus) | Rewriting logic's universal theory and Metamath show L0 vacuity is standard. L2–L4 theories (canonical systems, FDT, maximality) give *positive* structural criteria not based on excluding interpreters | **Reframed.** Non-vacuity may follow from L2–L4 invariants, not from anti-interpreter syntax |
| Wolfram multiway is a distinct new framework | Subsumed by polygraphs; few theorems | **Contradicted** as a research direction |

### Q5. Which directions deserve dedicated deep dives?

See §8 (DD1–DD5), each with the question that earlier reports did *not* answer.

### Q6. Which directions are unlikely to justify significant investment?

| Direction | Reason |
|---|---|
| **Wolfram multiway / ruliad** | Its mathematical content is polygraph or higher-rewriting theory without Squier-type results. Its main propositions are example-level or assume the homotopy hypothesis (E3, V). Any value is reachable through DD1 |
| **Langlands** | Methodological analogy only. Langlands calls the lectures informal (E7, V) |
| **Further L0 computability or framework-universality surveys** | Settled: trivial finite bases exist; the frameworks are documented (C3, E6) |
| **E-graphs / equality saturation** | No binding; an engineering tool (E2, V) |
| **Realizability, ordinal analysis, reverse mathematics** | Measure strength or computational content, not proof-operation structure. Keep as boundary references |
| **Full HoTT / cubical programme** | Foundation-specific. Only one narrow question matters (judgmental vs propositional identity as a design choice), and DD3 can absorb it |

### Q7. Which alternative formulations emerge?

| ID | Formulation | Source tradition |
|---|---|---|
| **F1 Finite-coherence classification** | For each foundation's proof category (with declared identity), decide whether it admits a finite coherent presentation (FDT / finite polygraphic resolution to dimension 3). Classify foundations by these invariants | Polygraphs; Squier; Guiraud |
| **F2 Doctrinal universality** | Is there a finite stock of doctrine-forming constructions (adjunctions, comonads, modes; cf. LSR / adjoint logic) from which every foundation's proof doctrine arises? Proofs are then free objects | Categorical proof theory; 2-monads |
| **F3 Justified-generation classification** | Characterise the finite rule schemas that are justified (canonical systems, display, hierarchy) and their closure and limit properties. Universality = expressive completeness of the justified class, *with known negative boundaries* (CGT Cor 7.2) | L2 |
| **F4 Indexed family** | An institution-like indexed category of foundations whose morphisms preserve a declared proof structure. Universality = existence of initial or colimit objects. The open part is morphisms that preserve proof identity | Institutions; MMT |
| **F5 Obstruction programme** | Develop invariants (FDT, homology, Lafont-type parity, p-simulation classes, Moller-type non-axiomatisability) that obstruct finite bases for proof structure | Polygraphs; process algebra; proof complexity |
| **F6 Canonical identity per foundation** | Determine the maximal coherent identity (Došen maximality) for each foundation, then ask whether these identities are preserved by any translations | General proof theory |

These overlap with Task 010's option list. F1, F5 and F6 are not on that list as stated and should be considered there.

---

## 5. Coverage matrix

States: **investigated** (decisive primary results read) / **partial** (some primary results; gaps named) / **unknown** (not reached) / **deferred** (with reason).

| Family | State after 011 | Evidence | Priority (decision value) |
|---|---|---|---|
| Deep inference | partial | Brünnler (V), Guiraud (V) | High, via DD1 |
| Identity of proofs | partial | Došen (V), Straßburger (V) | **Highest** (DD3) |
| Categorical proof theory | partial | Selinger (V); Lambek–Scott, Seely NA | High (DD3) |
| Proof nets / complexity | partial | Heijltjes–Houston (V) | Medium |
| Focusing | partial | Chaudhuri–Miller–Saurin (V) | Medium |
| Canonical systems / analytic hierarchy / display | partial (Belnap and Avron–Lev originals NA) | Avron–Zamansky (V), CGT08 (V) | **Highest** (DD2) |
| Game semantics | partial | Abramsky–Jagadeesan (V) | Medium |
| Clones / Lawvere | investigated (reports 010) | — | Done |
| Operads / PROPs | partial | Leinster, Lack (V) | Medium |
| Finite complete PROP presentations | partial | Lafont, Bonchi–Sobociński–Zanasi, ZX (V) | High (template) |
| Algebra with binding | partial | Fiore–Hur (abstract), Hirschowitz–Maggesi, AHLM (V) | High (DD1 gap; DD4) |
| Type theories as algebra / initiality | partial | Uemura, BHL (V) | **High** (DD4) |
| Combinatory logic | partial | Selinger (V), SEP (S) | Low (lesson recorded) |
| Tarski–Givant / algebraic logic | partial | Andréka–Németi (V) | Low (pre-emption recorded) |
| Abstract algebraic logic | partial (S) | SEP | Low |
| Proof-theoretic semantics | partial | SEP, Gheorghiu–Pym (V/S) | Medium (DD2) |
| Admissible rules | partial | Jeřábek (V) | Medium (DD2) |
| Logical frameworks | investigated (reports 001–003, C3) | Dedukti, Pure, Metamath (V) | Done |
| MMT / institutions / general logics | partial | Rabe, Meseguer (V); Goguen–Burstall, Diaconescu NA | High (DD5) |
| Combination / fibring | partial | Caleiro–Marcelino–Marcos (V) | Medium (DD5) |
| Interpretability / sameness of theories | partial | Barrett–Halvorson, Friedman–Visser (V) | Medium (DD5) |
| Reverse mathematics / ordinal analysis | deferred | SEP (S) | Low: strength, not structure |
| Realizability | deferred | Krivine (V) | Low |
| Logicality | deferred | SEP (S) | Low |
| Polygraphs / Squier / FDT | partial (core theorems V) | Polygraphs book, Guiraud–Malbos (V) | **Highest** (DD1) |
| Coherence theorems | partial | Selinger survey (V); Power, Kelly NA | Medium |
| HoTT | partial | HoTT book, Lumsdaine (V) | Medium-low (narrow) |
| Cubical type theory | partial | Coquand–Huber–Sattler, Sterling–Angiuli (V) | Low |
| Directed type theory | unknown (titles only) | — | Low-medium |
| Homological invariants | partial | Polygraphs book (V) | Inside DD1 |
| Event structures / concurrency | partial | Winskel notes (V) | Deferred to H_causal |
| Lévy residuals / optimal reduction | unknown (NA) | — | Deferred |
| Rewriting logic / Maude | partial | arXiv:1910.08416 (V) | Low (negative control) |
| E-graphs | partial | egg (V) | Low |
| Automated deduction | partial | Saturation framework (V) | Low-medium |
| Proof complexity | partial (S) | Buss notes, Pudlák | Low-medium (invariance analogy) |
| Process-algebra axiomatisability | partial | Aceto et al. (V); Moller (S) | Medium (obstruction template) |
| Wolfram multiway | investigated enough to deprioritise | E3 (V) | **Not pursued** |
| Langlands | investigated enough to deprioritise | Langlands lectures (V) | **Not pursued** |
| Still unknown | Ludics / geometry of interaction, transcendental syntax, Hilbert's 24th problem (Thiele), illative CL in detail, persistent homology of proofs (search found nothing), quantitative / graded proof theory, proof mining | — | Next landscape pass |

---

## 6. Strongest negative evidence (to carry forward)

1. **Squier S₁** (V). Even with decidable equality, a finitely presented structure can lack any finite coherent presentation, and this property is presentation-invariant. *Implication:* "finite basis for proof identity" can fail for reasons independent of computability.
2. **Undecidability of finite convergent presentability** (V). No algorithm decides whether a finite basis of the strongest kind exists.
3. **Joyal collapse and Selinger Cor 3.8** (V). Classical proof identity requires non-canonical structure.
4. **Došen §4** (V). Two natural identity criteria diverge.
5. **CGT Cor 7.2 / Ex 7.4** (V). Finite structural-rule bases cannot capture certain logics.
6. **Lafont's reversible-circuit parity** (V). Bounded-arity generators cannot generate everything, by an invariant.
7. **Moller; Aceto et al.** (S/V). Finiteness depends on the signature, and auxiliary operators of a restricted kind do not help.
8. **Admissible rules of IPC have no finite basis** (S).
9. **Heijltjes–Houston; Das–Straßburger** (V). Canonical forms or complete bases can be intractable.
10. **Caleiro–Marcelino–Marcos** (V). Combining logics is not modular.
11. **Krivine** (V). Computational content grows with axioms.

---

## 7. Directions not recommended (with reasons)

See Q6. In addition: no further broad surveys of logical frameworks. Their provability-level adequacy, and their trust in declared rules, are documented across reports 001–010 and C3.

---

## 8. Prioritized deep-dive portfolio

Each dive is one bounded question, using the common controls (`RESEARCH_PLAN.md`). The second column says why earlier reports did *not* answer it.

| Priority | Deep dive | Why not already answered | Bounded question | Decision value | Main uncertainty |
|---|---|---|---|---|---|
| **1** | **DD1: polygraphs and proof identity** (Guiraud 2006; Polygraphs book chs. 7–9, 13; Guiraud–Malbos) | Reports 001–010 never engaged polygraphs or Squier-type invariants; Guiraud 2006 was uncited | For the control suite (NJ βη, MLL, SKS / classical), is there a finite polygraphic presentation of the proof category modulo the declared identity, and does it have FDT? What exactly blocks binding, and is there a binding-aware polygraph theory? | High. Either supplies the formal object for F1/F5 or exposes binding as the decisive gap | Whether binding admits a polygraph treatment at all; dimension ≥ 3 pathologies |
| **2** | **DD2: justification theory** (Avron–Lev originals; CGT08 and its successors; Belnap C1–C8; Kracht; Chen–Greco–Palmigiano; admissible-rule bases) | Earlier "harmony" discussion (reports 002, 008) used local soundness and completeness only; canonical systems and the hierarchy were absent | What is the strongest known theorem of the form "a finite rule set is justified iff decidable condition C", and what are its proved limits (CGT Cor 7.2) and its relation to proof identity? | High. Could supply the L2 component and replace ad hoc non-vacuity predicates | Belnap and Avron–Lev originals NA; the extension to first order is unclear |
| **3** | **DD3: identity of proofs** (Došen, Došen–Petrić; maximality; Lamarche–Straßburger; Selinger; Hughes; Heijltjes–Houston) | Reports 004 and 008 cited single faithful-completeness results; none compared identity *criteria* | Is there a foundation-neutral criterion of proof identity (maximality? generality?) that is well defined for intuitionistic, linear and classical logic? If not, what must be declared per foundation? | High. Decides whether "preserve proof identity across foundations" is well posed | BCC maximality status unknown |
| **4** | **DD4: type theories as finite presentations** (Uemura; BHL; initiality; AHLM) | Report 008 used Uemura only for a definition; initiality and its scope were not assessed | Do existing general type-theory frameworks already give "foundation = finite schema presentation with initial semantics" for the controls? What do they leave out (justification, identity beyond judgmental equality, cross-theory fidelity)? | Medium-high. May show the L1 part is settled and redundant | Classical, linear and cyclic controls may not fit |
| **5** | **DD5: proof-structure-preserving cross-foundation morphisms** (institutions with proofs: Meseguer, Diaconescu, Fiadeiro–Sernadas; MMT / LATIN; Dedukti / Logipedia claims; interpretability hierarchy) | Earlier reports examined frameworks for *representation*; none asked whether any established morphism notion preserves proof identity | Does any established notion of morphism between logics preserve and reflect proof identity, or only theorems? | Medium-high. Decides the feasibility of "across foundations" | Goguen–Burstall and Diaconescu originals NA |
| 6 (optional) | **DD6: obstruction templates** (Lafont parity; Moller / Aceto; Squier; CGT) | Not studied | Can these templates produce an obstruction for a *proof* calculus in the control suite? | Medium | — |

**Sequencing.**
- DD1, DD2 and DD3 are independent: different traditions, separate sessions under the protocol.
- DD4 and DD5 depend on DD3's answer about identity.
- Synthesis (SYN-01) should compare DD1–DD3 against formulations F1–F6.

---

## 9. Limitations

- Many originals were **not accessed**: Belnap; Avron–Lev; Goguen–Burstall; Diaconescu; Lambek–Scott; Seely; Statman; Orevkov; Moller; Clavel–Meseguer; Tarski–Givant; Power; Kelly. Full lists are in the notes. Statements from these are S or M and marked as such.
- Several 2025–2026 preprints were relied on only for context. They are flagged as unrefereed: Stoltz; Stoltz–Vilmart; Paquet–Winskel; Enayat corrigendum.
- "Investigated" means that decisive primary results were read, not that the field was exhausted.
- This review does not declare the map complete (§5, last row).
- **An independent red-team review of this inventory and its priorities is still required by the S1 gate** (`RESEARCH_PLAN.md`). The fresh critique in §11 is an internal check, not that review.

## 10. Proposed changes to `research/LANDSCAPE.md`

These are applied in this PR as an **appended, clearly marked "Proposed additions (review 011)" section**. The seed table is not modified. Summary:
- add the missing families of Q2;
- update the coverage states per §5;
- mark Wolfram multiway and Langlands as "investigated enough to deprioritise";
- add the layer view (§2) as an organising axis.

## 11. Changes after the fresh critique

(Filled in after review.)
