# Strategic Partnership and Acquisition Signal Layer

## Purpose

This methodology defines the framework for detecting, classifying, and documenting strategic partnership and acquisition signals between companies within the ForesightGraph system. The layer enables evidence-backed graph signals that capture the evolving nature of corporate relationships from initial collaboration to confirmed transactions.

## Core Idea

Partnership signals and acquisition signals are related but not the same. A partnership signal indicates collaborative relationship development, while an acquisition signal indicates potential transactional intent. 

Key distinctions:
- Partnership signal is not acquisition proof
- Acquisition signal is not investment advice
- All signals require evidence, confidence, status, and human review

## Signal Orientations

1. **partnership_likely** - Early stage collaboration signals indicating potential for deeper partnership
2. **acquisition_possible** - Initial interest or preliminary discussions about potential acquisition
3. **acquisition_likely** - Stronger signals indicating high probability of acquisition process initiation
4. **confirmed_transaction** - Verified acquisition or partnership with formal documentation

## Signal Categories

1. **ecosystem signal** - Company's participation in industry ecosystems or networks
2. **technical integration signal** - Technical collaboration or integration activities
3. **commercial deal signal** - Business or commercial partnership agreements
4. **capital/investment signal** - Financial investment or capital allocation activities
5. **acquisition-interest signal** - Direct indicators of acquisition interest or intent
6. **acquisition-process signal** - Formal processes or stages in acquisition development

## Example Signals

### Ecosystem signals
- Startup ecosystem membership
- Industry consortium participation
- Technology platform membership

### Technical integration signals
- Joint product integration
- API or SDK sharing
- Shared development resources

### Commercial deal signals
- Joint press release
- Co-marketing agreements
- Distribution partnerships

### Capital/investment signals
- Strategic investment
- Venture capital funding
- Minority stake acquisition

### Acquisition-interest signals
- Board seat or observer rights
- Exclusivity or right-of-first-refusal
- Confidentiality agreements

### Acquisition-process signals
- Material definitive agreement
- Merger agreement
- Tender offer or acquisition announcement

## Graph Edge Idea

Relationships are visualized with color-coded edges:
- **Green** = partnership (collaborative relationship)
- **Yellow** = acquisition watch (potential acquisition interest)
- **Orange** = acquisition process likely (active acquisition process)
- **Red** = confirmed transaction (verified acquisition or partnership)

## Minimal Edge Fields

Each signal edge requires these fields:
- source_company
- target_company
- relationship_type
- signal_category
- orientation
- evidence_ids
- confidence
- signal_strength
- status
- observed_at
- last_verified_at
- review_due_at

## Out of Scope

This methodology does not include:
- Buy/Sell/Hold recommendations
- Price targets or financial projections
- Trading signals or market analysis
- Automated legal conclusions or compliance determinations
- Live scraping or real-time alerts