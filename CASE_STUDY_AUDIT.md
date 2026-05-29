# Case Study Audit — Pistos Security Awareness Training

Repository: `petepistos/Training`

Branch audited: `main`

Scope:

- `real-life-events/` case-study HTML files
- Relationship between case studies and the root training portal

No production files were modified during this audit. This file is documentation only.

## Summary

The repository contains 11 real-life case-study HTML files under `real-life-events/`:

1. `real-life-events/cs_01_target.html`
2. `real-life-events/cs_02_ubiquiti.html`
3. `real-life-events/cs_03_sony.html`
4. `real-life-events/cs_04_casino.html`
5. `real-life-events/cs_05_tesla.html`
6. `real-life-events/cs_06_colonial.html`
7. `real-life-events/cs_07_baltimore.html`
8. `real-life-events/cs_08_uber.html`
9. `real-life-events/cs_09_equifax.html`
10. `real-life-events/cs_10_maersk.html`
11. `real-life-events/cs_11_crowdstrike.html`

The sampled case-study structure matches the advanced-style module pattern:

- Pistos logo in the topbar
- sticky top navigation
- page sections
- narration bar
- quiz section
- inline CSS and JavaScript

The case-study pages appear to use the same asset path pattern as the training modules:

- `../images/pistos-logo.png`

That path resolves correctly from `real-life-events/` to the root `images/pistos-logo.png` asset.

## Current portal exposure

The current root `index.html` exposes only the three main training levels:

- Introduction
- Intermediate
- Advanced

The `real-life-events/` case-study files are not currently exposed from the root portal.

This makes the case studies effectively orphaned from the main user navigation unless users are given direct URLs.

## Findings

### Confirmed files

All 11 case-study files identified in the project inventory exist in the normalized lowercase folder:

- `real-life-events/`

Earlier history indicates the folder was renamed from:

- `Real Life Events/`

to:

- `real-life-events/`

The lowercase hyphenated folder is the current path and should be treated as canonical.

### Logo and asset path

The sampled case-study file uses:

- `../images/pistos-logo.png`

This is correct from inside `real-life-events/`.

### Navigation

The sampled case-study file has internal section navigation and quiz navigation, but no confirmed visible root portal link.

Recommended root link target from a case-study page:

- `../index.html`

### External dependencies

The sampled case-study file references Google Fonts:

- `https://fonts.googleapis.com`
- `https://fonts.googleapis.com/css2?...`

This matches the training module pattern and is an external runtime dependency, not a missing repository asset.

## Broken links

No confirmed broken repository-local link was identified in the sampled case-study file.

A full automated audit should include `real-life-events/` by running:

```bash
python scripts/link_audit.py --include-case-studies
```

## Suspicious links and gaps

1. **Case studies are not exposed from the root portal.**
   - Users cannot discover them from `index.html` unless a separate link is provided elsewhere.

2. **Case-study pages do not appear to have a confirmed visible back/home link.**
   - A consistent `Back to Portal` link to `../index.html` should be added if these pages are user-facing.

3. **The existing automated link-audit workflow does not include case studies by default.**
   - That was intentional for the first training-module audit, but the repository should now add a second audit mode or include case studies in the default workflow.

4. **Case-study naming has separate conventions from the 36-module training architecture.**
   - Current pattern: `cs_01_target.html`, `cs_02_ubiquiti.html`, etc.
   - This is acceptable if documented and kept stable.

## Recommended fixes

1. Add a root portal section titled `Real-Life Events` or `Case Studies`.
2. Add cards for the 11 case-study files under that section.
3. Add a visible `Back to Portal` link to each case-study page.
4. Update `scripts/link_audit.py` or the GitHub Actions workflow so case studies are included in regular link checks.
5. Update `README.md` to document the case-study folder and naming convention.
6. Avoid renaming the `real-life-events/` files unless all references are updated at the same time.

## Recommended case-study card map

If exposed on the root portal, the case-study section should link to:

- Target — `real-life-events/cs_01_target.html`
- Ubiquiti — `real-life-events/cs_02_ubiquiti.html`
- Sony — `real-life-events/cs_03_sony.html`
- Casino — `real-life-events/cs_04_casino.html`
- Tesla — `real-life-events/cs_05_tesla.html`
- Colonial Pipeline — `real-life-events/cs_06_colonial.html`
- Baltimore — `real-life-events/cs_07_baltimore.html`
- Uber — `real-life-events/cs_08_uber.html`
- Equifax — `real-life-events/cs_09_equifax.html`
- Maersk — `real-life-events/cs_10_maersk.html`
- CrowdStrike — `real-life-events/cs_11_crowdstrike.html`

## Next recommended action

Expose `real-life-events/` from the root portal as a separate case-study section and include it in the automated link-audit workflow.
