SELECT query_name, 
ROUND(AVG(rating / position), 2) quality, 
ROUND(AVG(rating < 3) * 100, 2) poor_query_percentage
FROM queries 
GROUP BY query_name;