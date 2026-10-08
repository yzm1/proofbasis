# Report 002: Fundamentality, environment separation, and non-vacuity

| | |
|---|---|
| **Task** | `tasks/002-fundamentality-and-anti-vacuity.md` (Stage 0.5) |
| **Base** | `research/stage-0-5-coordination` @ `62ec35d` |
| **Date** | 2026-10-08 |
| **Status** | Review requested. Nothing here is FORMALIZED; no checker was run. Every argument of my own is labelled INFERENCE (informal argument) or CONJECTURE. Source statuses use `docs/RESEARCH_PROTOCOL.md` vocabulary. |
| **Evidence log** | [`reports/002-source-notes/`](002-source-notes/README.md) |

**Disclosure.** This report was written in the same session, by the same model, that wrote PR #2 (report 001 and its self-review). That limits its independence from PR #2. PR #1 (Codex) and the Stage-0 synthesis were read in full. Their conclusions are treated as claims to check, not as results.

**Inputs read in full.** AGENTS.md, the charter, the definitions document, the falsification plan, `docs/STAGE_0_SYNTHESIS.md`, PR #1's report, PR #2's report, PR #2's self-review (`reports/001-review.md`) and the source notes of both PRs.

---

## 0. Executive verdict

**Recommendation: NARROW.** Do not proceed to any algebra or implementation, and do not stop on the evidence gathered here.

1. **A precise anti-vacuity definition exists, and it is independently motivated.**
   - **The property.** A representation must be a *homomorphism of the source's substitution structure*. Instantiating schematic variables, and substituting derivations for hypotheses, must be carried out by the target's own substitution (definition SN/HN, §2.3).
   - **What it rules out.** For finitely schematic sources (§2.1), this property forces each source rule to be sent to one fixed *derived rule* of the target (Lemmas 1–2, §3). This excludes every universal-interpreter construction examined:
     - Mossakowski–Diaconescu–Tarlecki (MDT) flattening;
     - the Clavel–Meseguer universal theory;
     - EF + reflection;
     - Jeřábek's ubiquitous conservative translations;
     - a Turing-machine step checker;
     - a Dedukti conversion checker.
     
     Interpreters inspect *instances*. A homomorphism can only act on *schemas* (§5).
   - **Why it is not tailored to the interpreter.** The same property is, under different names:
     - Łoś–Suszko structurality in algebraic logic;
     - Harper–Honsell–Plotkin's (HHP) compositional adequacy;
     - Cook–Reckhow's substitution-closed Frege rules;
     - Fiore–Plotkin–Turi and Fiore–Mahmoud morphisms of syntax with binding;
     - the "structurality" whose general formulation MDT left open.
2. **The property must be stated in its strong form.**
   - The weak, existential form ("for every substitution σ there is some σ\* with t(σφ) ≡ σ\*(tφ)") is satisfied by both MDT's flattening and Jeřábek's translations, so it excludes nothing (INFERENCE, §3.3).
   - Even the strong form has one documented loophole that I judge benign (§5, L-a), and it over-excludes in two documented ways (§5, L-f, L-g).
3. **Anti-vacuity is not fidelity.** A homomorphic encoding of multiplicative linear logic that uses unrestricted hypotheses passes the anti-vacuity property and still derives p ⊢ p⊗p, which linear logic does not prove (§6.2). Resource discipline needs *reflection of derivability* as a separate clause.
4. **"Fundamental operation" cannot be an invariant property of individual operations.**
   - The Boolean clone has the disjoint bases {nand} and {∧, ¬}, so no operation belongs to every basis (Böhler et al. Ex. 1.3).
   - Cook–Reckhow Thm 2.3 makes all Frege bases mutually translatable, rule by rule, with linear overhead.
   - Only *generated structures* and an *interpretability preorder* are presentation-invariant (§7). Comparing primitive counts is meaningless.
5. **The fundamentality question splits.** I give three inequivalent definitions:
   - **D1, relative:** rules may be declared in the environment.
   - **D2, fixed-core:** every object rule must be *derived* in the core.
   - **D3, generic:** logical rules are generated from structural data.
   
   For classical, intuitionistic and linear sequent calculi, D2 already has prior-art witnesses at the derivability level. One is a single extended intuitionistic linear calculus into which LK, LJ and ILL translate connective-wise and conservatively (Yamada 2021, preprint, Cor 3.18 / 3.37; Girard's LU was not accessed). So "a finite common basis exists" is **not novel** at levels R1–R2.
6. **The PR #2 vacuity–identity dilemma is not exhaustive, and its lemma stays retracted.**
   - Generic frameworks are a genuine third route: logical rules and β/η are generated, and per-logic data are structural (Licata–Shulman–Riley (LSR) 2017; Shulman 2023).
   - Their faithfulness on proof identity is still open. LSR's own Conjecture 8.5 has not been proved in the literature I could search (2017–2026).
   - Its unary analogue *has* been proved: Clarke–Scherer–Zeilberger 2026, Thm 1.17 (preprint).
   - Environment-supplied equivalence rules are not automatically vacuous. Preservation then holds by declaration, but reflection is a real theorem (§4.4).

**Strongest remaining mathematical uncertainty.**

> Is there an independently motivated, *restricted* class of admissible environment data under which a fixed framework is generative (D2/D3) for a cross-foundation class, without the environment becoming a universal rewriting layer?

- **Without a restriction, the problem just moves into the environment.**
  - The structural layer of generic frameworks can encode undecidable behaviour: KKNS Thm 8; Buszkowski's theorem as restated by KKS Thm 10; Clarke–Scherer–Zeilberger Thm 3.27.
  - Rule-shape restrictions such as bipoles do not prevent this (§8).
- **With a fixed menu, it is unknown which foundations are covered.** Pruiksma's adjoint-logic menu σ(m) ⊆ {W, C} is one such menu. Classical multi-conclusion non-linear logic (LK) is the known boundary. No generic type-theoretic framework found covers it natively.

The single next test is in §10.

---

## 1. Scope and method

**Source agents.** Three source-extraction agents ran under a written protocol (`002-source-notes/00-extraction-protocol.md`), covering:
- structurality and translations between logics;
- the algebra of binding and derived/admissible rules;
- generic-framework follow-ups.

**My own spot checks.** I re-located decisive passages in the downloaded texts myself (listed in `002-source-notes/own.md`, O3). I also extracted two sources directly: Holliday–Hoshi–Icard on Public Announcement Logic (PAL), and Yamada.

**Reuse of earlier logs.** Stage-0 and review logs from PR #2 are reused where cited, marked [S0] or [R].

**Access limits.**
- **Primary texts not read:** Sheffer 1913, Post 1941, Łoś–Suszko 1958 (SEP used), Feitosa–D'Ottaviano 2001 (definition via Jeřábek and MDT), Wójcicki 1970/1988, Prawitz–Malmnäs, Zolin 2000, Girard's LU, Buszkowski 1982 (via KKS), Chvalovský–Horčík 2016, Iemhoff, Humberstone, Schürmann's thesis, Fiore LICS 2008.
- **Not found:** the LSR dependent-type sequel, which is unpublished.
- **Citation search:** Semantic Scholar only, about 60 citing papers of LSR screened. No Google Scholar sweep.
- **Versions:** most texts are author preprints, so page numbers refer to those.

---

## 2. Exact definitions

### 2.1 Source side: finitely schematic calculi

A **finitely schematic calculus** S = (Σ, 𝒥, ℛ) consists of:
- a finite *sorted second-order signature* Σ for object syntax (sorts, and operators with binding arities);
- a finite set 𝒥 of judgment forms over Σ;
- a finite set ℛ of rule schemas.

Each rule r ∈ ℛ has:
- sorted metavariables X⃗ (with binding arities);
- premises, each possibly *hypothetical* (local hypotheses u:J′) and *parametric* (local eigen-parameters);
- a conclusion.

There are no side conditions beyond what sorts and binding express.

Derivations are terms over ℛ. **Schematic (open) derivations** may contain free metavariables, hypothesis variables and parameters. Derivations are closed under:
- *metasubstitution* θ (sort-respecting);
- *proof substitution* d[d′/u], including the second-order case for hypothetical premises.

This generalizes Łoś–Suszko structurality: a consequence relation is structural if "Γ ⊢ ϕ then σ[Γ] ⊢ σ(ϕ)" (SEP, Jansana, SECONDARY_ONLY).

**Sorting is essential: PAL.** Public Announcement Logic is "not closed under uniform substitution". The instance ⟨p⟩K_i p ↔ (p ∧ K_i p) of its reduction axiom (i), ⟨ϕ⟩p ↔ (ϕ ∧ p), is invalid (Holliday–Hoshi–Icard 2011, §§1.1–1.2, VERIFIED_SOURCE). PAL *is* finitely schematic once atoms are a separate sort, because axiom (i) is schematic in an atom-sorted metavariable. So structurality must always be read relative to the declared sorts.

**Finiteness is essential.** Caleiro–Gonçalves note that if every formula is redeclared as an atom, any map becomes "uniform" (C–G p. 7, VERIFIED_SOURCE). Requiring Σ and ℛ to be finite blocks this "sort-splitting" attack.

### 2.2 Target side: frameworks and environments

A **framework** A has:
- fixed typing rules;
- a substitution operation;
- a definitional equality ≡_A that is *stable under substitution*. This holds for LF, LLF, CLF, λΠ-modulo with substitution-stable rewriting, rewriting logic, and focused LL in proof-search form.

An **environment** E_S is a finite list of items. Each item is classified by its *logical role*, not by its syntactic form, following PR #1 F03 ("count constants by logical role"). The roles form the **trust ledger**:

| Role | Item | Trust consequence |
|---|---|---|
| (a) | Syntax declaration (sorts, constructors) | None for derivability; affects adequacy of syntax |
| (b) | Non-logical axiom / assumption: a closed inhabitant of a judgment type | Trusted as a hypothesis; provenance recorded |
| (c) | Primitive inference rule: a rule-typed item whose removal is non-conservative | Trusted object-logic content (F03) |
| (c′) | Structural datum: a mode, a 1-cell/2-cell, a subexponential signature, a polarity assignment | Trusted structural content (rule-like; see §8) |
| (d) | Definitional or derived item: eliminable, a term of A over the other items | No added trust |
| (e) | Extension of ≡_A: rewrite rules or equations | Trusted computation; needs confluence, subject reduction and conservativity obligations ([S0] Dedukti §3.1; Lambdapi manual) |
| (f) | External procedure: totality, coverage or confluence checker | Trusted tool (Twelf: mode/world/termination/coverage checkers, `%block` declarations, no `%trustme`; bnd notes S8) |

### 2.3 Representations and their properties

A representation of S in A is a triple (E_S, ⌜·⌝, F):
- ⌜·⌝ maps Σ-syntax to A-terms, sending object variables to A-variables;
- each judgment J goes to an A-type ⌜J⌝. A fixed *judgment-level wrapper* is allowed, as LF's `pf`/`true` or the outer ∀x of the standard modal → FOL translation;
- each derivation d of J goes to an A-term F(d) : ⌜J⌝ in the context of its metavariables, parameters and hypotheses.

The properties below are labelled with fixed names so later sections can refer to them.

| Name | Statement |
|---|---|
| **SN** (strong substitution naturality) | F is defined on *all* schematic derivations, and F(d[θ]) ≡_A F(d)[⌜θ⌝] for every metasubstitution θ, where ⌜θ⌝ is the *componentwise* translation of θ |
| **WN** (weak naturality, for contrast) | ∀θ ∃θ\* with F(d[θ]) ≡ F(d)[θ\*] |
| **HN** (hypothetical naturality) | F(d[d′/u]) ≡_A F(d)[F(d′)/u], including the second-order case, for the hypotheses of S's declared discipline. Hypotheses are realized as A-variables of the matching structural kind (intuitionistic, linear, …) |
| **HOM** (homomorphism) | For each r ∈ ℛ there is a fixed template M_r with F(r(d⃗)) ≡_A M_r[⌜θ⌝][λu⃗.F(dᵢ)] |
| **ADQ1** | S ⊢ J iff ⌜J⌝ is inhabited over E_S (derivability preserved and reflected) |
| **ADQ2** | F is a bijection between S-derivations (modulo α) and canonical inhabitants (modulo ≡_A) |
| **ADQ3** | Quotient version for a declared congruence ~_S. Deferred to Task 003 |

**Sources for these notions** (all VERIFIED_SOURCE unless marked):
- HHP define "compositional" as "substitution commutes with encoding; in particular substitution in the logical system is encoded as substitution in LF" (HHP typescript p. 2). Their Thm 4.1 states SN and HN for first-order natural deduction (FOL ND).
- Pfenning's handbook Thm 3.2(3) states SN and HN, including proposition substitution ⌜[C/p]D⌝ = [⌜C⌝/p]⌜D⌝ [S0].
- For syntax alone, SN is the definition of a morphism of Σ-monoids (Fiore–Plotkin–Turi, Thm 4.1: "T I … is an initial F-monoid"). It is also Fiore–Mahmoud's notion of syntactic translation (arXiv:1308.5409, Lemma 5.1: a syntactic translation "commutes with substitution and metasubstitution").
- Extending this to judgments and hypotheses as a "Σ-monoid morphism over a dependently sorted signature" is INFERENCE. No source found states it.

### 2.4 Three inequivalent definitions of "fundamental"

**D1, structural representation (relative fundamentality).** A finite framework A is a *structural basis for a class C* iff every S ∈ C has a representation with SN, HN (for S's hypotheses) and ADQ1. Environment items of any role are allowed, and the trust ledger is reported. ADQ2 is the strong variant.

**D2, fixed-core generativity.** A is *generative* for C iff every S ∈ C has a D1 representation whose E_S contains only items of roles (a), (b) and (d). Every inference rule of S must therefore be *derived* in A over syntax and axioms. This is PR #1's V-B "macro-only" environment, stated by logical role.

**D3, generic generativity modulo structural data.** A is generic-generative for C relative to a fixed class 𝒦 of admissible structural data iff every S ∈ C has a D1 representation whose E_S contains only items of roles (a), (b), (d) and (c′) drawn from 𝒦. Each logical rule of S must be an instance of one of A's finitely many generic rule schemas, parameterized by structural data. Examples are the F/U rules of LSR, the shifts of adjoint logic, and the cones of Shulman's doctrines.

**The three definitions are inequivalent (INFERENCE, using cited theorems).**
- LF, with declared rule constants, is D1 for FOL ND (HHP Thm 4.1) but not D2.
- STLC with ⊃ ↦ → (shallow) is D2 for NJ(⊃).
- Adjoint logic is D3 for intuitionistic linear logic (ILL) and intuitionistic logic, with σ(U) = {W, C} and σ(L) = {} (Pruiksma thesis, gfu notes). It is D2 only if structural data are not counted as rules.
- D2 ⇒ D3 ⇒ D1 for a fixed C. The converses fail by the examples above.

---

## 3. Lemmas: what strong naturality forces

All three are INFERENCE: elementary, informal, likely folklore. They need independent checking.

**Lemma 1 (SN ∧ HN ⇒ HOM).**
- *Claim.* Let M_r := F(r(u⃗)), the image of the one-step schematic derivation with generic metavariables and premise variables. Then r(d⃗)[θ] = r(u⃗)[θ][d⃗/u⃗], so SN and HN give F(r(d⃗)) ≡ M_r[⌜θ⌝][F(d⃗)/u⃗].
- *Status.* This is the derivation-level form of Fiore–Plotkin–Turi initiality: a morphism out of an initial Σ-monoid is determined by its values on generators. Rule locality is therefore a *consequence* of substitution naturality, not an independent stipulation.

**Lemma 2 (acceptance is schematic: no per-instance computation).**
- *Claim.* M_r is well typed at generic metavariables. Because typing and ≡_A are stable under substitution, every instance M_r[⌜θ⌝] is well typed.
- *Consequences.*
  - Any computation the representation performs while accepting a step of r is carried out once, *at the schema*. M_r is a derived rule of A + E_S.
  - A rule whose acceptance depends on inspecting the instantiated subterms cannot be represented, unless that inspection is itself stable on variables. Then it is a schematic match.
  - Corollary: ADQ1 then fixes the accepted instance set to be exactly S's schema instances.

**Lemma 3 (WN is vacuous).**
- *Claim.* WN is satisfied by MDT Prop 2.25: take θ\*(α(φ)) := α(θφ).
- It is also satisfied, up to CPC-equivalence, by Jeřábek's most general conservative translations: for structural L, f∘σ is again a translation, so f(σφ) ⊣⊢ τ(f(φ)) for some τ.
- *Status.* INFERENCE by the str agent, checked by me against Jeřábek Def 2.3 and Thm 2.4. Only the *componentwise* (strong) reading SN has force.

**Proposition 4 (strong structurality has teeth: ubiquity fails).** There is no schematic (componentwise, finite-variable) conservative translation of IPC consequence into CPC consequence.

*Argument (INFERENCE).*
1. A schematic translation sends formulas in one variable p into CPC formulas over the finitely many variables of t(p).
2. CPC is locally finite, so these images fall into finitely many equivalence classes.
3. IPC has infinitely many pairwise non-interderivable one-variable formulas (Rieger–Nishimura; UNVERIFIED-MEMORY).
4. Conservativity for consequence (φ ⊢ ψ iff t(φ) ⊢ t(ψ)) would make two of them interderivable. Contradiction.

Contrast: Jeřábek's Thm 2.4 gives a *non*-schematic conservative translation of every countable finitary system into CPC (VERIFIED_SOURCE). His own conclusion is that bare conservative translation "does not provide useful information … a more refined criterion is needed" (p. 14).

---

## 4. Machinery versus environment: (i) assumption, (ii) derived rule, (iii) declared rule, (iv) checker

### 4.1 Stability distinguishes (ii) from admissibility

- **Derivability is stable.** PFPL Thm 3.1 (Stability): "If [J is derivable from] R, then [J is derivable from] R ∪ R′" (VERIFIED_SOURCE, Harper, PFPL ch. 3).
- **Admissibility is not stable.** Harper gives an explicit counterexample.
- **No clean biconditional.** "Derivable iff admissible in every extension" depends on which class of extensions is meant.
  - Under the propositional reading (extensions closed under substitution), it fails: the Kreisel–Putnam rule is admissible in every intermediate logic but not derivable in IPC (UvA lecture handout Prop 8 and Thm 9; SECONDARY).
  - So any definition of "derived rule" must name its class of extensions.
- **In frameworks.** Derived rules are framework terms: LF "eliminates the distinction between primitive and derived rules" (HHP p. 2). Admissible rules are not. HHP p. 23 says LF "precludes the encoding of a proof of admissibility … that makes use of a principle of induction over a type of proofs", with the Hilbert deduction theorem as the example. Adding induction over the representation type destroys adequacy (Pfenning p. 47).

### 4.2 The four kinds in existing frameworks

| Framework | (i) Assumption | (ii) Derived rule | (iii) Declared object rule | (iv) Checker / reduction procedure |
|---|---|---|---|---|
| LF (HHP; Pfenning) | Context variable or base-typed constant | LF term of rule type | Signature constant of higher type: role (c) | Admissible rules via Twelf totality: role (f) |
| Isabelle/Pure (Paulson) | Meta-hypothesis | Meta-proof | Axiom of M_L: role (c) | ≡-definitions as axioms: role (e) if computational |
| Rewriting logic (Martí-Oliet–Meseguer; Clavel–Meseguer) | Equation or rule instance | Proof term | Rewrite rule of T: role (c) | Universal theory U with T as data. Fails SN (§5) |
| Dedukti / λΠ-modulo (Cousineau–Dowek; Dedukti manuscript; theory U) | Constant `c : Prf φ` | λΠ term | Constant of rule type: role (c) | Rewrite rules: role (e). Confluence and termination are "out of the scope of Dedukti itself" [S0] |
| Focused LL (Miller–Pimentel; Nigam–Miller) | Theory formula | Synthetic (bipole) derivation | Introduction clauses, plus Cut, Init, Pos/Neg: role (c) | Polarity assignment: role (c′). Cut-coherence decidable (MP Thm 22) |
| FPC (Chihani–Miller–Renaud) | — | — | None (fixed LKF/LJF kernel) | Clerks and experts are *untrusted guards*: "soundness by erasure" [S0]. A checker is harmless when it only filters derivations of a fixed sound kernel |
| Generic frameworks (LSR; Licata–Shulman; Shulman 2023; adjoint logic) | Context hypothesis | Generated F/U/shift rules: (ii) for *all* logical rules | None for connectives | Mode theory / doctrine: role (c′). Mode equality assumed decidable, or quotient metatheory assumed (LSR: "assume a metatheory with quotient sets/types") |

**The (iv) distinction (INFERENCE):**
- A checker is **benign** when it only restricts search in a fixed sound core. FPC is the example: soundness by erasure.
- It is **malignant** when it *generates conclusions*: an `acc` rule whose premise is "the checker accepts". SN excludes the second kind (Lemma 2), but not the first.

### 4.3 What an honest machine/environment separation requires

1. Classify every environment item by logical role, not by syntax (§2.2).
2. Report derived rules (role (d)) separately from declared ones (c).
3. Treat (c′) structural data as rule-like trust. Licata–Shulman 2016 note that the mode layer may need "an explicit equality judgement … if we needed a mode theory where equality of morphisms or 2-morphisms were undecidable" (VERIFIED, gen/R notes).
4. Treat (e) and (f) as trusted computation, with their metatheory obligations listed.

### 4.4 Environment-supplied equivalence rules (problem 3; PR #2 horn (ii))

- **Splitting the cases.** Following the fresh-context critique in PR #2's review, equations in E_S split into:
  - (α) equations computing on encoded data;
  - (β) schematic equations between proof constructors;
  - (γ) equations generated from universal properties.
- **SN deals with (α).**
  - A rule such as `valid c X ↪ …`, defined by recursion on the structure of a metavariable X, is stuck at generic X. So F is undefined on the schematic derivation, and SN fails.
  - With non-left-linear syntactic-equality rewriting, a deep embedding of certificates can be made SN. Its acceptance is then schematic (Lemma 2). This is loophole L-a in §5.
- **For (β), reflection is substantive.** Declaring the generators of ~_S makes *preservation* true by declaration. *Reflection* (that A + E_S identifies nothing more) is a theorem that can fail. Evidence:
  - Felicissimo–Winterhalter FSCD 2024, Table 1: no conservativity proofs, non-confluent encodings [S0];
  - Felicissimo FSCD 2022, Thm 46: reduction reflected for functional explicitly typed PTSs [S0].
- **Conclusion.** PR #2's horn (ii) ("E may extend ≡ ⇒ R3 vacuous") is false for (β) and (γ). Status: **withdrawn as stated**, in agreement with PR #2's own review.

---

## 5. Adversarial counterconstructions

Each construction is tried against SN, HN, HOM and ADQ1/2. Here "S" is the reference calculus NJ(⊃) unless stated otherwise.

| # | Construction | Source / status | SN | HN | ADQ1 | Verdict |
|---|---|---|---|---|---|---|
| I-H | MDT flattening: φ ↦ fresh variable α(φ); Δ = the whole consequence relation | MDT Prop 2.25, VERIFIED [S0] | **Fails**: α(φ[θ]) is unrelated to α(φ)[⌜θ⌝]. Passes WN (Lemma 3) | — | Yes | Excluded |
| I-J | Jeřábek's most general conservative translation into CPC (γₙ ∨ pₙ ∧ δₙ, from oracle queries) | Jeřábek Thm 2.4, pp. 4–5, VERIFIED | **Fails** (non-schematic; Prop 4 shows no schematic one exists for IPC → CPC) | — | Yes | Excluded |
| I-U | Clavel–Meseguer universal rewrite theory U with T as a data term | Thm 3.2, VERIFIED [S0]. Stated for *ground* t, t′ | **Fails**: object variables are ground codes, not U-variables | — | Yes (within hypotheses) | Excluded |
| I-R | EF + Refl_S | Krajíček 2019 Thm 8.4.3, SECONDARY [S0] | **Fails**: bit-encoding of φ does not commute with formula substitution; size-indexed family is not a finite schema | — | p-simulation | Excluded |
| I-S | Turing-machine step checker: `step : Πr ψ⃗ φ. Rule r → Prf ψ⃗ → Trace(run r⟨ψ⃗,φ⟩) → Prf φ` | PR #2 §6.1 (INFERENCE) | **Fails** if formulas are serialized to tapes: a metavariable cannot be serialized homomorphically. Passes only if the machine treats variables as opaque leaves, and then it is a schematic matcher (L-a) | — | — | Excluded, or degenerates to a schema |
| I-C | Dedukti conversion checker `acc : Πc φ. IsTrue(valid c φ) → Prf φ` | PR #2 §6.1 (INFERENCE) | **Fails** when `valid` recurses on φ: it is stuck at generic metavariables | — | Yes | Excluded |
| I-C′ | Certificate deep embedding with non-left-linear `eq x x ↪ true` and a projection `getcert` | This report (INFERENCE) | **Passes**, and HOM holds up to ≡ via `getcert`. But by Lemma 2 acceptance is a schematic match | **Fails** for ND sources (hypotheses become certificate data); vacuous for sequent/Hilbert sources | Yes | **Loophole L-a**: passes for sequent and Hilbert sources |
| I-E | Fixed universal environment E_fix independent of S (for example, a universal Horn program over codes) | INFERENCE | **Fails** (stuck on metavariables), unless E_fix is a generic "rules-as-data" pattern instantiator | — | — | Excluded. The rules-as-data variant still needs S's patterns in E_S, which the ledger counts as role (c) |
| I-W | Structural-looking wrapper around a checker: a template that hides an `acc` call | PR #1 §3 loophole (INFERENCE) | Same as I-C / I-C′: by Lemma 2 the hidden computation runs at the schema | — | — | Reduces to L-a |
| I-Q | Environment-supplied equivalence (β) for R3 | §4.4 | — | — | — | Not vacuous. Reflection is a proof obligation |
| I-K | Sort-splitting: every formula declared as its own atom or sort | Caleiro–Gonçalves p. 7 | Trivially "passes" | — | — | Excluded by the finiteness of Σ and ℛ |

**Loopholes and over-exclusions, stated plainly:**

- **L-a (benign, as judged).** SN does not determine *where* schema matching is implemented: in types (LF) or in conversion (I-C′).
  - For sources without hypothetical judgments (Hilbert, sequent calculi), a deep certificate embedding with a schematic checker passes SN and HOM. Its derivation algebra is the free term algebra of S's rules, which is isomorphic to the LF image. I classify it as legitimate.
  - The ledger still records the checker's rewrite rules as role (e).
- **L-b (scope, not vacuity).** E_S may contain computation that makes S's own derivability undecidable. Examples are finite axioms over a fixed calculus (Buszkowski via KKS Thm 10) and a single non-local contraction subexponential (KKNS Thm 8).
  - ADQ1 still holds: the representation is faithful to an undecidable logic.
  - This is not vacuity. It shows that anti-vacuity constrains the *representation*, not the *source*.
- **L-c.** The I-S exclusion relies on SN being defined on schematic derivations. Fresh-context critique N4 of PR #2 (variant I-S′, with an auxiliary `Trace` judgment in E_S) is answered by Lemma 2: the trace premise must be supplied at the generic schema, so it is a fixed derived proof.
- **L-d. Not resolved:** a source presented *deliberately* as an interpreter. Example: S = "certificate c ⊢ φ whenever check(c, φ)" with an arbitrary checker as a non-schematic side condition.
  - Such an S is outside the finitely schematic class (§2.1), so the definition says nothing about it.
  - Choosing the source class is a modelling decision. That is why the Stage-0 synthesis requires C to be fixed independently.
- **L-e. Admissible but not derivable rules.** By HHP p. 23, these are not representable as templates. Under D1 they need role (f) (Twelf-style totality) or role (c). This is a cost, not a vacuity.
- **L-f. Over-exclusion: foundations with conversion-by-computation** (type theories with a conversion rule; proofs by reflection in Coq/Lean).
  - SN forces either explicit conversion derivations, or sharing A's ≡_A (role (e) or generic).
  - The source system must be re-presented declaratively. This is a real restriction with a size cost (F09). The ≈16× slowdown reported for Felicissimo's adequate encoding is an indicator [R].
- **L-g. Over-exclusion: top-level non-schematic translations.** MDT note that schematic preservation "rules out e.g. the standard translation of modal logic to first-order logic, which adds a quantifier at the very top" (VERIFIED).
  - The repair here is a judgment-level wrapper: the translation is componentwise on syntax, and the outer ∀x is the wrapper on judgments.
  - Whether every reasonable non-schematic translation admits such a repair is UNKNOWN.

**Completion test (task requirement).**
- The interpreter violates SN: it inspects instances, and its images are not substitution-stable.
- SN is not tailored to the interpreter. It is:
  - the definition of a structural consequence relation (Łoś–Suszko);
  - HHP's definition of compositional adequacy;
  - the substitution-closure of Frege rules that Cook–Reckhow's basis-independence proof uses ("closure under substitution", their Lemma 2.5 [S0]);
  - the morphism notion for syntax with binding (Fiore–Plotkin–Turi; Fiore–Mahmoud);
  - the "structurality" MDT call for.
  
  None of these was motivated by excluding interpreters.
- **Caveat.** SN over-excludes in L-f and L-g, and has the benign loophole L-a.

---

## 6. Required tests

### 6.1 Reference calculus NJ(⊃)

NJ(⊃): formulas φ ::= p | φ ⊃ φ; rules hyp, ⊃I (discharging u:φ), ⊃E; formula metavariables are of sort o.

| Representation | SN | HN | HOM | ADQ1 | ADQ2 | D-level | Ledger | Verdict |
|---|---|---|---|---|---|---|---|---|
| LF signature {o, imp, pf, impi : ΠA B.(pf A → pf B) → pf(imp A B), impe} | Yes | Yes | Yes (templates impi, impe) | Yes | Yes (HHP Thm 4.1 for FOL ND, which includes this fragment; Pfenning Thm 3.2) | D1 | (a) o, imp; (c) impi, impe | **TRUE** |
| Shallow encoding in STLC (⊃ ↦ →, ⊃I ↦ λ, ⊃E ↦ application) | Yes | Yes | Yes | Yes | Bijection with raw terms modulo α | **D2** (no declared rules) | (a) base types only | **TRUE** |
| Universal machine (I-U, or I-S with tape serialization) | **No** | — | — | Yes | — | — | Universal program (e)/(c) | **FALSE** (loophole: an opaque-variable matcher degenerates to the LF row) |

### 6.2 Resource-sensitive negative control: MILL (⊗, ⊸)

| Representation | SN | HN | ADQ1 | Verdict |
|---|---|---|---|---|
| LF with linear hypotheses as ordinary LF hypotheses, `tensI : ΠA B. pf A → pf B → pf(A⊗B)` | Yes | Yes (for the *intuitionistic* discipline) | **No.** x:pf p ⊢ tensI p p x x : pf(p⊗p), but p ⊢ p⊗p is not MILL-derivable | **FALSE**: duplication masquerading as linear inference |
| LF with contexts as data (explicit context splitting) | Yes | **No** for MILL's linear discipline (hypotheses are data) | Expected yes (Cervesato–Pfenning p. 53: possible, but with "complex proofs" [S0]) | D1 without HN |
| LLF with `tensI : ΠA B. pf A ⊸ pf B ⊸ pf(A⊗B)` and linear hypotheses as LLF linear variables | Yes | Yes (linear) | Expected yes. Duplication is ill-typed. LLF is conservative over LF (Thm 2.9) [S0]; no MILL adequacy theorem was extracted, so INFERENCE | **TRUE (expected)** |

**Lesson.** SN (anti-vacuity) and HN (structural form) do not catch resource violations; ADQ1 does. This matches Gardner Cor 5.1.8: "There are no adequate representations of linear and relevant logics" in ELF+, where hypotheses are framework hypotheses [S0]. **Anti-vacuity and fidelity are separate requirements, and both are needed.**

### 6.3 Trust ledger (machinery vs environment)

| Representation | Fixed machine | Declared logical rules (c) | Structural data (c′) | Computation (e) | External checks (f) | Adequacy evidence |
|---|---|---|---|---|---|---|
| LF / FOL ND | λΠ, decidable (HHP Thm 2.6) | One constant per rule | Intuitionistic contexts, fixed | none | none | Informal per-signature theorem (HHP Thm 4.1) |
| LLF / MILL | λΠ⊸&⊤ | Per rule | Linear contexts, fixed | none | none | INFERENCE |
| Dedukti / functional PTS (Cousineau–Dowek) | λΠ-modulo | Per-PTS constants | — | εₛ / Π̇ decoding rules | Confluence and termination external | Conservativity Thm 1 (needs termination); Assaf Thm 5.24 [S0] |
| Theory U (Blanqui et al. 2021) | λΠ-modulo | 38 declarations, fixed once | — | 28 rules, fixed once | Confluence proved (Thm 9) | Fragment theorem only; not provability-conservative (§4) [S0] |
| Rewriting logic, universal U | Rewriting logic | none (T as data) | — | U's rules | none | Thm 3.2 (ground terms). **Fails SN** |
| Focused LL / LK (Miller–Pimentel) | LLF, focused | Bipole clauses + Cut/Init + Pos/Neg | Polarity | none | Cut-coherence decided (Thm 22) | Thm 6 at provability level; "full completeness of proofs" asserted, not written out [t002 gfu] |
| Adjoint logic / ILL, NJ (Pruiksma) | Adjoint connectives + shifts | none | Modes, σ(m) ⊆ {W, C} | none | none | Cut elimination, identity (by hand) |
| LSR / substructural-modal | F, U, cut and identity once (Thm 2.1) | none | Mode theory (1-cells, 2-cells, equations) | none | Equality of mode theory assumed | Logical adequacy proved; equational adequacy **Conj 8.5 open** |
| FPC | LKF/LJF kernel | none | Polarization | none | Clerks/experts untrusted | Soundness by erasure; theoremhood only [S0] |

---

## 7. Minimality, independence and invariant comparison (problem 5)

1. **Primitive counts are not invariant.**
   - Böhler–Creignou–Reith–Vollmer Ex. 1.3: "[nand] = BF". BF also has the base {and, not}.
   - So the intersection of all bases of BF is empty: **no individual operation is invariantly fundamental** (VERIFIED_SOURCE for the bases; the empty-intersection corollary is elementary).
   - Clones, "considered up to term equivalence", are in one-to-one correspondence with fragments of CPC (Jeřábek Def 3.4).
2. **Basis-independence is already a theorem for Frege systems.**
   - Cook–Reckhow Thm 2.3: "For any two Frege systems F1 and F2 over K there is a function f in ℒ and constant c" with linear line and size bounds. Cor 2.4: they "p-simulate each other" [S0, VERIFIED].
   - The simulation substitutes a fixed derivation for each rule, which is exactly a HOM translation. So within a substitution-closed class, *which* finite basis is chosen is invisible up to linear overhead.
3. **Invariant equivalences that exist:**

   | Equivalence | Source | Notes |
   |---|---|---|
   | Synonymy = translational equivalence | Pelletier–Urquhart Thm 2.6, VERIFIED (preprint) | For simple schemes. Invariant: number of reduced algebraic models of each cardinality (Cor 3.2), which separates K, T, B, S4, S5 (Thm 4.5) |
   | Mutual exact translations | Pelletier–Urquhart 2006 correction | Strictly weaker than synonymy |
   | Equipollence | Caleiro–Gonçalves Def 4.1 / Prop 4.3 | — |
   
   **All of these are at the level of formulas; none addresses proofs or binders.**
4. **Proposal (CONJECTURE about usefulness, not a theorem).**
   - *Comparison.* Compare frameworks by the preorder A ≼ A′ ⇔ "A has a D2 representation in A′" (all of A's rules derived in A′). This is SN + ADQ1 with role-(d) environments.
   - *Invariant objects.* The invariant objects are ≼-equivalence classes, with *minimal elements relative to a class C*. Minimal elements are invariant under re-presentation; primitive counts are not.
   - *Costs.* Report costs separately as template sizes and translation overhead (polynomial or linear p-simulation) (F09). Do not infer computational efficiency from a small basis.
   - *Risk.* As in group theory, the minimal size of a presentation may be uncomputable (by analogy with the Adian–Rabin unsolvability of group-theoretic properties; UNVERIFIED-MEMORY; not checked here).

---

## 8. The generic-framework route (problem 4)

**What is established** (VERIFIED_SOURCE unless marked):

- **LSR 2017** (LIPIcs 84, art. 25):
  - two generic connectives F and U, with cut and identity proved once for every mode theory (Thm 2.1);
  - §4: one equational theory on derivations, "the βη-laws for F and U", uniform in the mode theory [R];
  - per-logic data: a mode theory (1-cells, 2-cells, and equations between them).
- **Equational adequacy (reflection) is open in LSR.**
  - p. 25:17: "We conjecture that the converse is true … We have sketched a proof of equational adequacy for a simple case (ordered logic products), assuming a lemma …".
  - Extended version: "CONJECTURE 8.5. Completeness of Permutative Equality. If d ≡ d′ then d↓ ≡p d′↓" (VERIFIED, both texts).
- **No later proof found.** Search of about 60 Semantic Scholar citers, 2017–2026, found no proof or refutation.
  - Riley's thesis (2022) does not address it.
  - Shulman's MATT (MFPS 2023) calls LSR's "definitional equality … ill-behaved", and Remark 2.6 says "L[S†] can fail to have decidable equality even if L does".
- **Unary analogue proved.** Clarke–Scherer–Zeilberger (arXiv:2511.07314v3, Jan 2026, preprint):
  - Thm 1.17: the free bifibration on p is presented by the cut-free sequent calculus modulo permutation equivalence.
  - Thm 3.27: permutation equivalence is undecidable for some base "with locally finite factorizations"; the construction uses a universal Turing machine and infinitely many generating arrows.
  - Thm 3.28: it is decidable when the base is locally finite or factorization-preordered.
- **Shulman 2023** (LNL polycategories, LMCS 19(2)):
  - reaches classical *linear* logic generically;
  - "We leave cut-elimination for future study" [R];
  - non-linear objects are single-conclusion.
- **Adjoint logic** (Pruiksma thesis, CMU-CS-24-103):
  - the per-mode menu is σ(m) ⊆ {W, C}, monotone in the preorder of modes;
  - cut elimination and identity expansion are proved by hand;
  - intuitionistic only.
- **LK** is not covered natively by any generic type-theoretic framework examined. Miller–Pimentel cover LK with *declared* bipole clauses, adequacy proved at provability level (Thm 6).

**Is this a meaningful fixed generative mechanism?**
- **For logical rules, yes (D3).** Connective rules are instances of fixed generic schemas, and β/η is generic.
- **For the structural layer, no restriction exists.**
  - Structural data are rule-like (role (c′)), and an unrestricted structural layer can encode computation:
    - one non-local contraction subexponential makes derivability undecidable (KKNS Thm 8; C = ∅ gives PSPACE, Thm 15);
    - atomic, cut-admissible non-logical axioms over the Lambek calculus generate every r.e. language (Buszkowski 1982, restated in KKS Thms 9–10; Buszkowski SECONDARY_ONLY, and finiteness of A not verified);
    - free adjoints make proof identity undecidable for some infinite bases (CSZ Thm 3.27; Dawson–Paré–Pronk).
  - *My conjecture (UNVERIFIED):* directed 2-cells in a *finite* LSR mode theory behave like string rewriting, so derivability may be undecidable for some finite mode theory. No source proves this.
  - Rule-shape restrictions (bipoles: MP Def 3/4, Thm 22; MMPV Thms 12–13, 16–17) restrict *form*, not *computational power* (gfu notes, INFERENCE combining Buszkowski).

**What remains unproved:**
- multi-ary equational adequacy (LSR Conj 8.5);
- decidability conditions on mode theories in the multi-ary case (Shulman: "which (L, S) are decidable?");
- cut elimination for Shulman's doctrines;
- native or adequate generic treatment of LK.

---

## 9. Is PR #2's vacuity–identity dilemma exhaustive?

**No.** Taking PR #2's later corrections seriously:

1. **The supporting lemma stays retracted.** It swapped preservation and reflection, and in corrected form it is a near-tautology (PR #2 review §3.1). I do not cite it.
2. **Horn (ii)** ("E may extend ≡_A ⇒ vacuous") holds only for equations of kind (α), which SN independently excludes. For (β) and (γ), preservation is by declaration but reflection is substantive (§4.4).
3. **Horn (iii)** ("A natively contains each foundation's structure ⇒ union, not a basis") is refuted as a dichotomy by two mechanisms:
   - **D3 generic frameworks.** Connectives are instances of fixed schemas.
   - **D2 small cores.** Classical, intuitionistic and linear sequent calculi translate componentwise into one calculus:
     - Yamada 2021 (preprint), Cor 3.18: "a formal proof T!?(p) of the sequent !T!?∗(∆) ⊢ ?T!?∗(Γ) in ILCι" for each LK proof p, with T!?(A ∧ B) := ?T!?(A) & ?T!?(B), etc.;
     - Cor 3.37: conservativity for the restricted calculi.
   
   Girard's LU and Laurent–Regnier are prior "unities" cited there; I did not access them.
4. **What survives** (INFERENCE, plausibly provable):
   - Under rule-as-constant, rule-local encodings with fixed ≡_A (literal D1 with role (c) items), only identities generated by *permutations of independent rule instances* can be reflected by ≡_A.
   - This sharpened form (fresh-context critique N3) belongs to Task 003's domain (R3), and is recorded as conjecture C2 below.

---

## 10. Theorem-shaped formulations, recommendation and next test

### 10.1 Formulations

**T1 (Schematicity; INFERENCE, plausibly folklore).** For finitely schematic S and a framework with substitution-stable typing and conversion:
- every SN ∧ HN representation is HOM, with templates M_r = F(r(u⃗)) that are derived rules of A + E_S (Lemmas 1–2);
- hence representations satisfying SN cannot implement per-instance computation.

*Falsifier:* an SN ∧ HN ∧ ADQ1 representation of a finitely schematic S whose rule images are not substitution instances of fixed templates.

**C1 (Collapse; CONJECTURE).** Every SN ∧ HN ∧ ADQ2 representation, in LF, of a pure natural-deduction calculus with intuitionistic hypotheses is a judgments-as-types encoding up to:
- ≡_LF;
- definitional (role (d)) re-factoring of E_S;
- a bijective renaming of declarations.

Evidence and limits:
- Gardner Thm 6.4.4: an encoding of a logic with an intuitionistic consequence relation "is adequate if and only if" the indexed functor it induces is an indexed isomorphism.
- Gardner Thm 6.5.7 is the analogue for natural encodings (bnd notes, VERIFIED via OCR).
- These *characterize* a given encoding; they do not classify all encodings, and Gardner states the converse fails.
- If C1 holds, the non-vacuous "finite algebras of reasoning" for such sources *are* logical frameworks. That answers the definitional question, and it makes novelty at R1–R2 an F01 matter.

**C2 (Permutation-only reflection; CONJECTURE, handed to Task 003).** Under literal D1 with role-(c) rule constants and fixed ≡_A, a nontrivial ~_S is reflected only if it is generated by permutations of independent rule instances.

**Q3 (Generativity under a fixed menu; OPEN question).** Is there a finite framework A and an independently motivated finite menu 𝒦 of structural data such that A is D3-generative (with SN, HN, ADQ1) for C = {NJ, ILL, S4 in a dual-context or adjoint presentation, LK}? Known facts:
- yes for NJ, ILL and adjoint-presentable modal logics with σ ⊆ {W, C} (Pruiksma; LSR);
- LK only via *declared* clauses (Miller–Pimentel), or via a D2 translation into a linear calculus (Yamada, preprint) that is not a generic type-theoretic framework;
- with unrestricted 𝒦, the structural layer can encode computation (§8).

### 10.2 Decision gate check (`docs/STAGE_0_SYNTHESIS.md`)

| Gate requirement | Status after this report |
|---|---|
| (i) Exact quantified conjecture with source class fixed independently | **Partly.** The class is finitely schematic calculi (§2.1). T1, C1 and Q3 are stated. The benchmark list for Q3 is named. |
| (ii) Anti-vacuity test excluding a real interpreter without excluding legitimate encodings by fiat | **Met, with stated loopholes and over-exclusions.** SN excludes I-H, I-J, I-U, I-R, I-S, I-C and I-E. It is independently motivated. Loophole L-a and over-exclusions L-f, L-g remain. |
| (iii) Testable fidelity specification | **Met at derivability and derivation level** (ADQ1, ADQ2). Identity (ADQ3) is deferred to Task 003. |
| (iv) Explicit trust and equality boundaries | **Met as a ledger** (§2.2, §6.3). |
| (v) A concrete unsolved lemma or an independently checked counterexample | **Partly.** LSR Conj 8.5 is a concrete published open lemma, but it is *theirs*. Q3 is open. No counterexample is independently checked. |

### 10.3 Recommendation: NARROW

- **Do not PROCEED.**
  - No restricted theorem is ready that would justify building anything.
  - The R1–R2 existence question is answered by prior art: LF/LLF (D1), linear-logic unities (D2, preprint), adjoint logic (D3).
- **Do not STOP.**
  - The definitional question has a defensible answer (SN + ADQ, plus the ledger).
  - Two precise open problems remain, and they bear directly on the charter's "fundamental operations": Q3 (generativity under a fixed structural menu) and C1 (collapse).
- **Narrow the program to:**
  1. adopting SN + ADQ1 + ledger as the representation definition;
  2. one pen-and-paper investigation of Q3 at its boundary case.
- **Any novelty claim** must be measured against LSR, Shulman, Pruiksma–Pfenning, Miller–Pimentel and the linear-logic unity literature.

### 10.4 Single next test (pen and paper; no implementation)

> **Decide whether LK admits a D3 representation with SN ∧ ADQ1 in adjoint logic with the fixed menu σ(m) ⊆ {W, C}, possibly with multiple conclusions added. Equivalently, determine whether multi-conclusion classical contraction and weakening can be supplied by menu-restricted structural data rather than by declared rules (Miller–Pimentel) or by a dedicated core (Yamada's ILCι).**

**Starting points:**
- Pruiksma's adjoint logic (intuitionistic, single conclusion);
- Shulman's LNL polycategories (multi-conclusion linear);
- Yamada Cor 3.18 (the !Δ ⊢ ?Γ decomposition);
- Girard's LU (to be accessed).

**Outcomes:**

| Outcome | Meaning |
|---|---|
| **(a) Yes, with a known menu** | Q3 holds for the benchmark at R1. Fundamentality is a prior-art fact; the project's remaining content is R3 (Task 003). |
| **(b) A proof that every SN ∧ ADQ1 representation of LK needs a structural datum outside every finite menu, or a declared logical rule** | The first genuine obstruction to cross-foundation generativity. |
| **(c) Neither** | Record the exact missing lemma: whether multi-conclusion structural data can be menu-restricted while keeping cut admissibility. |

---

## 11. Limitations and unresolved questions

1. **Lemmas 1–2 and Prop 4 are informal arguments.**
   - Prop 4 relies on Rieger–Nishimura (UNVERIFIED-MEMORY).
   - The extension of Σ-monoid morphisms to judgments and hypotheses is my inference.
2. **SN is relative to the declared sorts and binding structure of S.** An adversarial *presentation* of S (L-d) is outside its scope by design.
3. **The over-exclusions are real costs.** Conversion-by-computation foundations (L-f) and top-level non-schematic translations (L-g) are partly repaired by wrappers; the general case is UNKNOWN.
4. **The resource control relies on expected, not extracted, LLF adequacy for MILL.**
5. **Yamada 2021 is a preprint.** Its conservativity results are for restricted calculi only, and its proof identity is "modulo permutations".
6. **Independence.** This report shares authorship with PR #2. A fresh-context adversarial read of a draft was used (see `002-source-notes/fresh-critique.md`), but outside review is still required.
7. **Scope.** Proof identity, causal order and the MLL net example are Task 003's subject. Nothing here claims them.

---

## 12. Source table (edition and location)

Statuses: **V** = VERIFIED_SOURCE in the version stated; **S** = SECONDARY_ONLY; **N** = NOT_ACCESSED. Notes files: own, str, bnd, gfu (this task); [S0] = PR #2 Stage-0 logs; [R] = PR #2 review logs.

### Logical frameworks and adequacy

| Source | Version | Location used | Status |
|---|---|---|---|
| Harper, Honsell, Plotkin, "A Framework for Defining Logics" (JACM 1993) | Author typescript | p. 2 (compositional); p. 17; p. 23; Thm 4.1 p. 21 | V [S0, bnd] |
| Pfenning, "Logical Frameworks" (Handbook of Automated Reasoning) | Preprint | Thm 3.2 p. 29; §3.6; p. 47; p. 70 | V [S0, bnd] |
| Gardner, PhD thesis (1992) | OCR | Def 5.2.1/5.2.3; Cor 5.1.8; Def 6.1.3; Thms 6.4.4, 6.5.7 | V [bnd] |
| Harper, *Practical Foundations for Programming Languages* | Ch. 3 | Thm 3.1 (Stability) | V [bnd] |
| UvA lecture handout on admissible rules | — | Prop 8, Thm 9 (Kreisel–Putnam) | S [bnd] |
| Twelf User's Guide 1.4 | — | §9 | V [bnd] |
| Cervesato, Pfenning, LLF | Author manuscript | Thm 2.9; p. 53 | V [S0] |
| Chihani, Miller, Renaud (JAR 2017) | HAL manuscript | p. 13 (soundness by erasure) | V [S0] |

### Syntax with binding

| Source | Version | Location used | Status |
|---|---|---|---|
| Fiore, Plotkin, Turi (LICS 1999) | — | Thms 2.1, 4.1, 4.2 | V [bnd] |
| Fiore, Mahmoud | arXiv:1308.5409 | Lemma 5.1 | V [bnd] |
| Hofmann (LICS 1999) | — | Prop 4.1 (syntax only) | V [bnd] |

### Translations between logics and invariant comparison

| Source | Version | Location used | Status |
|---|---|---|---|
| Jeřábek, "The ubiquity of conservative translations" | arXiv:1108.6263v2 | Defs 2.2–2.3; Thm 2.4; Def 3.4; Thms 3.6, 3.10; Rem 2.8; p. 14 | V [str, own] |
| Pelletier, Urquhart, "Synonymous logics" (+ 2006 correction) | Preprints | Thm 2.6; Cor 3.2; Thm 4.5; correction Thm 2.1 | V [str] |
| Caleiro, Gonçalves, "Equipollent logical systems" | — | Def 2.4; Def 4.1; Prop 4.3; p. 7 | V [str] |
| Böhler, Creignou, Reith, Vollmer, "Playing with Boolean blocks" | — | Ex. 1.3; Post's criterion | V [str] |
| SEP, "Algebraic Propositional Logic" (Jansana) | — | Łoś–Suszko structurality | S [str] |
| Mossakowski, Diaconescu, Tarlecki, "What is a logic translation?" | Preprint | Prop 2.25; §2.1 (schematic over-exclusion); conclusion | V [S0, own] |
| Cook, Reckhow (JSL 1979) | — | Thm 2.3; Cor 2.4; Lemma 2.5 | V [S0] |

### Interpreter constructions and Dedukti

| Source | Version | Location used | Status |
|---|---|---|---|
| Clavel, Meseguer (ENTCS 4, 1996) | — | Thm 3.2 | V [S0] |
| Felicissimo (FSCD 2022) | — | Thm 46 | V [S0] |
| Felicissimo, Winterhalter (FSCD 2024) | — | Table 1 | V [S0] |
| Krajíček, *Proof Complexity* (2019) | — | Thm 8.4.3 | S [S0] |

### Generic frameworks and structural data

| Source | Version | Location used | Status |
|---|---|---|---|
| Licata, Shulman, Riley (FSCD 2017, LIPIcs 84, art. 25) + extended version | — | Thm 2.1; §4; p. 25:17; Conj 8.5 | V [R, gfu] |
| Licata, Shulman (LFCS 2016) | Preprint | Mode-theory equality remark | V [R] |
| Shulman, "LNL polycategories and doctrines of linear logic" (LMCS 19(2), 2023) | — | Remark 2.7; "cut-elimination for future study" | V [R] |
| Shulman, "Semantics of multimodal adjoint type theory" (MFPS 2023) | — | Remark 2.6; open question (iv) | V [gfu, own] |
| Pruiksma, thesis CMU-CS-24-103 | — | σ(m) ⊆ {W, C}; cut elimination; identity | V [gfu] |
| Clarke, Scherer, Zeilberger, "The free bifibration on a functor" | arXiv:2511.07314v3 | Thms 1.17, 3.27, 3.28 | V [gfu, own] |
| Kanovich, Kuznetsov, Nigam, Scedrov (MSCS 2019) | arXiv:1709.03607 | Thms 8, 15 | V [gfu, own] |
| Kanovich, Kuznetsov, Scedrov | arXiv:1608.02254 | Thms 9–10, restating Buszkowski 1982 | V; Buszkowski itself S [gfu] |
| Miller, Pimentel (TCS 2013) | — | Defs 3, 4, 17, 18; Thms 6, 22 | V [S0, gfu] |
| Marin, Miller, Pimentel, Volpe (APAL 2022) | — | Thms 4, 6, 12, 13, 16, 17 | V [gfu] |

### Unities of logic and other sources

| Source | Version | Location used | Status |
|---|---|---|---|
| Yamada, "Sequent calculi for a unity of logic" | arXiv:2001.06138v3 (preprint) | Cor 3.18; Thm 3.26; Cor 3.37 | V [own] |
| Holliday, Hoshi, Icard (LORI-III 2011) | Author copy | §§1.1–1.2 | V [own] |
| Girard, LU; Laurent–Regnier (LICS 2003) unity diagram; Buszkowski 1982; Chvalovský–Horčík 2016; Zolin 2000; Sheffer 1913; Post 1941; Łoś–Suszko 1958 | — | — | N |
