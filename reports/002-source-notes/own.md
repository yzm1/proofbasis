# own — extractions made directly by the report author (Task 002)

Retrieved 2026-10-08. Status labels per PROTOCOL.

## O1. Holliday, Hoshi, Icard, "Schematic Validity in Dynamic Epistemic Logic: Decidability", LORI-III, LNAI 6953, pp. 87–96 (2011)
- URL: https://philosophy.berkeley.edu/file/808/Schematic_Validity.pdf. VERSION: author copy, which "corrects some minor
  errors in the publication". It states it is superseded by Holliday, Hoshi, Icard, "Information dynamics and uniform
  substitution", Synthese 190 (2013) 31–55 (that version is NOT_ACCESSED). Status: VERIFIED_SOURCE (author copy).
- Abstract: "Unlike standard modal logics, many dynamic epistemic logics are not closed under uniform substitution. The
  classic example is Public Announcement Logic (PAL)".
- §1.1: PAL's axiomatization includes the reduction axiom "(i) ⟨ϕ⟩p ↔ (ϕ ∧ p)", where p ∈ At (atomic sentences).
- §1.2: "the substitution instance ⟨p⟩K_i p ↔ (p ∧ K_i p) of reduction axiom (i) is not valid"; "an atomic sentence in PAL is
  not a propositional variable in the ordinary sense".
- Footnote 4: other modal logics not closed under substitution ("pure provability", Åqvist's two-dimensional logic as
  discussed by Segerberg, a Halpern epistemic-doxastic logic).
- INFERENCE (relevance): any substitution-naturality criterion must be stated relative to a SORTED signature in which
  atoms and formulas are distinct sorts. Under that reading PAL's axioms are finitely schematic (axiom (i) is schematic
  in an atom-sorted metavariable).

## O2. Yamada, "Sequent calculi for a unity of logic: Classicality is symmetric to non-linearity", arXiv:2001.06138v3 (6 Jan 2021)
- VERSION: arXiv preprint. Venue not verified. Status: VERIFIED_SOURCE (preprint text). Not peer-review checked by us.
- Abstract: "a single sequent calculus that embodies classical, intuitionistic and linear logics … only a sequent calculus
  for a conservative extension of ILL suffices for ILL, IL, CLL− and CL."
- Cor 3.18 ("Translation T!? of LK into ILCι"): assigns "to each formal proof p of a sequent ∆ ⊢ Γ in LK, a formal proof
  T!?(p) of the sequent !T!?∗(∆) ⊢ ?T!?∗(Γ) in ILCι", with the connective-wise clauses:
  - T!?(A ∧ B) := ?T!?(A) & ?T!?(B);
  - T!?(A ∨ B) := !T!?(A) ⊕ !T!?(B);
  - T!?(A ⇛ B) := !T!?(A) ⊸ ?T!?(B).
  (The ⊸ symbol was garbled in extraction.)
- Thm 3.26 (Commutative unity): T!?(p) and T?!(p) "coincide modulo permuting axioms and rules".
- Cor 3.37 (Conservative translations): conservativity is shown for the restricted calculi LKρ, INCρ, CLCρ, ILCρ.
- Intro p.~3: "Girard's translation works as the unlinearisation ILL ↦ IL, but not CLL ↦ CL." It cites earlier unities:
  Girard [13] (LU), and others including Laurent–Regnier [28] (via polarised LL and CPS).
- INFERENCE (relevance): this is published (preprint) evidence that one fixed finite calculus has the rules of LK, LJ and
  ILL as DERIVED templates. The translations are connective-wise (structural), act on proofs by induction, and are
  conservative for provability on the restricted variants. Proof identity is only "modulo permutations", and is otherwise
  not addressed (that is Task 003's subject).

## O3. Spot checks made by the author in the agents' downloaded texts (Task 002)
- Jeřábek arXiv:1108.6263v2: intro "translations are not required to respect the structure of formulas in any way"; Thm 2.4
  — confirmed.
- MDT preprint: schematic preservation "rules out e.g. the standard translation of modal logic to first-order logic, which
  adds a quantifier at the very top" — confirmed (mdt.txt l.167–168).
- Harper PFPL ch.3 "Theorem 3.1 (Stability)" — confirmed.
- Fiore–Mahmoud arXiv:1308.5409 "Lemma 5.1 (Compositionality). The extension of a syntactic translation between
  second-order signatures commutes with substitution and metasubstitution." — confirmed.
- Shulman MATT Remark 2.6: "L[S†] can fail to have decidable equality even if L does" — confirmed.
- Kanovich–Kuznetsov–Nigam–Scedrov (arXiv 1709.03607): Thm 8 (undecidable if some subexponential allows non-local
  contraction) and Thm 15 (C = ∅: PSPACE / NP) — confirmed.
- Clarke–Scherer–Zeilberger arXiv:2511.07314v3:
  - Thm 1.17 "Λp : Bif(p) → C is the free bifibration on p";
  - Thm 3.27 (undecidable permutation equivalence for some C "with locally finite factorizations");
  - Thm 3.28 (decidable if C locally finite or factorization preordered)
  — confirmed.
