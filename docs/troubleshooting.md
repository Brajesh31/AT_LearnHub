# 🧰 Troubleshooting guide

## Python

**ModuleNotFoundError:** Activate the intended virtual environment and install dependencies required by that specific exercise.

**Wrong Python version:** Check `python --version` and use the intended interpreter.

**File not found:** Run from the expected directory or resolve paths relative to the script. Quote paths containing spaces.

## Linux and shell

**Permission denied:** Check the executable bit, ownership, and whether the script needs a shell interpreter. Avoid using sudo as a first fix.

**Command not found:** Confirm the command exists in the current distribution and shell.

## SQL

**Cannot drop/create database:** Check the target schema and permissions. Never point practice scripts at production.

**Foreign-key error:** Inspect parent/child creation order and referenced IDs.

**Character set/collation error:** The script may assume a specific MySQL version or collation.

## Selenium

**Session not created:** Browser and driver versions may be incompatible.

**Driver executable not found:** Many old scripts contain hard-coded absolute paths. Replace with a local, configurable path or managed driver after confirming the intended environment.

**Element not found:** Page structure, selectors, timing, or consent/login state may have changed. Use explicit waits and a permitted test target.

**Browser hangs:** Ensure `quit()` runs in a `finally` block and inspect active browser processes.

**CAPTCHA/access denied:** Stop. Do not attempt to bypass controls. Use an authorized test environment.

## Office documents and archives

Use a compatible office suite. List archive contents before extracting; extract into a temporary directory rather than over the repository.
