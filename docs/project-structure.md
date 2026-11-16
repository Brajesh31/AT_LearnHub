# 🗂️ Project structure and content inventory

## Top-level catalog

| Path | Content class | Notes |
|---|---|---|
| `git/` | Git notes and reference documents | Learning material; no Git application |
| `Linux/` | Linux notes, shell practice, archives and text files | Use Linux environment for command semantics |
| `Python/` | Python lessons, practice scripts, assignments, transcripts and media | Organized in day/lesson folders |
| `Python_Web_Scraping/` | Python OOP and scraping examples | External-site behavior may change |
| `QA/` | QA exercises and assignment artifacts | Review assignment-specific context |
| `Selenium/` | Selenium exercises, assignment code, drivers, data and outputs | Drivers are platform/version-specific |
| `sql/` | SQL course documents and scripts | Includes scripts that create/drop databases |
| `docs/` | Maintained repository documentation | Navigation and contribution material |

## File-type guide

| Extension | Typical role | Recommended handling |
|---|---|---|
| `.py` | Python source | Compile/check individually |
| `.sh` | Shell scripts | Review commands, run `bash -n` |
| `.sql` | Database lessons/scripts | Review all DDL/DML before execution |
| `.odt`, `.docx`, `.ods` | Course/assignment documents | Use office suite; retain as reference |
| `.csv` | Tabular input | Inspect headers, provenance, privacy |
| `.json` | Data and generated output | Validate syntax and document schema |
| `.txt` | Notes, input, transcript | Identify whether source or generated |
| `.mp4` | Learning media | Check rights and context |
| `.tar` | Archive | List contents before extraction |
| Browser drivers | Executable binaries | Verify source and exact browser compatibility |

## Important historical artifacts

The repository includes large office documents, video, SQL data files, archives, browser drivers, and some OS/editor metadata. They were preserved. Do not remove them as part of unrelated documentation improvements.

## Naming and path conventions

Existing paths may contain spaces, mixed case, and historical spelling mistakes. Always quote paths in shell commands:

```bash
python "Python/Day-1/Python-1/Variables.py"
```

Future additions should use descriptive names, consistent capitalization, and avoid spaces where practical. Renaming existing material requires link/reference updates and should be a separate change.
