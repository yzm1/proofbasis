# cyc — cyclic proofs, trace conditions, p-simulation, cut-elimination blowup, infinitary boundary

Agent tag: cyc. Session date 2026-10-08. Download dir: `scratchpad/dl/cyc/` (PDFs converted with `pdftotext -layout`; nothing executed).
Page/line references below refer to the retrieved version named in each entry. "L.nnn" = line in the pdftotext output (for re-checking only, not a citation).

Status legend (per PROTOCOL): VERIFIED_SOURCE / SECONDARY_ONLY / UNVERIFIED-MEMORY / NOT_ACCESSED.
Additional label used: ABSTRACT_ONLY = only the official abstract/metadata was read (not the theorem text).

---------------------------------------------------------------------------------------------------

## Access summary

| # | Source | Status |
|---|--------|--------|
| 1a | Brotherston & Simpson, JLC 21(6) 2011, doi:10.1093/logcom/exq052 | NOT_ACCESSED (journal text). Metadata via Crossref. Content verified via Brotherston's 2006 PhD thesis (same systems) — see 1b |
| 1b | Brotherston, PhD thesis, Edinburgh 2006 | VERIFIED_SOURCE |
| 2a | Berardi & Tatsuta, FoSSaCS 2017 (LNCS, pp.301–317, doi:10.1007/978-3-662-54458-7_18) | NOT_ACCESSED; journal version LMCS 15(3:10) 2019 VERIFIED_SOURCE (arXiv:1712.09603v5) |
| 2b | Berardi & Tatsuta, LICS 2017 "Equivalence of inductive definitions and cyclic proofs under arithmetic" (doi:10.1109/LICS.2017.8005114, pp.1–12) | NOT_ACCESSED; described in their arXiv:1712.03502v1 (intuitionistic version, VERIFIED_SOURCE) → SECONDARY_ONLY |
| 2c | Simpson, "Cyclic arithmetic is equivalent to Peano arithmetic", FoSSaCS 2017, pp.283–300, doi:10.1007/978-3-662-54458-7_17 | NOT_ACCESSED (Springer bot wall). SECONDARY_ONLY via Das LMCS 2020 and Berardi–Tatsuta |
| 2d | Das, "On the logical complexity of cyclic arithmetic", LMCS 16(1) 2020 | VERIFIED_SOURCE |
| 3a | Nollet, Saurin, Tasson, TABLEAUX 2019, LNCS pp.317–334, doi:10.1007/978-3-030-29026-9_18 | ABSTRACT_ONLY (HAL API metadata; HAL PDF blocked by Anubis bot wall) |
| 3b | Nollet, Saurin, Tasson, "Local validity for circular proofs in linear logic with fixed points", CSL 2018, LIPIcs 119, paper 35 | VERIFIED_SOURCE |
| 3c | Baelde, Doumane, Kuperberg, Saurin, "Bouncing threads for infinitary and circular proofs", arXiv:2005.08257v1 | VERIFIED_SOURCE (arXiv v1; final venue not verified) |
| 3d | Cohen, Jabarin, Popescu, Rowe, "The Complex(ity) Landscape of Checking Infinite Descent", PACMPL 8 POPL, Art.46, 2024, doi:10.1145/3632888 | VERIFIED_SOURCE (author PDF) |
| 4 | Cook & Reckhow, JSL 44(1) 1979, 36–50 | VERIFIED_SOURCE (JSTOR scan on Cook's homepage) |
| 4' | Reckhow, PhD thesis, Toronto 1976 | NOT_ACCESSED; SECONDARY_ONLY via Cook–Reckhow 1979 |
| 5 | Ben-Sasson, Impagliazzo, Wigderson, Combinatorica 24(4) 2004, 585–603, doi:10.1007/s00493-004-0036-5 | ABSTRACT_ONLY (ECCC TR00-005 abstract read; PDFs downloaded but fonts unextractable) |
| 6a | Statman, "Lower bounds on Herbrand's theorem", Proc. AMS 75(1) 1979, 104–107 | NOT_ACCESSED (AMS Cloudflare). SECONDARY_ONLY via Buss 2012, Moser–Zach |
| 6b | Orevkov, J. Soviet Math 20 (1982) 2337–2350 (Russian 1979) | NOT_ACCESSED; SECONDARY_ONLY via Buss 2012, Moser–Zach |
| 6c | Buss, "Sharpened lower bounds for cut elimination", JSL 77(2) 2012 | VERIFIED_SOURCE (author's final version) |
| 6d | Boolos, "Don't eliminate cut", J. Phil. Logic 13(4) 1984, doi:10.1007/BF00247711 | NOT_ACCESSED (metadata via Crossref only) |
| 6e | Statman, "The typed λ-calculus is not elementary recursive", TCS 9(1) 1979, 73–81, doi:10.1016/0304-3975(79)90007-0 | NOT_ACCESSED (metadata via Crossref only) |
| 7a | ω-rule: Frittaion, "Completeness of the primitive recursive ω-rule", arXiv:2110.01270v1 | VERIFIED_SOURCE (secondary w.r.t. Shoenfield 1959 / Schütte 1950) |
| 7b | Second-order logic: Väänänen, SEP "Second-order and Higher-order Logic" (rev. 2024-08-31) | VERIFIED_SOURCE (encyclopedia = secondary/standard reference) |
| 7c | Shapiro 1991, Schütte, Pohlers, Shoenfield 1959 | NOT_ACCESSED |
| 8a | Kuperberg, Pinault, Pous, "Cyclic proofs, system T, and the power of contraction", PACMPL 5 POPL 2021, doi:10.1145/3434282 | VERIFIED_SOURCE. NOTE: the task attributed this to "Das"; actual authors are Kuperberg, Pinault, Pous |
| 8b | Oda & Kimura, arXiv:2203.05791v2 (2025), cut-elimination failure for CLKIDω | VERIFIED_SOURCE (arXiv) |
| 8c | Masuoka & Tatsuta, arXiv:2106.11798 (cut-elim counterexample) | NOT_ACCESSED; SECONDARY_ONLY via 8b |
| — | Afshari & Wehr, "Abstract cyclic proofs", MSCS 2024 | NOT_ACCESSED (proxy 502); only a search-engine snippet — treat as UNVERIFIED |
| — | Das & Pous / Afshari–Leigh (KA, μ-calculus) | NOT_ACCESSED (not pursued, time) |

---------------------------------------------------------------------------------------------------

## 1. Brotherston & Simpson — LKID, LKIDω, CLKIDω, global trace condition

### 1a. JLC paper (NOT_ACCESSED)
Bibliographic (Crossref): J. Brotherston, A. Simpson, "Sequent calculi for induction and infinite descent", Journal of Logic and Computation 21(6):1177–1216; doi:10.1093/logcom/exq052 (online 2010-09-30; issue 2011). Conference precursor: "Complete Sequent Calculi for Induction and Infinite Descent", LICS 2007, pp.51–62, doi:10.1109/LICS.2007.16 (Crossref).
SECONDARY (Berardi–Tatsuta LMCS 2019, §4.2): "The left-to-right inclusion is proved in [3], Lemma 7.3.1 and in [6], Thm. 7.6. The Brotherston-Simpson conjecture (the conjecture 7.7 in [6]) says that the provability LKID includes that of CLKIDω." ([6] = JLC paper.) So in the JLC paper: LKID ⊆ CLKIDω is Thm 7.6; the conjecture is Conjecture 7.7 — SECONDARY_ONLY numbering.

### 1b. Brotherston, PhD thesis (VERIFIED_SOURCE)
J. Brotherston, *Sequent calculus proof systems for inductive definitions*, PhD thesis, LFCS, University of Edinburgh, 2006. Retrieved: https://era.ed.ac.uk/bitstreams/de6ecd6d-65fc-4b72-a0a1-f383b1748f5a/download (168-page PDF). Page numbers = thesis pagination.

**Trace (Def 4.2.3, p.77–78).** "Let (vi) be a path in an LKIDω pre-proof D = (V, s, r, p). A trace following (vi) is a sequence (τi) such that, for all i: τi = Pji ti ∈ Γi, where Pji is an inductive predicate … if r(vi) is (Subst) then τi = τi+1[θ] … if r(vi) is some casesplit rule (Case Pk) then either τi+1 = τi, or τi is the active formula of the rule instance and τi+1 is a case-descendant of τi. In the latter case, i is said to be a progress point".

**Global condition (Def 4.2.5).** "An LKIDω pre-proof D is said to be an LKIDω proof if, for every infinite path in D, there is an infinitely progressing trace following some tail of the path."

**Soundness (Prop 4.2.6).** "If there is an LKIDω proof of Γ ⊢ ∆ then Γ ⊢ ∆ is valid (i.e. true in all standard models for (Σ, Φ))." (Standard models — not Henkin models.)

**Completeness of the infinitary system (Thm 4.3.9).** "If Γ ⊢ ∆ is valid with respect to standard models of (Σ, Φ), then it has a recursive cut-free proof in LKIDω." Plus Thm 4.3.10 cut-eliminability in LKIDω.

**Non-effectiveness of LKIDω (Ch.5 intro, p.~94).** "it is not possible to recursively enumerate the set of LKIDω proofs, for otherwise — via an embedding of Peano arithmetic into LKIDω … — it would be possible to recursively enumerate the true statements of arithmetic, which is impossible. In particular, although recursive LKIDω proofs can be encoded as natural numbers …, it is not even semidecidable whether a given natural number encodes an LKIDω proof".

**Cyclic pre-proof (Defs 5.1.1–5.1.2).** Companion: "A node C ∈ V is said to be a companion for B if r(C) is defined and s(C) = s(B)." Note: "we do not require companions to be ancestors of the bud nodes". "A CSω pre-proof of a sequent S is a pair (D = (V, s, r, p), R), where D is a finite Sω derivation tree with endsequent S, and R : V → V is a partial function assigning a companion to every bud node in D." CSω proof (Def 5.1.6): same global condition on every infinite path of the pre-proof graph GP.

**Global and decidable (Prop 5.1.10 and preceding text, p.98–99).** "The condition for a CSω pre-proof to be a proof (c.f. Definition 5.1.6) is of course a global condition in the sense that it can be determined only by examining the entire pre-proof structure (in general, anyway). However, in contrast to the situation of Sω … the soundness condition for CSω is decidable: Proposition 5.1.10. It is decidable whether a CSω pre-proof is a CSω proof." Proof is a **sketch**: "the property that every infinite path possesses a tail on which an infinitely progressing trace exists is an ω-regular property …, and hence reducible to the emptiness of a Büchi automaton." (Full construction in Appendix A, "Decidability of proof in trace-based cyclic proof systems", pp.147–154.) No complexity bound stated in the passage read.

**LKID ⊆ CLKIDω (Thm 7.3.2):** "Every LKID proof of Γ ⊢ ∆ can be transformed into a CLKIDω proof of Γ ⊢ ∆."

**Conjecture (Conj 7.3.3, p.137–138):** "If there is a CLKIDω proof of a sequent Γ ⊢ ∆ then there is an LKID proof of Γ ⊢ ∆." Authors: "A semantic proof of the conjecture would also be of interest, but we have no idea how to obtain one."

**Cut (Conj 5.2.4):** "Cut is not eliminable in the system CLKIDω." (Later confirmed — see §8b.)

**Trace manifolds (Def 7.2.1, Prop 7.2.3):** a stronger, more structured sufficient condition ("Any CSω pre-proof (in cycle normal form) with a trace manifold is a CSω proof"); whether every CLKIDω proof has one is stated as an open conjecture (p.138): "as the infinitely progressing traces on any two infinite paths in the pre-proof graph can behave entirely differently despite potential overlap between the paths, it is not obvious that a manifold need exist."

What is trusted/environment: the inductive definition set Φ (productions) is a parameter; the rules (Case Pk), (R) introductions are generated from Φ. Soundness relative to *standard* models; LKID (explicit induction) is sound+complete w.r.t. *Henkin* models (Prop 3.2.8 / thesis Ch.3).

Relevance (INFERENCE): F05 — correctness of a cyclic proof is, in the authors' own words, a *global* condition over all infinite paths; it is an ω-regular property of the finite graph, decidable, but not a conjunction of per-rule local checks. Any "finite operator algebra" claiming to represent CLKIDω proofs must either (i) carry the global check as a side condition outside the local operators, (ii) restrict to a locally-certifiable fragment (trace manifolds, labellings, reset proofs; see §3b, §3d), or (iii) translate to explicit induction — which fails in general (§2a). F07 — LKIDω (non-regular) proofs are not even semi-decidably recognizable.

---------------------------------------------------------------------------------------------------

## 2. Brotherston–Simpson conjecture: refuted in general, holds "under arithmetic"

### 2a. Berardi & Tatsuta, LMCS 2019 (journal version of FoSSaCS 2017) — VERIFIED_SOURCE
S. Berardi, M. Tatsuta, "Explicit induction is not equivalent to cyclic proofs for classical logic with inductive definitions", Logical Methods in Computer Science 15(3):10:1–10:25, 2019, DOI:10.23638/LMCS-15(3:10)2019. Retrieved https://arxiv.org/pdf/1712.09603v5 (LMCS-formatted). States it "is the journal version of [1]" = FoSSaCS 2017, 301–317 ("Classical System of Martin-Löf's Inductive Definitions is not Equivalent to Cyclic Proof System"; Crossref doi:10.1007/978-3-662-54458-7_18).

Global trace condition as stated there (Def 4.3, p.10:11): "An LKIDω pre-proof Π is defined to be an LKIDω proof if it satisfies the following global trace condition: for every infinite path π = (Γi ⊢ ∆i)i≥0 in Π, there is an infinitely progressing trace following some tail of the path". Def 4.6: "A CLKIDω proof is defined as a CLKIDω pre-proof such that its unfolding satisfies the global trace condition."

2-Hydra (Def 3.5): H = (Ha, Hb, Hc, Hd → ∀x,y∈N. p(x,y)) with "(Ha) ∀x ∈ N. p(0,0) ∧ p(1,0) ∧ p(x,1), (Hb) ∀x,y ∈ N. p(x,y) → p(sx,ssy), (Hc) ∀y ∈ N. p(sy,y) → p(0,ssy), (Hd) ∀x ∈ N. p(sx,x) → p(ssx,0)." Language ΣN: 0, s, N, binary predicate p (with equality).

**Main theorem (Thm 8.3, "Counterexample to the Brotherston-Simpson Conjecture"):** "Let H be the formula defined in Definition 3.5. Then H has a proof in CLKIDω(ΣN, ΦN), and no proof in LKID(ΣN, ΦN) + (0, s)-axioms."
Method: Henkin countermodel M with universe and N interpreted as N + Z; Henkin family = definable sets; via a new quantifier-elimination theorem (Thm 7.3) for sets of partial bijections closed under composition and inverse.
**Thm 8.4 (Non-Conservativity):** "There are Σ1, Φ1, Σ2, Φ2 such that LKID(Σ2, Φ2) is an extension of LKID(Σ1, Φ1) and LKID(Σ2, Φ2) is not conservative over LKID(Σ1, Φ1)." (Adding inductive predicate ≤ proves 0-axiom ⊢ H — Thm 3.7.)
Quantifiers: existence of one signature + one inductive definition set where provability differs. Only derivability (not proof identity) considered.

Relevance (INFERENCE): F01/F04/F05 — cyclic proofs and explicit-induction proofs over the *same* language and *same* inductive definitions do not even have the same theorems in general; therefore "cyclic proof ↦ inductive proof" cannot be assumed as a derivability-preserving translation without extra environment (arithmetic, extra inductive predicates). Thm 8.4 is also an F03 warning: adding an inductive definition to the "environment" can change the theorems in the old language (non-conservative), so environment content is not inert.

### 2b. Berardi & Tatsuta — equivalence under arithmetic
- LICS 2017 paper (Crossref: "Equivalence of inductive definitions and cyclic proofs under arithmetic", 32nd LICS, pp.1–12, doi:10.1109/LICS.2017.8005114): NOT_ACCESSED.
- Intuitionistic version VERIFIED_SOURCE: "Equivalence of Intuitionistic Inductive Definitions and Intuitionistic Cyclic Proofs under Arithmetic", arXiv:1712.03502v1 (10 Dec 2017). Abstract: "This paper first points out that the countermodel of FOSSACS 2017 paper by the same authors shows the conjecture for intuitionistic logic is false in general. Then this paper shows the conjecture for intuitionistic logic is true under arithmetic, namely, the provability of the intuitionistic cyclic proof system is the same as that of the intuitionistic system of Martin-Lof's inductive definitions when both systems contain Heyting arithmetic HA." Thm 6.14 "(Equivalence of LJID + HA and CLJIDω + HA) Let Σ = ΣN ∪ {Q, P, P′}, Φ = ΦN ∪ {P, P′}. Then the provability of CLJIDω + HA + (Σ, Φ) is the same as that of LJID + HA + (Σ, Φ)." Tools: HA proves Podelski–Rybalchenko and Kleene–Brouwer theorems "for induction".
- Their description of LICS 2017 (SECONDARY_ONLY): "[3] proved that if we add Peano arithmetic to both systems, CLKIDω and LKID are equivalent, namely the conjecture is true under arithmetic, by showing arithmetical Ramsey theorem and Podelski-Rybalchenko theorem for induction."

### 2c. Simpson, FoSSaCS 2017 — NOT_ACCESSED (SECONDARY_ONLY)
Bibliographic (Crossref/BT refs): A. Simpson, "Cyclic Arithmetic is Equivalent to Peano Arithmetic", FoSSaCS 2017, LNCS, pp.283–300, doi:10.1007/978-3-662-54458-7_17. Springer page reported as open access by a search engine, but PDF not retrievable (bot challenge).
Secondary descriptions (verified in those texts):
- Berardi–Tatsuta arXiv:1712.03502: "if we restrict both systems to only the natural number inductive predicate and add Peano arithmetic to both systems, the conjecture was proved to be true in [15], by internalizing a cyclic proof in ACA0 and using some results in reverse mathematics."
- Das LMCS 2020: "In [Sim17], Simpson showed that Peano Arithmetic (PA) is able to simulate cyclic reasoning by proving the soundness of the latter in the former. (The converse result is obtained much more easily.)" Das notes Simpson "relies on Weak König's" lemma (L.1469, context partial).

### 2d. Das, LMCS 2020 — VERIFIED_SOURCE
A. Das, "On the logical complexity of cyclic arithmetic", LMCS 16(1):1:1–1:39, 2020. Retrieved https://lmcs.episciences.org/4818/pdf.
- Abstract: "our main result is that IΣn+1 and CΣn prove the same Πn+1 theorems, for n ≥ 0. Furthermore, due to the 'uniformity' of our method, we also show that CA and Peano Arithmetic (PA) proofs of the same theorem differ only exponentially in size."
- **Thm 6.10:** "If π is a CA proof of ϕ, then we can construct a PA proof of ϕ of size exponential in |π|."
- Intro: IΣn+1 ⊆ CΣn (over Πn+1 theorems) "induces a non-elementary blowup in the size of proofs".
- **§3.2 (p.1:9), on checking:** "A cyclic preproof can be effectively checked for correctness by reduction to the inclusion of 'Büchi automata', yielding a PSPACE bound. As far as the author is aware, this is the best known upper bound, although no corresponding lower bound is known. … this is one of the reasons why we cannot hope for a 'polynomial simulation' of cyclic proofs in a usual proof system, and so why elementary simulations are more pertinent."
- **§10.2:** "the exponential simulation of CA by PA is optimal, unless there is a nondeterministic subexponential-time algorithm for PSPACE or, more interestingly, there is an easier way to check cyclic proof correctness. … PSPACE remains the best known upper bound for checking the correctness of general cyclic preproofs, although efficient algorithms have recently been proposed for less general correctness criteria, cf. [Str17, NST18]." And: "if CA were to have polynomial-size proofs of each correct Büchi inclusion then cyclic proof correctness would not be polynomial-time checkable, unless NP = PSPACE." (Conditional/heuristic; Das does not claim a proven lower bound for CA.)

Relevance (INFERENCE): F08/F09 — cyclic arithmetic and PA have the same theorems but the best known translation is exponential, and Das argues a *polynomial* simulation is unlikely because checking cyclic proofs is (as far as known) PSPACE, not P. A cyclic proof with the global trace condition is therefore, as far as known, NOT a Cook–Reckhow proof system (poly-time verifier) unless the trace condition is checked in P (conditional, see §3). This directly challenges any "basis-independence up to polynomial simulation" claim that includes cyclic systems.

---------------------------------------------------------------------------------------------------

## 3. Complexity of the trace/thread condition

### 3a. Nollet, Saurin, Tasson, TABLEAUX 2019 — ABSTRACT_ONLY
R. Nollet, A. Saurin, C. Tasson, "PSPACE-Completeness of a Thread Criterion for Circular Proofs in Linear Logic with Least and Greatest Fixed Points", TABLEAUX 2019, LNCS, pp.317–334, doi:10.1007/978-3-030-29026-9_18 (Crossref). HAL id hal-02173207 (HAL title says "Cyclic Proofs" instead of "Circular Proofs"). Abstract (HAL API, verbatim): "It is known that given a finite circular representation of a non-wellfounded preproof, one can decide in PSPACE whether this preproof is valid with respect to the thread criterion. We prove that the problem of deciding thread-validity for µMALL is in fact PSPACE-complete. Our proof is based on a deeper exploration of the connection between thread-validity and the size-change termination principle".
Hypotheses not verified beyond abstract: the result is for µMALL (multiplicative-additive linear logic with least/greatest fixed points), thread criterion, finite circular representation.

### 3b. Nollet, Saurin, Tasson, CSL 2018 — VERIFIED_SOURCE
"Local Validity for Circular Proofs in Linear Logic with Fixed Points", CSL 2018, LIPIcs vol.119, art.35. Retrieved https://drops.dagstuhl.de/storage/00lipics/lipics-vol119-csl2018/LIPIcs.CSL.2018.35/LIPIcs.CSL.2018.35.pdf.
- p.35:2: with the thread criterion "the logical correctness of circular proofs becomes a non-local property, much in the spirit of proof nets correctness criteria".
- Abstract: "a new fragment is described, based on a stronger validity criterion. This new criterion is based on a labelling of formulas and proofs, whose validity is purely local. … expressive enough to still contain all circular embeddings of Baelde's µMALL finite proofs with (co)inductive invariants … Moreover the Brotherston-Simpson conjecture holds for this fragment".
- Conclusion (§6): "turning a global and complex problem into a local and simpler one. Indeed, validity-checking is far from trivial … the best known bound for this problem being PSPACE." The finitizable labelled fragment "is too constrained to treat standard examples … namely: (i) interleaving of fixed-points and (ii) interleaving of back-edges resulting in various choices of a valid thread to support a branch."
Relevance (INFERENCE): F05 — direct prior art for "make a global criterion local by adding annotations": it succeeds only on a strict fragment (all embedded finitary proofs, but not all valid circular proofs).

### 3c. Baelde, Doumane, Kuperberg, Saurin, "Bouncing threads" — VERIFIED_SOURCE (arXiv:2005.08257v1, 17 May 2020; final venue not verified)
- Abstract: "We generalize the validity criterion for the infinitary proof system of the multiplicative additive linear logic with fixed points. Our criterion is designed to take into account axioms and cuts. We show that it is sound and enjoys the cut elimination property. We finally study its decidability properties, and prove that it is undecidable in general but becomes decidable under some restrictions."
- **Corollary 6.6:** "The problem of deciding whether a circular pre-proof of µMLLω is a proof is Σ01-complete." (Reduction from halting of 2-counter Minsky machines; §6.2.) Conclusion: "in the purely multiplicative fragment already, a parameter has to be bouned by an explicit value to make the criterion decidable."
Relevance (INFERENCE): F05/F07 — once cuts/axioms are allowed in circular proofs with a (natural, cut-eliminable) bouncing-thread criterion, validity of a *finite* circular object becomes undecidable (Σ01-complete). So even finite proof graphs need not have a decidable correctness predicate; a proof "algebra" over such objects cannot have decidable well-formedness = validity.

### 3d. Cohen, Jabarin, Popescu, Rowe, POPL 2024 — VERIFIED_SOURCE
"The Complex(ity) Landscape of Checking Infinite Descent", PACMPL 8(POPL) Art.46, 2024, doi:10.1145/3632888. Retrieved https://www.cs.bgu.ac.il/~cliron/pubs/POPL2024.pdf.
- Abstract: "The soundness of cyclic proof graphs is ensured by checking them against a trace-based Infinite Descent property. Although the problem of checking Infinite Descent is known to be PSPACE-complete, this leaves much room for variation in practice." Studied "in an abstract, logic-independent setting".
- Intro: "Deciding Infinite Descent has been shown to be PSPACE-complete [Lee et al. 2001; Nollet et al. 2019]." Automaton-based checks dominated by complementation "of complexity O(2^{k·log k})".
- §(Tractable restrictions): "Wehr [2023] also notes that checking Infinite Descent in 'reset' proof systems is polynomial, but that converting a general cyclic pre-proof into a reset pre-proof involves an exponential blowup in general." (Wehr 2023 itself NOT_ACCESSED → SECONDARY_ONLY.)
CAVEAT (my inference): the PSPACE-hardness cited is for abstract Infinite Descent / size-change termination (Lee–Jones–Ben-Amram 2001) and for µMALL threads (NST 2019). Das (2020) said no lower bound was known *for CA specifically*. I did not find a verified PSPACE-hardness proof specifically for CLKIDω/CA trace checking → status for CLKIDω: OPEN/UNCERTAIN (not verified).

---------------------------------------------------------------------------------------------------

## 4. Cook & Reckhow 1979 — VERIFIED_SOURCE
S. A. Cook, R. A. Reckhow, "The Relative Efficiency of Propositional Proof Systems", J. Symbolic Logic 44(1):36–50, March 1979. Retrieved https://www.cs.utoronto.ca/~sacook/homepage/cook_reckhow.pdf (JSTOR scan, stable URL http://www.jstor.org/stable/2273702). Page numbers = journal pages.

- **Def 1.3 (p.37):** "If L ⊆ Σ*, a proof system for L is a function f: Σ1* → L for some alphabet Σ1 and f in ℒ [polynomial-time computable functions] such that f is onto. We say that the proof system is polynomially bounded iff there is a polynomial p(n) such that for all y ∈ L there is x ∈ Σ1* such that y = f(x) and |x| ≤ p(|y|)."
- **Prop 1.4:** "A set L is in NP iff L = ∅ or L has a polynomially bounded proof system."
- **Def 1.5 (p.38):** "f2 p-simulates f1 provided there is a function g: Σ1* → Σ2* such that g is in ℒ, and f2(g(x)) = f1(x) for all x." (p-simulation = poly-time proof *translation* preserving the proved formula; nothing about proof identity.)
- Connective hypothesis (p.38): "K will always stand for an adequate set of propositional connectives which are binary, unary, or nullary … Adequate here means that every truth function can be expressed by formulas built up from members of K."
- **Def 2.1–2.2 (p.39):** "A Frege rule is a system of formulas (C1, ..., Cn)/D, where C1, ..., Cn ⊨ D. If n = 0, the rule is an axiom scheme. … An inference system is a finite set of Frege rules." "An inference system F is implicationally complete if A1, ..., An ⊢F B whenever A1, ..., An ⊨ B. A Frege system is an implicationally complete inference system."
- **Thm 2.3 (p.40):** "For any two Frege systems F1 and F2 over K there is a function f in ℒ and constant c such that for all formulas A1, ..., An, B and derivations π, if A1, ..., An ⊢π(F1) B then A1, ..., An ⊢f(π)(F2) B, and λ(f(π)) ≤ cλ(π) and ρ(f(π)) ≤ cρ(π)." (λ = number of lines, ρ = max formula size.)
- **Cor 2.4:** "Any two Frege systems over K p-simulate each other." Proof idea: replace each F1-rule instance by a substitution instance of a fixed F2-derivation of that rule (Lemma 2.5, closure under substitution). Linear blowup in lines.
- **Reckhow's generalization (p.40, SECONDARY w.r.t. Reckhow 1976 thesis):** "Reckhow [2] proves a generalization of the corollary to cover the case of Frege systems with different connective sets simulating each other, even when some of the connectives have arity greater than two. His proof is much more complicated … largely because of the difficulty of simulating systems using the connectives ≡ and ⊕ by systems without these connectives." ([2] = R. A. Reckhow, *On the lengths of proofs in the propositional calculus*, PhD thesis, Dept. of CS, Univ. of Toronto, 1976.)
- **Cor 3.4 (p.42–43):** "Let K be any adequate set of connectives. All Frege and natural deduction systems over K p-simulate all other Frege and natural deduction systems over K." Caveat (p.43): holds "for Gentzen systems with cut, provided a Gentzen proof is considered to be a sequence of sequents … as opposed to the more usual definition that a Gentzen proof is a tree of sequents. When a Gentzen proof is defined to be a tree, an exponential lower bound for the number of sequents in a minimum cut-free proof of a formula follows from an unpublished result of Statman."
- **Thm 4.5 (p.44):** extended Frege systems over K and K′: if every tautology over K has an eF proof with λ ≤ L(l(A)), then every tautology A′ over K′ has an eF′ proof with "λ(π′) ≤ cL(cl(A′)) and ρ(π′) ≤ cl(A′), where the constant c depends only on F and F′." **Cor 4.7:** "A given extended Frege system is polynomially bounded if and only if all extended Frege systems over all connective sets are polynomially bounded."
- **§5:** substitution rule; Thm 5.3: Frege + substitution p-simulates extended Frege (λ(f(π)) ≤ cλ(π)ρ(π)); converse "may be false". Substitution rule unsound for derivations from hypotheses.
Hypotheses to note: classical propositional logic only; finite rule set; each rule *sound*; implicational completeness (stronger than completeness for tautologies); connectives of arity ≤ 2 in the 1979 paper's own theorems (Reckhow's thesis covers higher arity — SECONDARY). Translation is on derivations; preserved: the conclusion and hypotheses (derivability), with linear size bounds; nothing about proof identity / normal forms.

Relevance (INFERENCE): F01/F08 — this is a known, classical *basis-independence* theorem: for classical propositional Frege systems, the choice of finite sound implicationally complete rule basis (and, per Reckhow, of adequate connective basis) is irrelevant up to p-simulation. Any ProofBasis claim of "basis-independence up to polynomial simulation" for propositional Frege is therefore *established prior art*, not novel. Strong limitation: it does NOT extend to tree-like vs dag-like (Cook–Reckhow's own caveat; §5), cut-free vs cut (§6), or cyclic systems (§2d, §3).

---------------------------------------------------------------------------------------------------

## 5. Ben-Sasson, Impagliazzo, Wigderson — ABSTRACT_ONLY
E. Ben-Sasson, R. Impagliazzo, A. Wigderson, "Near optimal separation of tree-like and general resolution", Combinatorica 24(4):585–603, 2004, doi:10.1007/s00493-004-0036-5 (Crossref). Preprint ECCC TR00-005 (2000), "Near-Optimal Separation of Treelike and General Resolution". Abstract read at https://eccc.weizmann.ac.il/report/2000/005 (verbatim): "constructing a natural family of contradictions, of size n, that have O(n)-size resolution refutations, but only exp(Ω(n/log n))-size tree-like refutations. … if S (S_T) is the minimal size of a (tree-like) refutation, we prove that S_T = exp(O(S log log S / log S))." Full text downloaded (IAS biw03.pdf and ECCC PDF) but text extraction produced garbage (Type-3 fonts); theorem numbers NOT verified.
Relevance (INFERENCE): F08/F09 — the *same rule set* (resolution) with a different proof-*shape* discipline (tree vs DAG, i.e. whether a derived line may be reused) differs exponentially. So "the basis" includes the sharing/structural discipline, not only the rule schemas.

---------------------------------------------------------------------------------------------------

## 6. Cut-elimination lower bounds

### 6c. Buss, JSL 2012 — VERIFIED_SOURCE (author final version)
S. R. Buss, "Sharpened lower bounds for cut elimination", J. Symbolic Logic 77(2), June 2012. Retrieved https://mathweb.ucsd.edu/~sbuss/ResearchWeb/lowerbdscutElim/JSL_FinalVersion.pdf.
- §1: "It is well-known that cut free proofs may need to be superexponentially larger than proofs that contain cut, as shown originally by Statman [21, 22] and Orevkov [15]." Superexponential: 2^n_0 = n, 2^n_{k+1} = 2^{2^n_k}. Upper bound (cited): depth-d proof P → cut-free proof of size 2^{h(P)}_{d+1}.
- **Thm 1:** "There are proofs Pℓ of sequents Sℓ of depth d and height O(d) such that any cut free proof of Sℓ requires size 2^0_{(1/2)d}. The formulas in Sℓ are purely universal and have depth O(1)." (reproves Statman/Orevkov-type bounds)
- **Thm 2:** "There is a constant c ∈ N and proofs Pℓ of depth ≤ ℓ + c and height O(ℓ) such that every cut free proof Qℓ with the same conclusion as Pℓ has height at least 2^0_ℓ. Furthermore, the same holds for Qℓ containing cuts on only quantifier-free formulas." Thm 3: same in a purely relational language.
- Refs as printed: [15] Orevkov, "Lower bounds for lengthening of proofs after cut-elimination", J. Soviet Math 20 (1982) 2337–2350 (Russian: Zap. Nauchn. Sem. LOMI 88 (1979) 137–162); [21] Statman, "Lower bounds on Herbrand's theorem", PAMS 75(1) (1979) 104–107; [22] Statman, "Speed-up by theories with infinite models", PAMS 81 (1981) 465–469.

### 6a/6b. Statman 1979, Orevkov 1979/82 — NOT_ACCESSED; SECONDARY_ONLY
Moser & Zach, "The Epsilon Calculus and Herbrand Complexity", arXiv:math/0510640v1 (forthcoming Studia Logica 2005), VERIFIED text: "Statman [22] and Orevkov [21] showed that this bound is not just an artefact of the particular cut-elimination procedure considered, but that proofs with cut essentially have hyper-exponential speedup over cut-free proofs." "(Statman's result requires equality, but Orevkov's does not.)" Orevkov example per Troelstra–Schwichtenberg §6.11: Hyp1 ≡ ∀x R(x,0,S(x)); Hyp2 ≡ ∀y∀x∀z∀z1 (R(y,x,z) ∧ R(z,x,z1) → R(y,S(x),z1)); Ck ≡ ∃zk…∃z0 (R(0,0,zk) ∧ R(0,zk,zk−1) ∧ ··· ∧ R(0,z1,z0)); R(n,m,k) expresses n + 2^m = k. Proofs with cut linear in k; Herbrand complexity ≥ 2^1_k (Thm 23 there).

### 6d. Boolos 1984 — NOT_ACCESSED
G. Boolos, "Don't eliminate cut", J. Philosophical Logic 13(4):373–378 (Nov 1984), doi:10.1007/BF00247711 (Crossref gives volume/issue; pages from a search snippet only). Content (an inference with a short derivation using cut but astronomically long cut-free derivation): UNVERIFIED-MEMORY. Do not cite specific numbers.

### 6e. Statman, "The typed λ-calculus is not elementary recursive", TCS 9(1):73–81, 1979, doi:10.1016/0304-3975(79)90007-0 (FOCS 1977 version pp.90–94, doi:10.1109/SFCS.1977.34) — NOT_ACCESSED. Content (deciding βη-equality of simply typed terms is not elementary recursive): UNVERIFIED-MEMORY.

Relevance (INFERENCE): F09 — eliminating a single rule (cut) preserves derivability but can cost a tower of exponentials (non-elementary); hence "rule set A and rule set B derive the same things" says nothing about polynomial simulation. Any basis claim must state the size measure. If Statman's TCS result is confirmed, F04 also bites: deciding *proof identity* under βη (normalisation-based identity) for simply typed proofs is non-elementary, so a "declared proof-identity congruence" may be decidable but infeasible.

---------------------------------------------------------------------------------------------------

## 7. Infinitary / non-effective boundary

### 7a. ω-rule — Frittaion, arXiv:2110.01270v1 (4 Oct 2021) — VERIFIED_SOURCE (secondary for Shoenfield/Schütte)
- Abstract: "Shoenfield's completeness theorem (1959) states that every true first order arithmetical sentence has a recursive ω-proof encodable by using recursive applications of the ω-rule. … We also show that the set of codes of ω-proofs, whether it is based on recursive or primitive recursive applications of the ω-rule, is Π11 complete. The same Π11 completeness results apply to codes of cut free ω-proofs."
- Intro p.2: "Shoenfield's completeness theorem [11], which asserts that the recursive ω-rule is complete for true arithmetical statements. (That this holds good for the unrestricted ω-rule is almost trivial, by induction on the build up of a true sentence.)" "Shoenfield's completeness theorem says that an arithmetical sentence A is true if and only if there is a recursive local code of an ω-proof of A." Thm 2.3: Π11-completeness of the code set (author: "The author was not able to find this result in the literature").
- Ref [11]: J. R. Shoenfield, "On a restricted ω-rule", Bull. Acad. Polon. Sci. Sér. Sci. Math. Astr. Phys. 7:405–407, 1959 (NOT_ACCESSED).
- SEP "Proof Theory" (via WebFetch summary; treat as SECONDARY): "The infinitary version of PA with the ω-rule was investigated by Schütte (1950)."
CORRECTION to task framing: the *set of theorems* of PA+ω-rule is true arithmetic (sound + complete for truth), which is not arithmetical (Tarski; Frittaion p.~ mentions TA not arithmetically definable — paraphrase) hence not r.e.; it is the *set of proof codes* that is Π11-complete (Frittaion Thm 2.3). That TA itself is Δ11 (hyperarithmetic, ≡T 0^(ω)) rather than Π11-complete is UNVERIFIED-MEMORY.

### 7b. Second-order logic — SEP (Väänänen), VERIFIED_SOURCE (secondary)
J. Väänänen, "Second-order and Higher-order Logic", Stanford Encyclopedia of Philosophy, first published 2019-08-01, substantive revision 2024-08-31; https://plato.stanford.edu/entries/logic-higher-order/.
- §1: "there was a simple finite categorical—hence complete (§10)—axiomatization of the structure (ℕ, +, ×) in second-order logic … This showed that there cannot be such a complete axiomatization of second-order logic as there was for first order logic."
- §5.1: "We know that truth of first order sentences in (ℕ,+,·,0) is undecidable, and even non-arithmetical by results of Gödel (1931) and Tarski (1933). This shows that second-order logic is not completely axiomatizable by effective means, or decidable even in the empty vocabulary."
- §5.2: "there is no hope of a Completeness Theorem for second-order logic." §9.1: Henkin (1950) completeness holds w.r.t. general (Henkin) models.
- Thm 4 (attrib. Tharp 1973 in the entry): "The set of Gödel numbers of valid second-order sentences is the complete Π2-set of natural numbers" — Π2 here is in the **Lévy hierarchy of set theory** (the entry is comparing with "the Levy hierarchy Σn ∪ Πn in set theory"), not arithmetical Π2.
- Shapiro 1991 ch.4: NOT_ACCESSED.

Relevance (INFERENCE): F07 — two canonical "proof forms" lie outside any finite effective algebra: ω-proofs (well-founded infinite trees; proof codes Π11-complete; theorems = TA, not r.e.) and standard-semantics second-order consequence (no effective sound+complete calculus). Plus LKIDω (§1b): even recursive non-wellfounded proofs are not semi-decidably recognisable. A project claiming "all foundations" must explicitly exclude these or restrict to Henkin semantics / regular (cyclic) proofs.

---------------------------------------------------------------------------------------------------

## 8. Cyclic vs inductive: computation, normalisation, cut

### 8a. Kuperberg, Pinault, Pous, POPL 2021 — VERIFIED_SOURCE
D. Kuperberg, L. Pinault, D. Pous, "Cyclic Proofs, System T, and the Power of Contraction", PACMPL 5(POPL), Art.1, 28pp., Jan 2021, doi:10.1145/3434282. Retrieved https://perso.ens-lyon.fr/denis.kuperberg/papers/popl21.pdf. (Task said "Das" — incorrect attribution.)
- Abstract: "We study a cyclic proof system C over regular expression types … Proofs in C can be seen as strongly typed goto programs. … In the general case, we prove that the two systems capture the same functions on natural numbers. In the affine case, i.e., when contraction is removed, we prove that they capture precisely the primitive recursive functions … Without contraction, we manage to give a direct and uniform encoding of C into T … Whether such a direct and uniform translation from C to T can be given in the presence of contraction remains open." Upper bounds via weak normalisation formalised in ACA0 (Thm 6.4) and RCA0 (Thm 6.12).
Relevance (INFERENCE): F04 — even where cyclic and inductive systems are extensionally equal (same definable functions), a *uniform, structure-preserving* proof translation is open in the contraction case; so no proof-identity-preserving translation is currently known there.

### 8b. Oda & Kimura, arXiv:2203.05791v2 (5 Mar 2025) — VERIFIED_SOURCE
"A study for recovering the cut-elimination property in cyclic proof systems by restricting the arity of inductive predicates". Abstract: "Recent researches have shown that the cut-elimination property … of cyclic proof systems for several logics does not hold. … This paper shows that the cut-elimination property still fails in a simple cyclic proof system even if we restrict languages to unary inductive predicates and unary functions". Intro: "The open problem about the cut-elimination property of CLKIDω by Brotherston was negatively solved in the first authors' recent work [13]" ([13] = Masuoka & Tatsuta, arXiv:2106.11798, 2021 — NOT_ACCESSED). Corollary 31: "We do not eliminate the cut rule in CLKIDω if we restrict predicates in the language to unary" (sentence truncated in extraction; counterexample sequent TeF(s) ⊢ FsT(e)).
Relevance (INFERENCE): F04/F09 — proof identity via cut-elimination/normal forms, standard for well-founded sequent calculi, is unavailable for CLKIDω; the cut-free fragment is strictly weaker.

---------------------------------------------------------------------------------------------------

## Synthesis against threats (INFERENCE unless marked)

- **F05 (global correctness).** Established: CLKIDω correctness is a global ω-regular condition (Brotherston thesis Prop 5.1.10, sketch; LMCS BT Def 4.3), decidable via Büchi automata; best known general upper bound PSPACE; PSPACE-complete for µMALL thread criterion (NST 2019, abstract only) and for abstract Infinite Descent (Cohen et al. 2024, citing Lee et al. 2001 + NST 2019). For CLKIDω/CA specifically a matching lower bound was reported unknown as of Das 2020; status for those: OPEN/UNCERTAIN. With cuts + bouncing threads (µMLLω) validity is Σ01-complete (undecidable). Local certification exists only for fragments (labellings NST 2018; reset proofs — Wehr 2023 via Cohen et al., exponential conversion). ⇒ A finite set of *local* operators whose well-formedness is checkable per node cannot coincide with CLKIDω validity unless P = PSPACE-type collapses are avoided by an exponential annotation, or the global condition is placed outside the algebra (an F03-type hidden trusted check).
- **F01/F04 (cyclic vs inductive).** Brotherston–Simpson conjecture is FALSE in general (BT LMCS 2019 Thm 8.3), TRUE with PA/HA added (BT LICS 2017 — secondary; Simpson 2017 for CA — secondary; BT arXiv:1712.03502 Thm 6.14 intuitionistic). Size: CA→PA exponential (Das Thm 6.10); PA→CA (logical-complexity-preserving) non-elementary. Cut not eliminable in CLKIDω.
- **F07.** LKIDω proofs not semi-decidable; ω-rule proof codes Π11-complete; standard SOL not effectively axiomatizable.
- **F08 (basis).** Cook–Reckhow Cor 2.4 / Cor 3.4 / Reckhow 1976 (secondary) / Thm 4.5: classical *propositional* Frege, natural deduction (dag), extended Frege are basis-independent up to p-simulation (eF: also across connective sets). This is established prior art for a "basis-independence" claim in the propositional case. Not novel.
- **F09 (blowups).** Tree-like vs dag resolution: exp(Ω(n/log n)) vs O(n) (BIW 2004, abstract). Cut elimination: superexponential, tower height ≈ depth (Buss 2012 Thm 2; Statman/Orevkov secondary). Cyclic→inductive: exponential (best known), with a conditional argument that polynomial is unlikely.

## Unresolved / not accessed (for follow-up)
Brotherston–Simpson JLC 2011 text; Berardi–Tatsuta FoSSaCS 2017 and LICS 2017 texts; Simpson FoSSaCS 2017; NST TABLEAUX 2019 full text (theorem statement and hypotheses); BIW full text (theorem numbering); Statman PAMS 1979; Orevkov 1979/82; Boolos 1984; Statman TCS 1979; Reckhow 1976 thesis; Afshari–Wehr MSCS 2024; Wehr 2023; Masuoka–Tatsuta 2021; Shapiro 1991; Schütte; Pohlers; Shoenfield 1959; Das & Pous, Afshari–Leigh.
