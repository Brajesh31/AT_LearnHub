# 🔌 APIs, websites and external interfaces

AT_LearnHub has no unified web API. Individual Selenium and scraping exercises may connect to public web pages or external services. Each integration is an isolated example and should have its own contract.

## Document every integration

| Attribute | What to record |
|---|---|
| Exercise path | Exact script or notebook path |
| Target | Domain and page/API purpose |
| Method | GET, POST, browser navigation, form action, etc. |
| Inputs | Parameters, files, selectors, data fields |
| Outputs | Console output, CSV, JSON, screenshots |
| Authentication | Whether a test account is required |
| Permissions | Written permission or approved target |
| Rate limits | Request/interaction frequency |
| Stability | Selectors, page markup, API may change |
| Data handling | Personal data, retention, redaction |
| Failure modes | Timeouts, changed selectors, access denial |

## Selenium behavior

Browser automation is not an authorization bypass. Do not evade CAPTCHAs, access controls, rate limits, or anti-abuse protections. Use local test applications or explicitly permitted test pages. Do not automate personal email, shopping, social, or other accounts without authorization.

## Web scraping

Respect site terms, robots guidance, privacy obligations, and request limits. Prefer documented APIs and public datasets. Do not collect personal or sensitive information without a legitimate basis and authorization.

## Output contracts

Where an exercise writes JSON/CSV, document encoding, column names, nested structure, timestamp format, and overwrite behavior. Validate output before using it elsewhere.
