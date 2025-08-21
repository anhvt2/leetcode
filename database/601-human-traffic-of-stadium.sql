# Write your MySQL query statement below
-- The idea is to find rows where the current row and its two neighbors (forward or backward) also have people >= 100.
-- We use 3 blocks of logic to detect:
-- 1. current + next + next
-- 2. previous + current + next
-- 3. previous + previous + current
-- Each block flags all rows in any valid 3-row group.
-- We use UNION to combine all matching rows and ORDER BY id to match required output order.
SELECT
    id,
    visit_date,
    people
FROM (
    SELECT
        s1.id,
        s1.visit_date,
        s1.people,
        if(
            s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100, 1, 0
        ) AS is_valid
    FROM stadium AS s1
    LEFT JOIN stadium AS s2 ON s2.id = s1.id + 1
    LEFT JOIN stadium AS s3 ON s3.id = s1.id + 2 # or s2.id + 1
) AS temp1
WHERE is_valid = 1

UNION DISTINCT

SELECT
    id,
    visit_date,
    people
FROM (
    SELECT
        s1.id,
        s1.visit_date,
        s1.people,
        if(
            s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100, 1, 0
        ) AS is_valid
    FROM stadium AS s1
    LEFT JOIN stadium AS s2 ON s2.id = s1.id - 1
    LEFT JOIN stadium AS s3 ON s3.id = s1.id + 1
) AS temp2
WHERE is_valid = 1

UNION DISTINCT

SELECT
    id,
    visit_date,
    people
FROM (
    SELECT
        s1.id,
        s1.visit_date,
        s1.people,
        if(
            s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100, 1, 0
        ) AS is_valid
    FROM stadium AS s1
    LEFT JOIN stadium AS s2 ON s2.id = s1.id - 1
    LEFT JOIN stadium AS s3 ON s3.id = s1.id - 2
) AS temp3
WHERE is_valid = 1

ORDER BY id;
