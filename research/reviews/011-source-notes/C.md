# Cluster C — justification, frameworks, cross-foundation translation, foundations comparison

Source agent C, session 2026-10-09. Downloads: `t011/dl/C/` (never executed); text extracts: `t011/txtC/` (pdftotext / HTML tag-strip, run outside dl dir).
Labels: VERIFIED_SOURCE = text inspected this session (URL, version, location); SECONDARY_ONLY = known only via another source inspected this session; UNVERIFIED-MEMORY = from model memory, not checked; NOT_ACCESSED = tried / not obtained.
Quotes are ≤80 words and taken from retrieved text.

## Sources actually retrieved (all VERIFIED_SOURCE unless noted)

| key | source | URL | version inspected |
|---|---|---|---|
| SEP-PTS | Schroeder-Heister, "Proof-Theoretic Semantics", SEP | https://plato.stanford.edu/entries/proof-theoretic-semantics/ | substantive revision Fri Aug 18, 2023 |
| GP-BeS | Gheorghiu & Pym, "From proof-theoretic validity to base-extension semantics for IPL" | https://arxiv.org/pdf/2210.05344 | arXiv v4, 12 Sep 2024 |
| J-admcomp | Jeřábek, "Complexity of admissible rules", Arch. Math. Logic 46(2) 2007 73–92 | https://users.math.cas.cz/~jerabek/papers/admcomp.pdf | author preprint dated Sept 19, 2006 |
| J-indep | Jeřábek, "Independent bases of admissible rules", Logic J. IGPL 16(3) 2008 249–267 | https://users.math.cas.cz/~jerabek/papers/indep.pdf | author PDF (intro only inspected) |
| J-abs | Jeřábek abstracts page | https://users.math.cas.cz/~jerabek/papers/ABSTRACTS.html | fetched 2026-10-09 |
| Dk | Assaf et al., "Dedukti: a Logical Framework based on the λΠ-Calculus Modulo Theory" | https://arxiv.org/pdf/2311.07185 | arXiv v1, 13 Nov 2023 |
| Rabe-MSCS | Rabe, "A Logical Framework Combining Model and Proof Theory" (MSCS) | https://kwarc.info/people/frabe/Research/rabe_combining_10.pdf | preprint "Revised 14 May 2011" |
| Rabe-JLC | Rabe, "How to Identify, Translate, and Combine Logics?" JLC 27(6) 2017 1753–1798, doi 10.1093/logcom/exu079 (bib data from search result) | https://kwarc.info/people/frabe/Research/rabe_howto_14.pdf | author preprint (undated in header) — may differ from journal version |
| FPC | Chihani, Miller, Renaud, "A semantic framework for proof evidence" (JAR 59(3) 2017, per search result) | https://www.lix.polytechnique.fr/Labo/Dale.Miller/papers/fpc-jar.pdf | "Draft: July 2, 2016" |
| Pure | Paulson, "The Foundation of a Generic Theorem Prover" | https://arxiv.org/pdf/cs/9301105 | arXiv PDF |
| MM | Megill (& Wheeler), *Metamath: A Computer Language for Mathematical Proofs* | https://us.metamath.org/downloads/metamath.pdf | dated 2019-06-02 |
| Mes | Meseguer, "General Logics" (Logic Colloquium '87, North-Holland 1989, SLFM 129, 275–329 per search result) | https://courses.grainger.illinois.edu/cs522/sp2016/GeneralLogics.pdf | course-hosted copy; provenance vs. published version not confirmed |
| CMM | Caleiro, Marcelino, Marcos, "Combining fragments of classical logic: When are interaction principles needed?" | https://arxiv.org/pdf/1810.05879 | arXiv v2, 16 Oct 2018 |
| BH | Barrett & Halvorson, "Morita Equivalence" | https://arxiv.org/pdf/1506.04675 | arXiv v1, 15 Jun 2015 |
| En | Enayat, "Variations on a Visserian Theme" | https://arxiv.org/pdf/1702.07093 | arXiv v1 (header date Sept 13, 2018) |
| En-corr | Enayat, "Corrigendum & Addendum to: Variations on a Visserian theme" | https://arxiv.org/pdf/2602.15081 | arXiv v1, 16 Feb 2026 |
| FV | Friedman & Visser, "When Bi-interpretability implies Synonymy" | https://arxiv.org/pdf/2506.01028 | arXiv v1, 1 Jun 2025 |
| SEP-RM | Eastaugh, "Reverse Mathematics", SEP | https://plato.stanford.edu/entries/reverse-mathematics/ | first published Fri Feb 2, 2024 |
| SEP-PT | Rathjen & Sieg, "Proof Theory", SEP | https://plato.stanford.edu/entries/proof-theory/ | substantive revision Wed Feb 21, 2024 |
| SEP-LC | MacFarlane, "Logical Constants", SEP | https://plato.stanford.edu/entries/logical-constants/ | substantive revision Thu Jun 18, 2015 |
| Kriv | Krivine, "Realizability algebras: a program to well order R", LMCS 7(3:02) 2011 | https://arxiv.org/pdf/1005.2395 | LMCS published version |

(Author attributions of SEP entries Eastaugh / Rathjen–Sieg / MacFarlane: UNVERIFIED-MEMORY — I did not grep author lines.)

NOT_ACCESSED: Belnap 1962 "Tonk, plonk and plink" (paywalled; only SEP restatement); Prawitz 1971/1973 originals; Dummett 1991; Read 2010; Tennant; Francez 2015; Tranchini 2023; Piecha–de Campos Sanz–Schroeder-Heister JPL 44 (2015) 321–335 and Piecha–Schroeder-Heister Studia Logica 107 (2019) 233–246 (only via SEP-PTS and GP-BeS); Sandqvist Logic J. IGPL 23 (2015) 719–731 (only via GP-BeS); Rybakov 1997 book; Iemhoff JSL 2001 (only via J-admcomp restatement); Iemhoff structural completeness papers; HHP JACM 1993 (only a .ps file was available; not rendered because interpreting PostScript = executing a download — deleted); Cousineau–Dowek TLCA 2007 (only via Dk Lemmas 30–32); Assaf thesis; Logipedia papers; Goguen–Burstall JACM 1992; Diaconescu 2008 book; Mossakowski Hets / Grothendieck institutions; Fiadeiro–Sernadas π-institutions; Caleiro–Ramos "cryptofibring" (only cited in CMM); Visser "Categories of theories and interpretations" (no open copy found; Utrecht repository record only); Simpson SOSOA (only via SEP-RM); Pohlers; Rathjen originals; Kleene; realizability toposes (Hyland); Feferman 1999/2010 logicality; Bonnay; McGee 1996 (only via SEP-LC); Brandom.

---

## C1 Proof-theoretic semantics (PTS) & harmony

**(1) Object.** Rules-as-meaning: introduction/elimination rules for connectives; *harmony/inversion* (elims justified by intros, or vice versa); *proof-theoretic validity* of arguments relative to atomic bases (Prawitz); *base-extension semantics* (B-eS: support relation ⊩_B over atomic bases B and extensions C ⊇ B); *definitional reflection* (clausal definitions A ⇐ Δ with intro + reflection rule).

**(2) Strongest results.**
- R1.1 *Incompleteness of IPC for (simplified) PTS.* "Prawitz (1971) conjectured that those consequence statements Γ ⊨ A, which are justified by proofs valid with respect to any atomic base, are exactly the derivability statements Γ ⊢ A … this conjecture turned out to be false. Harrop's rule … which is not derivable (but only admissible) in intuitionistic logic can be validated in this framework (Piecha and Schroeder-Heister, 2019)." [SEP-PTS §2.8]. GP-BeS (p. 2–3) adds: with the Kripke-like clause ⊩_B φ∨ψ iff ⊩_B φ or ⊩_B ψ, B-eS "renders IPL incomplete (see Piecha et al.)", and the original Prawitz P-tV conjecture "remains an open problem"; only a "slightly simplified" P-tV is shown to fail. Status: VERIFIED_SOURCE (secondary statement in SEP + GP-BeS); primary Piecha et al. papers NOT_ACCESSED. Scope note: SEP says that when the extension structure of bases is changed "beyond the set-theoretical superset relation … Kripke's completeness proof … becomes applicable (Goldfarb 2016; Stafford and Nascimento 2023)".
- R1.2 *Sandqvist completeness.* GP-BeS Theorem 25 (Sandqvist [59] = Logic J. IGPL 23 (2015)): Γ ⊩ φ iff Γ ⊢ φ (IPL), for support over "Sandqvist bases" (atomic rules with possibly discharged atom sets) and the second-order disjunction clause "⊩_B φ∨ψ iff ∀C ⊇ B and ∀p ∈ A, if φ ⊩_C p and ψ ⊩_C p, then ⊩_C p"; ⊥ not provable in any base. GP-BeS Thm 33: a version of P-tV based on elimination rules is complete, "assuming the set of reductions for arguments is supportive". Status: VERIFIED_SOURCE for GP-BeS statement; Sandqvist original NOT_ACCESSED.
- R1.3 *Harmony ≠ consistency/normalizability.* SEP §3.8: with naive-comprehension intro/elim rules (t∈{x:A(x)} from A(t) and back) "for r as {x: x ∉ x}, we can infer r ∈ r from r ∉ r and vice versa … Prawitz (1965, Appendix B) observed that the derivation of absurdity arising from Russell's paradox is non-normalizable, a feature that Tennant (1982) was able to demonstrate for a vast range of paradoxes." The rule pair is locally inverse (a reduction exists) yet yields absurdity. Status: VERIFIED_SOURCE (SEP restatement).
- R1.4 *Tonk.* SEP §2.2.1: inversion "excludes alleged inferential definitions such as that of the connective tonk, which combines an introduction rule for disjunction with an elimination rule for conjunction, and which has given rise to a still ongoing debate on the format of inferential definitions." Formal harmony characterizations "have used the translation of inference rules into second-order propositional logic (Girard's system F)". Status: VERIFIED_SOURCE (SEP); Belnap NOT_ACCESSED. Note SEP: the term harmony "is not uniform and sometimes not even fully clear" — i.e., no single accepted formal criterion.
- R1.5 *Intensional harmony / proof identity.* SEP §3.7: identity of proofs "is much neglected"; elimination pairs {A∧B/A, A∧B/B} vs {A∧B/A, A∧B, A / B} are extensionally interchangeable but "Identifying them corresponds to identifying A∧B and A∧(A→B), which is only extensionally, but not intensionally correct" (Došen: equivalent but not isomorphic). VERIFIED_SOURCE.

**(3) Represents / cannot.** Represents: a justification criterion for rules (intrinsic, not model-theoretic), local reductions = β-like proof transformations, a semantic validity notion for arguments. Cannot (as established): give a single agreed criterion; guarantee consistency/normalization from local harmony (R1.3); match IPC with the most natural base semantics (R1.1); it is mostly propositional/first-order and intuitionistic in spirit; classical logic needs separate treatment (bilateralism etc. — UNVERIFIED-MEMORY).

**(4) Strongest negative.** R1.1 (semantic incompleteness of IPC w.r.t. natural PTS variants; validity of the merely admissible Harrop rule) + R1.3 (locally harmonious rules can be paradoxical). Together: "justified-by-harmony" is neither a complete nor a safe (consistency-guaranteeing) generative criterion for inference justification, and the outcome depends on technical choices (base-extension relation, ⊥ in bases, disjunction clause).

**(5) Relation to ProofBasis.** *Direct prior art* for the "inference justification" component. A deep dive could change framing: it shows that "what makes a rule legitimate" has no settled intrinsic answer, and that the result depends on presentation choices; ProofBasis cannot simply posit harmony as its justification primitive without inheriting R1.1/R1.3. R1.5 bears directly on "proof identity" (presentation-sensitivity).

**(6) Neighbours.** C2 (admissible vs derivable: Harrop rule is exactly an admissible-non-derivable IPC rule — PTS validity leaks into admissibility); C7 (logicality/inferentialism); categorical proof theory (proof identity, Došen); C3 definitional reflection ↔ logic programming / Abella-style frameworks.

## C2 Admissible rules

**(1) Object.** A rule φ1..φk / ψ is *admissible* in L if the set of L-theorems is closed under all its substitution instances [J-admcomp p.1: "admissible in a logic L, if the set of theorems of L is closed under the rule"]; *derivable* if ψ follows from the φi in L. *Basis* of admissible rules: a set of rules from which (together with L's derivable rules) all admissible rules follow. *Structurally complete*: every admissible rule derivable.

**(2) Strongest results.**
- R2.1 *Decidability and no finite basis (Rybakov).* J-indep intro: Rybakov "has shown that admissibility is decidable for a large class of modal and intermediate logics, found semantic criteria for admissibility, proved nonexistence of finite bases of admissible rules for many logics (including IPC and K4)". Status: VERIFIED_SOURCE as restated by Jeřábek; Rybakov 1997 NOT_ACCESSED. Also J-admcomp: "Chagrov [4] constructed a decidable modal logic, which has undecidable admissibility problem."
- R2.2 *Explicit infinite basis for IPC (Iemhoff).* J-admcomp Theorem 1.5 (restating Iemhoff [11], reformulated for multiple-conclusion rules): Visser's rules ⋀_{i<n}(φi→ψi) → φn ∨ φn+1 ▷ ⋀_{i<n}(φi→ψi) → φj (j ≤ n+1), together with ⊥ ▷, form a basis of IPC-admissible rules. Thm 1.6: a rule Γ ▷ Δ is IPC-admissible iff every extensible model satisfying Γ satisfies some ψ∈Δ. VERIFIED_SOURCE (restatement); Iemhoff JSL 2001 NOT_ACCESSED. J-indep: IPC, K4, GL, S4 have *independent* bases (J-abs). Łukasiewicz logic "has no finite basis of admissible rules" (J-abs).
- R2.3 *Complexity gap.* J-admcomp abstract: "We state a broad condition under which the admissibility problem is coNEXP-hard. We also show that admissibility in several well-known systems (including GL, S4, and IPC) is in coNE"; intro: admissibility in typical logics is "coNEXP-complete (and in particular, strictly more complex than the derivability problem, under reasonable complexity-theoretic assumptions)" (derivability being PSPACE-complete for IPC, Statman). VERIFIED_SOURCE.

**(3) Represents / cannot.** Represents: the closure of a proof system under rules that do not add theorems — the precise gap between "a rule is part of the generating basis" and "a rule is merely closed-under". Cannot: admissibility is not stable under extension of the language/theory (an admissible rule may stop being admissible in an extension — UNVERIFIED-MEMORY as general statement; Jeřábek discusses "logics inheriting their admissible rules", which presupposes non-inheritance in general).

**(4) Strongest negative.** R2.1/R2.2: even for propositional IPC, the set of admissible rules is decidable but has *no finite basis*; the canonical basis is an infinite schema (Visser rules indexed by n). R2.3: deciding admissibility is (likely) strictly harder than deciding derivability.

**(5) Relation.** *Adjacent prior art / strong analogy*, and a direct warning: "finite generative basis" for the inference machinery must specify whether derivable or admissible rules are generated. For admissible rules the answer in a basic case (IPC) is already negative for *finite* bases, positive for *schematic* ones. A deep dive could change framing: ProofBasis should state "finite" as "finite modulo schemas indexed by ℕ" or not, and should treat admissible-vs-derivable as a mandatory distinction (cf. AGENTS.md rule 5).

**(6) Neighbours.** C1 (Harrop rule validity in PTS); unification theory (Ghilardi); structural proof theory (cut admissibility is an admissibility statement); C3 frameworks (a framework that adds admissible rules as primitives changes the trusted base).

## C3 Logical frameworks and universality claims

**(1) Object.** A meta-language (LF: dependent λΠ types; Dedukti: λΠ + user rewrite rules; Isabelle/Pure: intuitionistic higher-order logic M with ⇒, ⋀, ≡; Metamath: string substitution + disjoint-variable conditions; MMT: theories + morphisms over an arbitrary framework; FPC: focused LKF/LJF kernels + clerks/experts) in which object logics are *signatures/theories*, and proofs are terms/derivations.

**(2) Strongest results.**
- R3.1 *Dedukti encodings with provability iff.* Dk Theorem 21: "A proposition A has a proof in constructive logic if and only if the type eps |A| is inhabited. A proposition A has a proof in classical logic if and only if the type eps |A|c is inhabited." Thm 23 (STT, citing Assaf's thesis [8]): Γ ⊢ A in STT iff ∃π with Σ_STT, ‖Γ‖ ⊢ π : ‖A‖, "Moreover, the term π is a straightforward encoding of the original proof tree." PTS embedding: Lemma 30 preservation of computation (|M| →β N′ ≡βΣ |M′|), Lemma 31 typing, Lemma 32 "Conservativity, adequacy, [9]": if Σ,‖Γ‖ ⊢ M′ : ‖A‖ then ∃M with Γ ⊢ M : A and |M| ≡βηΣ M′; Thm 33 provability equivalence. VERIFIED_SOURCE (Dk arXiv v1). Hypotheses of Lemma 32 in [9] (e.g. functional/normalizing PTS) NOT inspected — UNVERIFIED.
- R3.2 *Dedukti trust conditions.* Dk §2: decidability of the congruence and subject reduction depend on confluence (and termination) of user rewrite rules; "Checking confluence is out of the scope of Dedukti itself, and is a separate concern". Coverage limit: "the Coq library is expressed in a Calculus of constructions with universes, modules and universe polymorphism. Those two latter features have not yet been expressed in Dedukti, so the Coq library cannot be checked directly" (status as of the paper; later work UNVERIFIED). VERIFIED_SOURCE.
- R3.3 *MMT/Rabe: logics = theories, translations/semantics = morphisms, combinations = colimits.* Rabe-JLC abstract: "the syntax and proof systems of logics are theories; that both semantics and translations are theory morphisms; and that combinations are colimits." Thm 2.31 (Preservation of Judgments): if ⊢_S J then ⊢_{S′} σ(J) for well-formed σ. Def 3.39: l is *proof-conservative* if l(Σ)-(dis)proofs of the image reflect to Σ-(dis)proofs; Thm 3.41 relates proof- and model-conservativity (converse only for classical L). Rabe-MSCS Def 13: adequacy = model expansion + "for any A, B, if there is a morphism from γΣ(A) to γΣ(B), then there is also one from A to B (proof theoretical adequacy)" — i.e., existence, not identity, of proofs. Rabe-JLC intro: universal logic: "no single conceptualization has become dominant". VERIFIED_SOURCE.
- R3.4 *Metamath single rule.* MM p.17: "Each individual step in a proof involves a single basic concept, the substitution of an expression for a variable". Logical axioms/rules are user `$a` statements; free/bound variables and proper substitution are not primitive but encoded via axioms and `$d` disjoint-variable restrictions (MM pp. ~120, Ch. 3). VERIFIED_SOURCE.
- R3.5 *Isabelle/Pure.* Pure: M is intuitionistic higher-order logic; "ML is faithful for L if ML is sound and complete for L" (provability-level faithfulness); Thms 2–5: Mipl/Mifol sound and complete for ipl/ifol. VERIFIED_SOURCE.
- R3.6 *FPC.* FPC abstract: semantics of proof evidence via focused LKF/LJF; "we shall limit ourselves to first-order logic in this paper"; soundness is kernel-based: "any proof in LKF^a is a proof in LKF, which guarantees the soundness of the LKF^a system" — clerks/experts (certificate semantics) are untrusted. VERIFIED_SOURCE.
- R3.7 *LF adequacy (HHP).* "Compositional bijection between canonical LF terms and object derivations" — UNVERIFIED-MEMORY (paper NOT_ACCESSED).

**(3) Represents / cannot.** Represents: binding (HOAS), judgments-as-types, proof checking uniformly; cross-system import (Dedukti libraries of HOL Light, Matita, Zenon, iProver, FoCaLiZe). Cannot by itself: (a) justify the object-level rules — they are user-supplied constants/rewrite rules/axioms (exactly AGENTS.md rule 6 "user-defined trusted rules"); (b) guarantee consistency/confluence of user rewrite systems (Dk); (c) faithfulness is stated at provability level ("iff inhabited"), proof-level adequacy is per-encoding (Dk Thm 23's "straightforward encoding" is informal; Lemma 32 gives βηΣ-convertibility, which is a proof-identity claim only modulo the framework's conversion).

**(4) Strongest negative.** Framework universality is *representational*, not *justificatory*: in every examined framework, the theory-specific content (axioms, rules, rewrite rules, `$a` statements) is supplied by the user and trusted; the framework's "finite basis" (λΠ + conversion; Metamath substitution) is finite precisely because all logic-specific content is pushed into signatures. Additionally, encodability of a foundation (e.g., Coq's full system) can lag (Dk R3.2).

**(5) Relation.** *Direct prior art / strongest redundancy threat.* A finite meta-level basis for "operations, composition, binding" across foundations already exists in several forms (LF/λΠ-modulo/Pure/Metamath), with provability-level adequacy theorems. ProofBasis can only be non-redundant if it targets something these do not: intrinsic justification (C1), proof identity/transformations (R1.5; R3.3 only gives existence), or a non-vacuity criterion separating a "basis" from an interpreter. A deep dive should check Dedukti/Logipedia and MMT/LATIN for proof-identity and transformation claims — could reframe the project as "a proof-identity-aware refinement of logical frameworks".

**(6) Neighbours.** C4 (Rabe merges LF with institutions; Meseguer); C1 (definitional reflection ↔ λProlog/Abella); C5 (Dk motivation: partial order of theories, reverse-engineering which axioms a proof needs ≈ reverse mathematics); C6 (Curry–Howard extraction).

## C4 General logics / institutions / combination of logics

**(1) Object.** Institution (Goguen–Burstall): (Sign, Sen, Mod, ⊨) with satisfaction condition; Meseguer *entailment system* E = (Sign, sen, ⊢) with reflexivity, monotonicity, transitivity, ⊢-translation [Mes Def 1]; *proof calculus* P = (Sign, sen, ⊢, P, Pr, π) [Mes Def 12]; maps of entailment systems/logics; fibring and other combinations.

**(2) Strongest results.**
- R4.1 Mes Def 12: proof calculus assigns each theory T a "proof-theoretic structure" P(T) ∈ Struct_P, a set of proofs Pr(P(T)), and a natural transformation π: proofs ⇒ sen whose image is the theory's closure Γ•. Mes p.15–16: the axioms "will not impose any particular structure; they will postulate that P(T) has some structure, by declaring it an object of some category of structures." Mes p.4: "The entailment relation ⊢ says nothing about the internal structure of a proof." VERIFIED_SOURCE (course-hosted copy).
- R4.2 *Combination collapse / interaction principles.* CMM abstract + Thm 4.1: for disjoint signatures, combining (by fibring, B_Σ1 • B_Σ2) two fragments of classical logic yields the classical fragment over Σ1∪Σ2 *iff* one of three narrow conditions holds (clone inclusions (a)–(c)); otherwise interaction principles are missing. Intro: "the smallest logic that conservatively extends both the 'logic of conjunction' and the 'logic of disjunction' is not distributive"; fibring of logics without quasi-theorems "is always conservative over each component"; Gentzen formalisms produce distributivity "as an artifact that is produced by the very choice of proof formalisms". VERIFIED_SOURCE.
- R4.3 Rabe-MSCS / Rabe-JLC as institution+LF integration (see R3.3). Proof-theoretic institutions (Diaconescu), Grothendieck institutions / Hets (Mossakowski) — NOT_ACCESSED (only cited in Rabe-MSCS lines ~207–212, 342–344).

**(3) Represents / cannot.** Represents: foundation-independent signatures, sentences, entailment, models, and translations (comorphisms) with preservation conditions; a slot for proof structures. Cannot: provide a canonical proof structure (it is a parameter, R4.1); guarantee that combining components yields the intended combined logic (R4.2).

**(4) Strongest negative.** R4.2: composition of logics is not compositional in general — either the combination is weaker than intended (needs extra interaction rules) or proof formalisms import unintended interaction/collapse. For ProofBasis "composition" across foundations, this is a concrete counterexample class to naive modular generation.

**(5) Relation.** *Direct prior art for the abstract shape* ("general theory of proof calculi and their maps"), explicitly agnostic about proof identity. Adjacent for generativity. A deep dive into Meseguer + proof-theoretic institutions could show that ProofBasis's "machinery" decomposition is already axiomatized, leaving only the "finite explanatory generators" claim as new.

**(6) Neighbours.** C3 (MMT/LATIN implements this), C5 (interpretations are theory morphisms), C1 (conservativeness restraint is shared with harmony debates: CMM intro cites it explicitly).

## C5 Comparing foundations

**(1) Object.** Relative interpretations (Tarski–Mostowski–Robinson); bi-interpretability, synonymy/definitional equivalence, Morita equivalence, categorical equivalence of model categories; proof-theoretic Φ-reducibility; reverse-mathematics equivalence over RCA0; proof-theoretic ordinals.

**(2) Strongest results.**
- R5.1 *Proof-theoretic reduction maps proofs, but only up to Φ-provability.* SEP-PT Def 1.3: T1 ≤_Φ T2 if there is a primitive recursive f with PRA ⊢ ∀x∀y[form_Φ(x) ∧ proof_T1(y,x) → proof_T2(f(y),x)]. Def 3.4: |T| = τ iff T ≡_{Π⁰₂} PRA + TI_qf(<τ). VERIFIED_SOURCE.
- R5.2 *Reverse mathematics Big Five.* SEP-RM §4: WKL0, ACA0, ATR0, Π¹₁-CA0 "are each equivalent over the base theory RCA0 to a multitude of ordinary mathematical theorems"; inclusion order ≠ consistency-strength order (RCA0, WKL0 equiconsistent; WKL0 Π¹₁-conservative over RCA0 and Π⁰₂-conservative over PRA, §4.1). Exceptions: RT²₂ "lies outside the Big Five classification" (Specker; Jockusch; Seetapun–Slaman; Liu 2012). VERIFIED_SOURCE (SEP); Simpson SOSOA NOT_ACCESSED.
- R5.3 *Sameness of theories is a hierarchy, and foundations are rigid.* BH: definitional ⇒ Morita ⇒ categorical equivalence; Thm 5.2 "Categorical equivalence does not entail Morita equivalence". FV abstract: sequential theories bi-interpretable via one-dimensional identity-preserving interpretations are synonymous; result optimal (finitely axiomatized sequential counterexample when one interpretation is not identity-preserving). En Thm 1.1 (Visser): deductively closed extensions U, V of PA are bi-interpretable iff U = V; Thm 1.2: same for Z2, ZF, (KM — but En-corr 2026: gap found by Gruza–Lelyk, "it is open whether KM and its higher order variants are solid", proof works for KM + CC_set). En Thm 1.5 PA and ZFfin + TC bi-interpretable; Thm 1.6 (Enayat–Schmerl–Visser) ZFfin and PA not bi-interpretable. VERIFIED_SOURCE.

**(3) Represents / cannot.** Represents: precise, graded notions of when two foundations are "the same" or one reduces to another, with proof transformations (R5.1) and theorem-level equivalence (R5.2–5.3). Cannot: these notions preserve *theorems* (or Φ-theorems, or model categories); none of the inspected definitions requires preservation of *proof identity* or proof structure — Def 1.3 only asks for some p.r. f.

**(4) Strongest negative.** R5.3: natural foundations (PA, ZF, Z2) are *tight* — distinct extensions are never bi-interpretable — and fine-grained sameness notions come apart (BH Thm 5.2, FV optimality). Hence "the same machinery across different foundations" cannot be read as "foundations are equivalent"; any cross-foundation claim must fix a sameness notion, and the answer changes with it. Also R5.2 shows strength comparisons are non-linear at fine grain (RT²₂).

**(5) Relation.** *Adjacent; essential for scoping*. ProofBasis's phrase "across different foundations" must specify the translation notion (interpretation, Φ-reduction, framework encoding) and the preserved property (theorems vs. proofs vs. proof identity). A deep dive could change framing by forcing ProofBasis to define cross-foundation invariance relative to one of these notions; no inspected result offers proof-identity-preserving comparison of foundations.

**(6) Neighbours.** C3 (Dk's "partial order between theories" and reverse engineering of proofs), C4 (interpretations as theory morphisms), C6 (realizability gives conservativity/independence results).

## C6 Realizability

**(1) Object.** Realizability interpretations (Kleene number realizability; Krivine classical realizability: realizers are terms of a machine with stacks, a pole ⊥⊥, |A| / ‖A‖ truth/falsity values; realizability algebras = "a three-sorted variant of the well known combinatory algebra of Curry").

**(2) Strongest results.** Kriv Thm 1.3 (Adequacy lemma): proofs yield realizers. Prop 1.6: cc ⊩ Peirce's law. Kriv intro: "when we realize usual axioms of mathematics, we need to introduce, one after the other, the very standard tools in system programming: for the law of Peirce, these are continuations …; for the axiom of dependent choice, these are the clock and the process numbering; for the ultrafilter axiom and the well ordering of R, these are no less than read and write instructions on a global memory". Open: measurable cardinals, determinacy ("A very interesting open problem"). VERIFIED_SOURCE (LMCS 2011).

**(3) Represents / cannot.** Represents: a uniform proof-to-program interpretation for classical analysis and beyond, extending to set theory with choice. Cannot: realize new axioms without enlarging the instruction set — each axiom brings its own primitive.

**(4) Strongest negative.** Kriv intro: the computational basis grows with the axioms (continuations, clock, global memory); no fixed finite instruction set for all foundations is known; large-cardinal axioms are open.

**(5) Relation.** *Analogy / adjacent*. Strong evidence that a "finite generative basis" for the *computational content* of proofs is foundation-dependent; also an instance of AGENTS.md rule 6 risk (axioms realized by ad hoc instructions). Deep dive unlikely to change framing beyond this point.

**(6) Neighbours.** C5 (realizability models give independence/conservativity), C3 (proof extraction in Dedukti/Coq), C1 (Gheorghiu–Pym relate the ND horizontal bar to realizability).

## C7 Missing families found / checked

- **Logicality / invariance (Tarski–Sher; McGee; Feferman critique).** SEP-LC §5: "McGee (1996) shows that every permutation-invariant operation can be defined in terms of operations with an intuitively logical character (identity, substitution of variables, finite or infinite disjunction, negation, and finite or infinite existential quantification)" and conversely. VERIFIED_SOURCE (SEP); McGee NOT_ACCESSED. Feferman (1999) proposes stricter invariance; criticizes permutation invariance (SEP-LC ~l.1186–1208). *Relevance:* the only "completeness of a logical basis" theorem found in this cluster yields an *infinitary* basis (L∞∞) — a semantic analogue warning against expecting finiteness. Analogy, not prior art.
- **Universal logic (Béziau).** Rabe-JLC: "Universal logic is the field of logic that investigates the common features of logics. Even though the field has arguably existed for decades, no single conceptualization has become dominant." VERIFIED_SOURCE (as Rabe's claim). Béziau originals NOT_ACCESSED.
- **Proof-theoretic reduction (Feferman) / conservativity theorems.** Covered in C5 (R5.1, R5.2). Feferman's own papers NOT_ACCESSED.
- **Inferentialism (Brandom).** Philosophy only; NOT_ACCESSED; no formal theorem expected.
- **Intensional PTS / Tranchini 2023** — flagged by SEP as the first monograph on intensional PTS; NOT_ACCESSED; potentially the closest work on proof-identity-sensitive justification. Recommend deep dive.
- **Categorical proof theory / Došen "identity of proofs"** — flagged by SEP-PTS (§3.7); belongs to another cluster but is the bridge between C1 and proof identity.

## Cross-cutting decision-relevant findings

1. Finite meta-level generators for representation (binding, substitution, proof checking) already exist with provability-level adequacy theorems (Dk Thms 21/23/33; Pure Thms 2–5; Metamath single substitution rule). Any ProofBasis "finite basis" that is satisfied by these is redundant; any that excludes them must say what they lack (justification; proof identity).
2. In all such frameworks, finiteness is achieved by pushing logic-specific content into user-trusted signatures/rewrite rules/axioms — the vacuity pattern AGENTS.md rule 6 forbids.
3. Intrinsic justification (harmony/PTS) is not a settled, complete or safe criterion (R1.1, R1.3), and its outcome is presentation-sensitive (R1.5).
4. Even the closure of a basic logic under admissible rules lacks a finite basis (R2.1–2.2), and admissibility is harder than derivability (R2.3).
5. Combination of logics is not modular in general (R4.2); general logics leave proof structure as a free parameter (R4.1).
6. Cross-foundation comparison notions preserve theorems (or Φ-theorems), not proof identity; strong rigidity (tightness) of PA/ZF/Z2 (R5.3).
7. Realizability: computational basis grows with axioms (C6).
