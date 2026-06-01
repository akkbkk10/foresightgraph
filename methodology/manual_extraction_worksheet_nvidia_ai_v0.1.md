# Manual Extraction Worksheet: NVIDIA AI Ecosystem v0.1

## Worksheet ID
manual_extraction_worksheet_nvidia_ai_v0.1

## Purpose
Prepare manual extraction from selected real sources for the first real-source dry run

## Selected Source List
1. **source_id**: real_nvidia_ai_001
   **title**: NVIDIA Blackwell Architecture

2. **source_id**: real_nvidia_ai_003
   **title**: NVIDIA NIM Microservices

3. **source_id**: real_nvidia_ai_004
   **title**: NVIDIA NeMo

## Important Notes
- No claims extracted yet
- No evidence extracted yet
- No benchmark run
- No provider decision
- Source content must be manually reviewed before extraction

## Source Extraction Sections

### Source 1: real_nvidia_ai_001
- **source_id**: real_nvidia_ai_001
- **source title**: NVIDIA Blackwell Architecture
- **date accessed**: 2026-06-01
- **locator candidates**: 
  - Seitentitel "NVIDIA Blackwell Architecture" / Abschnitt "A New Class of AI Superchip"
  - Abschnitt "Second-Generation Transformer Engine"
- **copied excerpt slots**: 
  - "GPUs pack 208 billion transistors"
  - "accelerate inference and training for large language models"
- **possible evidence_id placeholders**: 
  - evidence_nvidia_blackwell_001
  - evidence_nvidia_blackwell_002
- **possible claim_id placeholders**: 
  - claim_candidate_nvidia_blackwell_001
  - claim_candidate_nvidia_blackwell_002

## Claim Candidates

### Claim Candidate 1
- **claim_id**: claim_candidate_nvidia_blackwell_001
- **linked_evidence_id**: evidence_nvidia_blackwell_001
- **claim_text**: NVIDIA states on its Blackwell Architecture page that Blackwell GPUs pack 208 billion transistors.
- **claim_status**: manufacturer_claim
- **project_status**: not_reproduced
- **review_status**: reviewed_vendor_claim_only
- **notes**: This is a vendor-source claim candidate based only on the copied excerpt. It is not independently verified by the project.

### Claim Candidate 2
- **claim_id**: claim_candidate_nvidia_blackwell_002
- **linked_evidence_id**: evidence_nvidia_blackwell_002
- **claim_text**: NVIDIA states that the Second-Generation Transformer Engine is intended to accelerate inference and training for large language models.
- **claim_status**: manufacturer_claim
- **project_status**: not_reproduced
- **review_status**: reviewed_vendor_claim_only
- **notes**: This is a vendor-source claim candidate based only on the copied excerpt. It is not independently verified by the project.

- **source_id**: real_nvidia_ai_003
- **source title**: NVIDIA NIM Microservices
- **date accessed**: 2026-06-01
- **locator candidates**: 
  - Seitentitel "NVIDIA NIM Microservices" / Abschnitt "What Is NVIDIA NIM?"
  - Abschnitt "Accelerate AI Deployment With NVIDIA NIM"
- **copied excerpt slots**: 
  - "prebuilt, optimized inference microservices"
  - "prepackaged in enterprise-grade software containers ready to deploy and scale anywhere"
- **possible evidence_id placeholders**: 
  - evidence_nvidia_nim_001
  - evidence_nvidia_nim_002
- **possible claim_id placeholders**: 
  - claim_candidate_nvidia_nim_001
- **review_status**: reviewed_vendor_claim_only
- **reviewer_notes**: Diese Stellen sind relevant, weil sie NIM als produktisierte Software-Schicht für AI-Inferenz beschreiben. Der erste Excerpt belegt den Kernzweck: optimierte Inferenz-Microservices. Der zweite Excerpt belegt die Verpackung als enterprise-grade Container, also eine deploybare Software-Komponente. Daraus entsteht keine Aussage über Umsatz, Marktanteil, Wettbewerbsvorteil oder Investmentqualität.

- **source_id**: real_nvidia_ai_004
- **source title**: NVIDIA NeMo
- **date accessed**: 2026-06-01
- **locator candidates**: 
  - Seitentitel "NVIDIA NeMo" / Abschnitt "What Is NVIDIA NeMo?"
  - Abschnitt "What Is NVIDIA NeMo?"
- **copied excerpt slots**: 
  - "agent-first, open suite of libraries"
  - "integrates with existing AI tools and agent frameworks"
- **possible evidence_id placeholders**: 
  - evidence_nvidia_nemo_001
  - evidence_nvidia_nemo_002
- **possible claim_id placeholders**: 
  - claim_candidate_nvidia_nemo_001
- **source_status**: official_vendor_source
- **project_status**: not_reproduced
- **review_status**: reviewed_vendor_claim_only
- **reviewer_notes**: Diese Stellen sind relevant, weil sie NeMo nicht als einzelnes Modell, sondern als offene Software-Suite für AI-Agenten beschreiben. Der erste Excerpt belegt die Grundpositionierung von NeMo. Der zweite Excerpt belegt die Integrationsrolle mit bestehenden Tools und Agent-Frameworks. Daraus entsteht noch keine Aussage über technische Überlegenheit, Benchmarks, Umsatzwirkung oder Investmentqualität.

## Manual Extraction Checklist
- [ ] Verify source page manually
- [ ] Copy only short relevant excerpts
- [ ] Record locator
- [ ] Create evidence only after source text is visible
- [ ] Create claims only after evidence is reviewed
- [ ] Mark vendor claims as manufacturer/vendor claims
- [ ] Do not treat vendor claims as reproduced project facts

## Safety Boundaries
- [ ] No investment conclusions
- [ ] No performance verification
- [ ] No automation
- [ ] No scraping
- [ ] No SDK/runtime integration

## Smallest Next Step
User manually provides 1 or 2 short excerpts from one selected source for first evidence draft