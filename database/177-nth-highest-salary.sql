CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET N 
  );
END

-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--   RETURN (
--     # Write your MySQL query statement below.
--     SELECT DISTINCT e1.salary
--     FROM Employee e1
--     WHERE N-1 = (
--         SELECT COUNT(DISTINCT e2.salary) 
--         FROM Employee e2
--         WHERE e1.salary < e2.salary
--     )
--   );
-- END;
