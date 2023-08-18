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

=====================================================================================
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

=====================================================================================
  prfid, dptid, sal
  1

  select  dptid,  max(sal) from mytable group by dptid order by depid

  select dptid, prfid, rank() over ( partition by deptid order by sal) from mytable
=====================================================================================
SELECT
	p.id, p.title, coalsce(SUM(r.number_of_tickets), 0)as reserved_tickets
FROM plays p
LEFT JOIN reservations r ON p.id = r.play_id
GROUP BY p.id, p.title
ORDER BY reserved_tickets

=====================================================================================
sql for order in ascending order by score column, but nulls should come first

	ORDER BY score IS NULL DESC, score ASC
=====================================================================================
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
=====================================================================================
HackerRank: Value of Properties Owned

	SELECT H.BUYER_ID, SUM(P.PRICE) AS TOTAL_WORTH FROM HOUSE H
	JOIN PRICE P USING(HOUSE_ID)
	GROUP BY H.BUYER_ID HAVING SUM(P.PRICE) > 100 AND COUNT(H.BUYER_ID) > 1;
=====================================================================================
SELECT name, COUNT(sal) FROM users
GROUP BY email
HAVING COUNT(email) > 1

Select distinct salary from employee ORDER BY salary DESC limit 1 offset 1

Select * from table where id in (Select id from table t1 GROUP BY id HAVING COUNT(Id) > 1)

SELECT * FROM my_table WHERE created_at > DATE_SUB(NOW(), INTERVAL 1 DAY)
=====================================================================================
Q) Display all the column values in a single row separated by comma in MySQL?
Ans) select group_concat(Id)  from tableName GROUP BY tableName;

Q) Delete all Duplicate Rows except for One in MySQL?
Ans) DELETE n1 FROM names n1, names n2 WHERE n1.id > n2.id AND n1.name = n2.name

	When full row duplicate,
		add an id column virtually and delete all , but first in sequence
=====================================================================================
Q) delete duplicate records
Ans)
	DELETE c1 FROM contacts c1
	INNER JOIN contacts c2
	WHERE
		c1.id > c2.id AND
		c1.email = c2.email;
=====================================================================================
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
=====================================================================================
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
=====================================================================================
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
=====================================================================================
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
=====================================================================================
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
=====================================================================================
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
=====================================================================================
Q) A table wth 3 columns id, name and age

		id 	name 	age
		1     a      21
		2     b      23
		3     c      33
		4     d      34

	Query to remove duplicate for entire row
Ans)

		DELETE FROM table_name
		WHERE id IN (
			SELECT id
			FROM table_name
			GROUP BY id, name, age
			HAVING COUNT(*) > 1
		);
=====================================================================================
Q)
Ans) UPDATE customers AS c1, customers AS c2
SET
    c1.first_name = c2.first_name,
    c1.last_name = c2.last_name,
    c1.age = c2.age,
    c1.country = c2.country,

	c2.first_name = c1.first_name,
    c2.last_name = c1.last_name,
    c2.age = c1.age,
    c2.country = c1.country
WHERE
    c1.customer_id = 5 AND c2.customer_id = 2;
=====================================================================================
Q) You have a table named EMPLOYEE that looks like the following columns and data:
		-------------------------
		Name 	Earnings 	Age
		-------------------------
		abc		$50,000		35
		edf		$45,001		60
		hij		$30,000		25
		klm		$45,000		45
		nop		$75,000		55
		-------------------------

	What does the following query return?

		Select MAX(Earnings) as Salary
		From EMPLOYEE
		Where Salary < (select max(Earnings) from EMPLOYEE)

	a) $75,000
	b) $45,000 and $45,001
	c) $30,000
	d) $50,000
	e) Returns all rows, ordered by the largest salary to the lowest salary

Ans) d
=====================================================================================
Q) 	Table name: flight
	Columns: source, destination, dept_time, arrival_time

	Write the query returning all the flights between A to B on a given date, with one layover in between

	SELECT
		f1.source, f1.destination, f1.dept_time, f2.arrival_time
	FROM flight f1
	JOIN flight f2 ON f1.destination = f2.source
	WHERE f1.source = 'A'
	AND f2.destination = 'B'
	AND DATE(f1.dept_time) = '2022-07-21'
	AND f2.dept_time > f1.arrival_time


	To get the layover time between the connecting flights, we can calculate the difference between the arrival time of the first flight (f1) and the departure time of the second flight (f2).

	SELECT
	  f1.source,
	  f1.destination,
	  f1.dept_time,
	  f2.arrival_time,
	  TIMEDIFF(f2.dept_time, f1.arrival_time) AS layover_time
	FROM flight f1
	JOIN flight f2 ON f1.destination = f2.source
	WHERE
	  f1.source = 'A'
	  AND f2.destination = 'B'
	  AND DATE(f1.dept_time) = '2022-07-21'
	  AND f2.dept_time > f1.arrival_time
=====================================================================================
Q) migrate all vaues from 5th row to 2th row
	CREATE TABLE table1 (
	  id INT,
	  letter VARCHAR(1)
	);

	INSERT INTO table1 VALUES
	  (1, 'a'),
	  (2, 'b'),
	  (3, 'c'),
	  (4, 'd'),
	  (5, 'e');
Ans)
	To read only,
		SELECT
		  t1.id AS id,
		  CASE WHEN t1.id = 2 THEN t2.letter ELSE t1.letter END AS letter
		FROM table1 t1
		JOIN table1 t2 ON t2.id = 5;

	To update changes,

		DECLARE
		  c5_data customers%ROWTYPE;
		  c2_data customers%ROWTYPE;

		BEGIN
		  SELECT * INTO c5_data FROM customers WHERE customer_id = 5;
		  SELECT * INTO c2_data FROM customers WHERE customer_id = 2;

		  -- Swap values
		  UPDATE customers SET
			first_name = c5_data.first_name,
			last_name = c5_data.last_name,
			age = c5_data.age,
			country = c5_data.country
		  WHERE customer_id = 2;

		  UPDATE customers SET
			first_name = c2_data.first_name,
			last_name = c2_data.last_name,
			age = c2_data.age,
			country = c2_data.country
		  WHERE customer_id = 5;

		END;
=========================================================================================
Q) Design an object model for a learning management / university course management system like D2L.
	E.g Entities: teachers, students, courses, assignments etc

	Courses: Math 1, Math2, …
	Semesters: Spring 2022, Summer 2022, …
	Teachers: Mr. Smith, Mrs. McDonald
		Math 1 is offered in Spring 2022 by Mr. Smith
		Math 2 is offered in Spring 2022 by Mr. Smith and Summer 2022 by Mrs. McDonald
	Students:
		Julie and John Julie is enrolled in Math 2 in summer 2022 taught by Mrs. McDonald
		John is enrolled in Math 1 in spring 2022 taught by Mr Smith, and
		Math 2 in summer 2022 taught by Mrs. McDonald

	We have two assignments Assignment A, Assignment B in Math 2 offered on summer 2022 by Mrs McDonald
	We have two assignments assignment X, assignment Y in Math 2 offered on Spring 2022 by Mr Smith
	John got 95/100 in assignment A in Math 2 while he took in summer 2022 … Table_name

	Fiel_1: Int

	Ensure that students has completed some mandatory courses , before staring new course
	what if there were multiple prequestes

	After Desiginng, get all prequests for a given course SQL

Ans)
		Person
			id
			name

		Student
			id
			person_id (FK to Person table)

		Teacher
			id
			person_id (FK to Person table)

		Course
			id
			name
			teacher_id (FK to Teacher table)
			semester_id (FK to Semester table)

		Semester
			id
			name
			year

		Enrollment
			id
			student_id (FK to Student table)
			course_id (FK to Course table)

		Assignment
			id
			name
			course_id (FK to Course table)
			max_points

		Submission
			id
			student_id (FK to Student table)
			assignment_id (FK to Assignment table)
			points

		-- To ensure that students have completed mandatory prerequisites before starting a new course

		CoursePrerequisite
			id
			course_id (FK to Course table)
			prerequisite_course_id (FK to Course table)

		SELECT
			p.name
		FROM Course c
		JOIN CoursePrerequisite cp ON c.id = cp.course_id
		JOIN Course p ON cp.prerequisite_course_id = p.id
		WHERE c.name = 'Course 101';
===============================================================================================================
CREATE TABLE PRODUCTS
(
       PRODUCT_ID     INTEGER,
       PRODUCT_NAME   VARCHAR2(30)
);
CREATE TABLE SALES
(
       SALE_ID        INTEGER,
       PRODUCT_ID     INTEGER,  FK
       YEAR           INTEGER,
       Quantity       INTEGER,
       PRICE          INTEGER
);



SELECT * FROM PRODUCTS;

		PRODUCT_ID PRODUCT_NAME
		-----------------------
		100        Nokia
		200        IPhone
		300        Samsung

SELECT * FROM SALES;

		SALE_ID PRODUCT_ID YEAR QUANTITY PRICE
		--------------------------------------
		1       100        2010   25     5000
		2       100        2011   16     5000
		3       100        2012   8      5000
		4       200        2010   10     9000
		5       200        2011   15     9000
		6       200        2012   20     9000
		7       300        2010   20     7000
		8       300        2011   18     7000
		9       300        2012   20     7000

1. Write a SQL query to find the products which does not have sales at all?
	select P.PRODUCT_ID, P.PRODUCT_NAME
	FROM PRODUCTS P
	LEFT JOIN SALES S ON P.PRODUCT_ID = S.PRODUCT_ID
	WHERE S.SALE_ID IS NULL;

2. Write a SQL query to find the products whose sales decreased in 2012 compared to 2011?

	select P.PRODUCT_ID, P.PRODUCT_NAME
	FROM PRODUCTS P
	LEFT JOIN SALES S1 ON P.PRODUCT_ID = S1.PRODUCT_ID AND S1.YEAR= 2011
	LEFT JOIN SALES S2 ON P.PRODUCT_ID = S2.PRODUCT_ID AND S2.YEAR= 2012
	WHERE S1.QUANTITY  > S2.QUANTITY

3. Write a query to select the top product sold in each year?
	select S.YEAR, P.PRODUCT_ID, P.PRODUCT_NAME, MAX(QUANTITY)
	FROM PRODUCTS P
	LEFT JOIN SALES S ON P.PRODUCT_ID = S.PRODUCT_ID
	GROUP BY S.YEAR

4.Write a SQL query to find the products which have continuous increase in sales every year?
	SELECT P.PRODUCT_ID, P.PRODUCT_NAME
	FROM PRODUCTS P
	INNER JOIN SALES S1 ON P.PRODUCT_ID = S1.PRODUCT_ID AND S1.YEAR = 2010
	INNER JOIN SALES S2 ON P.PRODUCT_ID = S2.PRODUCT_ID AND S2.YEAR = 2011 AND S2.QUANTITY > S1.QUANTITY
	INNER JOIN SALES S3 ON P.PRODUCT_ID = S3.PRODUCT_ID AND S3.YEAR = 2012 AND S3.QUANTITY > S2.QUANTITY;
===============================================================================================================
