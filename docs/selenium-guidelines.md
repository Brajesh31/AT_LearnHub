# 🧭 Selenium and browser automation guidelines

## Browser setup
- Use an isolated browser profile.
- Match browser and driver versions.
- Prefer managed driver resolution or a documented local path.
- Keep browser binaries and profiles out of commits unless explicitly required as archival material.
- Close the driver in a `finally` block.

## Existing archive caveat
Some scripts contain machine-specific absolute paths and the repository contains platform-specific driver binaries. Those files are historical artifacts. They should not be assumed runnable on another machine. Verify binary source and compatibility before execution.

## Locator and wait guidance
Prefer stable IDs, names, or documented test attributes. Use explicit waits for observable conditions. Avoid arbitrary sleeps and fragile absolute XPath selectors.

## External services
Use local test pages or services that explicitly permit automation. Do not automate personal accounts or attempt to bypass CAPTCHA, login protections, anti-bot challenges, rate limits, or access restrictions.

## Data handling
Use synthetic data. Avoid saving cookies, browser profiles, credentials, or personal page content. Scraped output should include provenance and be checked for private information before committing.
