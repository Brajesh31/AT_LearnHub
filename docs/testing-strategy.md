# ✅ Testing and validation strategy

AT_LearnHub is not one application, so tests should be scoped by resource type.

| Artifact | Minimum validation | Stronger validation |
|---|---|---|
| Python `.py` | `python -m py_compile` | Unit tests and safe sample execution |
| Shell `.sh` | `bash -n` | Execute in disposable container/VM |
| JSON | `python -m json.tool` | Schema validation and semantic checks |
| SQL | Static review | Execute in disposable DB and verify schema/data |
| Selenium | Import/syntax check | Authorized browser integration test |
| CSV | Inspect headers/encoding | Validate schema and sample rows |
| Markdown | Link and fence checker | Human review and rendered GitHub check |
| SVG | XML parse | Render/visual review |
| Office docs/media | Open with compatible application | Verify content and distribution rights |

## Safety gates
- Do not run scripts with production data.
- Do not automate external services without permission.
- Do not execute destructive SQL against important databases.
- Do not assume a passing syntax check proves business correctness.
- Do not use real personal data in test output or screenshots.

## Current automation
The documentation-quality workflow validates Markdown local links and fenced blocks. A source-quality workflow performs safe syntax checks on selected Python and shell files, plus JSON parsing where applicable. These checks are intentionally limited and do not execute browser automation or SQL scripts.
