# Relationship Signal Source Template

## Purpose

This template defines the structure for recording evidence sources when observing strategic partnership or acquisition-related signals. It ensures all signal observations can be traced back to reliable sources with proper quality assessment, timing, and review status.

## When to use this template

Use this template whenever documenting any strategic partnership or acquisition signal. Every signal must be backed by at least one source that follows this template structure to maintain evidence integrity and traceability.

## Required Source Fields

- **source_id** - Unique identifier for this source instance
- **source_type** - Type of source document or communication
- **publisher** - Organization or entity that published/created the source
- **title** - Formal title or headline of the source material
- **url_or_locator** - Direct link or location reference to the source
- **published_at** - Official publication date of the source
- **observed_at** - Date when the signal was first observed and documented
- **company_a** - First company involved in the relationship
- **company_b** - Second company involved in the relationship
- **signal_category** - Category of the signal (ecosystem, technical, commercial, capital, acquisition-interest, acquisition-process)
- **orientation** - Signal orientation (partnership_likely, acquisition_possible, acquisition_likely, confirmed_transaction)
- **evidence_summary** - Brief description of the evidence found
- **confidence** - Confidence level (low, medium, high) in the signal interpretation
- **materiality** - Materiality assessment (low, medium, high) of the signal
- **review_status** - Current review status (pending, reviewed, confirmed, rejected)
- **review_due_at** - Date when review is due for this source

## Allowed source_type Examples

- company_press_release
- SEC_8K
- Schedule_13D
- investor_presentation
- earnings_call
- regulatory_filing
- conference_keynote
- product_documentation
- reputable_news
- ecosystem_program_page

## Review Rule

- One source can create a watch signal (yellow indicator)
- Stronger status requires multiple sources or regulatory/company confirmation
- Partnership signal is not acquisition proof
- Acquisition signal is not investment advice

## Out of Scope

This template does not include:
- Buy/Sell/Hold recommendations
- Price targets or financial projections
- Automated legal conclusions or compliance determinations
- Live scraping or real-time alerts