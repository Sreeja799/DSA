SELECT q.query_name, ROUND(AVG(rating / position), 2) quality, ROUND((SELECT COUNT(query_name) FROM queries WHERE rating < 3 AND q.query_name = query_name) * 100 / COUNT(q.query_name), 2) poor_query_percentage
FROM queries q
GROUP BY q.query_name;