SELECT IF (COUNT(num) = 1, num, null) num
FROM MyNumbers
GROUP BY num
ORDER BY num DESC
LIMIT 1