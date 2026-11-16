# 🔀 Git learning path

## Goal
Understand local version control and collaborative change history.

## Suggested sequence
1. Understand working tree, staging area, and repository history.
2. Practice `git status`, `git add`, and `git commit`.
3. Create and switch branches.
4. Inspect differences and commit history.
5. Practice merging in a disposable repository.
6. Learn remote operations, pull requests, and conflict resolution.

## Safe practice
```bash
mkdir git-practice
cd git-practice
git init
printf '# Practice\n' > README.md
git status
git add README.md
git commit -m "docs: add practice readme"
git log --oneline
```

This guide provides a practical path; consult the original Git course note files for the archived lesson content.
