SELECT p.project_id, ROUND(AVG(e.experience_years), 2)average_years 
FROM project p
CROSS JOIN employee e 
ON p.employee_id = e.employee_id
GROUP BY p.project_id; 