# Task 003 — Primary-source notes

Companion to [the structural-fidelity report](003-structural-fidelity.md). Access/reassessment date: 2026-10-08. These notes restate inspected theorem passages, not whole papers. VERIFIED_SOURCE means the statement and relevant hypotheses were recovered from a primary text; it does **not** certify the author's proof. No result here is FORMALIZED. Proposed applications and hand arguments are INFERENCE. Original PDFs are linked rather than redistributed.

## Audit provenance and reading boundary

The coordination base inspected was `62ec35d20336cb541cfc84ba06de8fdf7c7d21a2`. The research inputs were AGENTS.md, README.md, the charter, definitions/conjectures, falsification plan, research protocol, prior art, Stage-0 synthesis, and Task 003. The two audit heads were:

- [PR #1](https://github.com/yzm1/proofbasis/pull/1), `df725ef4c16fedf23c7ad08dce8bee6331061a46`: report and its bibliography/evidence qualifications.
- [PR #2](https://github.com/yzm1/proofbasis/pull/2), `9fa918c45a2f7a9e872ca70bdab4bfa7830fa06d`: original report, all source-note files, `reports/001-review.md`, all review-source-note files, and the subsequent review text on GitHub. The original PR description still contains claims corrected by the self-review; the report must not read that description as the final mathematical assessment.

PR #1 shares authorship/session with this task. The fixture was re-derived and the decisive sources rechecked, but this is not an outside independent review. PR #2's self-review also discloses its relationship to its original report. Source notes from either PR are leads, not substitutes for the primary passages below.

Author manuscripts, reports, and arXiv versions are used where specified; publisher/version differences are not silently reconciled. The reading claim is full repository/review-document reading and **selected primary theorem, definition, and proof passages**, not full reading of every cited book/paper. PDF page numbers below are one-based; printed pages are identified separately when they differ.

## LF fixture: complete administrative evidence

This fills in the report's `κ` shorthand; it is a mathematical signature specification, not a new prover. All schematic parameters below are ordinary explicit LF Π-binders. Use `atom:type`, `pos,neg:atom→fm`, and `ax:Πa:atom. prf [neg a,pos a]`. Thus `axp` abbreviates `ax p`; the family is one finite schema, not infinitely many primitive axioms. Take `p,r,q:atom` as distinct declarations. The list families have these constructors:

```text
take-head : take A (cons A Γ) Γ
take-tail : take A Γ Ω → take A (cons B Γ) (cons B Ω)

weave-empty : weave nil nil nil
weave-left  : weave Γ Δ Ω → weave (cons A Γ) Δ (cons A Ω)
weave-right : weave Γ Δ Ω → weave Γ (cons A Δ) (cons A Ω)
```

Let `H` mean `take-head`, and `T c` mean `take-tail c`, with indices inferred from its displayed judgment. Choose each `weave` by the recorded sequence of `L`/`R` steps, ending in `weave-empty`. Every selection is shown below; the last selection in each row is the rule's conclusion insertion.

| Rule instance | Principal premise selection(s) | Residue/interleaving | Conclusion insertion |
|---|---|---|---|
| inner tensor `i` | `p` from `[p⊥,p]` by `T H`; `r` from `[r⊥,r]` by `T H` | `[p⊥]`, `[r⊥]` → `[p⊥,r⊥]` by `L R` | `P` from `[p⊥,r⊥,P]` by `T(T H)` |
| first par `b₁` | `p⊥` from `[p⊥,r⊥,P]` by `H`; then `r⊥` from `[r⊥,P]` by `H` | `[P]` | `X` from `[X,P]` by `H` |
| first outer tensor `o₁` | `P` from `[X,P]` by `T H`; `q` from `[q⊥,q]` by `T H` | `[X]`, `[q⊥]` → `[X,q⊥]` by `L R` | `T` from `[X,T,q⊥]` by `T H` |
| second outer tensor `o₂` | `P` from `[p⊥,r⊥,P]` by `T(T H)`; `q` from `[q⊥,q]` by `T H` | `[p⊥,r⊥]`, `[q⊥]` → `[p⊥,r⊥,q⊥]` by `L L R` | `T` from `[p⊥,r⊥,T,q⊥]` by `T(T H)` |
| final par `b₂` | `p⊥` from `[p⊥,r⊥,T,q⊥]` by `H`; then `r⊥` from `[r⊥,T,q⊥]` by `H` | `[T,q⊥]` | `X` from `[X,T,q⊥]` by `H` |

The displayed source axiom `⊢q,q⊥` is an unordered context; its LF list representative is `[q⊥,q]`, as above. No LF exchange equation is used. Finite certificates select occurrences, and distinct repeated occurrences have different head/tail evidence. This auxiliary encoding can retain extra list/evidence distinctions; no full adequacy theorem for it is claimed. The two exhibited inhabitants nevertheless have the same target type and different normal heads, which suffices for the preservation counterexample. [INFERENCE]

## S1 — MALL proof nets identify rule commutations

Rob van Glabbeek and Dominic Hughes, *MALL proof nets identify proofs modulo rule commutation*, [arXiv manuscript 1609.04693](https://arxiv.org/pdf/1609.04693). Inspected §§2–4, Tables 2–4, Theorem 1 (p.7), and §§5/9 for cuts. The arXiv PDF was retrieved rather than an inferred journal version.

Theorem 1 quantifies over **two cut-free proofs in MALL without units**: equal translated proof nets iff a series of rule commutations converts one into the other. It holds both with and without MIX. Sequents are occurrence-bearing formula forests; a linking pairs complementary leaf occurrences, and an additive net is a set of linkings obtained by resolving additive conjunctions. In the pure multiplicative fragment there is a single linking. Table 3 includes the tensor/par commutation used by the fixture. [VERIFIED_SOURCE]

With cuts, translation need not be a function into the same presentation. Theorem 2 uses *proof-net equivalence* generated by proofs with a common translation, and §9 discusses alternatives and a conjecture. Therefore cut-free equality and cut-normalized equality must not be conflated. This audit uses Theorem 1 for the fixture, not a new cut theorem. Strongest objection to generalizing: units, boxes, and source-dependent equations can change the quotient.

## S2 — Free star-autonomous nets, including units

Dominic Hughes, *Simple free star-autonomous categories and full coherence*, [arXiv math/0506521v4](https://arxiv.org/pdf/math/0506521v4), version 27 March 2012. Inspected §§2–4, §6.1, and the proof roadmap in §7. The manuscript's venue line is not used as verified publication metadata.

For a category `A`, shapes use its objects, tensor, duality, and the unit. `A`-linkings carry atomic edges labeled by arrows of `A`, with the matching and switching conditions. Moving one unit edge, while retaining validity, generates rewiring equivalence. Morphisms of `N A` are those equivalence classes, not individually chosen jump placements. Theorem 2 (p.12) says composition respects rewiring; Theorem 3 (p.13) says `N A` is the free star-autonomous category generated by `A`. This supplies a compositional quotient with a universal property. [VERIFIED_SOURCE]

Theorem 4 (p.13) states equality decidable by finiteness of possible leaf functions. An effective comparison additionally needs decidable equality of the base labels; the finite discrete atom base used here satisfies that. “For any category” must not be read as an algorithm for arbitrary oracle arrow equality. §6.1's switching condition deletes one argument edge at each negative tensor node and requires a tree; in one-sided notation these are par switchings. These definitions verify the fixture's graph test without relying only on the theorem title.

Limitation: the free *multiplicative* categorical identity is a specified mathematical choice. The theorem does not cover all exponentials, dependent contexts, or causal histories of normalization. Its freeness is a positive result, not universality over foundations.

## S3 — CLF and exact individual-token trace adequacy

Kevin Watkins, Iliano Cervesato, Frank Pfenning, David Walker, *A Concurrent Logical Framework I: Judgments and Properties*, [CMU-CS-02-101](https://www.cs.cmu.edu/~fp/papers/CMU-CS-02-101.pdf); Iliano Cervesato, Frank Pfenning, David Walker, Kevin Watkins, *A Concurrent Logical Framework II: Examples and Applications*, [CMU-CS-02-102](https://www.cs.cmu.edu/~fp/papers/CMU-CS-02-102.pdf). Both March 2002, revised May 2003. Printed page = PDF page minus two. Inspected I Definition 5 pp.6–7, Theorem 6 pp.21–22; II §§5.2–5.4 pp.27–46 and §5.5's LLF comparison.

I's concurrent equality permutes monadic bindings subject to freshness and independence: bound patterns are disjoint, and neither operation's free variables intersect the other binding's bound variables. Canonical result expressions and ordinary term equality remain part of the relation. Theorem 6 decides equality. This is a native framework equality beyond ordinary LF's rule-tree order. [VERIFIED_SOURCE]

II explicitly departs from collective-token semantics: tokens have identities. A transition instance records its transition name, consumed token labels, and produced token labels. Well-labeled sequences produce/consume a given label at most once, and produce it before consumption unless it is initially present. The exchange relation forbids all four input/output intersections between the adjacent instances. Lemmas 5.1–5.3 pp.30–31 establish valid swaps and their relationship to the permitted permutations. Trace graphs are finite acyclic bipartite graphs with the specified token producer/consumer constraints; sequences of a trace are its legal linearizations. Trace identity allows the prescribed transition-label renaming while retaining token choices. [VERIFIED_SOURCE]

For a fixed net, the CLF signature has place/token families and one constant per transition, consuming linear inputs and returning monadic tensor outputs. Markings become labeled linear contexts. A chosen canonical ordering fixes the tuple representing the final marking. Lemmas 5.13–5.14 prove sequential soundness and inversion; **Theorem 5.15**, printed p.42/PDF p.44, gives a bijection between the specified execution sequences and sequential typed expressions. That theorem alone is not the concurrent quotient theorem.

The concurrent comparison adds the missing identity result:

- Lemmas 5.16–5.17, printed p.43, show that permitted exchanges yield concurrent equality.
- **Lemma 5.19**, printed pp.44–45/PDF pp.46–47: if the encoding of a well-labeled sequence is concurrently equal to `E`, then `E` is the encoding of a well-labeled sequence related to the original by the exchange equivalence. Its proof inducts on concurrent equality, including moved bindings. This is the decisive **reflection** argument.
- Lemmas 5.21–5.22 provide trace soundness/inversion; **Theorem 5.23**, printed p.46/PDF p.48, gives trace adequacy. The preceding §5.4 text and equality lemmas determine that this is a correspondence of trace classes with expression classes modulo concurrent equality; it cannot mean a bijection with distinct raw serializations. The theorem's literal wording suppresses that quotient notation and has minor editorial omissions. The interpretation is grounded in those preceding lemmas, not silently attributed to the isolated sentence.

All these are VERIFIED_SOURCE, not formal checks. Limitations: fixed signature, finite individually labeled traces, specified boundary ordering and freshness, no theorem of collective-token identity or bisimulation. Different choices of an indistinguishable token are intentionally distinct. The report's independent-step and conflict examples instantiate this mathematics; they do not establish MLL proof-net identity in CLF. The LLF encoding in §5.5 uses continuation-passing structure and retains sequential choices rather than this native concurrent equality.

## S4 — Fully faithful polarized proof semantics

Olivier Laurent, *Syntax vs. semantics: a polarized approach*, [author manuscript](https://perso.ens-lyon.fr/olivier.laurent/synsempol.pdf), dated 20 January 2005. Inspected the LLpol grammar and net definitions, game interpretations, Theorems 2–4 (PDF pp.18,22,24), and Definitions 25–26 defining the compared categories.

LLpol is polarized propositional linear logic: positive forms include positive atoms, `1,0`, tensor, sum, and `!N`; negative forms are dual, and a sequent has at most one positive formula. Sliced proof nets use the paper's equality/normalization discipline. Strategies must be **finite, total, and label-balanced**, on the specific arenas interpreting the formulas. Theorem 2 realizes every such strategy on `Γ⋆` by a proof of `⊢Γ`. Theorem 3 says that cut-free sliced nets with equal interpretations are equal nets. Theorem 4 says the syntactical sliced-net category and the game category are equivalent. Objects of the displayed categorical comparison are negative formulas/negative labeled arenas, with the specified proof-net/game hom-sets and composition. [VERIFIED_SOURCE]

This supplies equality preservation/reflection and full completeness together, with genuine nontrivial identity. It is not a theorem that *arbitrary* games are definable, or that ordinary LK has this βη identity without a translation/comparison theorem. Polarization, totality, finiteness, and balance are hypotheses, not decorations. The report invokes it as a strong positive representation, not as a universal encoding.

## S5 — LF adequacy and canonical forms

Robert Harper, Furio Honsell, Gordon Plotkin, *A Framework for Defining Logics*, [Edinburgh manuscript](https://era.ed.ac.uk/bitstreams/f02739c7-c52e-4764-9229-a1fcb46daad6/download). Inspected §2 normalization/canonical forms, Theorem 4.1 pp.21–22 and Theorem 4.2 p.24, and the distinction between object conversion and LF conversion. The retrieved manuscript has 37 PDF pages; theorem numbers/locations refer to it.

Theorem 4.1 gives, for every first-order formula and the specified term-variable/assumption context, a bijection of **valid raw proof expressions** with canonical LF inhabitants of the represented judgment. It is compositional under simultaneous substitution of object terms and hypothesis proofs, with their contexts properly accounted for. It treats pure FOL over the indicated language; mathematical axiom/rule extensions require their own treatment. Theorem 4.2 does the corresponding job for the presented HOL encoding. [VERIFIED_SOURCE]

LF β conversion handles substitution inside encoded syntax, but a constant such as `imp-e` is not a framework β-redex. The main presentation is β-based; its appendix discusses βη. Canonical forms are long applied heads, and typed normalization/confluence give unique normal forms. The report explicitly chooses βη LF for its test; two distinct constant heads at an atomic family remain distinct in either version. This is a hand application of those metatheorems, not a machine-checked LF file. Proof identity modulo object reduction or rule commutation is not supplied by raw-proof adequacy alone.

## S6 — LLF's resource discipline and limit

Iliano Cervesato and Frank Pfenning, *A Linear Logical Framework*, [author journal manuscript](https://www.cs.cmu.edu/~iliano/papers/ic02.pdf). Inspected its syntax/context split, Theorem 2.9 (PDF p.35), and conclusion (p.64). The core is `λΠ⊸&⊤`, combining unrestricted dependent functions with linear implication/additive constructions. Type-family arguments are **linearly closed**, so dependent indexing does not consume linear hypotheses. Theorem 2.9 reflects LF judgments from LLF when the signature, context, and compared terms are LF ones. [VERIFIED_SOURCE]

This preserves established LF representations and adds native linear assumption usage. The conclusion explains that adding other free linear connectives introduces commuting conversions that complicate canonical forms. That is a design/metatheory limitation, not an impossibility of encoding their syntax or using another framework such as CLF. Resource preservation alone does not prove fidelity for an independently chosen net quotient.

## S7 — Generic mode theory and the recovered equality conjecture

Daniel R. Licata, Michael Shulman, Mitchell Riley, *A Fibrational Framework for Substructural and Modal Logics*, FSCD 2017, [publisher PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol084-fscd2017/LIPIcs.FSCD.2017.25/LIPIcs.FSCD.2017.25.pdf), DOI [10.4230/LIPIcs.FSCD.2017.25](https://doi.org/10.4230/LIPIcs.FSCD.2017.25). Extended [author manuscript](https://dlicata.wescreates.wesleyan.edu/pubs/lsr17multi/lsr17multi-ex.pdf), recovered directly from the current author site. Inspected short §§2–5 and p.25:17; extended §8's equality material, Conjecture 8.5 p.59, §9.1 pp.59–61 and §9.2 pp.62–65.

Mode theories specify context descriptors, descriptor equations, structural transformations, and equations on transformations. Generic `F` and `U` types internalize these operations. FSCD Theorem 2.1 gives admissible cut, identity and structurality for every mode theory. Theorem 3.1's example adequacy is an **inhabitation iff**, not a bijection on mathematical proof classes. §4 specifies an equational theory, including generic βη. Theorems 5.6–5.7 construct a syntactic bifibration and interpretation in bifibrations; they do not state faithfulness of every external calculus embedding. [VERIFIED_SOURCE]

The extended statement is explicitly **Conjecture 8.5, Completeness of Permutative Equality**: for framework derivations `d,d′`, `d≡d′` implies their chosen cut-free forms satisfy `d↓≡p d′↓`. The problem is reflection of the full congruence into permutative equality; equality derivations can pass through extra types. §9.1 warns that the input class for the adequacy template is not precisely defined. §9.2's ordered-product adequacy is conditional on this lemma, in the monoid mode theory **without commutativity**. Remark 9.2 later calls 8.5 a “Theorem”; its explicit Conjecture heading controls the status. No unconditional commutative-tensor theorem is recovered by that typographical change. [VERIFIED_SOURCE]

This corrects both “generic frameworks already prove all R3” and “generic structural data are necessarily an interpreter.” The report proposes a restricted commutative-tensor comparison with an independently fixed symmetric-monoidal proof quotient. It does not claim that comparison is new or open today, or that it extends to native classical LK.

Targeted current-status searches used the title/authors together with “equational adequacy,” “permutative equality,” and “Conjecture 8.5.” They recovered this manuscript and related modal/generic work but **no primary resolution was verified**. This is an incomplete search, not evidence of nonexistence; current status and novelty remain UNKNOWN. The direct current author URL resolves the earlier PR #2 archived-link access gap.

## S8 — Free doctrinal semantics and external-comparison gap

Michael Shulman, *Semantics of linear/nonlinear lambda calculi*, [arXiv:2106.15042v5](https://arxiv.org/pdf/2106.15042v5), LMCS 19(2:1), 2023, DOI [10.46298/LMCS-19(2:1)2023](https://doi.org/10.46298/LMCS-19(2:1)2023). Inspected Theorem 7.4 (PDF p.42), §8 pp.43–48, Proposition 8.3 p.47 and its following equality passage, Remark 8.4, and the classical linear/nonlinear distinctions.

For each small LNL doctrine `D` and `D`-sketch `S`, Theorem 7.4 constructs a `D`-complete sketch and a map from `S`, with precomposition a surjective equivalence against any complete sketch. This is a free categorical completion. §8's displayed simple sequent syntax assumes an unsorted doctrine with subterminal underlying base and finite discrete cones. Proposition 8.3 gives a surjection from full derivations to the corresponding hom-set. The next passage gives the quotient by generic structural equations, β/principal-cut reductions, η/extensionality, and the original sketch composition equations. [VERIFIED_SOURCE]

This presents its own free semantics, including linear multiple-output structure and nonlinear cartesian single-output structure. It does not independently identify that quotient with every preselected external proof equivalence. The source explicitly leaves cut elimination to further study, and Remark 8.4 allows syntax changes/infinitary rules for more general cones. These qualifications prevent turning a universal-property theorem into an unrestricted finite-operational theorem for the charter.

## S9 — A positive full and faithful linear CPS representation

Masahito Hasegawa, *Linearly used effects: monadic and CPS transformations into the linear lambda calculus*, FLOPS 2002, pp.167–182, [author PDF](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/flops02.pdf). Inspected §§4–5, Proposition 5 (printed p.176/PDF p.10), the inverse/canonical-form lemmas and Theorem 1 (printed p.177/PDF p.11).

Proposition 5 states: `Γ⊢M=N:σ` in the computational lambda calculus iff `Γ°;∅⊢M°=N°:(σ°→o)⊸o` in the specified linear lambda calculus. The paper attributes that equational-completeness result to Sabry–Felleisen; the original attributed proof was not separately retrieved here. The statement in this primary transformation paper is VERIFIED_SOURCE; provenance of the older proof is SECONDARY_ONLY in this task.

Theorem 1 proves full completeness: every target term of that translated type/context is equal to a translated source term. **The answer type `o` must be a target base type absent from the source computational calculus.** Thus it is a real cross-calculus correspondence on the stated equations, not just derivability preservation. Unrestricted source variables live in the target's unrestricted context; continuations are used linearly. It does not imply fidelity for classical net permutations or every lambda calculus. In particular it is a different transformation/source from the Girard `λval` counterexample discussed in PR #2.

## S10 — Computational adequacy in a rewriting framework

Thiago Felicissimo, *Adequate and computational encodings in the logical framework Dedukti*, [arXiv:2205.02883v1](https://arxiv.org/pdf/2205.02883v1), 5 May 2022 extended text. Inspected EPTS hypotheses, decoding and inversion, Theorems 45–46 (Theorem 46 PDF p.22), and §8.

For the functional explicitly typed pure type system and its encoding, Theorem 46 gives a substitution-compatible bijection of typed source terms with **framework-β-normal** target terms modulo hidden annotation conversion. If the source type is a top sort, the target family is `U_A`; otherwise it is the specified `El` family. Every target inhabitant at the translated context/type has such a framework-β normal form. Source reduction reachability iff reachability between translations is also stated. Theorem 45 supplies inversion of arbitrary inhabitants. The object reduction can be nonnormalizing while administrative framework β still normalizes. [VERIFIED_SOURCE]

Different relations are doing different work: source/object computation, framework β, and hidden annotation equality. Do not silently infer reflection of every target-conversion zigzag solely from reflection of forward reachability between images. §8 separately addresses infinite-sort implementation limitations. Per-source rewrite declarations require justification; their presence alone proves neither vacuity nor cross-foundation identity fidelity.

## S11 — Relational injectivity and the no-jump caveat

Daniel de Carvalho, *The relational model is injective for Multiplicative Exponential Linear Logic*, [arXiv:1502.02404v4](https://arxiv.org/pdf/1502.02404v4). The arXiv stamp says 10 May 2016 while the PDF body is dated 1 June 2021; this audit records the retrieved bytes, not an inferred matching publication version. Inspected §1 including footnote 1, Definition 4, Theorem 9 (PDF p.13), and Remarks 5–6.

Theorem 9: if the paper's proof structures `R,R′` have the same free conclusion ports and equal relational interpretations, they are isomorphic by the specified boundary-fixing isomorphism. The initial setting omits axioms; the later remarks explain extensions using **infinite ground interpretations** and atomicity conditions to prevent replacing an axiom by a semantically identical expansion. The proof recovers boxed structure using injective experiments and reconstruction. [VERIFIED_SOURCE]

Decisive scope warning from introduction footnote 1: these nets have **no jump** and identify more sequent-calculus proofs than the usual multiplicative-unit treatment. Accordingly, the theorem is injectivity on *this* net syntax. It does not prove equality reflection for a finer quotient retaining unit rewiring classes. This is an additional caution to PR #2's positive lead. It does provide strong resource-sensitive semantic injectivity, including exponential structure; fullness for all relations and causal-history fidelity are separate questions.

## S12 — The cost of units, not representational impossibility

Willem Heijltjes and Robin Houston, *Proof equivalence in MLL is PSPACE-complete*, [arXiv:1510.06178](https://arxiv.org/pdf/1510.06178), LMCS 12(1:2), 2016, DOI [10.2168/LMCS-12(1:2)2016](https://doi.org/10.2168/LMCS-12(1:2)2016). Inspected §1's equivalence/units discussion and Theorem 9.1 (PDF p.32).

Theorem 9.1 quantifies over the paper's MLL proof equivalence **with units**, using jump rewiring and the established correspondence with proof commutations. It proves PSPACE membership and hardness via constraint-graph reconfiguration. The introduction makes the efficient-canonicalization obstruction conditional on `P≠PSPACE`. [VERIFIED_SOURCE]

A polynomial computation of a polynomially comparable canonical representation would yield polynomial-time equality; the theorem therefore obstructs that combination under the assumption. It does not forbid S2's finite quotient presentation, expensive comparison, or proof terms carrying other certificates. The unit-free fixture is not a witness of this hardness theorem.

## S13 — Established causality and conflict vocabulary

Glynn Winskel and Mogens Nielsen, *Models for Concurrency*, revised DAIMI PB-429, November 1993, [author report](https://www.cl.cam.ac.uk/~gw104/winskel-nielsen-models-for-concurrency.pdf). Inspected Chapter 8, printed pp.55–58/PDF pp.57–60. Event structures have a partial order of causality, finite causal pasts, and symmetric irreflexive hereditary conflict. Configurations are downward-closed conflict-free subsets. Concurrent events are neither causally comparable nor conflicting. [VERIFIED_SOURCE]

The report's competing-consumer example needs conflict as well as a partial order. Generational rank is a derived quantity on finite acyclic occurrence events, not a replacement for these relations or a claim from this source of uniform proof-generational semantics. A guessed BRICS report URL initially returned a different paper (Torben Brauner); that retrieval was rejected and is not cited as this source.

## S14 — Global proof-net correctness

Jean-Yves Girard, *Proof-nets: the parallel syntax for proof-theory*, in *Logic and Algebra* (1996), [author PDF](https://girard.perso.math.cnrs.fr/Proofnets.pdf). Inspected §§1.1–1.5, Definitions 1–10 printed pp.3–10, Theorems 1–2 p.10. The setting is weighted MALL, with its constraints on weights and switching/slicing choices; sequentialization characterizes its correct nets. [VERIFIED_SOURCE]

The fixture is purely multiplicative: no weights/additive choices, boxes, units, or MIX. S2 §6.1 additionally supplies its tree-switching criterion directly. This avoids generalizing a weighted MALL theorem by dropping its side conditions. Correctness quantifies over switchings of the entire graph; construction-dependency acyclicity is insufficient. Enumeration cost says nothing about existence of a categorical representation.

## S15 — Cyclic validity as a boundary, including a local positive result

James Brotherston and Alex Simpson, *Sequent calculi for induction and infinite descent*, [Edinburgh peer-reviewed manuscript](https://www.pure.ed.ac.uk/ws/files/12304236/bs_journal.pdf), DOI [10.1093/logcom/exq052](https://doi.org/10.1093/logcom/exq052). Shell PDF retrieval was blocked earlier; the web PDF reader exposed the primary text and was used again in this task. The cover's date/issue metadata differs from the published citation, so statements use manuscript theorem numbers. Definitions 5.4–5.5 at printed p.18 define traces and require every infinite path to have a tail admitting an infinitely progressing trace. Definition 7.3 and Proposition 7.4 at p.26 impose the condition on finite cyclic preproof graphs and decide it using automata. [VERIFIED_SOURCE through web text; no locally retrieved PDF hash]

David Nollet, Alexis Saurin, Christine Tasson, *Local validity for circular proofs in linear logic with fixed points*, CSL 2018, [publisher PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol119-csl2018/LIPIcs.CSL.2018.35/LIPIcs.CSL.2018.35.pdf). Propositions 22–23 (p.35:9) characterize validating sets and decide validity for the **restricted strong-validity/labeled fragment**, with the paper's formula labels/constraints. Proposition 30 extends soundness to the specified larger labeled calculus; it is not a theorem replacing all global cyclic criteria by unconditional local checks. [VERIFIED_SOURCE]

The audit uses these as validity distinctions. It does not reverify the stronger cut/bouncing-thread undecidability claims in PR #2. No impossibility of arbitrarily large finite validity certificates is inferred. The structural-loop counterexample in the report is a hand inference: no inductive unfolding occurs, so no progressing trace can witness the infinite branch.

## S16 — Rewriting and modularity: separate levels of adequacy

Narciso Martí-Oliet and José Meseguer, *Rewriting Logic as a Logical and Semantic Framework*, long 1993 report, [author-hosted compressed PostScript](https://maude.cs.illinois.edu/papers/postscript/MMlogframework_1993.ps.gz). Retrieved PostScript was converted to PDF for inspection; its hash below identifies that conversion, not original publisher bytes. Inspected the category/functoriality/exchange equations, linear-logic derivability statement (Theorem 14), and §4.3.3 printed pp.34–35. The representation's additive conjunction needs a further quotient to obtain a categorical product; derivability equivalence by itself does not settle mathematical proof-class bijection. Independent rewrite permutation is established for the specified rewriting equality. [VERIFIED_SOURCE]

Florian Rabe, *How to Identify, Translate, and Combine Logics?*, [author manuscript](https://kwarc.info/people/frabe/Research/rabe_howto_14.pdf), inspected Theorem 2.31 and Definition 3.39. Proof-conservativity quantifies over existence of proofs, not proof identity. Florian Rabe and Michael Kohlhase, *A Scalable Module System*, [arXiv:1105.0548](https://arxiv.org/pdf/1105.0548), inspected Theorem 34's regular-foundation/total-morphism hypotheses: typing/equality preservation, not general equality reflection. [VERIFIED_SOURCE]

These are relevant generic frameworks and causal prior art. No hom-set full faithfulness for all independent source proof congruences follows merely from modular theory morphisms or conservative theorem translation.

## S17 — Classical control avoids an overbroad collapse claim

Peter Selinger, *Control categories and duality: on the categorical semantics of the lambda-mu calculus*, MSCS 11 (2001), pp.207–260, [author PDF](https://www.mathstat.dal.ca/~selinger/papers/control.pdf). Inspected Definition 2.11, Lemma 2.7, Corollary 3.8 and Theorem 3.18 (PDF pp.8,7,12,17 respectively).

A control category is a cartesian-closed distributive symmetric **premonoidal** category with codiagonals satisfying the displayed natural-isomorphism axiom. Its bottom is initial in the restricted focal setting, not indiscriminately in the whole category. Theorem 3.18 represents control categories as categories of continuations. Corollary 3.8 says bifunctorial par forces collapse to a Boolean algebra. [VERIFIED_SOURCE]

This pinpoints why ordinary cartesian/dualizing collapse assumptions must not be transferred to all classical proof representations. It is not itself a uniform LF/CLF encoding theorem. The report's other positive classical witness is S4's full faithful polarized semantics.

## Unverified or excluded leads and counterarguments

- Gardner's thesis theorem text and the original Girard call-by-value counterexample were not newly recertified here. Their corrected scope is SECONDARY_ONLY via PR #2's review; no universal negative conclusion rests on them.
- A scan of Hasegawa's earlier 2000 paper was retrieved but its theorem text was not recovered reliably; it is not used to promote that paper's theorem numbering. S9 is the readable, inspected 2002 positive result.
- LSR's current conjecture status and the novelty of the proposed tensor restriction remain UNKNOWN. A related modal-framework result or a successful small translation is not evidence of reflection for the full ambient target congruence.
- A possible objection to the CLF claim is that Theorem 5.23's isolated wording omits explicit equality classes. The actual preservation/converse lemmas in §5.4 answer that objection; this task has not machine-checked their proofs or remedied editorial slips.
- A possible objection to the multiplicative positive result is that its identity is a categorical choice. That is accepted: fidelity must fix the source quotient first. Neither net equality, strategy equality, nor labeled trace equality is silently treated as the one identity of every foundation.
- None of these results proves a finite universal algebra meeting the entire charter. Failure to find that theorem proves neither impossibility nor novelty. The next research gate is an external comparison theorem inside existing mathematics, not construction of a new system.

## Retrieval fingerprints

SHA-256 of retrieved PDFs below; the converted rewriting report is explicitly marked. These are version-identification aids, not proof certificates. Brotherston–Simpson was read through web extraction and has no local-byte hash. URLs above are the durable retrieval paths; scratch filenames are only audit labels.

| Source / scratch label | SHA-256 |
|---|---|
| S1 `mall` | `1ff20d34d6ee16b9722d3c05fc0f13f440780e4840bfde9512589ec8d3a51320` |
| S2 `hughes` | `be814e88bc80ffe1af9dace01c5d903e56aefbd3f0cf5b68011b1a2f1770a698` |
| S3 `clf1` | `827c10fb8ba31419861b2c4c07cf671aaffa14efdc57f99806d2d105933a2ac9` |
| S3 `clf2` | `4ae549de4bc5ec664b24ba91b72d4ce39fdd0cadf534d0bb854915d78f034505` |
| S4 `laurent` | `1d46a1a4383512c628f797e9f2497e6dc60409304c08909f6e98c784c5252a82` |
| S5 `lf` | `4bd5b57ace8616b7e71d43df985f80686776220a178f30f9835a735d3fb81947` |
| S6 `llf` | `2f9472add7c0fcfaad99f9a64bb75115f6dbd9eaaa35a873004ca9fd0c83b555` |
| S7 `lsr2017` | `a9067d495ed1b3c16fa681ba5e33abc61a226b61858957622ad31f7bd797c160` |
| S7 `lsrext` | `7f04277218da9f12e7cf36cf487b4004ddfa1914bb7a4b364f74ab86bca1a7db` |
| S8 `shulman` | `253d5e39a3eb0c3410a93c8443d3109721d75c80f5ea9f823c6b305e2c8b240e` |
| S9 `flops` | `d2de8e8880445d8de6eb87200d678b6846991b925569df3c00d0f9576c946fee` |
| S10 `felicissimo` | `cf6173139633e82895b21f5685dacc30e58d56f6f3a8d3a3b88b259083812d4d` |
| S11 `mell` | `73c15adcff0c444136fce4e8e5a15a645fe0e9ea527823f6595f2baef462fbcf` |
| S12 `houston` | `49938ca71b7e1005b4964a9fed6d9c5b8ec9f5db2e1dc2360abfc33bedc5432b` |
| S13 `winskel` | `0e6f814f1621b1099b02169b46f54a14f76cea3b092fae13c72c79f6a927a28f` |
| S14 `nets` | `a8d8ddae04732d1d3d72150e8c4bf05276d105ca58604b33329fa9948477d5c7` |
| S15 `local` | `2e6ac15189132ba879c5f48134cb82c9b0cebea0b701f82772d457341ef14d1d` |
| S16 `general` (converted) | `c4abaaf5fac4b3a828a495ecace3255078e0905e619968ae3ca3d1ab6d58ba70` |
| S16 `rabe` | `0748353d13e2495691edecced5daea790f3c3a8fe2e428664fb86f5d55cc588e` |
| S16 `mmt` | `5f3d2168535647e206fa1805bcfefb48c08206af05ff29b826f1cbf38669f029` |
| S17 `control` | `5e2bc7e6dd4a995a0331b20f2df2d1870064a7628161f160c74329521ae84769` |
