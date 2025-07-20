
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
templater = jinja
sql_file_exts = .sql,.sql.j2,.dml,.ddl

[sqlfluff:indentation]
indented_joins = False
indented_using_on = True
template_blocks_indent = False

[sqlfluff:templater]
unwrap_wrapped_queries = True

[sqlfluff:templater:jinja]
apply_dbt_builtins = True

[sqlfluff:rules:capitalisation.keywords] #  # Enforces {upper, lower}case keywords.
capitalisation_policy = upper
```

How to use
```bash
sqlfluff fix 180-consecutive-numbers.sql --dialect mysql
```
