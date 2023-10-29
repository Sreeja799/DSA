SELECT SUBSTR(trans_date, 1, 7) month, country, COUNT(id) trans_count, SUM(IF (state = 'approved', 1, 0)) approved_count, SUM(amount) trans_total_amount, SUM(IF (state = 'approved', amount, 0)) approved_total_amount 
FROM transactions
GROUP BY month, country