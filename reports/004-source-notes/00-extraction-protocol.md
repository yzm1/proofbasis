# Source-extraction protocol (shared by all source agents)

Context (TASK 004 — positive existence): we test whether a FIXED finite core calculus (classical many-sorted first-order logic) is a universal "fundamental" core for an independently defined infinite class of propositional logics via CANONICAL standard (relational-semantics) translations, with the environment holding only first-order frame conditions, and where the boundary lies (Kripke incompleteness, non-elementary logics); and what proof-level (proof-identity) analogues exist. The program asks whether a FIXED FINITE "algebra" of proof-construction operations
can represent finite formal proofs across many logical foundations (assumptions/definitions held in a separate
"environment"), while preserving: (R1) derivability (preserve AND reflect), (R2) composition/substitution/binding/
assumption-discharge/resource discipline, (R3) a declared proof-identity congruence (preserve and reflect),
(R4) causal/independence structure. Key threats: F01 already solved by an existing framework theorem; F02 trivial
universal-interpreter encodings; F03 trusted inference rules hidden in the environment (signatures, rewrite rules);
F04 incompatible proof identities across foundations; F05 global (non-local) correctness such as cyclic-proof trace
conditions; F07 infinitary/non-effective proof forms; F08 basis choice is arbitrary under encodings; F09 size/search
blowups of derived/eliminated rules.

Your job: retrieve PRIMARY sources and extract EXACT theorem statements, hypotheses, quantifiers, definitions of
"adequacy"/"translation"/"conservativity"/"faithfulness", and what is (and is NOT) preserved, esp. proof identity.

Rules (strict):
1. Never fabricate. Do not state a theorem number, page, quote, DOI or URL you did not actually see in a text you
   retrieved during this session. If you rely on memory, label it UNVERIFIED-MEMORY.
2. Download PDFs with curl into a NEW empty subdirectory of
   <session-scratchpad>/t004/dl/<yourtag>/ and convert with
   `pdftotext -layout file.pdf file.txt` (run from outside that directory, passing paths). Do not execute anything
   downloaded. Grep the text for theorem statements. Prefer author homepages, arXiv, publisher open access, HAL,
   CiteSeerX, DROPS/LIPIcs, EPTCS.
3. For each source record:
   - Full bibliographic data (authors, title, venue, year, DOI if printed on the document).
   - URL actually retrieved, and which VERSION it is (journal / preprint / tech report / thesis) — page numbers refer to that version.
   - Status: VERIFIED_SOURCE (you read the passage in the retrieved text) / SECONDARY_ONLY (only seen in another
     paper's description; name it) / UNVERIFIED-MEMORY / NOT_ACCESSED.
   - Verbatim quotes (short, <= ~80 words each) of the key definition(s) and theorem(s), with location
     (section / theorem number / PDF page). Mark verbatim quotes with quotation marks; paraphrases clearly as paraphrase.
   - Hypotheses and quantifiers; what kind of translation; what is preserved/reflected; whether proof identity
     (beyond derivability) is addressed; what is placed in the "machine" vs the "environment"/signature, and what must be TRUSTED.
   - Known limitations / negative results stated in the source itself.
   - Relevance to threats F01–F10 above (1–3 sentences, your INFERENCE, labelled as such).
4. Write your notes to the markdown file named in your task (in the t004/notes/ dir) as you go. Your final message should
   summarize the most decisive findings (<= 600 words) and list any source you could NOT access.
5. Do not modify the git repository at /home/user/proofbasis.
