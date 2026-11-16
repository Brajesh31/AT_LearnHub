# 🚀 Installation and local environment

## General requirements

There is no single runtime for the entire repository. Install tools based on the lesson or assignment being used.

| Track | Tooling |
|---|---|
| Python | Python 3, pip, virtual environment |
| Linux | Linux shell, VM, WSL or container |
| Git | Git command-line client |
| SQL | MySQL-compatible server/client for supplied scripts |
| Selenium | Python, Selenium package, compatible browser and driver |
| Office reference files | Compatible ODT/DOCX/ODS viewer |
| Media | Compatible media player |

## Python environment

```bash
python --version
python -m venv .venv
```

Activation:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Install dependencies only when the chosen exercise needs them. Check local requirement files first. Avoid global package installation.

## Selenium environment

Install Selenium in a dedicated virtual environment. Use a browser and driver that are compatible with each other. Prefer the browser's managed driver integration where supported instead of relying on committed executables. See [Selenium guidelines](selenium-guidelines.md).

## SQL environment

Use a local disposable database instance. Read SQL files before execution, especially files containing `DROP DATABASE`, `DROP TABLE`, or destructive `DELETE` statements. See [SQL safety](sql-safety.md).

## Linux environment

Use a disposable VM/container or WSL environment. Do not run unfamiliar commands as root. Review filesystem paths, pipes, redirections, permissions, and destructive flags.

## Verify a Python example

```bash
python -m py_compile "Python/Day-1/Python-1/Variables.py"
python "Python/Day-1/Python-1/Variables.py"
```

Compile checks syntax only. Running the script verifies only that specific example in the current environment.
