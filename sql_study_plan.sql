-- SQL Study Plan Exercises https://leetcode.com/study-plan/sql/?progress=j0h56js

-- 1. 595. Big Countries
SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000; -- OR operator and condition

-- 2. 1757. Recyclable and Low Fat Products
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y'; -- string equal operator

-- 3. 584. Find Customer Referee
SELECT name FROM Customer WHERE 2 != referee_id OR referee_id IS NULL; -- WHERE omits NULL, so, we need to add by IS NULL

-- 4. 183. Customers Who Never Order
SELECT name as Customers -- use as to give different column name
FROM Customers c LEFT JOIN Orders o  -- LEFT JOIN: all rows in LEFT TABLE
ON c.id = o.customerId -- LEFT JOIN uses ON not WHERE.
WHERE o.id IS NULL; 

-- 5. 1873. Calculate Special Bonus
SELECT employee_id,  
CASE WHEN employee_id % 2 = 1 -- Filter by even, odd
AND -- Double condition 
name NOT LIKE 'M%' THEN salary -- Filter by string start
    ELSE 0
END AS bonus FROM Employees -- case statement as new column
ORDER BY employee_id ASC; -- order by

-- 6. 627. Swap Salary
UPDATE Salary -- UPDATE table_name
SET sex = -- Conditional set
(CASE WHEN sex = 'm' THEN 'f' WHEN sex = 'f' THEN 'm' END); -- CASE WHEN THEN 

-- 7. 196. Delete Duplicate Emails
DELETE FROM Person WHERE id % 2 = 1; -- Simple delete syntax
DELETE t1 FROM Person t1 JOIN Person t2 WHERE t1.id > t2.id AND t1.email = t2.email; -- Delete Join operation