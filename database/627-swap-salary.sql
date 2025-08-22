# Write your MySQL query statement below
# First solution
UPDATE Salary
SET
    Sex
    = CASE
        WHEN Sex = 'f' THEN 'm'
        WHEN Sex = 'm' THEN 'f'
    END;

-- # Second solution
-- UPDATE Salary
-- SET Sex = IF(Sex = 'm', 'f', 'm');
