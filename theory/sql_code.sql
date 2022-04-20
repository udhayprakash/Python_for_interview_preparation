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
