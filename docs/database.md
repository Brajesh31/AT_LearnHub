# 🗄️ Data and database inventory

The `sql/` directory contains course documents and MySQL-style SQL scripts. Other topics contain CSV/JSON datasets and generated outputs. No shared production database is configured.

## SQL course datasets

The visible SQL scripts include schemas such as `sql_invoicing`, `sql_store`, `sql_hr`, and `sql_inventory`. Scripts create tables and seed sample records. They are educational fixtures, not production database migrations.

## Data handling checklist

Before using a data file:
1. Identify the source and purpose.
2. Inspect column names and a small sample.
3. Check for names, contact information, credentials, or other personal data.
4. Confirm redistribution rights.
5. Document encoding, delimiter, date format, and schema.
6. Avoid committing private or licensed datasets without approval.

## SQL schema exploration

Read CREATE TABLE statements to understand primary keys, foreign keys and referential actions, data types and constraints, indexes, insert order, and dependencies.

## Generated files

JSON output, transcripts, logs, and temporary files should be distinguished from curated source fixtures. Avoid committing machine-specific paths or personal data in generated outputs.
