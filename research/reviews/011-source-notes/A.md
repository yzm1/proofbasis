# Cluster A — structural, general and categorical proof theory: source notes (t011)

Session date 2026-10-09. Every primary PDF was downloaded to `<session-scratchpad>/t011/dl/A/` and converted with `pdftotext -layout` into `<session-scratchpad>/t011/txtA/`. Quotes are verbatim from those text files and are at most 80 words. Status labels:
- **VS** = VERIFIED_SOURCE: text read this session, with its location given.
- **SO** = SECONDARY_ONLY: the secondary source is named.
- **UM** = UNVERIFIED-MEMORY.
- **NA** = NOT_ACCESSED.

"Established" here means a published theorem that I read in its source. None of it was checked by a machine in this audit.

## Sources actually read (primary)

| key | source | what was inspected |
|---|---|---|
| DOS03 | K. Došen, "Identity of Proofs Based on Normalization and Generality", arXiv:math/0208094v12 (2004); BSL 9 (2003) [venue: UM] | §§2–5 in full, including Props 1–3 |
| STR06 | L. Straßburger, "Proof Nets and the Identity of Proofs", ESSLLI notes, arXiv:cs/0610123v2 | the classical-collapse section, pp. 58–59 |
| STR07 | L. Straßburger, "On the Axiomatisation of Boolean Categories with and without Medial", arXiv:cs/0512086v3 (TAC 2007 [venue: UM]) | abstract and introduction |
| HH16 | W. Heijltjes, R. Houston, "Proof equivalence in MLL is PSPACE-complete", LMCS 12(1:2) 2016, arXiv:1510.06178v2 | abstract, introduction, Thm 9.1 |
| HUG06 | D. Hughes, "Proofs Without Syntax", Annals of Math. (accepted 2005), arXiv:math/0408282v3 | abstract and §1 |
| HUG19 | D. Hughes, "First-order proofs without syntax", arXiv:1906.11236v1 | abstract only |
| GG08 | A. Guglielmi, T. Gundersen, "Normalisation Control in Deep Inference via Atomic Flows", LMCS 4(1:9) 2008, arXiv:0709.1205v3 | abstract, theorem list, complexity remarks |
| BRU03 | K. Brünnler, "Locality for Classical Logic", arXiv:math/0301317v1; NDJFL 47(4) 2006 | introduction and §3.5 |
| BGGP | Bruscoli, Guglielmi, Gundersen, Parigot, "Quasipolynomial normalisation in deep inference via atomic flows and threshold formulae", arXiv:0903.5392v5 | abstract only |
| DS16 | A. Das, L. Straßburger, "On linear rewriting systems for Boolean logic and some applications to proof theory", LMCS 12(4:9) 2016, arXiv:1610.08772v4 | abstract and §1 |
| AJ92 | S. Abramsky, R. Jagadeesan, "Games and Full Completeness for MLL", Imperial TR DoC 92/24, arXiv:1311.6057v1 (JSL 1994 [venue: UM]) | §1, Theorem 1 |
| CMS08 | K. Chaudhuri, D. Miller, A. Saurin, "Canonical Sequent Proofs via Multi-Focusing", IFIP TCS 2008 (author PDF, lix.polytechnique.fr/~dale/papers/tcs08trackb.pdf) | abstract, Def 6, Thm 7 |
| CHM12 | K. Chaudhuri, S. Hetzl, D. Miller, "A Systematic Approach to Canonicity in the Classical Sequent Calculus", CSL 2012, LIPIcs 16, doi:10.4230/LIPIcs.CSL.2012.183 | abstract |
| SEL01 | P. Selinger, "Control Categories and Duality", MSCS 11 (2001) 207–260 (author PDF mathstat.dal.ca/~selinger/papers/control.pdf) | abstract, §3.4 (Lemma 3.7, Cor 3.8) |
| AZ08 | A. Avron, A. Zamansky, "Canonical calculi with (n,k)-ary quantifiers", arXiv:0806.0081v2 (LMCS 2008) | abstract, introduction, Def 2.9, Prop 2.10, Thm 4.7 statement |
| CGT08 | A. Ciabattoni, N. Galatos, K. Terui, "From axioms to analytic rules in nonclassical logics", LICS 2008, author PDF cs.du.edu/~ngalatos/research/22lics08.pdf | Thm 4.2, Thm 5.6, Cor 7.2, Cor 7.3, Ex 7.4, Cor 8.6 |
| MZ05 | G. Moser, R. Zach, "The Epsilon Calculus and Herbrand Complexity", arXiv:math/0510640v1 | used only as a secondary source for Statman and Orevkov (text near ref. list [21],[22]) |

---

## A1. Deep inference, the calculus of structures, atomic flows and open deduction

**(1) Object.** Derivations in the calculus of structures. Rules rewrite inside any context S{ } ("deep"), and derivations are top-down symmetric. Atomic flows are graphs obtained from derivations by tracing atom occurrences and forgetting the logical structure. The main systems are SKS (classical, symmetric) and KS (cut-free).

**(2) Results.**
- **BRU03 (VS, NDJFL 2006; arXiv intro and §3.5).** Classical propositional logic has a system SKS whose identity, cut, weakening and contraction are all atomic. It adds medial and keeps switch. The paper says this "leads to rules that are local: they do not require the inspection of expressions of unbounded size." It also states that "Contraction, however, cannot be replaced by its atomic form in known sequent systems [2]. In fact, I believe that such a system cannot be presented in the sequent calculus."
  - Status: established result (locality, the strong equivalence SKS ≅ SKSg, Thm 3.24). The sequent-calculus impossibility is a **belief/conjecture** in this paper. The narrower technical result is in Brünnler's "Two restrictions on contraction" (TR WV-2002-04), which I did NOT access.
  - The predicate case is only partially local. Quoted: "local except for the rules that instantiate variables or check for free occurrences of a variable."
- **BRU03 caveat (VS, §3.5).** Quoted: "The concept of locality depends on the representation of structures. Rules that are local for one representation may not be local when another representation is used. For example, the switch rule is local when structures are represented as trees, but it is not local when structures are represented as strings."
- **GG08 (VS, LMCS 4(1:9)).** The paper proves a general normalisation theorem for propositional SKS that contains cut elimination as a special case. Atomic flows support this. Quoted: "the technique they support is largely independent of syntax; 2) indeed, it is largely independent of logical inference rules". The algorithms Str/HStr (Thms 5.25, 5.29) "streamline" every SKS derivation. The complexity is exponential (§6 remark), and flow reduction by contraction "can blow the size of atomic flows exponentially" (Remark 4.23).
- **BGGP (VS, abstract only).** Cut elimination in deep inference for classical propositional logic takes quasipolynomial time. The result is attributed to Jeřábek and is given a direct proof via atomic flows.

**(3) Represents / does not.** The formalism represents classical, linear (Straßburger), BV and modal logics. Atomic flows record only structural information, namely the creation, duplication and erasure of atoms. Many distinct derivations share one flow, so a flow is not an invariant of proof identity in any established sense. Binding is not handled: first-order instantiation stays non-local.

**(4) Strongest limitation.**
- Locality is a property of a *representation*, not of a logic (BRU03 quote above).
- Finiteness of the rule set is easy and uninformative. The interesting property is locality or atomicity, and that property fails at binders.
- DS16 (see A8) shows a hard limit for *linear* rules.

**(5) Relation to ProofBasis.** This is **direct prior art for the "finite local generators" sub-question**, at least propositionally: a fixed finite set of local rewrite rules generates all classical propositional proofs. A deep dive *could* change the framing. ProofBasis must say what its "generator" adds beyond (a) a finite rule set and (b) locality. BRU03 shows both are already achieved for classical propositional logic, and both are relative to a representation.

**(6) Neighbours.** Atomic flows connect to proof nets and Lamarche–Straßburger "N-nets" (A3/A6). Medial underlies Straßburger's Boolean categories (A6). Combinatorial proofs (Hughes, A2) are related to deep-inference proofs; see "Hug04 Deep inference proof theory equals categorical proof theory minus coherence", which is cited in STR06 and which I did NOT access.

---

## A2. Identity of proofs and general proof theory

**(1) Object.** Equivalence relations on derivations with fixed assumptions and conclusion, and the free categories that arise as their quotients.

**(2) Results.**
- **Normalization vs Generality Conjecture (DOS03, VS §§2–4).** Prawitz proposed identifying derivations by βη-equivalence (normalization). Lambek proposed identifying them by having the same maximal generalisation, which DOS03 formalises as faithfulness of a functor into a "graphical category", i.e. a coherence theorem. Quoted (§4): "The Normalization Conjecture and the Generality Conjecture agree only for limited fragments of logic." They agree for conjunctive logic, for disjunctive logic, and for conjunction-disjunction logic without distribution, ⊤ and ⊥. Both the soundness and completeness parts of coherence fail for cartesian closed categories with Kelly–Mac Lane-type graphs. The cause is contraction, illustrated by the λ-term λx⟨x,x⟩.
- **Maximality (DOS03, VS p.13–14).** For free cartesian categories, quoted: "take any equation in the language of free cartesian categories that does not hold in free cartesian categories. If a cartesian category K satisfies this equation, then K is a preorder". The paper calls this a "Post completeness" of βη. It is proved for CCCs via a typed Böhm theorem (Statman; Simpson). Quoted: "The maximality of bicartesian closed categories ... is, as far as I know, an open problem". That is the status as of DOS03 v12 (2004). The current status of BCC maximality is NA.
- **Joyal collapse (DOS03 §5, VS).**
  - Prop 1: in every CCC with initial ⊥, Hom(A,⊥) has at most one element.
  - Prop 2: a CCC with ⊥ and a natural ζ_A: ¬¬A→A is a preorder.
  - Prop 3: a BCC with a dinatural ξ_A: ⊤→A+¬A is a preorder.
  - Attribution (quoted): "In [32] the discovery of that fact is credited to Joyal (p. 116)". Here [32] is Lambek–Scott 1986.
  - STR06 (VS, p.59) gives Lafont's sequent-calculus version: confluent cut elimination with weakening and contraction identifies any two proofs of B.
- **Combinatorial proofs (HUG06, VS abstract and §1).** Quoted: "It defines a combinatorial proof of a proposition φ as a graph homomorphism h : C → G(φ) ... The main theorem is soundness and completeness: φ is true iff there exists a combinatorial proof". Quoted: "Each condition can be checked in polynomial time, so combinatorial proofs constitute a formal proof system [CR79]." HUG19 (VS abstract) extends this to first-order logic.
- **Hilbert's 24th problem.** R. Thiele, "Hilbert's twenty-fourth problem", Amer. Math. Monthly 110 (2003) 1–24. The **citation is VS via DOS03 ref [52]**; the content is **NA**. Doubrovinski, arXiv:2508.02764 (2025), takes a Kolmogorov-complexity approach. I read only its abstract, which is not decisive.
- Pistone, arXiv:2110.02630, proposes a criterion that identifies proofs via the naturality of rules. Abstract only (VS for abstract). It is adjacent work.

**(3) Represents / does not.** Normalization-based identity works for intuitionistic logic (CCC, BCC). Generality/coherence-based identity works for fragments without full contraction and distributivity. Neither gives a single accepted answer for classical logic. Combinatorial proofs give a syntax-free proof *object* for classical logic. They are not an identity criterion that is proved to coincide with any rewrite theory.

**(4) Strongest negative result.** The Joyal collapse: with the natural classical structure on top of a CCC, the identity of proofs collapses to provability. Consequence: any "explanatory generator" whose equations include CCC + ⊥ + natural ¬¬-elimination has *no* proof-identity content. This is a hard theorem constraint on ProofBasis's "proof identity across foundations" goal.

**(5) Relation to ProofBasis.** This is **direct prior art** for the proof-identity component. DOS03's "maximality" is the closest existing rigorous notion to "the equations are explanatory and complete": every further equation collapses the structure. A deep dive *should* change the framing. ProofBasis needs to say which identity criterion it uses (normalization, generality, or something else). The criterion cannot be foundation-neutral, because the classical and intuitionistic cases already diverge at the level of theorems.

**(6) Neighbours.** A6 supplies the categorical side: free categories, coherence, and Boolean categories. A3 gives identity via proof nets. A4 gives canonical sequent proofs. A1 gives combinatorial and deep-inference proofs.

---

## A3. Proof nets, geometry of interaction and ludics

**(1) Object.** Graphs (proof structures) with a correctness criterion. Danos–Regnier: every switching is acyclic and connected. Each proof structure that satisfies the criterion is a sequentialisable proof.

**(2) Results.**
- **Canonicity without units (HH16 intro, VS).** Quoted: "at least in the case of multiplicative linear logic without units, proof nets are canonical in the sense that two sequent calculus proofs give rise to the same proof net if and only if they are equivalent." The same holds for MALL without units (Hughes–van Glabbeek 2005) and for the additive fragment with units (Heijltjes 2011). These are cited in HH16, and the sources themselves are NA.
- **Units: negative result (HH16 Thm 9.1, VS).** Quoted: "MLL proof equivalence is PSPACE-complete." From the abstract: "It is also known as the word problem for ∗-autonomous categories ... An important consequence of the result is that the existence of a satisfactory notion of proof nets for MLL with units is ruled out (under current complexity assumptions). The PSPACE-hardness result extends to equivalence of normal forms in MELL without units".
- Danos–Regnier criterion: it is used as the definition in AJ92 and STR06 (VS that it is used). The original DR89 paper is NA.
- Geometry of interaction and ludics: **NA** this session. AJ92's abstract mentions "strong connections ... between history-free strategies and the Geometry of Interaction".

**(3) Represents / does not.** Proof nets quotient away rule permutations and give canonical objects for MLL−, MALL− and similar fragments. With units they cannot be canonical in polynomial time unless P = PSPACE: deciding equality is PSPACE-complete. Classical logic has no agreed proof nets (see STR07: "recent work has shown that there is no canonical axiomatisation of a Boolean category").

**(4) Strongest limitation.** HH16: even the free ∗-autonomous category, the most basic categorical proof theory with units, has a PSPACE-complete word problem. **A finite equational presentation of proof identity does not imply tractable or canonical normal forms.**

**(5) Relation to ProofBasis.** This is **direct prior art and a counterexample generator.** Any ProofBasis claim of the form "finite generators + equations ⇒ canonical proof objects" must survive HH16 as a baseline control. The rubric already lists "proof-net permutation" as a control. A deep dive would sharpen what is decidable or efficient, and it would not change the question itself.

**(6) Neighbours.** A6 (∗-autonomous categories). A7 (full completeness is stated for proof nets of MLL+MIX). A4 (multi-focusing recovers MLL− proof nets inside the sequent calculus).

---

## A4. Focusing and canonical forms

**(1) Object.** Focused sequent calculi (Andreoli). They alternate invertible ("asynchronous") phases with focused ("synchronous") phases. Multi-focusing allows several foci at once, and a proof is *maximal* when its foci are as parallel as possible.

**(2) Results.**
- **CMS08 Thm 7 (VS).** Quoted: "Theorem 7 (canonicity) If D ≃ E ⊢ Γ ⇑ · are both maximal, then D ≈ E." The abstract states a bijection to MLL proof nets without units. Quoted: "We validate this definition by proving a bijection to the well-known proof-nets for the unit-free multiplicative linear logic".
- **CHM12 (VS, abstract).** For classical first-order logic, quoted: "the maximally multi-focused proofs that make the foci as parallel as possible are canonical. Moreover, such proofs are isomorphic to expansion proofs".
- Andreoli 1992 (completeness of focusing for LL) and Liang–Miller 2009 (LJF/LKF): **NA**. That focusing is complete for LJ and LK via polarity assignment is UM.

**(3) Represents / does not.** Focusing gives canonical representatives modulo *permutations of inferences in cut-free proofs*. It says nothing about the identification of proofs with cuts, beyond what cut elimination gives. The identity it captures is the one of proof nets or expansion proofs, which is coarser than the sequent calculus and finer than provability. For classical logic it fixes one particular identity criterion (expansion proofs) and does not justify that choice.

**(4) Limitation.** Canonicity is relative to a chosen polarisation and to a chosen equivalence (permutations). For MLL with units, HH16 implies that there is no polynomial canonical form unless P = PSPACE.

**(5) Relation to ProofBasis.** This is adjacent structure and partial prior art: a "finite rule set + discipline ⇒ canonical proof forms" result already exists. Polarity and focusing also count as an explanatory generative principle: synchronous/asynchronous behaviour explains *why* rules invert. ProofBasis's "generative basis" should be compared with focusing as a baseline. It could change the framing by suggesting that the basis is a *polarity discipline*, not an algebra of operations.

**(6) Neighbours.** A3 (proof nets). A2 (identity via expansion proofs). A1 (deep inference has its own focusing results; NA). A8 (canonical systems also concern introduction rules).

---

## A5. Complexity of cut elimination

**(1) Object.** The size blow-up from proofs with cut to cut-free proofs, or to Herbrand disjunctions.

**(2) Results.**
- **Statman 1979, "Lower bounds on Herbrand's theorem", Proc. AMS 75:104–107; Orevkov 1979/1982, "Lower bounds for increasing complexity of derivations after cut elimination", J. Soviet Math 20:2337–2350.**
  - Status: **SO**, via Moser & Zach (MZ05), arXiv:math/0510640v1, section on lower bounds. Quoted: "Statman [22] and Orevkov [21] showed that this bound is not just an artefact of the particular cut-elimination procedure considered, but that proofs with cut essentially have hyper-exponential speedup over cut-free proofs." Also quoted: "(Statman's result requires equality, but Orevkov's does not.)"
  - The exact statements of the primary papers are NA. A web-search summary gave an Orevkov statement (a linear-size LK proof of C_k*, with no elementary bound on cut-free size). I treat that as unverified.
- **Propositional case:**
  - BGGP (VS abstract): quasipolynomial cut elimination in deep inference (attributed to Jeřábek).
  - GG08 (VS): its streamlining algorithms are exponential.
  - The exponential separation between propositional LK and cut-free LK is UM.

**(3)–(4) Implication.** Cut is *admissible* but not polynomially *derivable*. Admissibility (the same theorems) and derivability (one rule can be simulated by others with bounded overhead) come apart at a non-elementary cost in first-order logic. So "is cut primitive or derived?" has different answers depending on whether the criterion is provability, proof identity, or proof size.

**(5) Relation to ProofBasis.** This is **a hard constraint** on any "minimal basis" claim. Removing an admissible rule from a basis preserves the theorems and destroys proof complexity, and possibly the explanatory content: proofs with cut are where lemmas live. ProofBasis must fix which of {derivability, admissibility, polynomial simulation, proof identity} its notion of "generated" preserves. That choice is AGENTS.md rule 5.

**(6) Neighbours.** A1 (deep inference gives better propositional bounds). A2 (the normalization-based identity of proofs passes through this non-elementary process). Proof complexity in the Cook–Reckhow sense (HUG06 cites CR79; DS16).

---

## A6. Categorical proof theory

**(1) Object.** Free categories with structure, as quotients of derivations:
- CCC ↔ NJ(→,∧) with βη (Lambek–Scott);
- ∗-autonomous categories ↔ MLL (Seely; Barr);
- multicategories / Lambek deductive systems;
- control categories ↔ λμ (Selinger);
- "Boolean categories" (Führmann–Pym; Lamarche–Straßburger; Straßburger).

**(2) Results.**
- **Collapse theorems (DOS03 Props 1–3, VS; see A2).**
- **SEL01 §3.4 (VS).**
  - Lemma 3.7, quoted: "There is no central morphism f : 1 → A, unless A ≅ 1".
  - Cor 3.8, quoted: "A control category in which # is bifunctorial is equivalent to a boolean algebra."
  - Classical proof theory therefore avoids collapse only by making disjunction **premonoidal** (non-bifunctorial). That is, it builds evaluation order (call-by-name vs call-by-value) into the structure. The abstract, quoted: "We show that the call-by-name λµ-calculus forms an internal language for control categories, and that the call-by-value λµ-calculus forms an internal language for the dual co-control categories."
- **STR07 (VS abstract).** Quoted: "recent work has shown that there is no canonical axiomatisation of a Boolean category. In this work, we will see a series (with increasing strength) of possible such axiomatisations, all based on the notion of *-autonomous category." Führmann–Pym and Lamarche–Straßburger "Constructing free Boolean categories" are cited there; their own text is NA.
- **HH16.** The word problem for free ∗-autonomous categories is PSPACE-complete (A3).
- Lambek–Scott 1986, Seely 1989, Lambek's 1968–69 deductive systems: **NA**; cited in DOS03 and HH16.

**(3) Represents / does not.** Categorical proof theory gives exactly the "operations + composition + equations" presentation ProofBasis seems to want, for each logic separately. Each logic has its own doctrine. There is no single finite doctrine across foundations. The classical case forces a choice: a premonoidal or evaluation-order-sensitive structure (Selinger), or one of several non-equivalent Boolean-category axiomatisations (Straßburger).

**(4) Strongest negative result.**
- Classical collapse (Joyal; Selinger Cor 3.8).
- Non-canonicity of Boolean categories.
- PSPACE-completeness of the ∗-autonomous word problem.

**(5) Relation to ProofBasis.** This is **direct prior art and the strongest redundancy threat.** For each fixed logic, "a finite generative basis for proof operations, composition and identity" *is* the free-category or doctrine presentation. The open part is the uniformity *across* foundations, together with the explanatory/justification layer. A deep dive could reframe ProofBasis as a question about a **meta-doctrine** (for example 2-categorical, polycategorical, or the theory of doctrines and monads). The existing per-logic results serve as both baselines and counterexamples.

**(6) Neighbours.** A2 (maximality and coherence). A3 (proof nets as free ∗-autonomous categories). A7 (full completeness, the fullness of the functor from the free category). A1 (medial came from deep inference into Boolean categories).

---

## A7. Game semantics and full completeness

**(1) Object.** Categories of games and strategies in which formulas denote games and proofs denote winning strategies.

**(2) Results.**
- **AJ92 Theorem 1 (VS).** Quoted: "Every proof net in MLL + MIX denotes a uniform, history independent winning strategy for Player in our game interpretation. Conversely, every such strategy is the denotation of a unique cut-free proof net." Definition, quoted: "Full Completeness: Any f : A → B is the denotation of a proof of A ⊢B. (This amounts to asking that the unique functor from the relevant free category to C be full ...) One may even ask for there to be a unique cut-free such proof, i.e. that the above functor be faithful."
- Hyland–Ong; Blute–Scott (full completeness for MLL via dinaturality or vector spaces); Devarajan–Hughes–Plotkin–Pratt: **NA**. DHPP99 is cited in STR06's bibliography as "Full completeness of the multiplicative linear logic of Chu spaces" (citation title VS, content NA).
- Abramsky, "Axioms for definability and full completeness", arXiv:1401.4735: title seen only, content NA.

**(3) Represents / does not.** Full completeness yields a *semantic* characterisation of proofs: "every morphism is a proof". It is per-logic. It needs restrictions such as MIX, uniformity and history-freeness. It holds for fragments (MLL+MIX) and not for all of classical or dependent logic.

**(4) Limitation.** Full completeness is fragile. It depends on MIX and on uniformity conditions that are added precisely to exclude non-proofs. The conditions are tailored to the logic, so they are an existence result and not an explanation.

**(5) Relation to ProofBasis.** This is adjacent structure. It gives an *intrinsic* justification of inference: proofs are exactly the winning, uniform strategies. That bears on the rubric item "is validity external or intrinsic?". A deep dive could supply a fidelity criterion (fullness + faithfulness of the interpretation functor) that ProofBasis should adopt as its notion of "explains proof".

**(6) Neighbours.** A3 (proof nets). A6 (free categories). Geometry of interaction and ludics (NA).

---

## A8. Missing families: canonical systems, analytic calculi, display, hypersequents and linear rules

### A8a. Canonical Gentzen-type systems (Avron–Lev; Avron–Zamansky)

**(1) Object.** Sequent systems with the standard axioms and structural rules plus "canonical" logical rules. A canonical rule introduces exactly one occurrence of a connective or (n,k)-ary quantifier and mentions no other connective.

**(2) Results.**
- **AZ08 (VS, abstract and §2, §4).** Quoted: "Propositional canonical Gentzen-type systems, introduced in [2], are systems which in addition to the standard axioms and structural rules have only logical rules in which exactly one occurrence of a connective is introduced and no other connective is mentioned. In [2] a constructive coherence criterion is provided for the non-triviality of such systems and shows that a system of this kind admits cut-elimination iff it is coherent."
- Coherence (Def 2.9), quoted: "A canonical calculus G is coherent if for every two dual canonical rules Θ1 / ⇒ A and Θ2 /A ⇒, the set of clauses Rnm(Θ1 ∪ Θ2) is classically inconsistent."
- Prop 2.10: coherence is decidable.
- Thm 4.7, for k ∈ {0,1}: G is coherent ⇔ G has a strongly characteristic 2Nmatrix ⇔ G admits strong cut-elimination. Quoted: "coherence is not a necessary condition for standard cut-elimination". Extending to k > 1 (Henkin quantifiers) is left open.
- The original Avron–Lev paper ([2] in AZ08) is **NA**. Its venue and date are listed inconsistently in secondary records (IJCAR 2001 vs. a 2005 journal version), so they are UNVERIFIED.

**(3) Represents / does not.** A decidable syntactic criterion says when a *finite set of introduction rules* defines a well-behaved connective, with the semantics given by non-deterministic matrices. This is a theorem about the *propositional or quantifier layer*. The structural rules are fixed (LK-style), and proof identity is not addressed.

**(4) Limitation.** The structural layer is fixed. The semantics is two-valued and non-deterministic. There is nothing about identity or composition of proofs.

**(5) Relation to ProofBasis.** **Very close direct prior art** for "inference justification" and "finite rules define operations". Coherence ⇔ cut-elimination ⇔ 2Nmatrix semantics is exactly a theorem of the form "a finite rule schema is justified iff a decidable condition holds". ProofBasis must cite it and either subsume it or explain its difference. A deep dive could change the framing: the justification component may already have a decidable answer in this restricted setting.

### A8b. From axioms to analytic rules: the substructural hierarchy (CGT08, VS)

- Thm 4.2, quoted: "Every axiom in N2 is equivalent to a finite set of structural rules."
- Thm 5.6(1), quoted: "Every axiom in P3 is equivalent to a finite set of hyperstructural rules in HFLe."
- Cor 8.6, "Uniform cut-elimination": completed hyperstructural rules preserve cut-free provability.
- **Negative results.** Cor 7.2, quoted: "Any structural rule is either derivable in Gentzen's LJ or derives every formula in LJ." Cor 7.3: any hyperstructural rule is derivable in HSM or derives α ∨ ¬α^n. Ex 7.4: no (hyper)structural rule is equivalent to the Łukasiewicz axiom.
- So **finite structural-rule bases provably cannot capture certain logics.** Their expressive power is bounded by a polarity-alternation hierarchy. Going beyond P3 uniformly was open as of 2008.
- Relation to ProofBasis: direct prior art for "which axioms become finite analytic rules", including a provable *limit*.

### A8c. Display logic, hypersequents, nested and labelled sequents

- Belnap's display logic and its general cut-elimination theorem (eight conditions); Kracht's characterisation of properly displayable modal logics (primitive axioms); Negri's labelled calculi; Gabbay's labelled deduction; Ciabattoni–Ramanayake–Wansing (hypersequent ↔ display): all **NA** this session.
- On arXiv I saw only titles: Chen–Greco–Palmigiano–Tzimoulis, "Syntactic completeness of proper display calculi" (2102.11641); Goré–Postniece–Tiu (1103.5286).
- UM: Belnap's theorem says that any display calculus satisfying C1–C8 enjoys cut elimination. It is a *general* cut-elimination theorem over a family of finite rule sets, and so it is prior art of the same kind as A8a. This needs verification before it is cited.

### A8d. Linear rewriting bases for Boolean logic (DS16, VS)

- Quoted: "the set of all sound linear inference rules in Boolean logic is already coNP-complete". The paper then asks, quoted: "Question 1.1. Can we find a complete 'basis' of linear inference rules?"
- Main result (§1), quoted: "there is no polynomial-time decidable linear TRS that is complete for L, unless coNP = NP."
- This is a **direct negative result on a "complete basis" question** that has nearly ProofBasis's wording. It concerns linear inferences in Boolean logic, and it is conditional on coNP ≠ NP.

---

## Cross-cutting adversarial findings for ProofBasis

1. **Per-logic finite generative presentations of proofs and proof identity already exist and are standard.** Examples: free CCC/BCC ↔ NJ βη; free ∗-autonomous ↔ MLL; control categories ↔ λμ; SKS ↔ classical with local rules. Novelty, if any, can only lie in cross-foundation uniformity or in a precise "explanatory" criterion. (Status: VS for the cited theorems.)
2. **Theorem-level obstacles to foundation-neutral proof identity.**
   - Joyal collapse (DOS03 Props 1–3); Selinger Cor 3.8.
   - Normalization- and generality-based identity disagree beyond small fragments (DOS03 §4).
   - Boolean categories have no canonical axiomatisation (STR07).
3. **Complexity obstacles to canonical forms.**
   - MLL with units: equivalence is PSPACE-complete (HH16).
   - Cut elimination: non-elementary (Statman/Orevkov, SO), quasipolynomial in propositional deep inference (BGGP).
   - Complete linear bases: impossible in polynomial time unless coNP = NP (DS16).
4. **Prior theorems of the form "finite rule set justified iff decidable condition".**
   - Avron–Lev coherence ⇔ cut-elimination ⇔ 2Nmatrix (AZ08 Thm 4.7).
   - CGT08 hierarchy with negative Cor 7.2/7.3.
   - Belnap C1–C8 (UM).
   - These are the most decision-relevant missing items for ProofBasis's "inference justification" component.
5. **"Local" and "finite" are representation-relative** (BRU03 §3.5). Any ProofBasis finiteness claim must fix the representation (trees vs strings vs graphs) and the cost model.
6. **The DOS03 maximality (Post-completeness) notion** is a ready-made rigorous candidate for "the equations are complete/explanatory". Status: proved for CCC; open for BCC as of 2004 (current status NA).

## Not accessed (NA) or unverified

- Primary texts: Statman 1979; Orevkov 1982; Thiele 2003; Avron–Lev 2001/2005; Belnap 1982; Kracht 1996; Andreoli 1992; Liang–Miller 2009; Danos–Regnier 1989; Girard (proof nets, GoI, ludics); Lambek–Scott 1986; Seely 1989; Führmann–Pym; Lamarche–Straßburger "Naming proofs"/"Constructing free Boolean categories"; Straßburger "What is the problem with proof nets for classical logic?"; Hyland–Ong; Blute–Scott; Došen–Petrić "Proof-Theoretical Coherence" (book); Negri; Gabbay; Gundersen–Heijltjes–Parigot atomic λ-calculus; Hughes "Towards Hilbert's 24th problem" (combinatorial proof invariants); Brünnler "Two restrictions on contraction".
- Venue details marked [venue: UM] above (DOS03 in BSL 9 2003; AJ in JSL 1994; STR07 in TAC) were not checked against the publisher.
