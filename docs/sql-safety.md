# ⚠️ SQL execution safety

Some SQL files in this repository create, drop, and seed databases. They are educational materials, not production migration scripts.

## Before running any SQL file
1. Open and inspect the complete script.
2. Search for `DROP`, `TRUNCATE`, `DELETE`, `ALTER`, and `CREATE DATABASE`.
3. Confirm the target server and database.
4. Use a disposable local database instance.
5. Take a backup if any existing data must be preserved.
6. Confirm the SQL engine/version and collation compatibility.
7. Run and inspect errors before continuing to later exercises.

## Destructive statement example
```sql
DROP DATABASE IF EXISTS sql_hr;
CREATE DATABASE sql_hr;
USE sql_hr;
```

This will remove an existing database named `sql_hr`. Do not run it on production or a database containing important work.

## Suggested safe workflow
```text
Review SQL → Create disposable instance → Create test schema
     ↓
Run script → Validate tables and rows → Record result
     ↓
Drop disposable instance when finished
```

Do not add credentials to SQL files or commit production dumps.
