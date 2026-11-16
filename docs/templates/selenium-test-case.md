# Selenium Test Case: [Title]

## Purpose

## Target environment
Use a local or explicitly authorized test application.

## Preconditions
- Browser/version:
- Selenium version:
- Test account or synthetic fixture:
- Driver setup:

## Test steps
| Step | Browser action | Expected result |
|---|---|---|
| 1 | Open permitted test page | Page loads |
| 2 | Locate test element | Element is present |
| 3 | Interact with control | Expected UI state |
| 4 | Verify output | Assertion passes |

## Automation requirements
- Prefer stable locators.
- Use explicit waits.
- Do not bypass CAPTCHA or access restrictions.
- Keep credentials outside source control.
- Close the browser in a finally block.

## Cleanup
Delete generated data and close the session.
