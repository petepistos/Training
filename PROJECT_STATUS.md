# Pistos Security Awareness Training — Project Status

Generated for repository: `petepistos/Training`

Branch reviewed: `main`

Purpose: establish a clean baseline inventory before additional structural changes.

## Current architecture

The repository contains a static HTML training platform with the following major parts:

- Root landing page: `index.html`
- Training module folders:
  - `Introduction/`
  - `Intermediate/`
  - `Advanced/`
- Brand/image assets:
  - `images/pistos-logo.png`
- Real-life event case studies:
  - `real-life-events/`
- Utility / cleanup scripts:
  - `brand_mathisi.py`
  - `cleanup_mathisi.py`
- Repository configuration and test artifacts:
  - `.gitignore`
  - `write-test.txt`
  - `write-test-chatgpt.txt`

The landing page uses inline CSS and JavaScript. It renders three selectable training levels and dynamically creates topic cards from an internal JavaScript map.

## HTML inventory

### Root

- `index.html`

### Introduction modules

The Introduction level currently has all 12 expected topic modules:

1. Security Architecture — `Introduction/01_intro_cyber.html`
2. Multifactor Authentication — `Introduction/02_intro_mfa.html`
3. Securing Data in the Quantum World — `Introduction/03_intro_quantum.html`
4. Malware — `Introduction/04_intro_malware.html`
5. Social Engineering — `Introduction/05_intro_social.html`
6. Passwords — `Introduction/06_intro_passwords.html`
7. Email — `Introduction/07_intro_email.html`
8. Data Protection — `Introduction/08_intro_dlp.html`
9. Network Security — `Introduction/09_intro_network.html`
10. Internet Security — `Introduction/10_intro_internet.html`
11. Incident Management — `Introduction/11_intro_incident_response.html`
12. Encryption — `Introduction/12_intro_encryption.html`

### Intermediate modules

The Intermediate level currently has all 12 expected topic modules:

1. Security Architecture — `Intermediate/int_01_security_arch_intermediate.html`
2. Multifactor Authentication — `Intermediate/int_02_mfa_intermediate.html`
3. Securing Data in the Quantum World — `Intermediate/int_03_quantum_intermediate.html`
4. Malware — `Intermediate/int_04_malware_intermediate.html`
5. Social Engineering — `Intermediate/int_05_social_eng_intermediate.html`
6. Passwords — `Intermediate/int_06_passwords_intermediate.html`
7. Email — `Intermediate/int_07_email_intermediate.html`
8. Data Protection — `Intermediate/int_08_data_protection_intermediate.html`
9. Network Security — `Intermediate/int_09_network_intermediate.html`
10. Internet Security — `Intermediate/int_10_internet_intermediate.html`
11. Incident Management — `Intermediate/int_11_incident_intermediate.html`
12. Encryption — `Intermediate/int_12_encryption_intermediate.html`

### Advanced modules

The Advanced level currently has all 12 expected topic modules:

1. Security Architecture — `Advanced/adv_01_security_arch_advanced.html`
2. Multifactor Authentication — `Advanced/adv_02_mfa_advanced.html`
3. Securing Data in the Quantum World — `Advanced/adv_03_quantum_advanced.html`
4. Malware — `Advanced/adv_04_malware_advanced.html`
5. Social Engineering — `Advanced/adv_05_social_eng_advanced.html`
6. Passwords — `Advanced/adv_06_passwords_advanced.html`
7. Email — `Advanced/adv_07_email_advanced.html`
8. Data Protection — `Advanced/adv_08_data_protection_advanced.html`
9. Network Security — `Advanced/adv_09_network_advanced.html`
10. Internet Security — `Advanced/adv_10_internet_advanced.html`
11. Incident Management — `Advanced/adv_11_incident_advanced.html`
12. Encryption — `Advanced/adv_12_encryption_advanced.html`

### Real-life event case studies

The repository also contains 11 real-life event case-study HTML files:

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

## Image, CSS, JavaScript, and asset inventory

### Images

- `images/pistos-logo.png`

### CSS

No standalone `.css` files were identified in the inventory. Styling appears to be embedded inline inside the HTML files.

### JavaScript

No standalone `.js` files were identified in the inventory. Interactive behavior appears to be embedded inline inside the HTML files.

### Other assets

- `Intermediate/files.zip`
- `.gitignore`
- `brand_mathisi.py`
- `cleanup_mathisi.py`
- `write-test.txt`
- `write-test-chatgpt.txt`

## Landing page link map

The current `index.html` JavaScript map points to all 36 expected training modules.

### Introduction landing links

- `Introduction/01_intro_cyber.html`
- `Introduction/02_intro_mfa.html`
- `Introduction/03_intro_quantum.html`
- `Introduction/04_intro_malware.html`
- `Introduction/05_intro_social.html`
- `Introduction/06_intro_passwords.html`
- `Introduction/07_intro_email.html`
- `Introduction/08_intro_dlp.html`
- `Introduction/09_intro_network.html`
- `Introduction/10_intro_internet.html`
- `Introduction/11_intro_incident_response.html`
- `Introduction/12_intro_encryption.html`

### Intermediate landing links

- `Intermediate/int_01_security_arch_intermediate.html`
- `Intermediate/int_02_mfa_intermediate.html`
- `Intermediate/int_03_quantum_intermediate.html`
- `Intermediate/int_04_malware_intermediate.html`
- `Intermediate/int_05_social_eng_intermediate.html`
- `Intermediate/int_06_passwords_intermediate.html`
- `Intermediate/int_07_email_intermediate.html`
- `Intermediate/int_08_data_protection_intermediate.html`
- `Intermediate/int_09_network_intermediate.html`
- `Intermediate/int_10_internet_intermediate.html`
- `Intermediate/int_11_incident_intermediate.html`
- `Intermediate/int_12_encryption_intermediate.html`

### Advanced landing links

- `Advanced/adv_01_security_arch_advanced.html`
- `Advanced/adv_02_mfa_advanced.html`
- `Advanced/adv_03_quantum_advanced.html`
- `Advanced/adv_04_malware_advanced.html`
- `Advanced/adv_05_social_eng_advanced.html`
- `Advanced/adv_06_passwords_advanced.html`
- `Advanced/adv_07_email_advanced.html`
- `Advanced/adv_08_data_protection_advanced.html`
- `Advanced/adv_09_network_advanced.html`
- `Advanced/adv_10_internet_advanced.html`
- `Advanced/adv_11_incident_advanced.html`
- `Advanced/adv_12_encryption_advanced.html`

## Missing modules

No missing modules were identified for the primary 36-module training architecture. Each of the 12 expected topics exists in Introduction, Intermediate, and Advanced.

## Broken links and naming issues

Known prior broken landing page links were caused by generated filenames such as `security_arch_introduction.html`. The current landing page now uses explicit repository-relative paths.

No broken landing-page links were identified in the current 36-module training map.

Potential naming debt remains from older filenames that were removed or renamed:

- `Introduction/01_intro_cybersecurity.html` was removed and replaced by `Introduction/01_intro_cyber.html`.
- `Introduction/05_intro_social_engineering.html` was removed and replaced by `Introduction/05_intro_social.html`.
- `Introduction/07_intro_email_security.html` was removed and replaced by `Introduction/07_intro_email.html`.
- `Introduction/08_intro_data_protection.html` was removed and replaced by `Introduction/08_intro_dlp.html`.
- `Introduction/09_intro_network_security.html` was removed and replaced by `Introduction/09_intro_network.html`.
- `Introduction/10_intro_internet_security.html` was removed and replaced by `Introduction/10_intro_internet.html`.

If any module still links internally to the old names above, those links should be corrected in a future pass.

## Orphaned or duplicate content

Potential orphaned items:

- `real-life-events/` contains 11 case-study HTML files, but the current root landing page only exposes the three main training levels. These case studies may need a landing-page section or a separate case-study index.
- `Intermediate/files.zip` is present but its purpose is unclear from the current baseline inventory.
- `write-test.txt` and `write-test-chatgpt.txt` appear to be write-access test files and may not belong in production.
- `brand_mathisi.py` and `cleanup_mathisi.py` appear to be one-time maintenance scripts. Their continued role should be documented or they should be moved to a tooling/archive area.

Possible duplicate/history artifacts:

- Removed Introduction filenames indicate the project has undergone filename normalization. No duplicate live module files were identified in the current 36-module map.

## Technical debt

1. Inline CSS and JavaScript are repeated across module files. This makes global style or behavior updates more difficult and increases the chance of inconsistent module behavior.
2. Root `index.html` is heavily minified/condensed, which makes manual review harder.
3. Module naming is not fully uniform across levels:
   - Introduction uses `01_intro_*` style.
   - Intermediate uses `int_01_*_intermediate` style.
   - Advanced uses `adv_01_*_advanced` style.
4. Real-life event files are outside the three-level architecture and are not currently represented in the landing page baseline.
5. No standalone CSS or JS bundle exists, so every module is effectively its own self-contained application page.
6. There is no automated link checker, HTML validation, or static-site test workflow documented in the repository baseline.
7. No README or developer guide was identified in the current inventory.

## Recommended next actions

1. Add a lightweight link-audit script that parses `index.html` and verifies that every linked module file exists.
2. Add a real-life events section or separate case-study index if those 11 files are intended to be user-facing.
3. Decide whether `write-test.txt` and `write-test-chatgpt.txt` should be deleted from production.
4. Decide whether `Intermediate/files.zip` is required; document it if retained.
5. Create a `README.md` explaining the platform structure, naming conventions, and deployment process.
6. Consider extracting shared CSS and JavaScript into reusable assets after the current content baseline is stable.
7. Standardize naming only after a full link audit, because renaming module files can easily break existing links.

## Warnings and limitations

- The inventory was built from repository metadata, current file fetches, and commit comparison output. The available GitHub connector does not expose a direct full tree-list command in this session, so this document should be treated as a strong baseline but still worth verifying with a local clone or CI-based file tree audit.
- The root landing page was confirmed to point to all 36 primary module files. Internal links inside every individual module were not exhaustively tested in this pass.
- Real-life event files were identified, but their internal links and content were not fully reviewed in this pass.
- Because this file is intended as a baseline, no structural changes were made while creating it.
