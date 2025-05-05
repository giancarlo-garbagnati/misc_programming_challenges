-- https://www.programmerinterview.com/database-sql/advanced-sql-interview-questions-continued-part-2/

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

CREATE TABLE Customer (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    City VARCHAR(100),
    Industry_Type CHAR(1)
);

INSERT INTO Customer (ID, Name, City, Industry_Type) VALUES
(4, 'Samsonic', 'pleasant', 'J'),
(6, 'Panasung', 'oaktown', 'J'),
(7, 'Samony', 'jackson', 'B'),
(9, 'Orange', 'Jackson', 'B');


/* 
Here is the problem: find the largest order amount for each 
salesperson and the associated order number, along with the 
customer to whom that order belongs to. You can present your 
answer in any database’s SQL – MySQL, Microsoft SQL Server, 
Oracle, etc.
*/

SELECT s.Name, MAX(o.Amount), o.Number, c.Name
FROM Orders o
LEFT JOIN Salesperson s
ON o.salesperson_id = s.ID
LEFT JOIN Customer c
ON o.cust_id = c.ID
GROUP BY s.Name;
