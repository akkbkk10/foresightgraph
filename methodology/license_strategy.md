# License Strategy for ForesightGraph

## Current State
- Private repository with no formal release yet
- No LICENSE file decision made
- Project in early development stage

## License Options Comparison

### No License/Private
- Full control over usage and distribution
- No legal protection for the code
- Cannot be legally distributed or used by others
- Not suitable for future open-source release

### MIT License
- Permissive, allows commercial use
- Simple terms
- No obligation to share modifications
- Widely accepted and understood
- Good for research and company use

### Apache-2.0 License
- Permissive but includes patent protection
- Clear warranty and liability limitations
- Compatible with most other licenses
- Good for commercial use
- Explicitly allows patent use

### GPL-3.0 License
- Strong copyleft protection
- Ensures derivative works remain open source
- Very restrictive for commercial use
- Would require any derivative works to be open source
- Not suitable for company/research use with proprietary features

### AGPL-3.0 License
- Strong copyleft with network use provisions
- Ensures web-based modifications remain open source
- Even more restrictive than GPL-3.0
- Not suitable for company/research use with proprietary features
- Very restrictive for commercial applications

## Recommendation
- Keep private/no public license until v0.1.0 release readiness
- Likely prefer Apache-2.0 for future public release due to patent protection and commercial compatibility
- Consider MIT as simpler alternative for easier adoption

## Rationale
- Future research/company use with potential proprietary features
- Plugins, agents, tools, and benchmarks
- Avoid accidental open-source release before project is mature
- Maintain flexibility for both research and commercial applications

## Non-Goals
- No legal advice provided
- No LICENSE file added at this time
- No release/tag created at this time