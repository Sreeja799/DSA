SELECT DISTINCT p1.product_id, IFNULL(p2.new_price, 10) price
FROM products p1 
LEFT JOIN 


(SELECT * 
FROM products 
WHERE (product_id, change_date) IN 
(SELECT product_id, MAX(change_date) FROM products WHERE change_date <= '2019-08-16' GROUP BY product_id)) p2


ON p1.product_id = p2.product_id 
WHERE p2.change_date IS NULL OR p1.change_date = p2.change_date
ORDER BY p1.product_id;