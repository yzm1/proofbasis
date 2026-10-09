# Cluster E notes — concurrency, causality, rewriting, computation, deduction, complexity, analogies

Source agent E, session date 2026-10-09. All downloads in `<session-scratchpad>/t011/dl/E/`, text extracted (pdftotext / html-strip run from outside) into `<session-scratchpad>/t011/txtE/`. Nothing executed from downloads. Repo not modified.

Labels: VERIFIED_SOURCE = text retrieved and inspected this session (URL, version, location given). SECONDARY_ONLY = statement seen only as a restatement in a retrieved secondary source. UNVERIFIED-MEMORY = from background knowledge, not checked this session. NOT_ACCESSED = tried or listed, not obtained.

## Source register (retrieved this session)

| key | URL / version | used for |
|---|---|---|
| AGE21 | https://arxiv.org/abs/2105.10822v2 (Arsiwalla–Gorard–Elshatlawy, v2 25 Nov 2021, math.CT) | E3 |
| GZX20 | https://arxiv.org/abs/2010.02752v1 (Gorard–Namuduri–Arsiwalla, ZX + multiway I) | E3 |
| WMM22 | https://writings.stephenwolfram.com/2022/03/the-physicalization-of-metamathematics-and-its-implications-for-the-foundations-of-mathematics/ (HTML, fetched 2026-10-09) | E3 |
| GM09 | https://arxiv.org/abs/0810.1442v2 (Guiraud–Malbos, "Higher-dimensional categories with finite derivation type", v2 20 Oct 2009) | E2/E3 |
| GM14 | https://arxiv.org/abs/1402.2587v2 (Guiraud–Malbos, "Polygraphs of finite derivation type") | downloaded, only title checked |
| egg | https://arxiv.org/abs/2004.03082v3 (Willsey et al., egg; PACMPL POPL 2021) | E2 |
| Hir13 | https://arxiv.org/abs/1307.6318v3 (Hirschowitz, LMCS 9(3:10) 2013) | E1/E2 |
| Maude19 | https://arxiv.org/abs/1910.08416v1 (Durán, Eker, Escobar, Martí-Oliet, Meseguer, Rubio, Talcott, "Programming and Symbolic Computation in Maude", accepted JLAMP Oct 2019) | E2 |
| Win17 | https://www.cl.cam.ac.uk/~gw104/ecsym-notes.pdf (Winskel, "Event Structures, Stable Families and Concurrent Games", notes dated Feb 2017) | E1 |
| PW26 | https://arxiv.org/abs/2609.37815v1 (Paquet–Winskel, "Concurrent Strategies as Street Fibrations", v1 29 Sep 2026, "Submitted to MFPS 2026") | E1 (abstract only) |
| CP10 | https://www.cs.cmu.edu/~fp/papers/concur10.pdf (Caires–Pfenning, "Session Types as Intuitionistic Linear Propositions", CONCUR 2010 author copy) | E1 |
| Wad12 | https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-sessions/propositions-as-sessions.pdf (Wadler, ICFP 2012 author copy) | E1 |
| WTRB | https://matryoshka-project.github.io/pubs/saturate_article.pdf (Waldmann–Tourret–Robillard–Blanchette, journal manuscript) + AFP entry https://www.isa-afp.org/entries/Saturation_Framework.html | E4 |
| Alethe | https://arxiv.org/abs/2107.02354v1 (Schurr–Fleury–Barbosa–Fontaine, PxTP 2021 ext. abstract) | E4 (abstract only) |
| Buss97 | https://mathweb.ucsd.edu/~sbuss/ResearchWeb/marktoberdorf97/paper.pdf (Buss, "Propositional Proof Complexity: An Introduction") | E5 |
| Pud | https://arxiv.org/abs/1601.01487v2 (Pudlák, "Incompleteness in the finite domain", BSL 23(4) 2017/18) | E5 |
| Kha19 | https://arxiv.org/abs/1904.01362v2 (Khaniki 2019) | E5 |
| SEP-RF | https://plato.stanford.edu/entries/recursive-functions/ (first pub. 2020, rev. 1 Mar 2024) | E6 |
| W-Craig | https://en.wikipedia.org/wiki/Craig%27s_theorem (fetched 2026-10-09; tertiary) | E6 |
| Lan11 | https://publications.ias.edu/sites/default/files/functoriality.pdf (Langlands, "Functoriality and Reciprocity", two IAS lectures March 2011) | E7 |
| Fre05 | https://arxiv.org/abs/hep-th/0512172v1 (Frenkel, Lectures on the Langlands Program and CFT) | E7 |
| ACFIL | https://arxiv.org/abs/2010.01943v3 (Aceto–Castiglioni–Fokkink–Ingólfsdóttir–Luttik, v3 30 Mar 2022) | E8 |
| AFIL06 | https://arxiv.org/abs/cs/0608001v2 (Aceto et al., "A Finite Equational Base for CCS with Left Merge and Communication Merge") | E8 (title only) |

Irrelevant download: arXiv math/0206310 ("Optimal reduction", Ortega) is symplectic geometry, a name collision with Lévy optimal reduction. Do not cite it.

NOT_ACCESSED (paywalled or not found): Nielsen–Plotkin–Winskel 1981 TCS (the Elsevier linking page only); Rideau–Winskel LICS 2011 (author URL 404); Meseguer 1992 TCS (ScienceDirect 403); Clavel–Meseguer reflection papers; Martí-Oliet–Meseguer "RL as a logical and semantic framework"; Cook–Reckhow 1979 JSL and Reckhow 1976 thesis (I saw only Buss's restatement); Krajíček–Pudlák 1989 (seen only as cited, with its theorem restated in Kha19); Moller 1989/1990 (seen only as restated in ACFIL); Craig 1953 and Craig–Vaught 1958; Lévy 1978 thesis, Lamping 1990, Asperti–Guerrini 1998, Asperti–Mairson 1998; Mazurkiewicz; Engberg–Winskel; Kohlenbach; Statman/Orevkov; Robinson 1965; Bachmair–Ganzinger handbook chapter; LFSC; Gorard "Some quantum mechanical properties of the Wolfram model" (no arXiv hit for that title); Wolfram's book version of Metamathematics (I used only the essay); the Maude manual (URL 404 or TLS failure).

---

## E1 Concurrency and causality

**(1) Object.** An event structure (Winskel's general form) is (E, ≤, Con), where ≤ is causal dependency and Con is a family of finite consistent sets. The axioms are: finite causes, {e} ∈ Con, Con closed downward, and closure of consistent sets under causes. Concurrency is defined as `e co e′ iff {e,e′} ∈ Con & e ≰ e′ & e′ ≰ e`. [VERIFIED_SOURCE Win17 §"event structures", txt l.586–600.] Concurrent games and strategies use polarised event structures: a strategy is a map σ: S → A⊥∥B, and composition is by synchronised product plus hiding. Session-type Curry–Howard: π-calculus processes typed by linear propositions.

**(2) Strongest results.**
- Copycat characterisation [VERIFIED_SOURCE Win17 Thm 4.12 and Thm 4.18, pp. ~53–56]. "If σ⊙γA ≅ σ and γB⊙σ ≅ σ, then σ is receptive and innocent," and receptive, innocent pre-strategies are closed under composition. Thm 4.18 gives σ⊙γA ≅ σ (for receptive, innocent σ). The notes attribute the chapter to joint work with Rideau [ref 5, LICS 2011]. Status: established, peer reviewed in the LICS version (NOT_ACCESSED). The notes give the result together with its proofs. **Meaning:** "strategies" are exactly the pre-strategies for which copycat is an identity. The identity/composition law forces two local causal conditions (receptivity and innocence). This is a genuine *theorem that derives admissible causal shape from categorical identity*.
- PW26 (v1, Sep 2026, preprint, not peer reviewed) [VERIFIED_SOURCE abstract only]. It characterises, with symmetry, the classes of strategies where composition has an identity "up to a 'weak' and a 'strong' notion of equivalence". The weak class is "precisely those inducing Street fibrations over the game". Status: preprint.
- Caires–Pfenning 2010 [VERIFIED_SOURCE CP10 abstract and §1 l.79–87]. They give a π-calculus type system that "exactly corresponds to the standard sequent calculus proof system for dual intuitionistic linear logic". It has "a tight operational correspondence between π-calculus reductions and cut elimination steps" (Thms 5.3, 5.6) and deadlock absence (Thm 5.8). Wadler 2012 [VERIFIED_SOURCE Wad12 abstract] does the same for classical linear logic (CP) and gives a translation from GV. "Top-level cut elimination corresponds to lack of deadlock" (l.477).
- Permutation equivalence for higher-order rewriting has a sound and complete 2-categorical semantics [VERIFIED_SOURCE Hir13 Thm 4.2]: "There exists an identity-on-objects, identity-on-morphisms, locally full cartesian closed 2-functor H(X) → R(X)." Hir13 builds on Bruggink's generalisation of permutation equivalence (Terese Ch. 8).

**(3) Represents / cannot.** These frameworks represent causal dependency and conflict among *events*, and composition of interactive behaviours, with identity forced by copycat. Through Curry–Howard for sessions they also represent cut reduction as communication. They do not provide a foundation-neutral account of inference *justification*. The logic (DILL/CLL) is fixed in advance, and games model types and strategies, not arbitrary proof systems. Proof identity is modelled only up to the chosen semantic equivalence (iso of strategies, or of weak/strong symmetry classes in PW26). Causal order in event structures is a *semantic* partial order; it is not an execution schedule. This matches the ProofBasis requirement (AGENTS.md rule 7) and is a precedent for keeping the two apart.

**(4) Strongest limitation.** The session correspondences only cover the logic they were built for. The deadlock-freedom guarantee comes from the tree-shaped cut structure of linear-logic proofs, so cyclic process topologies that are deadlock-free in practice are excluded [UNVERIFIED-MEMORY as a stated limitation; the Wad12 l.477 link between cut and deadlock is verified]. With symmetry, the game model has *several inequivalent notions of equivalence* (PW26 abstract). This is a direct warning that "proof identity" here is not canonical.

**(5) Relationship to ProofBasis.** Adjacent; partly direct prior art for the "graph/time" and "proof identity via composition" axes. The copycat theorem is the strongest example in the cluster of a *derived* (not stipulated) constraint on causal shape. A deep dive (Rideau–Winskel 2011, Castellan–Clairambault–Rideau–Winskel "Games and strategies as event structures" LMCS 2017 [UNVERIFIED-MEMORY]) could change the framing. It would push ProofBasis to define its "causal" layer as a bicategory of strategies, rather than as a new primitive.

**(6) Neighbours.** Proof nets / linear logic (cluster with Girard). Polygraphs (E2/E3): permutation equivalence = 3-cells. Optimal reduction (Lévy families, Lamping sharing graphs: NOT_ACCESSED). Petri-net models of linear logic (Engberg–Winskel: NOT_ACCESSED). Mazurkiewicz traces = equivalence classes of words under an independence relation [UNVERIFIED-MEMORY; not inspected].

## E2 Rewriting, rewriting logic, e-graphs

**(1) Objects.** Term rewriting systems and abstract rewriting. Rewriting logic: a rewrite theory (Σ, E, R) with "Computation = Deduction". Polygraphs/computads as presentations of higher categories. E-graphs: union-find plus hash-consed e-nodes representing a congruence.

**(2) Strongest results.**
- **Squier's theorem and its higher-dimensional failure** [VERIFIED_SOURCE GM09 Introduction l.190–193 and Thm 4.3.9]. Squier: when a monoid "admits a presentation by a finite and convergent word rewriting system, then it has finite derivation type". Hence "rewriting is not a universal way to decide the word problem of finitely generated monoids". Squier exhibited a finitely presented monoid with decidable word problem that lacks FDT. GM09 Thm 4.3.9: "For every natural number n ≥ 2, there exists an n-category which does not have finite derivation type and admits a presentation by a finite convergent (n + 1)-polygraph." The proof uses Prop. 3.3.4 to show that FDT is *independent of the finite presentation chosen*. Status: established (peer-reviewed version: Math. Struct. Comp. Sci. 2009 [UNVERIFIED-MEMORY for venue]).
- **Rewriting logic reflection / universal theory** [VERIFIED_SOURCE Maude19 §1 l.222–229]. "Rewriting logic is a reflective logic. This means that its meta-theory, including notions such as theory and term, can be represented as data at the so-called object level of the logic in a universal theory. It also means that such a universal theory, like in the case of universal Turing machines, can simulate any other theory, including itself." Also (l.124–130): "a logic's inference system can be naturally specified as a rewrite theory whose (possibly conditional) rewrite rules are exactly the logic's inference rules". The paper names linear, first-order, modal and lambda-cube logics. The underlying theorem (Clavel–Meseguer) is NOT_ACCESSED; this is the authors' own summary. Status: established result cited in a secondary summary by the original authors.
- **E-graphs** [VERIFIED_SOURCE egg Def 2.1–2.5, §3.2.2]. "An e-graph efficiently represents a congruence relation over many expressions". Rebuilding preserves the congruence closure (proof given, §3.2.2). Equality saturation runs "until saturation or timeout". Footnote 7: "E-graphs do not have any 'built-in' support for binding; for example, equality modulo alpha renaming is not free."

**(3) Represents / cannot.** Rewriting logic represents any r.e. inference system as rewrite rules, with concurrency as parallel rewriting (proof terms modulo the RL equations [UNVERIFIED-MEMORY on the exact axioms of Meseguer 1992]). It does *not* explain why rules are justified: soundness is external. E-graphs represent equivalence classes of first-order terms, i.e. "proof identity as a congruence". They cannot represent binding natively, and saturation need not terminate. Polygraphs represent proofs-of-equality and the identities between them (homotopy bases).

**(4) Strongest limitation and negative results.**
- (a) **Squier/GM09.** Finite convergent presentation does not imply finite homotopical basis in dimension ≥ 3. FDT is a *presentation-invariant* finiteness property that can fail. This is the cleanest established **negative finite-basis theorem for "identities between derivations"** found in this cluster.
- (b) **The RL universal theory is vacuous universality** in the sense of AGENTS.md rule 6. The authors themselves compare it to universal Turing machines. It is the model case of an encoding that ProofBasis must not count as an explanatory basis.

**(5) Relationship to ProofBasis.** Direct prior art. RL/Maude is an existing finite logical framework that claims to specify all those logics "without any encoding". Any ProofBasis claim must be strictly stronger than that, e.g. by preserving proof identity or justification. Squier/FDT is direct prior art for the "proof identity / transformations finitely generated?" question, with a known *negative* answer in general. A deep dive into Guiraud–Malbos (GM14; Guiraud's habilitation "Rewriting methods in higher algebra" 2019 [cited in AGE21, NOT_ACCESSED]) could change the framing. ProofBasis's "finite basis for proof identity" may reduce to known FDT and homological finiteness (FP∞) questions, which are already known to fail in general.

**(6) Neighbours.** E3 (multiway = abstract rewriting with all branches). E1 (permutation equivalence). E4 (completion / critical pairs = superposition). E8 (finite equational axiomatisability).

## E3 Wolfram multiway systems, ruliad, Gorard et al.

**(1) Object.** Multiway system = an ARS with all rewrite branches recorded as a DAG (AGE21 Defs 2.1–2.2). "Rulial space" is defined as "the category of cospans of a … adhesive category" (AGE21 Def 2.3, l.237). The *ruliad* is "the entangled limit of all possible computations" (WMM22). It is not given a mathematical definition in the essay.

**(2) What is theorem vs. exposition.**
- AGE21 [VERIFIED_SOURCE]. Prop 3.1 concerns *one specific example* ("The multiway rewriting system shown in Figure 5 … yielding a double category"). Prop 3.2 says that, *so long as additional rewrite rules … are admissible*, that example "can be enhanced" to an n-fold category; the proof is "a simple inductive construction". Prop 3.3 says the n→∞ limit "is an ∞-groupoid". Its proof is one paragraph that asserts "The n → ∞ limit of an n-fold groupoid is precisely an ∞-groupoid." The paper then invokes Grothendieck's homotopy *hypothesis* to obtain "a formal homotopy space" (abstract). **Assessment (informal argument, mine):** these are illustrative constructions on an example, conditional on unspecified admissibility. The step from n-fold (cubical) structure to ∞-groupoid is asserted, not proved. The homotopy hypothesis is used as a premise. No theorem compares the construction with existing higher rewriting (polygraphs, Squier, Guiraud–Malbos) beyond citing Burroni and Guiraud. Status: preprint with propositions of limited scope; not a general theorem.
- GZX20 [VERIFIED_SOURCE]. A grep finds no Theorem, Proposition or Lemma environments. Completeness and consistency of a calculus are "straightforwardly infer[red] … by simply inspecting the state vertices" of a finite multiway graph, using toy string-rewrite examples (l.1990–2004). It contains an explicit conjecture: "which we conjecture is given by the inversion of multiway evolution edges, although we have not yet …" (l.3541). Status: expository/computational. **Objection:** inspecting a finite prefix of the multiway graph cannot establish completeness or consistency of an infinite system in general (Rice/undecidability, E6).
- WMM22 [VERIFIED_SOURCE]. The essay abstract is explicitly non-theorematic: metamathematics and physics "are posited to emerge"; "It is argued that mathematics as currently practiced can be viewed as derived from the ruliad". Critical-pair lemmas are acknowledged as standard ATP machinery (l.633: "In automated theorem proving these bisubstitution events are typically called 'critical pair lemmas'"). Status: conjectural/philosophical. It contains empirical explorations of entailment graphs, not proofs.

**(3) Represents / cannot.** Multiway graphs represent the full nondeterministic derivation space of a *given* rule set, with branch/merge (critical pairs) and "homotopies" (2-cells). They cannot supply a criterion of soundness or justification. The "ruliad" is not a finitely generated object, so it is not a finite basis in any sense ProofBasis can use.

**(4) Strongest limitation.** Everything provable here is already a special case of higher-dimensional rewriting (polygraphs, Squier resolutions, GM09). That theory has *negative* finiteness results (E2(4a)) which the Wolfram-programme papers do not engage. "All possible rules" is universal computation, i.e. a vacuous solution under AGENTS.md rule 6.

**(5) Relationship to ProofBasis.** Analogy and speculative prior art. A deep dive could change the framing only negatively: it would confirm that ProofBasis must not adopt "all rules" universality. The publicity of this programme also makes a "finite generative basis for proof" pitch prone to being read as Wolfram-adjacent, so ProofBasis should differentiate itself explicitly.

**(6) Neighbours.** E2 (polygraphs, completion), E6 (universality), E1 (causal graphs vs event structures; the "causal invariance" notion relates to confluence [UNVERIFIED-MEMORY on precise definition]).

## E4 Automated deduction

**(1) Object.** In WTRB [VERIFIED_SOURCE l.170–175] an "F-inference system Inf is a set of F-inferences", i.e. an *arbitrary set* of tuples (Cn,…,C0). A redundancy criterion Red = (Red_I, Red_F) satisfies (R1)–(R4) (l.179–186). N is saturated iff Inf(N) ⊆ Red_I(N). Static refutational completeness: every saturated N with N ⊨ ⊥ contains ⊥ (l.249–253).

**(2) Strongest results.**
- WTRB Lemma 10 [VERIFIED_SOURCE]: static refutational completeness implies dynamic refutational completeness, for fair derivations. Further results cover lifting to non-ground calculi and given-clause architectures. **Formally checked:** AFP entry "A Comprehensive Framework for Saturation Theorem Proving" (Tourret, 9 Apr 2020, Isabelle/HOL, BSD license) "verifies a framework for formal refutational completeness proofs of abstract provers that implement saturation calculi, such as ordered resolution or superposition" [VERIFIED_SOURCE AFP page]. I did not record the Isabelle version used; the AFP release must be checked.
- Robinson resolution completeness; Bachmair–Ganzinger superposition completeness via model construction [UNVERIFIED-MEMORY; NOT_ACCESSED].
- SMT certificates: Alethe aims to be a generic SMT proof format [VERIFIED_SOURCE abstract only]. Its abstract stresses that solver heterogeneity makes a common format hard. LFSC: NOT_ACCESSED.

**(3) Represents / cannot.** This framework abstracts *calculus + redundancy + prover loop* in a calculus-agnostic way, and it is mechanised. That is a real existing "generic machinery" theorem. It does not represent binding or higher-order proof identity, and it is restricted to refutational first-order-style settings. Finiteness of the rule *schema* is **not** part of the abstract definition: Inf is any set.

**(4) Limitation.** Completeness is relative to a consequence relation |= supplied as a parameter. Justification is external, so the framework is neutral but not explanatory. Proof certificates (Alethe) carry many solver-specific rules, and the extended abstract presents the format's generality as aspirational ("Towards").

**(5) Relationship to ProofBasis.** Direct prior art for "inference system as generation, with saturation" and a formally checked baseline. It gives ProofBasis a required control: any proposed basis must say what it adds beyond WTRB's abstract (Inf, Red) framework.

**(6) Neighbours.** E2 (completion = superposition for equations; e-graphs = ground congruence closure). E5 (resolution as a Cook–Reckhow proof system).

## E5 Proof complexity

**(1) Object.** Cook–Reckhow: "a proof system is a polynomial time computable function P from Σ* onto TAUT" [SECONDARY_ONLY, Pud §5 p.23, quoting [11] = Cook–Reckhow JSL 44 (1979)]. Pud notes that this captures poly-time checkability, soundness and completeness, and that "a proof can be any evidence that shows logical validity". A Frege system is a propositionally complete language L, a finite set of schematic axioms and a finite set of schematic rules [VERIFIED_SOURCE Buss97 §2, l.140–150].

**(2) Strongest results.**
- **Robustness of Frege** [SECONDARY_ONLY via Buss97, citing Cook–Reckhow 1979 [20] and Reckhow 1976 thesis [39]]. Thm 2: "Let F1 and F2 be Frege systems over the same language. Then there is a constant c > 0 such that for all φ and n, if F1 ⊢ⁿ φ, then F2 ⊢^{≤cn} φ". Thm 3: for any two sound and complete Frege systems, under the natural translation, there is a polynomial p bounding proof size, and the translation is poly-time computable. Thm 5: "Any two extended Frege proof systems p-simulate each other." The proof idea of Thm 2 is to prove the smallest instance of each schematic axiom and rule once, then substitute (Cook–Reckhow Lemma 2.5).
- **p-optimal proof systems** [SECONDARY_ONLY via Kha19 Thm 2.4 citing Krajíček–Pudlák 1989]. A p-optimal proof system for TAUT exists iff some theory T proves Con_S(n̄) by poly-time-constructible proofs for every S in the class 𝒯 (the theory class there). Status: whether one exists is open (the conjecture "CON" that none exists, Pud l.1266). Polynomially bounded proof systems exist iff NP = coNP (Pud §5). Caveat: Pud's displayed definition of "length-optimal" appears to have P and Q transposed in the extracted text (l.1060–1063); I relied on Kha19's Def. 2.3 for p-simulation.

**(3) Represents / cannot.** The Cook–Reckhow definition is a *universal, foundation-neutral definition of a proof system*, but only up to verifier semantics: a proof is any string that a poly-time function maps to a tautology. It deliberately erases structure, composition, binding and proof identity. Frege robustness shows that *finite schematic presentations* of classical propositional logic are p-equivalent, i.e. presentation-invariance holds at the level of proof size.

**(4) Limitation.** Robustness is about lengths and polynomial simulation. It says nothing about proof identity or structural correspondence. It is specific to propositional Frege (same consequence relation; classical). Optimality is open and tied to major complexity conjectures.

**(5) Relationship to ProofBasis.** Strong adjacent prior art and an important control. (a) A universal *definition* of proof system already exists and is trivial-by-design (a poly-time surjection); ProofBasis's universality must not collapse to it. (b) "All Frege systems are p-equivalent" is the best established precedent for a *theorem* of the form "any finite schematic basis is as good as any other, up to a robust equivalence". A ProofBasis analogue would need a finer equivalence than p-simulation. A deep dive could reframe the goal as finding the right "simulation" notion that preserves identity.

**(6) Neighbours.** E6 (Craig: r.e. ⇒ decidable axiomatisation; poly-time version). E4 (resolution, cutting planes as proof systems). Cut elimination and Statman/Orevkov non-elementary blowups [UNVERIFIED-MEMORY, NOT_ACCESSED].

## E6 Computability and universality

**(1) Objects.** Partial recursive functions, Kleene T-predicate, index sets, r.e. theories.

**(2) Results.**
- Kleene Normal Form [VERIFIED_SOURCE SEP-RF Thm 2.3]. There is a primitive recursive T_k and a primitive recursive u such that every k-ary partial recursive f has an index e with f(n⃗) ≃ u(μs T_k(e,n⃗,s)). This is a *single finite universal form* for all computation.
- Rice [VERIFIED_SOURCE SEP-RF Thm 3.4]: "If I is a non-trivial index set, then I is undecidable."
- Craig's theorem [SECONDARY_ONLY, W-Craig, tertiary]: "any recursively enumerable set of well-formed formulas of a first-order language is recursively axiomatizable, and even primitively recursively axiomatizable, and even decidable in polynomial time." Original Craig 1953 is NOT_ACCESSED. Craig–Vaught (finite axiomatisability with extra predicates for r.e. theories with only infinite models, as I recall it) is UNVERIFIED-MEMORY.

**(3)/(4) Consequence.** At the level of *derivability* or *computation*, "a finite basis exists" is trivially true (Kleene NF; universal TM; RL universal theory; Craig). Any nontrivial semantic property of an arbitrary rule system is undecidable (Rice), which bounds what a basis can certify automatically. The limitation is the converse of triviality: these results preserve extension (what is derivable or computed), not structure.

**(5) Relationship.** This is the decisive *trivialisation baseline*. ProofBasis must state precisely which invariant (proof identity, justification, compositional structure) is not captured by Kleene/Craig-style universality. Otherwise the north-star question is already answered positively and vacuously.

**(6) Neighbours.** E2 (RL reflection explicitly analogised to UTM), E3 (ruliad), E5 (Cook–Reckhow = poly-time Craig-style generality).

## E7 Langlands functoriality (analogy check)

**(1) Object.** Given an L-group homomorphism φ: ᴸH → ᴸG, functoriality predicts a transfer of automorphic representations of H to G. Frenkel [VERIFIED_SOURCE Fre05 footnote 44, p.~60] describes a "functoriality principle … asserts the existence of a relationship between automorphic representations of two adèlic groups H(A) and G(A) … for any given homomorphism Gal(F̄/F) ⋉ ᴸH → ᴸG". Langlands himself [VERIFIED_SOURCE Lan11 pp.1–2] calls it "best to regard as a possibility that with sufficient effort and imagination can be realized". He uses it to "isolate the generating elements of the relevant mock Tannakian categories", the "hadronic" pairs. All other pairs "are obtained [from] one of hadronic type by the functorial transfer associated to a homomorphism φ : ᴸH → ᴸG". He also says "There is no reason to believe that φ is uniquely determined", and that the lectures "are certainly intended to be informal".

**(2) Status.** Functoriality in general is conjectural. Many special cases are proved [UNVERIFIED-MEMORY; not inspected this session].

**(3)–(5) Assessment.** Langlands's own framing contains a structural analogy that is closer to ProofBasis than expected: "generating elements" plus transfers along morphisms, with non-uniqueness of φ. But there is **no technical link**: the objects are automorphic representations and L-groups, not proofs, and no theorem transfers. Relevance is methodological or analogical only. A deep dive would not change ProofBasis framing. It would at most supply rhetoric, and that rhetoric is risky: invoking Langlands suggests depth not earned.

**(6) Neighbours.** Tannakian reconstruction (a group recovered from its representation category) is the only plausibly technical bridge, via categorical logic. It is speculative and was not investigated.

## E8 Missing families — finite axiomatisability in process algebra (NEGATIVE analogue)

**(1) Object.** Equational axiomatisations of bisimilarity over CCS fragments (with or without auxiliary operators).

**(2) Results** [VERIFIED_SOURCE ACFIL §1 and Thms 1–2].
- Hennessy–Milner's ground-complete axiomatisation "included infinitely many axioms, which were instances of the expansion law".
- Bergstra–Klop: finite axiomatisation with left merge and communication merge.
- Moller: "even in the presence of a single action, bisimilarity does not afford a finite ground-complete axiomatisation over the closed terms" of prefixing + choice + interleaving, so "auxiliary operators are indeed necessary" [Moller SECONDARY_ONLY].
- Aceto et al.: the same failure holds with Hennessy's merge.
- ACFIL Thm 1: if a binary operator f satisfies Assumptions 1–3, "bisimilarity admits no finite equational axiomatisation over CCS_f". Thm 2 strengthens this to no finite *ground-complete* axiomatisation. The setting is the recursion-, relabelling- and restriction-free fragment, and the full question (their "Problem 8") remains open.

**(3)/(4).** This is a mature *negative* theory: whether a finite equational basis exists depends on the choice of auxiliary operators. Adding operators can turn an infinitely based theory into a finitely based one. **Implication (informal argument, mine):** "finite basis exists" is presentation-sensitive. Expressivity can be traded for finiteness, so ProofBasis must fix the signature, or quantify over admissible auxiliary operators, before a finite-basis question is meaningful. Otherwise auxiliary operators play the role of smuggled interpreter operations (AGENTS.md rule 6).

**(5)** Direct methodological prior art: it is the closest established analogue of ProofBasis's question, with techniques for proving non-finite-basedness (Moller's proof-theoretic technique). A deep dive could materially change the framing toward "under which signature-extension rules is a finite basis possible?"

**Other E8 items, not investigated:** ZX-calculus completeness (relevant as a diagrammatic proof system with *proved* completeness theorems, unlike GZX20's use of it) [UNVERIFIED-MEMORY]; Engberg–Winskel Petri-net semantics of linear logic; Kohlenbach proof mining; Griffin / λμ classical Curry–Howard. All NOT_ACCESSED.

## Cross-cutting decision-relevant points
1. **Trivial positive answer exists** at the levels of derivability, computation and verifier (Kleene NF, Craig, Cook–Reckhow, RL universal theory). ProofBasis must name the invariant beyond these.
2. **Established negative finite-basis theorems exist** for (a) identities between derivations (Squier; GM09 Thm 4.3.9, presentation-invariant FDT failure) and (b) equational axiomatisation of concurrency (Moller; ACFIL). They are the strongest adversarial prior art found.
3. **Presentation invariance precedents:** Frege p-equivalence (size level); FDT independence from finite presentation (homotopy level).
4. **Formally checked generic machinery:** the saturation framework (Isabelle AFP).
5. **Wolfram/Gorard:** the theorems are of limited scope (an example-level double category; an asserted ∞-groupoid limit); the rest is exposition or conjecture. It is subsumed by polygraph theory, which it does not engage.
