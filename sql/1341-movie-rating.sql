# Write your MySQL query statement below
(
    SELECT u.name AS results
    FROM movierating AS mr
    INNER JOIN users AS u ON mr.user_id = u.user_id
    GROUP BY u.user_id, u.name
    ORDER BY count(*) DESC, u.name
    LIMIT 1
)

UNION ALL

(
    SELECT m.title AS results
    FROM movierating AS mr
    INNER JOIN movies AS m ON mr.movie_id = m.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id, m.title
    ORDER BY avg(mr.rating) DESC, m.title
    LIMIT 1
);
