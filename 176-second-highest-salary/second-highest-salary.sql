SELECT MAX(salary) SecondHighestSalary 
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);