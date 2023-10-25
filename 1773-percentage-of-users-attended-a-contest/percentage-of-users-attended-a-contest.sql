SELECT r.contest_id, ROUND(COUNT(r.user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM users), 2) percentage
FROM users u
INNER JOIN register r
ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id