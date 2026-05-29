# Pistos Security Awareness Training

This repository contains the static HTML Pistos Security Awareness Training platform.

## Platform structure

The platform uses a root landing page and three training levels:

- `index.html` — root training portal
- `Introduction/` — introductory modules
- `Intermediate/` — intermediate modules
- `Advanced/` — advanced modules

Each level contains twelve core security topics:

1. Security Architecture
2. Multifactor Authentication
3. Securing Data in the Quantum World
4. Malware
5. Social Engineering
6. Passwords
7. Email
8. Data Protection
9. Network Security
10. Internet Security
11. Incident Management
12. Encryption

## Current module naming

Do not invent filenames. Inspect the repository before changing links.

### Introduction

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

### Intermediate

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

### Advanced

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

## Link auditing

A repository-local link checker is available at:

```bash
python scripts/link_audit.py
```

The default audit checks:

- `index.html`
- all HTML files under `Introduction/`
- all HTML files under `Intermediate/`
- all HTML files under `Advanced/`

To include case-study files as well:

```bash
python scripts/link_audit.py --include-case-studies
```

The script verifies local `href` and `src` references. It ignores external URLs, `mailto:`, `tel:`, `javascript:`, `data:`, fragments, and in-page anchors.

A GitHub Actions workflow runs this audit automatically on pushes to `main` and on pull requests.

## Development rules

- Inspect the repository before editing.
- Preserve existing content unless instructed otherwise.
- Do not invent filenames.
- Prefer repository-relative links.
- Run the link audit after link, filename, or asset changes.
- Commit directly to `main` only when explicitly instructed.

## Documentation files

- `PROJECT_STATUS.md` — architecture and inventory baseline
- `LINK_AUDIT.md` — first link audit report and recommended fixes
