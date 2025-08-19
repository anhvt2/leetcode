SELECT DISTINCT c1.seat_id
FROM Cinema AS c1
-- INNER JOIN cinema AS c2
JOIN Cinema as c2
    ON abs(c1.seat_id - c2.seat_id) = 1 -- Expand to (n x n) rows table if matched
WHERE c1.free = 1 AND c2.free = 1
ORDER BY c1.seat_id;
