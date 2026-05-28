# Relationship Signal Examples

## Purpose

This document provides illustrative examples of how strategic partnership and acquisition signals should be documented using the relationship signal source template. These examples demonstrate the structure and content requirements for different signal orientations and confidence levels.

## Note

These examples are illustrative only and use fictional company names. They do not constitute investment advice or legal conclusions. All claims are hypothetical and should not be interpreted as statements about real companies or their actual business activities.

## Example 1: Partnership Likely (Green Edge)
**Signal Category:** commercial
**Orientation:** partnership_likely

source_id: REL-2026-001
source_type: company_press_release
publisher: TechGlobal Inc.
title: TechGlobal Announces Strategic Partnership with CloudNexus
url_or_locator: https://www.techglobal.com/press/strategic-partnership-announcement
published_at: 2026-03-15
observed_at: 2026-03-16
company_a: TechGlobal Inc.
company_b: CloudNexus
signal_category: commercial
orientation: partnership_likely
evidence_summary: Press release announces joint development of cloud infrastructure solutions and shared customer access
confidence: medium
materiality: medium
review_status: pending
review_due_at: 2026-04-15

*Why this orientation was chosen:* The announcement describes a strategic partnership with joint development and shared resources, which indicates a strong likelihood of collaboration. The evidence is based on a formal press release from the company.

*What would increase confidence:* Additional evidence such as a signed memorandum of understanding, public statements from leadership teams, or specific technical integration details would strengthen this signal.

## Example 2: Acquisition Possible (Yellow Edge)
**Signal Category:** capital
**Orientation:** acquisition_possible

source_id: REL-2026-002
source_type: reputable_news
publisher: Financial Times
title: TechGlobal Inc. Shows Interest in Acquiring DataFlow Solutions
url_or_locator: https://www.ft.com/article/techglobal-acquisition-interest
published_at: 2026-04-01
observed_at: 2026-04-02
company_a: TechGlobal Inc.
company_b: DataFlow Solutions
signal_category: capital
orientation: acquisition_possible
evidence_summary: Financial Times article reports TechGlobal Inc. has expressed interest in acquiring DataFlow Solutions, with no official confirmation yet
confidence: low
materiality: high
review_status: pending
review_due_at: 2026-05-01

*Why this orientation was chosen:* The article reports interest from a major player in the industry without confirmation, which indicates potential acquisition interest. This is a speculative signal that requires further verification.

*What would increase confidence:* Official acquisition announcement, SEC filing, or direct confirmation from either company's leadership would significantly increase confidence in this signal.

## Example 3: Confirmed Transaction (Red Edge)
**Signal Category:** acquisition-process
**Orientation:** confirmed_transaction

source_id: REL-2026-003
source_type: SEC_8K
publisher: TechGlobal Inc.
title: TechGlobal Inc. Files 8-K for Acquisition of CloudNexus
url_or_locator: https://www.sec.gov/Archives/edgar/data/1234567/8-k/techglobal-20260415.htm
published_at: 2026-04-15
observed_at: 2026-04-16
company_a: TechGlobal Inc.
company_b: CloudNexus
signal_category: acquisition-process
orientation: confirmed_transaction
evidence_summary: Official SEC 8-K filing confirms acquisition agreement with specific terms and closing date
confidence: high
materiality: high
review_status: reviewed
review_due_at: 2026-04-30

*Why this orientation was chosen:* The official SEC filing provides concrete evidence of a completed acquisition transaction with specific terms, making this a confirmed signal. The filing contains legally binding information about the transaction.

*What would increase confidence:* Additional details about the transaction value, integration plans, or post-acquisition strategic alignment would provide more comprehensive understanding of the deal's implications.