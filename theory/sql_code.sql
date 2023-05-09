https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

A) What are the products ordered by customerId =4 (Around the horn)

	SELECT C.CustomerName, O.OrderID, O.CustomerID, OD.ProductID, P.ProductName FROM [Customers] C
	JOIN Orders O ON O.CustomerID= C.CustomerID
	JOIN OrderDetails OD ON OD.OrderID = O.OrderID
	JOIN Products P ON P.ProductID = OD.ProductID
	where C.CustomerID	= 4

B) Which customer has most orders?

	SELECT C.CustomerName, COUNT(O.OrderID) as cnt FROM [Customers] C
	JOIN Orders O ON O.CustomerID= C.CustomerID
	GROUP BY  C.CustomerID
	ORDER BY cnt DESC LIMIT 1

C) What customers have not placed an order?

	SELECT  C.CustomerName FROM [Customers] C
	LEFT JOIN Orders O ON O.CustomerID= C.CustomerID
	WHERE O.CustomerID is NULL
	ORDER BY C.CustomerName ASC

newscorp
--------

1) Given the following table structure and records therein, write a query which selects userId and average minutes for each user who has more than one activity record:

	CREATE TABLE activity (
	  id INTEGER NOT NULL PRIMARY KEY,
	  userId INTEGER NOT NULL,
	  minutes DECIMAL NOT NULL
	);

	INSERT INTO activity(id, userId, minutes) VALUES(1, 1, 11);
	INSERT INTO activity(id, userId, minutes) VALUES(2, 2, 19);
	INSERT INTO activity(id, userId, minutes) VALUES(3, 1, 17);


	Please use http://sqlite.online/ for your test environment and paste the final query below:

2) Given the following table structure and records therein, write a query which selects names of users who are not managers:

	CREATE TABLE users (
	  id INTEGER NOT NULL PRIMARY KEY,
	  managerId INTEGER REFERENCES users(id),
	  name VARCHAR(50) NOT NULL
	);

	INSERT INTO users(id, managerId, name) VALUES(1, NULL, 'Moe');
	INSERT INTO users(id, managerId, name) VALUES(2, 1, 'Tori');


	Please use http://sqlite.online/ for your test environment and paste the final query below:



3) BONUS: Given the following table structure and records therein,
   write a query which selects names of people who have a grade that is more
   than 3.5 and have taken all of the classes offered - without use of keyword ‘join’

DROP TABLE IF EXISTS `courses`;
CREATE TABLE courses (
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);
DROP TABLE IF EXISTS `people`;
CREATE TABLE people (
  id INTEGER NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);
DROP TABLE IF EXISTS `grades`;
CREATE TABLE grades (
  pid INTEGER REFERENCES people(id),
  cid INTEGER REFERENCES courses(id),
  grade DECIMAL NOT NULL
);

-- We've got 3 classes
INSERT INTO courses(id, name) VALUES(1, 'Biology');
INSERT INTO courses(id, name) VALUES(2, 'Python');
INSERT INTO courses(id, name) VALUES(3, 'Math');

-- We've got 4 people
INSERT INTO people(id, name) VALUES(1, 'Victor');
INSERT INTO people(id, name) VALUES(2, 'Raz');
INSERT INTO people(id, name) VALUES(3, 'Mr. Miyagi');
INSERT INTO people(id, name) VALUES(4, 'Karate Kid');

-- Victor took all 3 classes and got 100% on all!
INSERT INTO grades(pid, cid, grade) VALUES(1, 1, 100.0);
INSERT INTO grades(pid, cid, grade) VALUES(1, 2, 100.0);
INSERT INTO grades(pid, cid, grade) VALUES(1, 3, 100.0);

-- Raz took all 3 classes and got 100% on all!
INSERT INTO grades(pid, cid, grade) VALUES(2, 1, 100.0);
INSERT INTO grades(pid, cid, grade) VALUES(2, 2, 100.0);
INSERT INTO grades(pid, cid, grade) VALUES(2, 3, 100.0);

-- Mr. Miyagi tried taking all 3 classes but failed Biology with 1.0% grade!
INSERT INTO grades(pid, cid, grade) VALUES(3, 1, 1.0);
INSERT INTO grades(pid, cid, grade) VALUES(3, 2, 100.0);
INSERT INTO grades(pid, cid, grade) VALUES(3, 3, 100.0);

-- Karate Kid just did not have enough ambition and only took Python and Math, but he did get 100% on both!
INSERT INTO grades(pid, cid, grade) VALUES(4, 2, 100.0);
INSERT INTO grades(pid, cid, grade) VALUES(4, 3, 100.0);

Please use http://sqlite.online/ for your test environment and paste the final query below:

1)
select * from (select userid, count(id) as cnt, sum(minutes) from activity
group by userId) res where res.cnt > 1

2)
select DISTINCT name from users where managerid is not NULL

3) - a) sets are mutable
     e) A given element can’t appear in a set more than once.

4) Which of the following in Python define the set {'a', 'b', 'c'}:
    all true except last option

5)
	select DISTINCT p.name from grades g, people p, courses c
	where grade > 3.5 AND g.pid = p.id  AND g.cid = c.id


============================
CREATE TABLE Employees (
Name varchar(255),
Salary int
);

insert into Employees
(Name,Salary)
values
('Joseph',100),
('Ananth',1000),
('Ram',200),
('Thilak',300)


================================================================================================
SELECT *
FROM(
  SELECT MAX(NoOfM) AS MostMeetingsHappened
  FROM(
    select pe1.first_name || ' ' || pe1.last_name as first_person,
           pe2.first_name || ' ' || pe2.last_name as second_person,
          COUNT(1) AS NoOfM
    from participant pa1
    join participant pa2
      on  pa2.meeting_id = pa1.meeting_id
      and pa2.person_id > pa1.person_id
    join person pe1
      on pe1.person_id = pa1.person_id
    join person pe2
      on pe2.person_id = pa2.person_id
    group by (pe1.first_name || ' ' || pe1.last_name),
             (pe2.first_name || ' ' || pe2.last_name)
   ) A
)H
JOIN
 (
 select pe1.first_name || ' ' || pe1.last_name as first_person,
       pe2.first_name || ' ' || pe2.last_name as second_person,
      COUNT(1) AS NoOfM
from participant pa1
join participant pa2
  on  pa2.meeting_id = pa1.meeting_id
  and pa2.person_id > pa1.person_id
join person pe1
  on pe1.person_id = pa1.person_id
join person pe2
  on pe2.person_id = pa2.person_id
group by (pe1.first_name || ' ' || pe1.last_name),
         (pe2.first_name || ' ' || pe2.last_name)
 ) T
 ON H.MostMeetingsHappened = T.NoOfM
JOIN participant P
  ON P.person_id = t.first_person AND P.person_id = T.second_person
 JOIN meeting M
 ON P.meeting_id = M.meeting_id

================================================================================================
Order and Product tables
	Order - order_date, order_id, product_id, customer_id, price
	Product - product_id, product_name

Q) select the products those are not part of any order in the last 30 days

	select  distinct  p.product_name from product p
	JOIN  Order o  on p.product_id = o.product_id AND o.order_date < DATE(SUB(NOW(), INTERVAL 30 DAY ))
	WHere o.order_id is NULL

Q) select products ordered by same customer more than once in the last 30 days

	select o.customer_id, GROUP_CONTACT(Distinct p.product_name) from product p
	JOIN Order o ON p.product_id = o.product_id AND o.order_date < DATE(SUB(NOW(), INTERVAL 30 DAY ))
	GROUP BY o.cutomer_id HAVING  Count(p.product_name) > 1
	ORDER BY o.customer_id

================================================================================================
  prfid, dptid, sal
  1

  select  dptid,  max(sal) from mytable group by dptid order by depid

  select dptid, prfid, rank() over ( partition by deptid order by sal) from mytable
===================================================================================================
SELECT
	p.id, p.title, coalsce(SUM(r.number_of_tickets), 0)as reserved_tickets
FROM plays p
LEFT JOIN reservations r ON p.id = r.play_id
GROUP BY p.id, p.title
ORDER BY reserved_tickets

===================================================================================================
sql for order in ascending order by score column, but nulls should come first

	ORDER BY score IS NULL DESC, score ASC
===================================================================================================
sql for nth highest salary from employees table

	SELECT FIRST_NAME , SALARY FROM
	(SELECT FIRST_NAME, SALARY, DENSE_RANK() OVER (ORDER BY SALARY DESC) AS SALARY_RANK
	FROM EMPLOYEES)
	WHERE SALARY_RANK = n;

	or

	SELECT MAX(SALARY) 'SECOND_MAX' FROM EMPLOYEES
	WHERE SALARY <> (SELECT MAX(SALARY) FROM EMPLOYEES);

	OR

	SELECT FIRST_NAME, SALARY FROM EMPLOYEES
	WHERE SALARY = (SELECT DISTINCT SALARY FROM EMPLOYEES ORDER BY SALARY LIMIT 1 OFFSET 1)
===================================================================================================
HackerRank: Value of Properties Owned

	SELECT H.BUYER_ID, SUM(P.PRICE) AS TOTAL_WORTH FROM HOUSE H
	JOIN PRICE P USING(HOUSE_ID)
	GROUP BY H.BUYER_ID HAVING SUM(P.PRICE) > 100 AND COUNT(H.BUYER_ID) > 1;
===================================================================================================
SELECT name, COUNT(sal) FROM users
GROUP BY email
HAVING COUNT(email) > 1

Select distinct salary from employee ORDER BY salary DESC limit 1 offset 1

Select * from table where id in (Select id from table t1 GROUP BY id HAVING COUNT(Id) > 1)

SELECT * FROM my_table WHERE created_at > DATE_SUB(NOW(), INTERVAL 1 DAY)
===================================================================================================
Q) Display all the column values in a single row separated by comma in MySQL?
Ans) select group_concat(Id)  from tableName GROUP BY tableName;

Q) Delete all Duplicate Rows except for One in MySQL?
Ans) DELETE n1 FROM names n1, names n2 WHERE n1.id > n2.id AND n1.name = n2.name

	When full row duplicate,
		add an id column virtually and delete all , but first in sequence
=====================================================================================================
Q) delete duplicate records
Ans)
	DELETE c1 FROM contacts c1
	INNER JOIN contacts c2
	WHERE
		c1.id > c2.id AND
		c1.email = c2.email;
=====================================================================================================
Q) Per total number of hours, by employee
Employees
    Employees.id
    Employees.Name

TimeSheet
    TimeSheet.Id
    Employee_id
    Hours
Ans)
	Select e.name, SUM(t.Hours) as total_hours
	from employees e
	JOIN TimeSheet t on t.Employee_id = e.id
	GROUP BY e.name
	ORDER BY total_hours DESC
=====================================================================================================
Q) Table contains ages of people. Generate SQL query to classify less than 13 as child, 13 till 20 as teens, 20 till 60 as adult
   and greater than 60 as OLD.

Ans)

	SELECT
		age,
		CASE
			WHEN age < 13 THEN 'Child'
			WHEN age >= 13 AND age < 20 THEN 'Teen'
			WHEN age >= 20 AND age < 60 THEN 'Adult'
			ELSE 'Old'
		END AS age_category
	FROM people;
=====================================================================================================
Q) if there are two tables, write query to get the records not present in tableA but present in tableB,
   and vice-versa. Also, combine all those records

   Table1 has two columns: c1, c2
   Table2 has two columns: c1, c2

Ans)

	SELECT *
	FROM table1
	LEFT JOIN table2 ON table1.column1 = table2.column1
	WHERE table2.column1 IS NULL;

	UNION

	SELECT *
	FROM table2
	LEFT JOIN table1 ON table1.column1 = table2.column1
	WHERE table1.column1 IS NULL;

	Union removes duplicates, where Union All wont.
=====================================================================================================
Q) Find me all the books which are available in more than 50% of the languages?
	books
		- bookname char, lang char
Ans)
	select bookname
	FROM books
	GROUP BY bookname
	HAVING (COUNT(DISTINCT lang) / COUNT(*))  > 0.5;
=====================================================================================================
﻿1. Employee History Query
Two tables are provided that contains people's names, their current and previous employers. First determine the company or companies that have the highest number of people that were previously employed there. For all of the people who work at one of those companies currently, list the person's name and the name of their previous employer. Results should be in the form people.NAME companies.NAME. The order of the results is not important.
▼Schema
There are 2 tables: PEOPLE, COMPANIES.
PEOPLE table
	ID 				STRING ID of the person.
	NAME 			STRING Name of the person.
	DOJ 			DATE Date of Joining the current company.
	PREV_COMPANY_ID STRING ID of the previous company.
	CURR_COMPANY_ID STRING ID of the current company.

COMPANIES table
	ID STRING ID of the company.
	NAME STRING Name of the company.

Ans)

	SELECT p.NAME, c.NAME
	FROM PEOPLE p
	JOIN COMPANIES c ON p.PREV_COMPANY_ID = c.ID
	WHERE p.CURR_COMPANY_ID IN (
	  SELECT c2.ID
	  FROM COMPANIES c2
	  WHERE c2.NAME = (SELECT c3.NAME FROM COMPANIES c3
					   JOIN PEOPLE p2 ON c3.ID = p2.PREV_COMPANY_ID
					   WHERE c3.NAME = (SELECT c4.NAME
										FROM COMPANIES c4
										JOIN PEOPLE p3 ON c4.ID = p3.PREV_COMPANY_ID
										GROUP BY c4.NAME
										ORDER BY COUNT(*) DESC
										LIMIT 1)
					   GROUP BY c3.NAME
					   ORDER BY COUNT(*) DESC
					   LIMIT 1)
	)
=====================================================================================================
2. Orders Query

Company X has a record of its customers and their orders.
Find the customer(s) with the highest order price for orders placed within
10 years of the first order (earliest order_date) in the database.
Print the customer name and order price.
If multiple records are returned, they can be in any order.

▼Schema
There are 2 tables: CUSTOMERS, ORDERS.

CUSTOMERS
	ID		STRING ID of the customer. This is the primary key.
	NAME 	STRING Name of the customer.
	ORDER_ID STRING ID of the customer's order.

ORDERS
	ID			STRING ID of the order.
	PRICE		INTEGER Price of the order.
	ORDER_DATE	DATE Date of the order.
Ans)
	SELECT c.NAME, o.PRICE
	FROM CUSTOMERS c
	JOIN ORDERS o ON c.ORDER_ID = o.ID
	WHERE o.ORDER_DATE >= (
	  SELECT MIN(ORDER_DATE)
	  FROM ORDERS
	) AND o.ORDER_DATE <= DATE_ADD((SELECT MIN(ORDER_DATE) FROM ORDERS), INTERVAL 10 YEAR)
	ORDER BY o.PRICE DESC
	LIMIT 1;
=====================================================================================================
Q) What will be the output of when we perform inner join, left outer join, right outer join, full outer join and cross join ob below given tables?
Table1
	Col_1
	1
	1
	1

Table2
	Col_2
	1
	1
	1
Ans)

Inner Join, Left Outer Join, Right Outer Join will give 3 row

	Col_1	Col_2
	1		1
	1		1
	1		1

Full Outer Join: 3*3 = 9 rows
	A full outer join returns all the records from both tables and matching records based on the join condition. Since both tables have the same value in their respective columns, the join will result in all 9 possible combinations of rows from both tables.

	Col_1	Col_2
	1		1
	1		1
	1		1
	1		1
	1		1
	1		1
	1		1
	1		1
	1		1

Cross Join:
	A cross join returns all possible combinations of rows between two tables. Since both tables have only one distinct value in their respective columns, the cross join will result in only one row.

	Col_1	Col_2
	1		1
=====================================================================================================
