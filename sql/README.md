
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
