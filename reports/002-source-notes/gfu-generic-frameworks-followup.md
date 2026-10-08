# Notes [gfu]: generic frameworks — follow-ups (LSR conjecture, classical coverage, undecidable structural data, adjoint logic, bipoles)

Builds on scratchpad/review/notes/gen.md (LSR17, LS16, Shulman LNL 2023, PCPR18 manuscript, MTT, Gratzer
normalization, Zeilberger, Uemura, Kaposi–Xie). That work is NOT redone here.
Download dir: scratchpad/t002/dl/gfu/ (PDF -> `pdftotext -layout`). Line refs (l.N) are to those .txt files.
Date of search: 2026-10-08. Web search + Semantic Scholar citation list for LSR17 (DOI 10.4230/LIPIcs.FSCD.2017.25)
used to find follow-ups.

---------------------------------------------------------------------------------------------------
## Q1. Status of LSR's equational-adequacy conjecture (LSR FSCD 2017 p.25:17; ext. version Conjecture 8.5)

### Search method and result
- Semantic Scholar "citations" API for DOI 10.4230/LIPIcs.FSCD.2017.25 returned ~60 citing works (2017–2025).
  Titles screened; none has a title indicating equational adequacy / completeness of permutative equality for
  LSR. Relevant hits retrieved and read below (Riley thesis, Shulman MATT, Blanco thesis, Clarke–Scherer–
  Zeilberger, Pruiksma thesis, Jang et al.). Web search for "equational adequacy" + LSR found nothing new.
- **Finding: no source retrieved proves or refutes LSR Conjecture 8.5 / equational adequacy for the LSR
  framework.** Status: OPEN as far as this search found (absence-of-evidence; not exhaustive — Google Scholar
  not queried, Licata's pubs page returned HTTP 503, Riley's homepage copy of the LSR extended version could not
  be fetched (TLS certificate mismatch on mvr.hosting.nyu.edu; TLS verification not disabled), so a later revision of
  the extended version, if any, was not checked).

### G1. Mitchell Riley, "A Bunched Homotopy Type Theory for Synthetic Stable Homotopy Theory", PhD thesis,
Wesleyan University, May 2022 (advisor D. R. Licata). (The "Linear HoTT" title is a 2022 talk, not the thesis.)
- URL: https://ncatlab.org/nlab/files/Riley-BunchedHoTT.pdf (thesis PDF). DOI 10.14418/wes01.3.139 reported by
  search engine only — NOT seen on the document. STATUS: VERIFIED_SOURCE (text grepped).
- Does NOT address LSR equational adequacy. Relevant verbatim passages:
  - l.7782–7789: "Some additional related work develops frameworks for modal type theories in general [LSR17; LRS22;
    GKNB20], but our setting is not quite an instance of these frameworks. The first [LSR17] lacks dependent types,
    but can describe the simply-typed fragment of our type theory. The in-progress extension of this work to
    dependent types [LRS22] should be able to capture the same semantic situation".
  - l.12783: "We anticipate that the fibrational framework [LSR17; LRS22] (once appropriately extended to dependent
    types), will be able to capture the rules of our theory, if not useful strict equalities on raw syntax."
  - Bibliography l.13413: "[LRS22] Daniel R. Licata, Mitchell Riley, and Michael Shulman. 'A Fibrational Framework
    for Substructural and Modal Dependent Type Theories'. 2022. In preparation."
  - INFERENCE: the dependent LSR extension was still unpublished in 2022; I found only 2019 talk slides
    (HoTTEST 2019, Licata) — NOT_ACCESSED by me.

### G2. Michael Shulman, "Semantics of multimodal adjoint type theory", MFPS XXXIX, ENTICS vol. 3 (2023),
DOI 10.46298/entics.12300 (printed on PDF, l.51). URL: https://arxiv.org/pdf/2303.02572v5 (ENTICS layout; pages
"18–n"). STATUS: VERIFIED_SOURCE.
- Not about equational adequacy. Its verdict on LSR, verbatim (§1, l.38): "the 'LSR' theory of [26,27] is only
  simply typed, its definitional equality is ill-behaved, and it uses awkward global context operations."
- Decidability, verbatim (Remark 2.6, p.18–5/18–6): "It seems likely that normalization for MTT [10] extends to
  MATT. But to deduce decidability of type-checking from this requires decidability of equality for M, whereas
  L[S†] can fail to have decidable equality even if L does [7]. However, we can hope that L[S†] will have
  decidable equality if L is, say, locally finite (this is true for for 1-categories [6])." [7] = Dawson, Paré,
  Pronk 2003 (see G8).
- Open problem (iv), §conclusion: "Does MATT satisfy normalization, and which (L, S) are decidable?"
  (vi): "In [27], simple modal type theories were unified with substructural ones. Is there a context-lock
  approach to substructurality? Can it be unified with modal dependent type theory?"
- Classical: no (MLTT-based; "classical" only in the sense of Set-valued mode, l.925).

### G3. Clarke, Scherer, Zeilberger, "The free bifibration on a functor", arXiv:2511.07314v3 (15 Jan 2026), preprint
(LMCS-style layout; publication venue not verified). URL: https://arxiv.org/pdf/2511.07314. STATUS: VERIFIED_SOURCE.
**Most relevant advance found** — but for a UNARY (category, not multicategory) analogue of LSR, not for LSR itself.
- Motivation explicitly cites LSR (l.291–293): substructural and modal logics "may be naturally modelled in certain
  bifibrations ... Licata, Shulman, and Riley [38]"; the calculus is "inspired in part ... from the bifibrational
  calculus of Licata, Shulman, and Riley [38]" (l.1301).
- Abstract: "a construction of the free bifibration Λp : Bif(p) → C in which objects of Bif(p) are formulas of a
  primitive 'bifibrational logic', and arrows are derivations in a cut-free sequent calculus modulo a notion of
  permutation equivalence."
- Thm 1.17 (l.1126): "Λp : Bif(p) → C is the free bifibration on p : D → C."
  INFERENCE: this is the unary analogue of what LSR ext. "conjecture" ("the syntax is the initial bifibration over
  M") + Conjecture 8.5 (cut-free derivations modulo permutations ≡ full equational theory) would give — here
  PROVED, but only for a 1-category base (single hypothesis, no multicategory/products), so it does not settle LSR.
- Decidability (Thm 3.27, l.3381, "cf. Theorems 2 and 3 of Dawson, Paré, and Pronk"): "There is a category C with
  locally finite factorizations for which the following equivalent problems are both undecidable: • given two
  stacks of double cells in Z(C), determine whether they vertically compose to the same double cell; • given two
  proofs in the bifibrational calculus generated by p = id_C, determine whether they are permutation equivalent."
  Proof uses C = C_{G_M}, "the subcategory of Set generated by" 0,1,V,W,E and constants for every vertex/edge of a
  bipartite configuration graph of a universal Turing machine M (l.3326–3340) — i.e. a base category with
  INFINITELY many generating arrows (computable, but not finitely presented).
- Thm 3.28 (l.3417): if C "is locally finite, or ... factorization preordered; then for any two proofs α1, α2 ...
  it is decidable whether α1 ∼ α2." Plus constructive caveats (l.3440–3446): must be able to enumerate homsets,
  decide squares, "equality of morphisms in C and D to be decidable".
- Canonical forms (Thm 3.23 / Cor 3.25): under the FP condition, unique maximally multifocused derivations.
- Relevance (INFERENCE): (a) F04/R3: In the simplest LSR-like setting, proof identity = permutation equivalence
  of cut-free proofs (proved), and it is UNDECIDABLE for some (infinite, computable) mode data. Proof identity
  decidability is therefore a property of the per-logic mode data, not of the fixed framework. (b) LSR Conj. 8.5
  remains open in the multicategorical case.

### G4. Nicolas Blanco, "Bifibrations of polycategories and classical multiplicative linear logic", PhD thesis,
Univ. Birmingham, March 2023; arXiv:2305.15139v1. STATUS: VERIFIED_SOURCE (abstract, TOC, grep).
- Semantic (category theory): representability, bifibrations of polycategories, lifting models (FVect→FBan),
  polycategorical Bénabou–Grothendieck. Cites LSR only for pushforward/pullback (l.9115). No syntactic
  equational-adequacy result; scope = classical MULTIPLICATIVE linear logic only. Not LK.
- (Blanco & Zeilberger, ENTCS 352 (2020) 29–52 — NOT_ACCESSED; bibliographic data from search engine only.)

### Q1 verdict
- ESTABLISHED (since 2017): unary analogue (free bifibration = cut-free derivations mod permutation) — G3 Thm 1.17
  (preprint, not peer-review-verified by me); undecidability of permutation equivalence for some infinite
  computable base — G3 Thm 3.27, and DPP 2003 for free adjoints (G8).
- OPEN: LSR Conjecture 8.5 and equational adequacy for LSR mode theories (no proof/refutation found).
  The dependent extension (LRS) was "in preparation" (Riley 2022); Shulman 2023 calls LSR's definitional equality
  "ill-behaved" and the field (MTT/MATT) moved to context-lock frameworks where the analogous decidability
  question is again open ("which (L,S) are decidable?").

---------------------------------------------------------------------------------------------------
## Q2. Does any generic framework cover CLASSICAL multi-conclusion NON-linear logic (LK)?

Summary table (per-logic data vs fixed part; what is proven):
| Framework | LK native? | LK via translation? | Level of adequacy proven |
|---|---|---|---|
| LSR17 | No ("single-conclusioned"; classical = future work) | none stated | — |
| LS16, MTT, MATT, PCPR adjoint logic, Pruiksma 2024, Jang et al. 2024 | No (intuitionistic) | none stated | — |
| Shulman LNL doctrines 2023 | No (classical LINEAR only; nonlinear side cartesian multicategory) | not claimed | — |
| Blanco 2023 | No (classical MLL only) | — | semantic |
| Zeilberger 2008 | provability via polarization | yes, Thm 27 focusing completeness | provability; proof identity depends on chosen polarization |
| Miller–Pimentel 2013 (focused classical LL as meta-logic) | **LK specified as a theory** | yes | Thm 6: relative completeness (provability) PROVED; "full completeness of proofs" asserted informally; "full completeness of derivations" NOT achieved for these specs |
| Marin–Miller–Pimentel–Volpe 2022 (LKF) | LK + bipolar axioms | LK ↔ LKF | Thm 4/6: rule-by-rule correspondence of derivations (non-structural rule ↔ synthetic rule) |

### G5. Dale Miller & Elaine Pimentel, "A formal framework for specifying sequent calculus proof systems",
Theoretical Computer Science 474 (2013) 98–116 (venue data from search engine/IP-Paris portal — not printed on
retrieved copy). URL: https://www.lix.polytechnique.fr/~dale/papers/Llinda.pdf = author preprint "Preprint
submitted to Elsevier November 6, 2012" (l.49). Page numbers below are preprint pages. STATUS: VERIFIED_SOURCE (preprint).
- Fixed part: focused classical linear logic LLF (Andreoli), Thm 1 (l.171) "If B is a linear logic formula, then
  ⊢LL B if and only if the sequent ·; · ⇑ B is provable in LLF". Object-level formulas encoded with predicates
  ⌈·⌉ (right) and ⌊·⌋ (left).
- Per-logic data: a "proof system theory": "a finite set of linear logic formulas all of which are either Init,
  Cut, Neg, or Pos of Figure 5 or an introduction clause as given by Definition 4" (§5, l.940). These clauses ARE
  the object logic's inference rules, placed in the environment (F03, INFERENCE) — but restricted in shape.
- Def. 3 (monopole/bipole, l.276): "A monopole formula is a linear logic formula that is built up from atoms and
  occurrences of the negative connectives, with the restriction that ? has atomic scope. A bipole is a positive
  formula built from monopoles and negated atoms using only positive connectives, with the additional restriction
  that ! can only be applied to a monopole."
- Def. 4 (introduction clause, l.347): "a closed bipole formula of the form ∃x1...∃xn[(q(⋄(x1,...,xn)))⊥ ⊗ F]
  where ⋄ is an object-level connective of arity n (n ≥ 0) and q ∈ Q. Furthermore, F does not contain negated
  atoms and an atom occurring in F is either of the form p(xi) or p(xi(y)) ..." (i.e. one connective, immediate
  subformulas only — a syntactic "fundamentality" restriction).
- Three adequacy levels (§3.4, l.512–520), verbatim: "relative completeness: ... an object-level sequent has a proof
  if and only if the corresponding meta-level sequent has a proof. The second level of adequacy is based on full
  completeness of proofs: that is, the proofs of an object-level sequent are in one-to-one correspondence with the
  meta-level proofs of the specifications of the object sequent. Finally, the most restrictive level of adequacy is
  based on full completeness of derivations: that is, the object-level derivations (partial proofs, such as
  inference rules themselves) are in one-to-one correspondence."
- Thm 6 (l.604): "The sequent −→ B has a linear logic proof if and only if the sequent LL, Cut, Init; ⌈B⌉ ⇑ · is
  provable in linear logic; has an LK proof if and only if LK, Cut, Init, Pos, Neg; ⌈B⌉ ⇑ · is provable in linear
  logic; and has an LM proof if and only if LM, Cut, Init, Pos; ⌈B⌉ ⇑ · is provable".
  Following text (l.617–621): "While this proposition states that these proof system specifications are adequate at
  the level of relative completeness ..., the direct proofs of these statements easily show that the actual
  adequacy result is at the level of full completeness of proofs. As the next example illustrates, adequacy at the
  level of full completeness of derivations is not achieved by these specifications".
  => LK: provability PROVED; bijection of proofs CLAIMED ("easily show", no written proof) — informal argument;
  derivation-level not achieved (Example 7 for LM). LJ only at "relative completeness" (Example 8, l.708).
  No proof-identity (equational) theory for LK is addressed.
- Limitation stated (l.818–823): a multi-conclusion intuitionistic system IIL* "is not composed of introduction
  clauses ... it is impossible to specify IIL* in our setting using only 'one-headed' clauses ... Linear logic
  allows only for one linear and one classical context, a shortcoming that can be overcome by using
  subexponentials [24, 34]."
- Non-bipole failure (l.905–909): "if a clause has a body that is not a bipole, then the meta-level can take steps
  that are not available at the object-level and, as a result, the meta-level specification of inference rules
  might not be adequate."
- Decidable meta-theory for the restricted class (Q5): Prop. 13 (l.963), Prop. 16 (l.1000) "Let ∆ be a (cut-free)
  proof system theory and let D be an introduction clause. It is decidable whether or not the sequent ∆; · ⇑ D⊥ is
  provable." Def. 17 (l.1098) canonical clause/theory; Def. 18 cut-coherence ("the sequent Cut; · ⇑ ∀x̄(Fl⊥ ⅋ Fr⊥)
  is provable in LLF"); Prop. 20 + Prop. 21 (cut reduces to atomic cut, atomic cut eliminable for cut-coherent
  theories); Thm 22 (l.1222): "Determining whether or not a canonical proof system is cut-coherent is decidable.
  ... achieved by proof search in LLF bounded by the depth v + 3 where v is the maximum number of premise atoms in
  the bodies of the introduction clauses." Def. 24/25 initial-coherence, coherent theory; Thm 27 (l.1347)
  non-atomic initial rules eliminable for coherent theories.
- Relevance (INFERENCE): F01 — a fixed meta-logic (focused LL) with a syntactic restriction (canonical bipole
  clauses) DOES cover LK, LJ, LL, LM, and decides cut-coherence; this is a strong prior-art "fixed framework +
  restricted per-logic rule data" result for derivability, but NOT for proof identity (R3), and the per-logic data
  are rule clauses (F03 — trusted rules in environment, though shape-restricted).

### G6. Nigam, Pimentel, Reis subexponential extension ("An extended framework for specifying and reasoning
about proof systems", J. Logic Comput.; year/volume inconsistent in DBLP per search engine). STATUS: SECONDARY_ONLY
(search-engine abstract): claims encodings of "a multi-conclusion intuitionistic logic, classical modal logic S4,
and intuitionistic Lax logic" and methods for checking cut-elimination, atomic identity, invertibility. Not read.

### Zeilberger and Shulman LNL: see gen.md S6, S3 (not redone).

---------------------------------------------------------------------------------------------------
## Q3. Can per-logic structural data encode computation (undecidable derivability / proof identity)?

Two distinct phenomena — keep separate:
(A) Undecidability arising from a FIXED, tiny structural datum (the logic itself is undecidable) — e.g. one
    contractible subexponential. Data does not "encode a machine"; the formulas do.
(B) Undecidability where the per-logic data (signature / mode theory / non-logical axioms / rule set) itself
    encodes an arbitrary machine — the "trusted computation in the environment" threat (F02/F03).

### G7. Kanovich, Kuznetsov, Nigam, Scedrov, "Subexponentials in non-commutative linear logic", MSCS 29(8) (2019)
(journal data from search engine; Cambridge DOI 10.1017/S0960129518000117 from search engine only). Retrieved:
arXiv:1709.03607v1 (11 Sep 2017) — preprint; page refs are arXiv pages. STATUS: VERIFIED_SOURCE (preprint).
- Per-logic data = subexponential signature (l.132–141), verbatim: "Σ = ⟨I, ⪯, W, C, E⟩, where I = {s1,...,sn} is a
  set of subexponential labels with a preorder ⪯, and W, C, and E are subsets of I. The sets W, C, and E are
  required to be upwardly closed with respect to ⪯. ... Since contraction (in the non-local form, see below) and
  weakening yield exchange, here we explicitly require W ∩ C ⊆ E."
- Thm 1 (l.334): "A sequent is derivable in SCLLΣ +(cut) if and only if it is derivable in SCLLΣ." (for all Σ)
  Cut elimination depends on "the ⪯ relation is transitive and that the sets W, C, and E are upwardly closed"
  (l.379–381) and on contraction being non-local.
- Thm 7 (l.1161): "The extension of the Lambek calculus with a unary connective ! axiomatised by rules (! →), (→ !),
  (contr), and, optionally, (weak) does not admit (cut)." (counterexample r/q, !p, !(p\q), q\s → r·s) — i.e. the
  naive local-structural-rule datum breaks the framework's generic cut theorem.
- Thm 8 (l.1221): "If C ≠ ∅ (i.e., at least one subexponential allows the non-local contraction rule), then the
  derivability problem in SLC1Σ is undecidable." Proof encodes semi-Thue systems (Markov–Post, Thm 9) in formulas.
  Thm 12 / Cor 13 / Cor 14 (l.1384–1390): same for SLCΣ, SMALCΣ, SCLLΣ whenever C ≠ ∅.
- Thm 15 (l.1397): "If C = ∅, then the decidability problem for SCLLΣ belongs to PSPACE and the decidability problem
  for SMCLLΣ belongs to NP."
- INFERENCE: phenomenon (A). Derivability is decidable/undecidable as a function of the structural datum
  (C = ∅ vs C ≠ ∅); a single bit of per-logic data flips decidability. The undecidable instance's computation is in
  the end-sequent's formulas, not in Σ.

### G8. Dawson, Paré, Pronk, "Undecidability of the free adjoint construction", Applied Categorical Structures 11
(2003) 403–419 (data from MATT/CSZ bibliographies, DOI 10.1023/A:1025712521140 printed in MATT ref [7]).
Retrieved: author preprint dated August 1, 2002, https://mathstat.dal.ca/~pare/UndecidabilityFreeAdjoints.pdf.
STATUS: VERIFIED_SOURCE (preprint).
- Abstract: "show how the equivalence relation on the 2-cells for an appropriately chosen category CA can be used to
  simulate a 2-register abacus A, so that deciding whether two 2-cells with different representatives are equal
  becomes equivalent to solving the halting problem for the abacus. In particular, this implies that (in general)
  equality of 2-cells in such categories is undecidable."
- Thm 1 (l.808); Thm 3 (l.920): "The equivalence of fences over Set is undecidable." Cor 1: "If Set is a full
  subcategory of C, then the equivalence of fences over C is undecidable." Prop. 2/3 (l.943/965): decidable if C is
  locally finite / satisfies condition (15) (factorization preordered).
- Caveat (verified, l.619–633): C_A has 8 objects but infinite hom-sets {xm | m ∈ N}, {yn | n ∈ N}, {cs | s ∈ S}
  with relations — not a finite category.
- Relevance (INFERENCE): phenomenon (B) for PROOF IDENTITY: freely adding adjoints (what F⊣U / MATT co-dextrification
  do to mode data) can turn a mode theory with decidable equality into one with undecidable 2-cell equality
  (MATT Remark 2.6 states exactly this). Note: the base is infinite; I found no statement that a FINITE base
  category already yields undecidability.

### G9. Kanovich, Kuznetsov, Scedrov, "Reconciling Lambek's restriction, cut-elimination, and substitution in the
presence of exponential modalities", arXiv:1608.02254v2 (9 May 2019), "Preprint submitted to Annals of Pure and
Applied Logic". STATUS: VERIFIED_SOURCE (preprint).
- Thm 1 (l.113): "The derivability problem for EL∗ is undecidable." (Lambek + full exponential; credited to
  Kanovich 1993 CSLI report [9], de Groote 2005 [10] — SECONDARY_ONLY.)
- Buszkowski's theorem as restated (l.649–660, 691–700): "by L + A we denote L augmented with sequents from A as new
  axioms ... Further we consider non-logical axioms of a special form: either p, q → r, or p / q → r, where p, q, r
  are variables. ... L + A can be formulated in a cut-free way [19]: instead of non-logical axioms ... we use rules
  [(red1): from Π1 → p and Π2 → q infer Π1, Π2 → r; (red2): from Π, q → p infer Π → r] ... This calculus admits the
  cut rule [19]." "Theorem 9. Every language generated by a generative grammar can be generated by an L/-grammar with
  special non-logical axioms." "Theorem 10. There exists such A that the derivability problem for L/ + A is
  undecidable." [19] = W. Buszkowski, "Some decision problems in the theory of syntactic categories", Z. Math. Logik
  Grundlagen Math. 28 (1982) 539–548, doi 10.1002/malq.19820283308 (printed in KKS bibliography). Buszkowski paper
  itself: SECONDARY_ONLY.
- Relevance (INFERENCE): phenomenon (B) for DERIVABILITY with a strikingly "innocent" rule format: per-logic
  rules that are atomic, cut-admissible, and look like ordinary 2-premise sequent rules suffice to encode any r.e.
  language. So "cut-admissible + local + atomic rule shape" is NOT an anti-vacuity criterion against encoding
  computation in the environment. (Whether A is finite: the quoted Theorem 10 says "There exists such A";
  finiteness is UNVERIFIED in the text I read — Buszkowski's original should be checked.)

### G10. Chvalovský & Horčík, "Full Lambek calculus with contraction is undecidable", JSL 81(2) (2016) 524–540,
DOI 10.1017/jsl.2015.18 — STATUS: SECONDARY_ONLY (search engine summary; not retrieved). Claimed: FL + contraction
(a single added structural rule) has undecidable provability; positive fragment already undecidable. Phenomenon (A).

### G11. LSR / Licata–Shulman remarks on undecidable mode theories
- LS16 (gen.md S2, VERIFIED there): "An alternative would be to give a syntax and explicit equality judgement for the
  mode category, which would be helpful if we needed a mode theory where equality of morphisms or 2-morphisms were
  undecidable." LSR ext.: meta-level quotient equality, decidability not addressed. MATT Remark 2.6 (G2). Gratzer
  Remark 7 (gen.md S5b). No theorem in LSR/LS16 on undecidable mode theories.
- INFERENCE (not stated in any source read): LSR mode theories permit directed structural axioms α ⇒ α′ on
  context-descriptor terms of a finitely presented signature. Such axioms are semi-Thue rules; since derivability
  of a hypothesis/F-rule requires exhibiting a 2-cell β ⇒ α, it is plausible that word-problem/semi-Thue
  reachability reduces to LSR derivability for some finite mode theory, making derivability undecidable. This is
  an unproved conjecture of mine; it should be checked, e.g. via the Markov–Post semi-Thue reduction applied to
  x1:p1,...,xn:pn ⊢_α ... with atoms.

### G12. Adjoint logic decidability (see Q4): none of the adjoint-logic sources read states a decidability result
for proof search. UNVERIFIED-MEMORY: Lincoln–Mitchell–Scedrov–Shankar (1992) proved propositional (intuitionistic
and classical) linear logic with exponentials and additives undecidable; adjoint logic with two modes U ≥ L,
σ(U)={W,C}, σ(L)={} subsumes ILL with ! (Pruiksma thesis l.570–576 says this two-mode instance models linear
logic's !), so derivability for that fixed 2-mode datum would be undecidable — phenomenon (A). Not verified here.

---------------------------------------------------------------------------------------------------
## Q4. Pruiksma, Chargin, Pfenning, Reed adjoint logic — exact per-mode data and results

PCPR18 manuscript already in gen.md S4. Newer full treatment:

### G13. Klaas Pruiksma, "Adjoint Logic with Applications", PhD thesis, CMU, CMU-CS-24-103 (May 2024).
URL: https://www.csd.cmu.edu/sites/default/files/phd-thesis/CMU-CS-24-103.pdf. STATUS: VERIFIED_SOURCE.
- Per-logic data (Ch. 2, p.~10–11): modes "drawn from a preordered set, i.e., a set equipped with a transitive and
  reflexive relation ≤. We think of k ≤ m as expressing exactly the idea that a proof of a proposition at mode k may
  depend on hypotheses at mode m" (l.583–586). "There does not appear to be any fundamental obstacle to working with
  some more general structure (and indeed, other approaches to adjoint logic have used more complex structures such
  as 2-categories [58, 59]), but a preorder is sufficient" (l.587–590).
  "declaration of independence: A proof of a proposition Ak may only depend on hypotheses Bm for which m ≥ k."
  (l.593–594), enforced globally: sequents Ψ ⊢ Ak with Ψ ≥ k.
  "we make use of a monotone map σ that takes modes to subsets of the two-element set {W, C} ... While we always allow
  the structural rule of exchange, we see no inherent obstacle to a system that restricts exchange as well, as in the
  system of Licata et al. [59], or that of Kanovich et al. [49]." (l.652–657)
- Fixed part: "The propositions at each mode are constructed uniformly, using the syntax of linear logic for
  connectives, other than the newly added shifts ↑m_k Ak and ↓ℓ_m Aℓ" (l.658–660); shifts require k ≤ m, m ≤ ℓ.
  Categorical semantics for ↓ ⊣ ↑ "out of scope of this work" (l.649–650).
- Theorems (ADJ_E, explicit structural rules): Thm 1 (Admissibility of multicut): "If Ψ1 ≥ m ≥ k, n ∈ µ(m),
  Ψ1 ⊢⊢E Am, and Ψ2, A^n_m ⊢⊢E Ck, then Ψ1, Ψ2 ⊢⊢E Ck." with µ(m) = {n | (n = 0 ∧ W ∈ σ(m)) ∨ n = 1 ∨ (n ≥ 2 ∧
  C ∈ σ(m))} (l.895). Thm 2 (Cut elimination for ADJ_E): "If Ψ ⊢E Am, then Ψ ⊢⊢E Am." Thm 3 (Identity Expansion):
  "If Ψ ⊢E Am, then there exists a proof that Ψ ⊢E Am using identity rules only at atomic propositions pm, which is
  cut-free if the original proof is." ADJ_I (implicit structural rules): Thm 4/5 soundness/completeness w.r.t. ADJ_E,
  Thm 7 cut admissibility, Thm 8 cut elimination; focusing ADJ_F: Thm 9 defocalization, Thm 10 cut, Thm 11 identity,
  Thm 12 focalization; semi-axiomatic SAX: Thm 14/15.
- Checking status: proofs are by hand; the thesis says (l.1219–1231) proof assistants would help and "a formalization
  ... would be a valuable piece of future work" — so NOT machine-checked.
- Scope: intuitionistic only (Fig. 1.1 "intuitionistic purely linear logic"); no classical/multi-conclusion
  instance found by grep. No decidability result found (grep "decid" yields only unrelated uses).
- Proof identity: no equational theory of proofs for the logic as a whole located by grep (thesis focuses on
  operational/process interpretation: session fidelity, deadlock freedom, diamond lemma) — UNVERIFIED that none exists
  anywhere in the 8.6k-line text; not exhaustively read.

### G14. Jang, Roshal, Pfenning, Pientka, "Adjoint Natural Deduction (Extended Version)", arXiv:2402.01428v1
(2 Feb 2024) (FSCD 2024 version not retrieved). STATUS: VERIFIED_SOURCE (preprint).
- "Each mode m comes with a set σ(m) ⊆ {W, C} of structural properties ... We further have a preorder m ≥ r ...
  m ≥ k implies σ(m) ⊇ σ(k). This is required for cut elimination to hold." (l.134–139)
- Thm 1 (admissibility of weakening and contraction), Thm 2 (admissibility of cut and identity), Thm 12 (from sequent
  calculus to natural deduction) => "every provable proposition has a verification" (abstract). "surprisingly
  subtle algorithm for type checking" (abstract) — type checking of terms, not proof search decidability.
- Instances: STLC = one mode U with σ(U)={W,C}; linear λ-calculus σ(L)={}; etc. (l.475–500). Intuitionistic only.

---------------------------------------------------------------------------------------------------
## Q5. Bipoles / canonical systems / synthetic rules as a syntactic class of admissible object rules

### Miller–Pimentel 2013: see G5 (Defs 3, 4, 17, 18, 24, 25; Props 13, 16, 20, 21, 26; Thms 22, 27).
Key point: the admissible per-logic data are restricted syntactically (bipole introduction clauses mentioning one
connective and its immediate subformulas; canonical = no left/right atoms with same head variable in a body), and
for that class cut-coherence and initial-coherence are DECIDABLE (bounded search) and imply cut/identity elimination
for the encoded object logic.

### G15. Marin, Miller, Pimentel, Volpe, "From axioms to synthetic inference rules via focusing", Annals of Pure and
Applied Logic 173(5) (2022) Art. 103091, DOI 10.1016/j.apal.2022.103091 (journal data from UCL repository listing
via search engine — not printed on my copy). Retrieved: https://www.lix.polytechnique.fr/~dale/papers/synthetic-rules-via-focusing.pdf,
author version "Preprint submitted to Elsevier January 15, 2022". STATUS: VERIFIED_SOURCE (preprint).
- Fixed part: LKF / LJF focused classical/intuitionistic sequent calculi (Thm 1 completeness of LKF and LJF, l.376).
- Def. 2 (Synthetic inference rule, l.510): an inference rule from border sequents Γi ⇑ · ⊢ · ⇑ ∆i to Γ ⇑ · ⊢ · ⇑ ∆
  "justified by a derivation ... Π ... such that no synchronous rule application occurs above an asynchronous rule
  application. We also assume that Π contains at least one inference rule."
- Def. 7 (Bipole for B, l.757): "a synthetic inference rule for B ... in which all formulas stored using the store
  rules ... are atomic formulas."
- Def. 9/10 (l.814–840): polarity-alternation hierarchy N^C_n, P^C_n (classical), N^I_n, P^I_n (intuitionistic);
  "Any formula in the class N^C_2 is a classical bipolar formula. Any formula in the class N^I_2 is an intuitionistic
  bipolar formula."
- Thm 12 (l.859): "A synthetic inference rule for a bipolar formula is a bipole." Thm 13 (l.877): "If every synthetic
  inference rule for a given negative formula is a bipole then that formula is bipolar." (exact characterization)
- Def. 14 (l.960): LK⟨δ,T⟩ = LK extended, for every B ∈ T (finite set of bipolar formulas, polarized by atom-bias δ)
  and every synthetic inference rule for B, with the depolarized rule.
- Thm 16 (l.1005): "Let ⟨δ,T⟩ be a set of bipolar formulas. The cut rule is admissible for the proof systems
  LJ⟨δ,T⟩." Thm 17 (l.1042): "Let ⟨δ,T⟩ be a polarized, geometric theory. The cut rule is admissible for the proof
  systems LK⟨δ,T⟩." (NB: classical case stated for geometric theories, intuitionistic for bipolar — as printed.)
- LK ↔ LKF derivation correspondence: Thm 4 (l.682): "Let Π be an LK derivation of a sequent S from the sequents
  S1,...,Sn. Then there exists an LKF derivation Π′ of [S] from [S1],...,[Sn] such that each application in Π of a
  non-structural rule corresponds to a synthetic inference rule in Π′." Thm 6 (l.726): converse for proofs, "each
  synthetic inference rule in Π′ corresponds to a single rule application in Π."
- Non-uniqueness stated (abstract): "Since there are different choices in how polarity is assigned, it is possible
  to produce different synthetic inference rules for the same formula." Classical bipolars strictly exceed
  intuitionistic ones (l.1066–1073: (P1 ⊃ P2) ∨ (Q1 ⊃ Q2) is classically but not intuitionistically bipolarizable).
  Geometric axioms are "a proper subclass of bipolars" (l.1090); non-bipolar examples handled only outside
  (systems-of-rules / hypersequents, §~5, l.1288–1300).
- Relevance (INFERENCE): this is the clearest existing "fundamentality-style" restriction: an axiom may be turned
  into an object rule iff it is (polarizable as) bipolar (Thm 12+13), with cut admissibility for the resulting
  calculus. But (i) the resulting rule set depends on a non-canonical polarity choice δ (F08: basis choice
  arbitrary); (ii) bipolarity bounds rule SHAPE (alternation depth ≤ 2), not computational power — combined with
  G9 (Buszkowski: atomic, cut-admissible 2-premise rules encode any r.e. language), a bipole-only restriction does
  NOT prevent the environment from encoding undecidable derivability (F02/F03). Note Buszkowski's rules are in the
  non-commutative Lambek setting, not LK; for LK with geometric/Horn axioms, undecidability of first-order Horn
  theories (standard, UNVERIFIED-MEMORY) gives the same lesson.

---------------------------------------------------------------------------------------------------
## Sources NOT accessed
- Licata pubs page (HTTP 503); Riley-hosted LSR extended version (TLS cert mismatch) — possible later revision unchecked.
- LRS dependent framework (in preparation; only 2019 slides exist per search) — NOT_ACCESSED.
- Blanco & Zeilberger ENTCS 2020; Nigam–Pimentel–Reis JLC; Chvalovský–Horčík JSL 2016; Buszkowski 1982;
  Lincoln–Mitchell–Scedrov–Shankar 1992; Olarte–Pimentel–Xavier "A linear logic framework for multimodal logics"
  (MSCS 2022, seen only as a citing-title) — NOT_ACCESSED / SECONDARY_ONLY.
- Google Scholar citation sweep not performed (Semantic Scholar only).
