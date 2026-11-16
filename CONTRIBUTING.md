# 🤝 Contributing to AT LearnHub

AT LearnHub is a learning archive. Contributions should make individual learning resources easier to discover, understand, execute, and verify.

## Choose the right location
Use the closest existing topic folder. Add a new top-level topic only when it represents a distinct learning track. Update the topic catalog and learning path when adding substantial content.

## Lesson and exercise standard
Every new runnable example should include:
- Title and learning objective.
- Prerequisites and optional dependencies.
- Concepts demonstrated.
- Exact execution command and working directory.
- Expected output or observable behavior.
- Common mistakes and safe cleanup.
- Next exercise or reference.

## Safety requirements
- Use synthetic sample data.
- Remove credentials, browser cookies, profiles, tokens, and personal information.
- Review SQL destructive statements before inclusion.
- Use authorized Selenium and scraping targets only.
- Do not include CAPTCHA bypass, access-control evasion, or rate-limit circumvention.
- Verify licenses for copied documents, media, datasets, binaries, and packages.

## Validation
```bash
python -m py_compile path/to/example.py
bash -n path/to/example.sh
python -m json.tool path/to/example.json > /dev/null
```

Run SQL in a disposable database. Verify browser/driver compatibility for Selenium changes.

## Pull request checklist
- [ ] Topic folder and filename are appropriate.
- [ ] Learning objective and prerequisites are documented.
- [ ] New code is scoped and understandable.
- [ ] Validation result is included.
- [ ] No secrets or private data included.
- [ ] External resources and licensing reviewed.
- [ ] README/index/learning path updated.
- [ ] Existing course artifacts preserved.

## Review approach
A contribution should help a learner understand a concept, not merely add file count. Empty placeholders, copied boilerplate, and unverified screenshots are not useful contributions.
