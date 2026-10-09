# Review 011: S1 landscape audit and missing prior art (Task 009)

**Assignment:** `tasks/009-landscape-audit.md` (MAP-01). Baseline: main `22dd02fc4f320b3d93d0e44b1d705c042f3fa626`.

**Author / date:** Claude (Claude Code session), 2026-10-09. **Revision 2:** after a fresh-context adversarial critique (§12; critique preserved in `011-source-notes/fresh-critique.md`).

**Role:** landscape agent (`research/OPERATING_PROTOCOL.md`). This review does not:
- design an algebra;
- freeze a conjecture;
- declare the map complete;
- edit the canonical plan.

Proposed changes to `research/LANDSCAPE.md` are an appended, clearly marked section of that file. The seed table itself is untouched.

### Method

- Five parallel source passes (clusters A–E) using the comparison rubric. The notes are in `research/reviews/011-source-notes/{A,B,C,D,E}.md`; each claim carries a status and a location.
- The fresh critique re-fetched four primary texts (Avron–Zamansky, Andréka–Németi, Guiraud 2006, CGT08).
- It also resolved 15 cited arXiv identifiers, including all 2025–26 preprints, against the arXiv API. No fabricated references were found.
- I re-checked the decisive passages myself:
  - Guiraud 2006 abstract;
  - Andréka–Németi Thm 2.1;
  - Polygraphs book Thm 8.2.4;
  - Avron–Zamansky Thm 4.7;
  - Došen's preorder passage;
  - Heijltjes–Houston Thm 9.1;
  - Lafont Thm 10.

### Status labels

| Label | Meaning |
|---|---|
| **V** | Statement read in a primary text this session or in a cited prior ProofBasis note |
| **S** | Secondary source only |
| **M** | Memory, unverified |
| **NA** | Not accessed |
| **INF** | My inference |

Prior ProofBasis reports are evidence, not authority. Where this review overlaps them, §0 says so.

---

## 0. Relation to prior ProofBasis reports (what is actually new here)

The first draft of this review claimed that several families were "never engaged". **That was false**, and the critique was right. Corrected inventory:

| Topic | Already in the repo | What 011 adds |
|---|---|---|
| Polygraphs book: Squier, S₁ (Thm 8.2.4), §10.4 infinitely many critical branchings | 001 notes `adequacy-levels-translations.md` §S6a; report 010 (FDT invariance, Kapur–Narendran) | Thms 7.3.5, 8.1.2, 8.2.1, 9.3.4, 9.3.15, 13.4.8; undecidability (§4.2.7); Guiraud–Malbos Thm 4.3.9; use as a *classification and obstruction* method rather than a single counterexample |
| **Guiraud 2006, "The three dimensions of proofs"** | Not cited (Guiraud appears only as a co-author of the book) | **New.** Direct prior art for a finite polygraphic presentation of proofs modulo a stated identity |
| Joyal collapse; Heijltjes–Houston; Lafont non-generation; Straßburger; Hughes | 001 notes `proof-identity.md`; 001-review §2 (classified as impossibility-under-hypotheses, intractability, analogy) | Došen's normalisation-versus-generality divergence (§4); maximality; Selinger Cor 3.8 |
| **LSR fibrational framework, adjoint logic, MTT, Shulman LNL polycategories, Laurent polarised semantics** | 001-review §5: the closest active programme. It names **LSR Conj 8.5 ("Completeness of Permutative Equality")** as the "single discriminating next test"; 002 also cites it | Nothing new in content. 011 re-ranks it as the **first** deep dive (§8, DD0), because the repo never executed that test |
| Uemura; Kaposi–Xie (linear and modal theories not definable as SOGATs) | 001-review l.125–127; 008 | Ahrens–Hirschowitz–Lafont–Maggesi presentable⇒representable; Arkor–McDermott; Brunerie et al. initiality |
| Admissible rules (Rybakov, Iemhoff); Jeřábek translations | 002 | Jeřábek 2007 complexity (coNEXP vs PSPACE) |
| Clones / Lawvere theories / Tietze | 010 | Leinster: the doctrine (operad vs clone) encodes the structural rules |
| Logical frameworks (Dedukti, LF, Isabelle, Metamath) | 001–003 | Dedukti Thms 21/23/33 scope; Metamath's single rule |
| **Canonical Gentzen systems (Avron–Lev / Avron–Zamansky), CGT analytic hierarchy, display logic** | Absent (grep) | **New** |
| **Tarski–Givant / Andréka–Németi; abstract algebraic logic** | Absent | **New** (as an L0 boundary) |
| **Combinatory and illative logic** | Absent | **New** (precedent and warning) |
| **Process-algebra finite axiomatisability (Moller, Aceto et al.)** | Absent | **New** |
| **Interpretability, sameness of theories, tightness; fibring** | Absent | **New** |
| **Binding-aware 2-dimensional rewriting (Hirschowitz 2013; reduction monads)** | Absent | **New, but only partly read** (§3.4) |

---

## 1. Executive summary

1. **Seven distinct questions are in play** (§2):
   - L0 computation / derivability;
   - L1 generation of syntax with binding;
   - L2 justification of rules;
   - L3 proof identity;
   - L4 higher-dimensional transformations;
   - L5 cross-foundation translation;
   - L6 causality.

   Any novelty claim must name its layer.
2. **At L0 a finite basis is known and cheap.**
   - Andréka–Németi Thm 2.1 (V): a recursive Tr with ZF ⊨ φ iff Tr(ZF) ⊢_d Tr(φ). Here ⊢_d is a finite Hilbert-style calculus for 3-variable logic, and **Tr(ZF) is an infinite recursive premise set**. The abstract's equivalent form uses Df₃, an equational setting.
   - Metamath has one substitution rule (V). Other frameworks are provability-adequate (V).
   - **A derivability-only reading of the north star is pre-empted.** That is consistent with the charter, which already excludes it.
3. **At L1, finite schema presentations with initial semantics exist for structural dependent type theories** (Uemura Thm 6.10, bi-initial, V). They do **not** exist for linear or modal ones by these methods (Kaposi–Xie, via 001-review, V).
   - Bauer–Haselwarter–Lumsdaine give a *definition* with metatheorems. **They do not prove initiality** (B4, V).
   - L1 is therefore **partly settled**, not settled.
4. **At L3, finite presentations of proofs with a declared identity exist one logic at a time.**
   - Free *-autonomous categories for MLL (V). Control categories for λμ (Selinger, V).
   - Guiraud 2006 (V): a finite 3-polygraph. Formulas are 2-cells and **inference rules are 3-cells**. "The free 3-category generated by this 3-polygraph describes the proofs of classical propositional logic modulo structural bureaucracy."
   - Guiraud's identity is **only "structural bureaucracy"**: reordering independent rule applications, realised by the interchange law. It is **not** βη or generality identity. Proof transformations would be 4-cells, which he treats only informally (§5).
   - Free CCC ↔ NJ(→, ∧, ⊤) βη is standard, but **M this session**: Lambek–Scott and Seely were not accessed. Sums and ⊥ need separate treatment.
5. **The closest active programme to the objective is not new to ProofBasis.** It is LSR / adjoint logic / MTT / Shulman (001-review §5):
   - a fixed generic framework;
   - per-logic structural data;
   - an **open, published proof-identity conjecture** (LSR Conj 8.5).

   The repo identified it as the discriminating test and never pursued it. **This review's main prioritisation change is to put it first (DD0).**
6. **Presentation-invariant obstruction theory exists and is under-used.**
   - FDT is Tietze-invariant (Thm 8.1.2, V).
   - Squier's S₁ has a decidable word problem but no FDT (Thm 8.2.4, V).
   - Existence of a finite convergent presentation is undecidable (§4.2.7, V).
   - At dimension ≥ 3, finite convergent does **not** imply FDT (Guiraud–Malbos Thm 4.3.9, V).
   - Equational analogues: McKenzie's undecidability of the finite basis property for finite algebras, and the Lyndon / Murskiĭ / Perkins examples (**M**, flagged as a gap).
   - These are **monoid / category / algebra** results. Transferring them to proof identity is **INF** until shown for a proof calculus.
7. **Justification (L2) has decidable criteria, but only inside fixed structural settings.**
   - Avron–Zamansky Thm 4.7 (V): for canonical calculi with k ∈ {0,1}, coherent ⇔ strongly characteristic 2Nmatrix ⇔ **strong** cut-elimination.
   - Standard cut-elimination does **not** imply coherence (calculus G₀, §4, V). Coherence is decidable (Prop 2.10, V).
   - CGT08 (V) work over FLe. Axioms in N₂ become equivalent structural rules (Thm 4.2), which preserve cut-elimination under an acyclicity condition or with weakening.
   - Limits (V): Cor 7.2 (over LJ, a structural rule is either derivable or trivialising) and Ex 7.4 (Łukasiewicz).
   - **No source gives "a finite rule set is justified iff a decidable condition holds" in general.** Equating "justified" with "coherent" is INF.
8. **Proof identity is plural, and the charter already says so** (requirement 5: "explicitly chosen notion(s)"). What the literature adds:
   - normalisation- and generality-based identity diverge (Došen §4, V);
   - the classical collapse holds under specific hypotheses (Joyal: natural ¬¬-elimination with initial ⊥ in a CCC; Selinger Cor 3.8: bifunctorial ⅋), and Laurent's polarised semantics avoids it (001-review, V);
   - Boolean categories have no canonical axiomatisation (Straßburger, V).

   **Every L3 result surveyed is propositional.** First-order proof identity (expansion trees, first-order combinatorial proofs, hyperdoctrines) is a recorded gap.
9. **Cross-foundation comparison (L5) is mature at theorem level.**
   - Institutions and general logics leave proof structure as a parameter (Meseguer Def 12, V).
   - Interpretability / sameness hierarchies separate (Barrett–Halvorson Thm 5.2, V).
   - Fibring is non-modular (Caleiro–Marcelino–Marcos Thm 4.1, V).

   Some *specific* translations do preserve identity: Selinger's cbn/cbv duality and CPS; the LF bijection on canonical forms; Dedukti up to βηΣ (Lemma 32). I found **no general framework-level morphism notion** that preserves and reflects proof identity. That is a search result, not a theorem. Mossakowski–Diaconescu–Tarlecki on logic translations was not accessed.
10. **Portfolio (§8):**
    - **DD0** LSR Conj 8.5 reconciliation;
    - **DD3** identity notions for the controls (narrowed);
    - **DD1** polygraphs and binding-aware 2-dimensional rewriting, parametrised by DD3;
    - **DD6** finite-basis obstruction theory (McKenzie, Squier);
    - **DD2** justification theory, only after the originals are accessed;
    - **DD5** logic-translation theory.

    DD4 (type-theory presentations) is folded into a scope note.

    Wolfram multiway, Langlands, e-graphs, and further L0 or framework surveys are not recommended.

---

## 2. The landscape as a layered map

| Layer | Question | Families | State of the art (status) |
|---|---|---|---|
| **L0** computation / derivability | Finite device deriving exactly the theorems? | Universal machines, Kleene normal form; Craig; Cook–Reckhow; rewriting-logic universal theory; Tarski–Givant; frameworks at provability level | **Yes for r.e. theories** (V/S). Negative control only |
| **L1** syntax with binding | Finite data presenting syntax and judgments | Clones / Lawvere, operads / PROPs / polycategories, second-order algebra (Fiore et al., Hirschowitz–Maggesi, Arkor–McDermott), GAT / CwF / Uemura / BHL / SOGAT, polynomial functors, combinatory logic | **Partly settled**: structural dependent type theories (Uemura); linear and modal open (Kaposi–Xie). The doctrine choice encodes the structural rules (Leinster, V) |
| **L2** justification | When does a finite rule set define a meaningful operation? | PTS / harmony; canonical systems; CGT hierarchy; display logic; admissible rules; logicality; AAL | Decidable criteria in **fixed structural settings** (V); harmony incomplete or unsafe (S/V); IPC admissible rules have no finite basis (S) |
| **L3** proof identity | When are two proofs the same; finite presentation modulo identity? | Došen general proof theory; categorical proof theory (CCC, *-autonomous, control, Boolean categories, polycategories, Cockett–Seely); proof nets; combinatorial proofs; focusing; game semantics, GoI, relational injectivity; **generic frameworks (LSR / adjoint / MTT / Shulman)** | Per-logic presentations exist, **propositionally**. Identity criteria diverge. Generic-framework faithfulness is an open conjecture (LSR 8.5) |
| **L4** higher transformations | Finite presentation of transformations and their coherence | Polygraphs, Squier / FDT / homology, coherence theorems, string diagrams, higher-order rewriting in 2-categories, HoTT / cubical, directed type theory | Presentation-invariant invariants with negative instances (V). Binding-aware 2-dimensional semantics exists (Hirschowitz 2013 Thm 4.2, V); FDT-type invariants for it are **unknown** |
| **L5** cross-foundation | Relating foundations while preserving something | Institutions, general logics, MMT / LATIN, Dedukti / Logipedia, logic-translation theory, fibring, interpretability / tightness, reverse mathematics, ordinal analysis | **Theorem-level mature; proof-level only per translation** |
| **L6** causality | Dependency, independence, conflict | Event structures, traces, Petri nets, Lévy residuals, concurrent games, session types, process algebra | Rich. Deferred under reconciliation decision **D5** (H_causal) |
| Analogies | — | Wolfram multiway; Langlands | Not technical prior art (§3.5) |

**Open territory (INF).** The charter's conjunction is roughly L1 (binding) ∧ L2 ∧ L3/L4 ∧ L5, with L6 deferred under D5. Each conjunct has mature mathematics. **The LSR programme is the only one surveyed that attacks L1 ∧ L3 ∧ L5 together.** It leaves L2 implicit (connectives are justified by universal properties) and classical non-linear logic open.

---

## 3. Family-by-family assessment (comparison rubric, condensed)

Rel: **P** = direct prior art; **Adj** = adjacent structure; **An** = methodological analogy; **Sp** = speculative. Evidence locations are in the notes, keyed by cluster and item (e.g. A6, B3).

### 3.1 Proof theory (A) and generic frameworks

| Family | Key result (status) | Limit | Rel | Deep dive |
|---|---|---|---|---|
| **LSR / adjoint logic / MTT / Shulman** (001-review) | A fixed generic framework instantiated by mode theories or doctrines. MTT canonicity (Gratzer et al., V via 001-review). Shulman covers classical *linear* logic (V via 001-review) | **Conj 8.5 open**. LK not native. Undecidable mode theories may reintroduce vacuity (INF, 001-review) | **P (closest)** | **DD0** |
| Identity of proofs (Došen) | Normalisation vs generality agree only on limited fragments (§4, V). Preorder collapse under the stated hypotheses (§5, V). CCC maximality (V); BCC maximality open as of 2004 (status not updated, NA) | No foundation-neutral criterion known | P | DD3 |
| Categorical proof theory | *-autonomous ↔ MLL (V); control categories ↔ λμ, collapse iff ⅋ bifunctorial (Selinger Cor 3.8, V); Laurent polarised faithfulness (001-review, V); free CCC ↔ NJ βη (**M**) | Classical identity requires choices; propositional only | P | DD3 |
| Deep inference | SKS local rules (Brünnler, V); locality depends on the representation (§3.5, V) | Quantifiers lose locality (S) | P | via DD1 |
| Proof nets / complexity | MLL **with units** equivalence is PSPACE-complete (Heijltjes–Houston Thm 9.1, V; already 001) | Intractability, not impossibility | P | — |
| Focusing | Maximal multifocusing ↔ MLL proof nets (Chaudhuri–Miller–Saurin Thm 16, V) | Per logic | Adj | — |
| Game semantics / GoI / relational | Full completeness for MLL + MIX (Abramsky–Jagadeesan, V); relational injectivity for MELL (001-review, V); GoI / ludics **NA** | Per logic | Adj | DD3 if needed |
| Canonical systems | Thm 4.7 (k∈{0,1}): coherent ⇔ strongly characteristic 2Nmatrix ⇔ strong cut-elimination; G₀ counterexample; coherence decidable (Prop 2.10). All V (Avron–Zamansky); Avron–Lev original NA | Fixed LK structural layer; no identity | P | DD2 |
| CGT hierarchy | Over FLe: N₂ axioms ≡ structural rules (Thm 4.2); P₃ ≡ hyperstructural rules (Thm 5.6); Cor 7.2; Ex 7.4. All V | Conditions on cut-elimination; bounded class | P | DD2 |
| Display logic | Belnap C1–C8 (**M**); Kracht (NA) | — | P | DD2 (after access) |
| Complete linear bases | No polynomial-time complete linear TRS for Boolean logic **unless coNP = NP** (Das–Straßburger, V) | Conditional | P (negative) | DD6 |
| Combinatorial proofs | Sound, complete, polynomial-time checkable; first-order version 1906.11236 (V) | Identity candidate only | Adj | DD3 |
| First-order proof identity (expansion trees, proof forests, hyperdoctrines) | **NA**: gap | — | Adj | DD3 |

### 3.2 Algebra and type-theoretic structure (B)

| Family | Key result (status) | Limit | Rel | Deep dive |
|---|---|---|---|---|
| Clones / Lawvere | Already covered (010) | No binding; generators not invariant | Adj | done |
| Operads / PROPs / polycategories | Plain operads ↔ strongly regular theories (Leinster, V); composite PROPs (Lack Thm 4.6, V); polycategories / Cockett–Seely **NA** | Doctrine is a parameter | Adj | in DD1 |
| Finite complete PROP presentations | Lafont F[2] (Thm 10, V); reversible circuits not finitely generated (already 001, rated an analogy); Bonchi–Sobociński–Zanasi Thm 6.4 (V); ZX completeness (V; 2026 minimality preprints unrefereed) | Complete relative to a **fixed semantics** | P (method) | template |
| Algebra with binding | Fiore–Hur (abstract V); Hirschowitz–Maggesi Thms 2–3 (V); Ahrens–Hirschowitz–Lafont–Maggesi Thm 6.3, Non-ex 5.5 (V); Arkor–McDermott Prop 24 (V) | Syntax and reduction, not identity in general | P (L1) | scope note |
| Type theories as presentations | Uemura Thm 6.10 (V); BHL definitions (V, **no initiality**); MLTT initiality in Agda (Brunerie et al., slides V); Kaposi–Xie limit (001-review) | Linear and modal excluded; identity = judgmental equality | P | scope note |
| Combinatory logic | Combinatory completeness (Selinger Thm 5.1, V); λβ needs extra axioms (§5.4, V); illative CL and Curry's paradox (S) | Computation basis ≠ logic basis | P (precedent) | — |
| Tarski–Givant / algebraic logic | Andréka–Németi Thm 2.1 as in §1.2 (V); Monk (S); AAL (S) | Derivability only | P (L0 boundary) | — |
| Equational finite-basis problem | Tarski's problem; McKenzie 1996; Lyndon, Murskiĭ, Perkins (**M**, gap) | — | P (obstruction theory) | DD6 |

### 3.3 Justification, frameworks, cross-foundation (C)

| Family | Key result (status) | Limit | Rel | Deep dive |
|---|---|---|---|---|
| PTS / harmony | IPC incompleteness of PTS variants (S); Sandqvist's nonstandard ∨ clause (S); Prawitz conjecture open (S); naive comprehension harmonious yet paradoxical (SEP, V) | Not safe as a sole criterion | P | DD2 |
| Admissible rules | No finite basis for IPC (Rybakov, S; in 002); coNEXP vs PSPACE (Jeřábek 2007, V) | Derivable ≠ admissible | P | DD2 |
| Logical frameworks | Dedukti Thms 21/23/33, Lemma 32 (V); Isabelle/Pure (V); Metamath (V) | Provability-level; declared trusted rules | P | — |
| MMT / institutions / general logics | Rabe Thm 2.31 (V); Meseguer Def 12 (V); Goguen–Burstall, Diaconescu NA | Proof structure is a parameter; colimits as logic combination already exist (Rabe, V) | P | DD5 |
| Logic-translation theory | Mossakowski–Diaconescu–Tarlecki (**M**, gap) | — | P | DD5 |
| Fibring | Non-modular (Caleiro–Marcelino–Marcos Thm 4.1, V) | — | Adj (negative) | DD5 |
| Interpretability / sameness / tightness | Barrett–Halvorson Thm 5.2; Friedman–Visser 2025; Visser; Enayat (2026 corrigendum leaves KM open). All V | Theorem-level | Adj | DD5 |
| Reverse mathematics / ordinal analysis | Big Five (S); reductions map proofs primitive-recursively (SEP, V) | Strength, not structure | An | — |
| Realizability | Krivine: instructions grow with axioms (introductory remark, V; **not a theorem**) | — | An | — |
| Logicality | McGee (S) | Infinitary | An | — |

### 3.4 Higher-dimensional structure (D)

| Family | Key result (status) | Limit | Rel | Deep dive |
|---|---|---|---|---|
| Polygraphs / Squier | Thms 7.3.5, 8.1.2, 8.2.1, 8.2.4, 9.3.4, 9.3.15, 13.4.8; §4.2.7; §10.4. All V; partly already 001/010 | Results are about **2-polygraphs (monoids / categories)** | P | DD1 / DD6 |
| Guiraud 2006 | As in §1.4 (V): Thm 2.4.3 provability correspondence; Thm 3.3.1 bureaucracy ↔ exchange relations | Propositional; identity = bureaucracy only; transformations informal | **P** | DD1 |
| Dimension ≥ 3 | Infinitely many critical branchings (V); finite convergent does not imply FDT (Guiraud–Malbos Thm 4.3.9, V) | Squier does not lift | P (negative) | DD1 |
| Higher-order rewriting in 2-categories | Hirschowitz 2013 Thm 4.2: sound and complete cartesian-closed 2-categorical semantics of permutation equivalence for higher-order rewriting (V, notes E1/E2). Reduction monads (downloaded, **not read**). Seely 1987, Hilken, Hamana, explicit substitutions, Melliès's λσ counterexample (**M/NA**) | **Directly addresses the binding gap**; whether finiteness invariants exist there is unknown | P | DD1 |
| "No binding in the Polygraphs book" | Text search found none (**INF**, not exhaustive) | — | — | DD1 |
| Coherence theorems | Joyal–Street via the Selinger survey Thm 3.1 (V); coherence via convergent rewriting (V) | Structural identity only | Adj | DD1 / DD3 |
| HoTT / cubical | HoTT book facts (V); Lumsdaine (V); Coquand–Huber–Sattler; Sterling–Angiuli (V) | Foundation-specific identity tower | Adj | narrow, in DD3 |
| Directed type theory | Licata–Harper, Riehl–Shulman (V titles and abstracts) | — | Adj | later |

### 3.5 Computation, causality, deduction, analogies (E)

| Family | Key result (status) | Rel | Deep dive |
|---|---|---|---|
| Event structures / games | Copycat-as-identity forces receptivity and innocence (Winskel notes, V); multiple identity notions (2026 preprint, unrefereed) | Adj | deferred (D5) |
| Lévy residuals / optimal reduction | NA | Adj | deferred (D5) |
| Session types | Caires–Pfenning; Wadler (V) | Adj | — |
| Rewriting logic | Reflective universal theory (V) | negative control | — |
| E-graphs | egg (V); binding extensions exist in later work (M) | An | — |
| Automated deduction | Saturation framework, Isabelle AFP (V, formally checked there) | Adj | — |
| Proof complexity | Frege p-equivalence (S). p-simulation is an **invariance** phenomenon, not an obstruction | An | — |
| Process-algebra axiomatisability | Moller (S); Aceto et al. Thms 1–2 under their Assumptions 1–3 (V) | P (negative template) | DD6 |
| Wolfram multiway | Arsiwalla–Gorard–Elshatlawy Prop 3.1 is an example; Prop 3.3 assumes the homotopy hypothesis (V). "Subsumed by polygraphs" is **INF** | Sp | **No** |
| Langlands | Langlands' 2011 lectures, self-described informal (V) | An | **No** |

---

## 4. Answers to the seven required questions

### Q1. Indispensable traditions

1. **Structural, general and categorical proof theory, including the generic-framework programme (LSR / adjoint / MTT / Shulman).** The only traditions that define proof identity, and the only programme pursuing a fixed generic basis across logics with an identity conjecture.
2. **Higher-dimensional rewriting (polygraphs, Squier theory) and higher-order rewriting semantics.** Presentation-invariant finiteness and obstruction theory for identities between derivations.
3. **Algebraic theories with binding and type-theoretic semantics.** To state what is presented. Partly settled; linear and modal are open.
4. **Justification theory** (canonical systems, CGT, display, PTS, admissibility). The only mathematical handle on "explanatory".
5. **Logic-translation theory** (institutions, general logics, translation theory, interpretability). To state "across foundations".
6. **Computability** as a boundary only.

### Q2. Overlooked traditions

Overlooked by the **whole repo**, verified absent by grep:
- canonical Gentzen systems and coherence;
- the CGT analytic hierarchy;
- display logic;
- Guiraud 2006;
- Tarski–Givant and Andréka–Németi;
- abstract algebraic logic;
- combinatory and illative logic;
- process-algebra finite axiomatisability;
- interpretability, sameness of theories, tightness;
- fibring and its non-modularity;
- binding-aware 2-dimensional rewriting (Hirschowitz 2013, reduction monads);
- Tarski's finite basis problem and McKenzie (**M**, needs access);
- first-order proof identity;
- logic-translation theory (Mossakowski–Diaconescu–Tarlecki);
- logicality;
- realizability's growth remark.

**Present but under-weighted:**
- Squier theory as an obstruction theory, rather than a single counterexample;
- the LSR conjecture as the decisive test;
- Kaposi–Xie's limit on L1.

### Q3. Structures closest to the objective

| Rank | Structure | Why | Gap |
|---|---|---|---|
| 1 | **Generic frameworks: LSR fibrational framework, adjoint logic, MTT, Shulman LNL polycategories** | Fixed generic machinery; per-logic structural data; cut and identity generic; explicit open faithfulness conjecture (Conj 8.5) | LK not native; decidability moves into mode theories; justification implicit |
| 2 | **Free structured categories over doctrines**, with Došen's maximality as a completeness criterion for identity | Per-logic identity with universal properties | Classical non-canonical; propositional |
| 3 | **Polygraphs / higher-order rewriting semantics** | Finite cells, identity as higher cells, invariant finiteness and obstruction theory; Guiraud 2006 instance | Binding open; dimension-3 pathologies; identity only bureaucracy so far |
| 4 | **Type theories as finite schema presentations** | "Foundation = finite presentation + initial semantics" | Linear and modal excluded (Kaposi–Xie); identity = judgmental equality |
| 5 | **Canonical systems / CGT** | Decidable justification inside a fixed structural layer | No identity; bounded classes |
| 6 | **Institutions / general logics** | Indexing by foundations | Proof structure is a parameter |

The first draft ranked polygraphs first. That ignored rank 1, which 001-review had already identified.

### Q4. Assumptions contradicted or weakened

Each row targets what the repo actually holds. Earlier draft rows that attacked positions the charter does not hold have been removed (see §12).

| Repo position | Evidence | Effect |
|---|---|---|
| Earlier S1 framing (LANDSCAPE) rated polygraphs and HoTT "thin" and Wolfram "seed", as though open | Polygraphs and Squier were engaged in 001/010; Wolfram is subsumed (INF) | **Corrected:** the map was already partly covered; Wolfram deprioritised |
| Stage-0.7 work treated non-vacuity mainly as anti-interpreter syntax (N_split, N_rep, N_amb) | Canonical-system coherence, CGT, FDT and maximality are *positive* structural criteria not based on excluding interpreters | **Reframed:** candidate non-vacuity criteria exist in L2–L4 literature (INF that they apply) |
| Charter req. 1: "fixed finite primitives" | Locality depends on the representation (Brünnler, V); bases depend on the signature (Aceto et al., V); bases depend on the doctrine (Leinster, V); IPC admissible rules have no finite basis (S); McGee is infinitary (S) | **Weakened:** finiteness must be stated relative to representation, signature, doctrine and the derivable / admissible distinction |
| 001-review's narrowed target C\*\* (fixed G + class 𝒦) as the next test | Never executed; nothing in 002–010 or research/ addresses Conj 8.5 | **Still the strongest single test.** Re-prioritised as DD0 |
| Use of harmony as the default justification notion (002, 008) | PTS incompleteness; comprehension; canonical-system alternatives | **Weakened** |
| Task 010 strategy option (f) relational/multiway | Multiway adds no theorems beyond polygraphs (INF from E3) | **Weakened** |

### Q5. Deep dives

See §8.

### Q6. Directions unlikely to justify significant investment

| Direction | Reason |
|---|---|
| Wolfram multiway / ruliad | No theorems beyond example level, and those conditional on the homotopy hypothesis (V). Content reachable via DD1 (INF) |
| Langlands | Analogy only (V) |
| Further L0 computability and framework-universality surveys | Settled (V) |
| E-graphs | Engineering; no bearing on identity or justification |
| Realizability, reverse mathematics, ordinal analysis | Measure strength or computational content. Narrow exception: ordinal and termination methods for proof transformations (M), relevant only if DD1 needs termination of 3-cells |
| Full HoTT / cubical programme | Only the judgmental-vs-propositional identity design choice matters; absorbed into DD3 |
| L6 causality | Deferred by **D5**, not dismissed |

### Q7. Alternative formulations

Task 010 already lists strategic options (a)–(g): finite algebra; universal property; family or hierarchy; institution or fibration; higher-dimensional; relational or multiway; impossibility or classification. The formulations below are **refinements of those options, not new ones**, with vacuity checks.

| ID | Formulation | Task 010 option | Vacuity / ill-posedness check |
|---|---|---|---|
| F1 | For a declared proof category with declared identity, decide whether it has a finite coherent polygraphic presentation, then classify foundations by such invariants | (e) | **Ill-posed as stated** for calculi with binding or schema-indexed infinitely many objects: FDT is defined for 2-polygraphs. Needs DD1 to supply a binding-aware notion |
| F2 | Fixed finite stock of doctrine-forming constructions from which every foundation's proof doctrine arises | (b)/(c) | If the stock may grow per foundation: **vacuous**. If fixed: **it is the LSR / MTT programme** (prior art). Presentations of 2-monads (Kelly–Power, M) are the vacuity test |
| F3 | Classify finite rule schemas that are justified, with closure and limits | new emphasis | Already **negative** for natural classes (CGT Cor 7.2, Ex 7.4). Useful as a classification, not a universality claim |
| F4 | Indexed family of foundations with proof-structure-preserving morphisms; universality as initial or colimit objects | (d) | The initial object is trivial, and colimits as combination already exist (Rabe). **The content lies only in the morphism notion** (DD5) |
| F5 | Obstruction programme: presentation-invariant obstructions to finite bases for proof structure (FDT, homology, McKenzie-type undecidability, Moller-type non-axiomatisability, parity) | (g) | p-simulation removed (an invariance result, not an obstruction). Transfer to proofs is INF |
| F6 | Canonical identity per foundation (maximality), then preservation by translations | new emphasis | A maximal consistent identity **need not be unique** (INF). Must be "a declared maximal identity" |

---

## 5. Coverage matrix

States as in Task 009: **investigated / partial / unknown / deferred.** Every seed row is listed.
- Evidence = note item (cluster and number), or prior report.
- Priority = decision value: would the answer change which formulation or deep dive we pursue?

| Family (seed rows first) | State | Evidence | Priority |
|---|---|---|---|
| Structural proof theory (ND, sequent, focusing, deep inference, cut elimination) | partial | A1–A4; 001 | medium |
| General proof theory / identity of proofs | partial | A6; 001 `proof-identity.md` | **high** (DD3) |
| Categorical logic (CCC, *-autonomous, monoidal, multicategories, doctrines) | partial | A6, B1; Lambek–Scott NA | high (DD3) |
| Universal algebra, clones, Lawvere | investigated | 010 | done |
| Many-sorted / second-order algebra, binding, contextual categories | partial | B3, B4; 001-review | medium (scope note) |
| Proof-theoretic semantics / harmony | partial | C1; 002, 008 | medium (DD2) |
| Logical frameworks (LF, LLF / CLF, Dedukti, MMT, FPC) | investigated (LLF / CLF NA this session) | C3; 001–003 | done |
| General logics, institutions, fibrations, equipment | partial | C4; Goguen–Burstall NA | medium (DD5) |
| Polygraphs, computads, rewriting modulo, coherence | partial | D3, D4, D6; 001 S6a; 010 | **high** (DD1, DD6) |
| HoTT / univalent / cubical | partial | D1, D2 | low (narrow) |
| Rewriting logic, term-graph rewriting, e-graphs | partial (term-graph rewriting NA) | E2, E6 | low |
| Concurrency (event structures, Petri nets, traces) | deferred (D5) | E1 | deferred |
| Automated deduction / proof complexity | partial | E4, E5 | low |
| Model theory, proof-relevant semantics | **unknown** this session | — | medium (affects DD3) |
| Computability, universal machines, incompleteness | investigated | E6; 001–006 | done |
| Operads, PROPs, polycategories, double categories | partial (polycategories via 001-review; double categories NA) | B1, B2 | medium |
| Type theory, logical relations, parametricity, effect modalities | partial (parametricity NA) | B4; 001-review | low-medium |
| Homological analogies / rewrite invariants | partial | D6 | in DD1 / DD6 |
| Wolfram multiway | investigated enough | E3 | **not pursued** |
| Langlands | investigated enough | E7 | **not pursued** |
| *New:* generic frameworks (LSR, adjoint, MTT, Shulman) | partial (001-review) | 001-review §5 | **highest** (DD0) |
| *New:* canonical systems / CGT / display | partial (originals NA) | A8a–A8c | medium-high (DD2) |
| *New:* Guiraud 2006 | partial | D3 | high (DD1) |
| *New:* binding-aware 2-dimensional rewriting | partial | E1 (Hirschowitz 2013); B3 | high (DD1) |
| *New:* finite complete PROP presentations | partial | B2 | medium (template) |
| *New:* Tarski–Givant / AAL | partial | B8, B9 | low (boundary) |
| *New:* combinatory and illative logic | partial | B7 | low (lesson) |
| *New:* Tarski finite basis / McKenzie | unknown (M) | — | **high** (DD6) |
| *New:* admissible-rule bases | partial | C2; 002 | medium |
| *New:* process-algebra axiomatisability | partial | E8 | medium (DD6) |
| *New:* logic-translation theory | unknown (M) | — | medium (DD5) |
| *New:* interpretability / sameness / tightness | partial | C5 | low-medium |
| *New:* fibring | partial | C4 | low-medium |
| *New:* first-order proof identity, hyperdoctrines | unknown | — | **high** (DD3) |
| *New:* reverse mathematics, ordinal analysis, realizability, logicality | deferred | C5–C7 | low |
| *New:* GoI, ludics, transcendental syntax | unknown | — | low-medium |
| *New:* Hilbert's 24th problem, light logics, proof mining, directed type theory | unknown | — | low |

**The map is not complete.** The "unknown" rows are the next landscape pass.

---

## 6. Strongest negative evidence (with exact scope)

1. **Squier S₁** (Thm 8.2.4, V): a monoid with decidable word problem and no FDT. *Scope:* monoids. Transfer to proof categories is INF.
2. **Finite convergent presentability is undecidable** (§4.2.7, V). *Scope:* as stated in the book, for monoid presentations.
3. **Dimension ≥ 3:** finite convergent does not imply FDT (Guiraud–Malbos Thm 4.3.9, V). This is the dimension where Guiraud's proof presentation lives.
4. **Classical collapse** under its hypotheses (Došen §5; Selinger Cor 3.8; V). Avoided in polarised semantics (Laurent, via 001-review, V).
5. **Normalisation ≠ generality** (Došen §4, V).
6. **CGT Cor 7.2 / Ex 7.4** (V): limits of structural-rule bases over LJ and for Łukasiewicz.
7. **Lafont** (V): reversible circuits are not finitely generated. *Scope:* one category. Already 001; an analogy.
8. **Moller (S); Aceto et al. Thms 1–2 under Assumptions 1–3 (V):** signature-dependent non-axiomatisability.
9. **IPC admissible rules have no finite basis** (S).
10. **Heijltjes–Houston** (MLL with units, PSPACE-complete, V). **Das–Straßburger** (no polynomial-time complete linear TRS *unless coNP = NP*, V).
11. **Fibring is non-modular** (V).
12. Krivine's remark that realizers grow with axioms: an introductory remark (V), **not a theorem**.

---

## 7. North-star red team (Task 009 item 5)

North star (RESEARCH_PLAN): "whether the structural machinery of mathematical proving admits a **finite, mathematically explanatory generative basis** spanning meaningfully different mathematical foundations".

| Challenge | Evidence | Consequence |
|---|---|---|
| **"Finite" is not a stable property** | Representation (Brünnler), signature (Aceto et al.), doctrine (Leinster), schemas (every type-theory framework), derivable vs admissible (Rybakov). McGee's logicality is infinitary | The north star needs a declared notion of presentation. Without it, "finite" is satisfiable trivially (L0) or refutable trivially (wrong signature) |
| **"Explanatory" has no mathematical definition** | The only candidate mathematical proxies are L2 criteria (coherence, analyticity, harmony) and L3 criteria (maximality, universal properties). None is general | Either adopt a proxy explicitly, or say the property is informal. Silently using one is a risk |
| **"Foundation" may be the wrong index** | For ZF-style foundations, proofs are first-order derivations plus axioms; the proof structure is first-order logic's, not ZF's. Interpretability results compare *theories*, not proof machinery | The index may need to be "logic + structural discipline" (as in LSR mode theories), with foundations as theories over it (INF) |
| **"Spanning" may already be done, or be impossible, depending on identity** | Provability-level spanning: done (L0). Identity-level spanning with one fixed identity: blocked under the collapse hypotheses. With per-foundation identity: LSR Conj 8.5 | The live question is approximately LSR Conj 8.5 extended to classical / first-order / dependent cases |
| **What would stop the programme?** | (i) A proof of Conj 8.5 in a generality covering the charter's controls ⇒ the core question is answered by prior work. (ii) A counterexample to it ⇒ the first genuine obstruction. (iii) A presentation-invariant obstruction (F5) for a control calculus | These are decisive tests; §8 targets them |
| **Missing expertise** (S1 gate) | Higher categories and polygraphs (DD1); proof theory of substructural and modal logics (DD0, DD2); universal algebra and finite-basis theory (DD6) | The owner should seek a domain reviewer for each before S2 decisions |

---

## 8. Prioritised deep-dive portfolio

| Priority | Deep dive | Not already answered because | Bounded question | Depends on | Uncertainty |
|---|---|---|---|---|---|
| **1** | **DD0: LSR Conj 8.5 reconciliation** | 001-review named it the "single discriminating next test"; no later report or task executed it (grep) | What is the current status of Conj 8.5 (any proof or counterexample since publication)? For the smallest case beyond LSR's sketch (ILL with ⊗; S4), does permutative equality coincide with the free-structure identity? Which charter controls fall outside the framework? | — | Post-publication literature not yet searched |
| **2** | **DD3: identity notions for the controls (narrowed)** | 001 catalogued collapse and intractability results. No report compared *criteria* (normalisation, generality, maximality, polarised) across the controls, or at first order | For each control (NJ βη, MLL, classical, first-order), which identity notions are well defined, and do they coincide? | DD0 (shares cases) | First-order identity literature unread |
| **3** | **DD1: polygraphs and binding-aware 2-dimensional rewriting** | 001/010 used Squier for one counterexample; Guiraud 2006 and Hirschowitz 2013 were not engaged | Does a finite polygraphic or 2-categorical presentation exist for the controls modulo the DD3 identities? Is there an FDT-like invariant with binding? | DD3 | Dimension-3 pathologies; binding |
| **4** | **DD6: finite-basis obstruction theory** | Never studied as a theory | Can McKenzie / Squier / Moller-style arguments yield an obstruction for a control proof calculus? | DD1 | McKenzie NA (M) |
| **5** | **DD2: justification theory** | Canonical systems and CGT are absent from the repo | The strongest theorem of the form "rule set justified ⇔ decidable condition" and its limits; its relation to identity. **Prerequisite:** access Avron–Lev, Belnap, Kracht originals | — | Originals NA |
| **6** | **DD5: logic-translation theory with proofs** | Earlier reports studied frameworks for representation, not morphism notions | Does any established morphism notion (Mossakowski–Diaconescu–Tarlecki; proof-theoretic institutions; Meseguer maps) preserve and reflect identity? | DD3 | Sources M/NA |

**Folded:** DD4 (type theories as presentations) becomes a scope note. 001-review and B3/B4 already establish what Uemura, BHL and Kaposi–Xie cover. The one new point is that Kaposi–Xie exclude the linear control.

---

## 9. Limitations

- **Originals not accessed:** Belnap; Avron–Lev; Kracht; Goguen–Burstall; Diaconescu; Mossakowski–Diaconescu–Tarlecki; Lambek–Scott; Seely; Statman; Orevkov; Moller; Clavel–Meseguer; Tarski–Givant; McKenzie; Power; Kelly; Kelly–Power; GoI / ludics; reduction monads (downloaded, unread).
- **Unrefereed 2025–26 preprints are used only for context:** Stoltz; Stoltz–Vilmart; Paquet–Winskel; Enayat corrigendum.
- **No post-publication search for LSR Conj 8.5** has been done. That is DD0's first step.
- The red-team critique (§12) was produced by a fresh-context agent in the same session. **It is not the independent review the S1 gate requires.**

## 10. Proposed LANDSCAPE changes

Appended to `research/LANDSCAPE.md` as "Proposed additions from review 011 (pending owner review)". The seed table is unchanged.

## 11. Bridge to the north star

- Every recommended dive targets one of the decisive tests in §7: the Conj 8.5 outcomes and F5-type obstructions.
- None assumes the universal basis exists.

## 12. Changes after the fresh critique

The critique found 2 blocking, 14 major and 11 minor issues. It is preserved in `011-source-notes/fresh-critique.md`.

| # | Critique finding | Verified? | Change |
|---|---|---|---|
| B1 | "Never engaged" claims false: Squier / S₁, Joyal, Heijltjes–Houston, Lafont, Uemura / Kaposi–Xie, admissible rules were in 001 / 002 / 010 | **Yes** (grep of 001 notes S6a, `proof-identity.md`, 001-review §2, 002) | New §0 delta table; Q2 split into repo-absent vs under-weighted; DD rationales rewritten |
| B2 | LSR / adjoint / MTT / Shulman omitted though 001-review named Conj 8.5 the discriminating test | **Yes** | Added as Q3 rank 1, a §3.1 row, a matrix row, and DD0 (priority 1) |
| M1 | Avron–Zamansky misstated (strong cut-elimination; G₀; Prop 2.10) | Yes (critique's re-fetch) | §1.7 and §3.1 corrected; "justified = coherent" marked INF |
| M2 | Guiraud over-read: rules are 3-cells; identity is bureaucracy only; dimension-3 FDT failure | Yes (abstract plus critique's grep) | §1.4, Q3, F1 corrected |
| M3 | Free CCC ↔ NJ βη labelled V | Yes | Now M, with its fragment stated |
| M4 | L1 "settled"; BHL initiality | Yes (note B4) | "Partly settled"; BHL = definitions; Kaposi–Xie limit |
| M5 | "No binding" as V; Hirschowitz 2013 ignored | Yes | Marked INF; binding-aware row added; DD1 re-scoped |
| M6 | "No framework preserves identity" ignores specific translations | Yes | Scoped to framework-level morphism notions; specific translations listed |
| M7 | Charter misquoted; strawman Q4 rows | Yes (no such phrase in charter, plan or tasks) | Q4 rewritten against actual repo positions |
| M8 | Matrix incomplete; no evidence column; vocabulary mismatched | Yes | Matrix rebuilt with all seed rows, evidence column and Task 009 vocabulary |
| M9 | DD1 depends on DD3 | Yes | Dependency column added |
| M10 | Open territory omitted L1 and L6 | Yes | Restated with D5 |
| M11 | CGT hypotheses dropped | Yes | FLe, acyclicity / weakening stated |
| M12 | §6 mixed kinds; Krivine as theorem; coNP condition dropped | Yes | Scopes added |
| M13 | North star barely red-teamed | Yes | New §7 |
| M14 | F1–F6 flaws; false claim of novelty versus Task 010 | Yes (Task 010 lists (e), (g)) | Q7 rebuilt with vacuity checks and Task 010 mapping |
| minor | Malformed table; "with units"; Andréka–Németi phrasing; Wolfram "contradicted"; e-graph binding remark; proof complexity in F5; §11 placeholder | Yes | Fixed |
| not adopted | Critique's suggestion to treat ordinal analysis as a narrow exception | Partly | Recorded in Q6 as conditional; not a dive |
