CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR2(100),
    city VARCHAR2(50),
    commission DECIMAL(5,2)
);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES (5001, 'James Hoog', 'New York', 0.15);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES (5002, 'Nail Knite', 'Paris', 0.13);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES (5005, 'Pit Alex', 'London', 0.11);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES (5006, 'Mc Lyon', 'Paris', 0.14);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES (5007, 'Paul Adam', 'Rome', 0.13);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES (5003, 'Lauson Hen', 'San Jose', 0.12);

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR2(100),
    city VARCHAR2(50),
    grade INT,
    salesman_id INT
);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3002, 'Nick Rimando', 'New York', 100, 5001);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3007, 'Brad Davis', 'New York', 200, 5001);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3005, 'Graham Zusi', 'California', 200, 5002);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3008, 'Julian Green', 'London', 300, 5002);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3004, 'Fabian Johnson', 'Paris', 300, 5006);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3009, 'Geoff Cameron', 'Berlin', 100, 5003);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3003, 'Jozy Altidor', 'Moscow', 200, 5007);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES (3001, 'Brad Guzan', 'London', NULL, 5005);

CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70001, 150.5, TO_DATE('2012-10-05', 'YYYY-MM-DD'), 3005, 5002);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70009, 270.65, TO_DATE('2012-09-10', 'YYYY-MM-DD'), 3001, 5005);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70002, 65.26, TO_DATE('2012-10-05', 'YYYY-MM-DD'), 3002, 5001);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70004, 110.5, TO_DATE('2012-08-17', 'YYYY-MM-DD'), 3009, 5003);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70007, 948.5, TO_DATE('2012-09-10', 'YYYY-MM-DD'), 3005, 5002);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70005, 2400.6, TO_DATE('2012-07-27', 'YYYY-MM-DD'), 3007, 5001);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70008, 5760, TO_DATE('2012-09-10', 'YYYY-MM-DD'), 3002, 5001);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70010, 1983.43, TO_DATE('2012-10-10', 'YYYY-MM-DD'), 3004, 5006);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70003, 2480.4, TO_DATE('2012-10-10', 'YYYY-MM-DD'), 3009, 5003);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70012, 250.45, TO_DATE('2012-06-27', 'YYYY-MM-DD'), 3008, 5002);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70011, 75.29, TO_DATE('2012-08-17', 'YYYY-MM-DD'), 3003, 5007);
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (70013, 3045.6, TO_DATE('2012-04-25', 'YYYY-MM-DD'), 3002, NULL);

#####################---------------------------------------------------------########################

es.1
select s.name Salesman
 	 , c.cust_name
 	 , c.city
from salesman s 
   , customer c
where s.city = c.city