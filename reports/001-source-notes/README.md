# Source-extraction logs for report 001

These files are the **evidence log** behind `reports/001-existence-and-novelty.md`. They are working notes, not polished prose. Their purpose is auditability: every theorem the report cites should be traceable to an entry here with
the URL retrieved, the version read (journal / preprint / tech report / thesis), the location, a verbatim quote, and a
status label.

## Provenance

- Produced on 2026-10-08 by six source-extraction agents (Claude subagents) working under a common protocol
  (`00-extraction-protocol.md`). Each agent downloaded primary texts, converted them with `pdftotext` (or
  ghostscript / OCR for scans), and grepped and read the relevant passages.
- The synthesising author then independently re-located ten decisive passages in the downloaded texts:
  - MDT Prop. 2.25
  - Clavel–Meseguer Thm 3.2
  - HHP Thm 4.1
  - Gardner Cor. 5.1.8 (OCR)
  - GLT App. B "noticed by Joyal"
  - Heijltjes–Houston Thm 9.1
  - Blanqui et al. §4 non-conservativity disclaimer
  - Felicissimo Thm 46
  - Dedukti manuscript §3.1 "out of the scope"
  - Maraist et al. §8.3 counterexample
  
  This is agreement between agents. It is **not** formal verification.
- Downloaded PDFs are **not** committed, for copyright reasons. The notes give the URL each was retrieved from.
  Paths such as `scratchpad/dl/...` refer to the ephemeral session workspace.
- Page numbers refer to the version actually retrieved, which is often a preprint. Journal pagination may differ.

## Status vocabulary used in the notes

| Label | Meaning |
|---|---|
| VERIFIED_SOURCE | The passage was read in the retrieved text |
| SECONDARY_ONLY | Seen only as described in another source, which is named |
| UNVERIFIED-MEMORY | Agent recollection, not checked |
| NOT_ACCESSED | Source could not be retrieved |
| ABSTRACT_ONLY | Only the official abstract or metadata was read |
| INFERENCE | The agent's own reasoning, not a source claim |

## Files

| File | Scope |
|---|---|
| `lf-isabelle-fpc.md` | Harper–Honsell–Plotkin, Harper–Licata, Pfenning handbook, LLF, CLF, Paulson (Isabelle/Pure), Foundational Proof Certificates, Avron–Honsell–Mason, Gardner thesis |
| `rewriting-logic-general-logics-mmt.md` | Clavel–Meseguer universal theory, Clavel–Meseguer–Palomino, Martí-Oliet–Meseguer, General Logics, Mossakowski–Diaconescu–Tarlecki, Rabe, Goguen–Burstall, Meseguer survey |
| `dedukti.md` | Cousineau–Dowek, Assaf, Dedukti manuscript, theory U, Felicissimo, rewrite-rule checking, Felicissimo–Winterhalter, Dowek |
| `proof-identity.md` | Joyal collapse (GLT, Došen), Heijltjes–Houston, Hughes–van Glabbeek, Girard 1987, Straßburger, Lamarche–Straßburger, Hughes, deep inference, Selinger, Hasegawa |
| `cyclic-infinitary-complexity.md` | Brotherston thesis, Berardi–Tatsuta, Das, Nollet–Saurin–Tasson, Baelde et al., Cohen et al., Cook–Reckhow, Ben-Sasson et al., Buss, ω-rule, second-order logic, Kuperberg–Pinault–Pous, Oda–Kimura |
| `adequacy-levels-translations.md` | Nigam–Miller, Miller–Pimentel, Harper–Sannella–Tarlecki, Selinger, Hofmann–Streicher (secondary), Maraist–Odersky–Turner–Wadler, Benton–Wadler, Benton, EF+reflection, polygraphs, Lafont |

## Known corrections recorded in the notes

These are errors in the prompts given to the agents, not errors in the repository.

- "Cyclic proofs, system T, and the power of contraction" is by Kuperberg, Pinault and Pous, not Das.
- The polygraphs monograph (arXiv:2312.00429) is by Ara, Burroni, Guiraud, Malbos, Métayer and Mimram.
- Theorems of PA plus the ω-rule are exactly true arithmetic, which is not arithmetical and so not r.e. It is the
  set of ω-proof *codes* that is Π¹₁-complete (Frittaion, Thm 2.3).
