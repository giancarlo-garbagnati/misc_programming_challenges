-- https://www.programmerinterview.com/database-sql/advanced-sql-interview-questions-and-answers/

CREATE TABLE Salesperson (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Salary INT
);

INSERT INTO Salesperson (ID, Name, Age, Salary) VALUES
(1, 'Abe', 61, 140000),
(2, 'Bob', 34, 44000),
(5, 'Chris', 34, 40000),
(7, 'Dan', 41, 52000),
(8, 'Ken', 57, 115000),
(11, 'Joe', 38, 38000);

CREATE TABLE Orders (
    Number INT PRIMARY KEY,
    order_date DATE,
    cust_id INT,
    salesperson_id INT,
    Amount INT
);

INSERT INTO Orders (Number, order_date, cust_id, salesperson_id, Amount) VALUES
(10, '1996-08-02', 4, 2, 540),
(20, '1999-01-30', 4, 8, 1800),
(30, '1995-07-14', 9, 1, 460),
(40, '1998-01-29', 7, 2, 2400),
(50, '1998-02-03', 6, 7, 600),
(60, '1998-03-02', 6, 7, 720),
(70, '1998-05-06', 9, 7, 150);

/* 
We want to retrieve the names of all salespeople that have more than 1 order 
from the tables above. You can assume that each salesperson only has one ID.
*/

-- My solution

SELECT s.Name
FROM Salesperson s
LEFT JOIN Orders o
ON s.ID = o.salesperson_id
GROUP BY o.salesperson_id, s.Name
HAVING COUNT(o.salesperson_id) > 1;

/*
If that is the case, then what (if anything) is wrong with the following SQL?:

SELECT Name
FROM Orders, Salesperson
WHERE Orders.salesperson_id = Salesperson.ID
GROUP BY salesperson_id
HAVING COUNT( salesperson_id ) >1
*/

/*

*/
