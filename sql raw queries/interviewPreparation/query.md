# How to get 3rd highest salary from the employee table

SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

`SELECT DISTINCT salary:` This returns all unique salary values from the employee table.

`ORDER BY salary DESC:` This sorts the salary values in descending order, so the highest salary comes first.

`LIMIT 1 OFFSET 2:` This retrieves only one row (1) starting from the third row (OFFSET 2). Since the salary values are sorted in descending order, the third highest salary will be the value returned.

# print all students where the marks are in between 10 and 50?

SELECT * FROM student
WHERE roll BETWEEN 10 AND 50;


stuff function, sub query, joins


SELECT DISTINCT salary
FROM employee
ORDER BY DESC
LIMIT 1 OFFSET 3;



