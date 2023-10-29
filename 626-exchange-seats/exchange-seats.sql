SELECT s2.id, s1.student
FROM seat s1, seat s2
WHERE s1.id = s2.id-1
AND s1.id % 2 != 0

UNION

SELECT s2.id, s1.student
FROM seat s1, seat s2
WHERE s1.id = s2.id+1
AND s1.id % 2 = 0

UNION

SELECT id, student
FROM seat 
WHERE id % 2 = 1 AND id = (SELECT MAX(id) FROM seat)

ORDER BY id