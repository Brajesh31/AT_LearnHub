# 🛠️ Development and contribution workflow

## Guiding principles

- Treat the archive as learning material, not one application.
- Preserve original exercises, assignment files, and outputs unless a task explicitly requests their replacement.
- Make additions easy to navigate and independently runnable.
- Explain prerequisites and expected output.
- Use synthetic data and test accounts.
- Attribute third-party content accurately and respect license terms.
- Prefer focused changes by topic.

## Adding a new learning resource

1. Choose the closest existing topic directory.
2. Use a descriptive filename and preserve the neighboring lesson structure.
3. Add a short topic README or index link where useful.
4. State the objective, prerequisites, concepts, run command, and expected result.
5. Include safe sample input/output.
6. Add a test or validation instruction.
7. Review for secrets, personal data, copyrighted material, and destructive commands.
8. Update the learning path and documentation index.

## Validation commands

Python: `python -m py_compile path/to/example.py`

Shell: `bash -n path/to/example.sh`

JSON: `python -m json.tool path/to/data.json > /dev/null`

SQL: review and execute only against a disposable database.

Selenium: use a permitted test target, safe test identity, compatible browser/driver, and explicit browser cleanup.

## Documentation quality standard

A good learning exercise explains its problem, concepts, runtime/package/browser/database prerequisites, exact working directory and command, expected output, common mistakes, cleanup, and next lesson.

Keep unrelated file renames, formatting, and data cleanup out of a documentation change. Binary replacement or removal needs a separate review because files may be course evidence or source material.
