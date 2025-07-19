
```bash
sqlite3 test.db < 1757-create-product-db.sql
sqlite3 test.db
# SQL code then follow
```

```sql
.headers on
.mode column
SELECT name FROM sqlite_master WHERE type='table';
```

For auto-reformatting, use SQLFluff at [https://docs.sqlfluff.com/en/stable/index.html](https://docs.sqlfluff.com/en/stable/index.html)

Here is a template for `~/.sqlfluff`

```
[sqlfluff]
dialect = ansi  # Specifies the SQL dialect to use (e.g., ansi, postgres, bigquery).
max_line_length = 120 # Sets the maximum line length for formatting.

[sqlfluff:indentation]
tab_space_size = 2 # Sets the indentation to use 2 spaces.

[sqlfluff:rules:capitalisation.keywords] #  # Enforces {upper, lower}case keywords.
capitalisation_policy = upper
```

How to use
```bash
sqlfluff fix 180-consecutive-numbers.sql --dialect mysql
```
