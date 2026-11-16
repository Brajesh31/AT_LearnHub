# 🗄️ SQL learning path

## Goal
Learn relational database structure and SQL through the course scripts and supporting documents in `sql/`.

## Datasets visible in the archive
The scripts create examples including `sql_invoicing`, `sql_store`, `sql_hr`, and `sql_inventory`.

## Suggested sequence
1. Read database creation and table-definition statements.
2. Understand primary keys, foreign keys, data types, and constraints.
3. Practice SELECT, WHERE, ORDER BY, LIMIT, and expressions.
4. Practice joins across related tables.
5. Practice GROUP BY, HAVING, aggregates, and subqueries.
6. Review inserts, updates, deletes, and transactions.

## Safe execution
The scripts are not production migrations. Some drop and recreate schemas. Use a disposable local MySQL database, inspect the whole script first, and back up anything that matters.

See [SQL safety](../sql-safety.md) before executing a file.
