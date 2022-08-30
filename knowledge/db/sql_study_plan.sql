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

-- 8. 1667. Fix Names in a Table

-- RIGHT(name, k) : Last k letters in string,
-- LEFT(name, k) : First k letters in string,
-- SUBSTRING(name, 2) : subString after k
-- UPPER, LOWER, CONCAT : String operations
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name FROM Users ORDER BY user_id ASC;

-- 9. 1484. Group Sold Products By The Date

-- PRIMARY KEY: Only one per table. UNIQUE values to identify, not NULL.
-- GROUP_CONCAT: combine multiple rows as string. 
    -- Distinct: It eliminates the repetition of values from result.
    -- Order By: It sort the values of group in specific order and then concatenate them.
    -- Separator: By default, the values of group are separated by (, ) operator. In order to
    -- Syntax: GROUP_CONCAT ( [DISTINCT] col_name1 [ORDER BY clause]  [SEPARATOR str_val] ) 

-- SQL aggregate functions:　COUNT(), MAX(), MIN(), SUM(), AVG()
    -- Syntsax: SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country;
    -- GROUP BY: Obvious

-- 10. 1527. Patients With a Condition

-- WHERE LIKE operator
    -- The percent sign (%) represents zero, one, or multiple characters
    -- The underscore sign (_) represents one, single character
    -- WHERE CustomerName LIKE 'a%'	   Finds any values that start with "a"
    -- WHERE CustomerName LIKE '%a'	   Finds any values that end with "a"
    -- WHERE CustomerName LIKE '%or%'  Finds any values that have "or" in any position
    -- WHERE CustomerName LIKE '_r%'   Finds any values that have "r" in the second position
    -- WHERE CustomerName LIKE 'a_%'   Finds any values that start with "a" and are at least 2 characters in length
    -- WHERE CustomerName LIKE 'a__%'  Finds any values that start with "a" and are at least 3 characters in length
    -- WHERE CustomerName LIKE 'a%o'   Finds any values that start with "a" and ends with "o"

-- MySQL REGEXP performs a pattern match of a string expression against a pattern.
SELECT * FROM Patients WHERE conditions like '% DIAB1%' OR conditions like 'DIAB1%'; 
SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'

-- 11. 1965. Employees With Missing Information
(SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION  -- To join 2 tables 
SELECT employee_id FROM Salaries WHERE employee_id NOT IN (SELECT employee_id FROM Employees))
ORDER BY employee_id -- Add logic on unioned table use () on union.

-- 12. 1795. Rearrange Products Table
(SELECT product_id, "store1" as store, store1 as price FROM Products WHERE store1 IS NOT NULL
UNION
SELECT product_id, "store2" as store, store2 as price FROM Products WHERE store2 IS NOT NULL
UNION
SELECT product_id, "store3" as store, store3 as price FROM Products WHERE store3 IS NOT NULL);

-- 13. 608. Tree Node
SELECT id, 
CASE 
    WHEN p_id IS NULL THEN "Root"
    WHEN id IN(SELECT p_id FROM Tree) THEN "Inner"
    ELSE "Leaf"
END AS TYPE
FROM Tree;

-- 14. 176. Second Highest Salary
select max(salary) as SecondHighestSalary 
from Employee
where salary <(select max(salary) from employee);

-- 15. 175. Combine Two Tables
SELECT p.firstName, p.lastName, a.city, a.state FROM Person p LEFT JOIN Address a ON p.personId = a.personId;

-- 16. 1581. Customer Who Visited but Did Not Make Any Transactions
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
FROM Visits v LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id 
WHERE v.visit_id NOT IN (SELECT visit_id FROM Transactions) 
GROUP BY v.customer_id;

-- 17. 1148. Article Views I
SELECT DISTINCT author_id AS id -- Distinct will give you only unique IDs
FROM Views WHERE author_id = viewer_id ORDER BY author_id ASC;

-- 18. 197. Rising Temperature
SELECT w1.id FROM Weather w1 LEFT JOIN Weather w2 
    ON w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY) 
    WHERE w1.temperature > w2.temperature

-- 19. 607. Sales Person
SELECT s.name FROM salesperson s
WHERE s.sales_id NOT IN (SELECT o.sales_id
    FROM orders o LEFT JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'RED');

-- 20. 1141. User Activity for the Past 30 Days I
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users FROM Activity -- Distinct is more useful than I thought
WHERE activity_date > DATE_SUB(CAST('2019-07-27' AS DATE), INTERVAL 30 DAY)  -- Date comparison & CAST to date
AND activity_date <= CAST('2019-07-27' AS DATE) GROUP BY activity_date;

-- 21. 1693. Daily Leads and Partners
SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS unique_leads, COUNT(DISTINCT partner_id) AS unique_partners 
FROM DailySales GROUP BY date_id, make_name; -- We can group by multiple columns and count multiple columns

-- 22. 1729. Find Followers Count
SELECT user_id, COUNT(DISTINCT follower_id) AS followers_count FROM Followers GROUP BY user_id;

-- 23. 586. Customer Placing the Largest Number of Orders
SELECT customer_number FROM Orders GROUP BY customer_number -- Can order by COUNT
ORDER BY COUNT(order_number) DESC LIMIT 1; -- GET MAX By sort and limit 1

HAVING COUNT(*)>3; -- The HAVING clause is used instead of WHERE clause with SQL COUNT() function.

-- 24. 511. Game Play Analysis I
SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id; -- Can get min date by MIN, GROUP BY can be used with MIN
-- GROUP BY statement is often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()

-- 25. 1890. The Latest Login in 2020

WHERE YEAR(time_stamp) = 2020
-- TIMESTAMP is YYYY-MM-DD HH:MM:SS which is fixed at 19 characters.
-- YEAR(time_stamp) = 2020 

SELECT user_id, MAX(time_stamp) AS last_stamp FROM Logins WHERE time_stamp >= '2020-01-01 00:00:00' AND time_stamp < '2021-01-01 00:00:00' GROUP BY user_id;

-- 26. 1741. Find Total Time Spent by Each Employee
SELECT event_day AS day, emp_id, SUM(out_time) - SUM(in_time) AS total_time FROM Employees GROUP BY event_day, emp_id; -- We can subtract

-- 27. 1393. Capital Gain/Loss
SELECT x.stock_name, sell - buy as capital_gain_loss FROM 
(SELECT stock_name, SUM(PRICE) as Buy FROM Stocks WHERE operation = "Buy" GROUP BY 1 ) x  -- GROUP BY 1 : GROUP BY first column 
JOIN
(SELECT stock_name, SUM(PRICE) as Sell FROM Stocks WHERE operation = "Sell" GROUP BY 1 ) y
ON x.stock_name = y.stock_name;

-- 28. 1407. Top Travellers
SELECT name, IFNULL(distance, 0) as travelled_distance  -- IFNULL(distance, 0)
FROM Users LEFT JOIN (SELECT user_id, SUM(distance) as distance FROM Rides GROUP BY 1) x 
ON Users.id = x.user_id ORDER BY travelled_distance DESC, name ASC; -- You can double sort