SELECT
IF (id < (SELECT COUNT(*) FROM seat), IF(id % 2 = 0, id-1, id+1), IF(id % 2 = 0, id-1, id)) id, student
FROM seat
ORDER BY id