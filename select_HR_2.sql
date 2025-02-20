SELECT EMPLOYEES.FIRST_NAME
     , EMPLOYEES.LAST_NAME
     , JOBS.JOB_TITLE
  FROM EMPLOYEES
  JOIN JOBS
       ON EMPLOYEES.JOB_ID = JOBS.JOB_ID;
       
       
SELECT *
  FROM EMPLOYEES;

SELECT E.FIRST_NAME, E.LAST_NAME, J.JOB_TITLE, D.DEPARTMENT_NAME
  FROM EMPLOYEES E
  JOIN JOBS J
       ON E.JOB_ID = J.JOB_ID
  JOIN DEPARTMENTS D
       ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;
       
  select first_name PIPPO
    from employees
   WHERE EMPLOYEE_ID > 200
group by first_name

UNION

select distinct JOB_ID
  from employees
WHERE JOB_ID LIKE 'A%';




/* From the following table, write a SQL query to find those employees whose 
salaries are less than 6000. Return full name (first and last name), and 
salary.*/

SELECT    FIRST_NAME 
       || ' ' 
       || LAST_NAME FULL_NAME
     , SALARY
  FROM EMPLOYEES
 WHERE SALARY < 6000;


SELECT FIRST_NAME
  FROM EMPLOYEES
 WHERE UPPER(FIRST_NAME) NOT LIKE '%M%';
 
 
 
/* From the following table, write a  SQL query to find those employees who 
earn between 8000 and 12000 (Begin and end values are included.) and get some 
commission. These employees joined before ‘1987-06-05’ and were not included in 
the department numbers 40, 120 and 70. Return all fields. */

SELECT *
  FROM EMPLOYEES
 WHERE     SALARY BETWEEN 8000 AND 12000
       AND COMMISSION_PCT IS NOT NULL
       AND COMMISSION_PCT != 0
       AND HIRE_DATE < TO_DATE('2015-05-06','yyyy-mm-dd')
       AND DEPARTMENT_ID NOT IN (40, 120, 70);
       
SELECT *
  FROM EMPLOYEES
 WHERE HIRE_DATE BETWEEN TO_DATE('2015-05-06','yyyy-mm-dd')
                     AND TO_DATE('2016-01-06','yyyy-mm-dd');
SELECT *
  FROM EMPLOYEES
 WHERE DEPARTMENT_ID IN (90, 70);
                     

 WHERE    DEPARTMENT_ID = 90
       OR DEPARTMENT_ID = 70;
       
/*From the following table, write a  SQL query to find employees whose first
names contain the letters D, S, or N. Sort the result-set in descending order 
by salary. Return all fields.*/
                     
SELECT *
  FROM EMPLOYEES
 WHERE    (   UPPER(FIRST_NAME) LIKE '%Z%'
           OR UPPER(FIRST_NAME) LIKE '%Y%'
           OR UPPER(FIRST_NAME) LIKE '%X%')
       AND
          (   UPPER(LAST_NAME) LIKE '%Z%'
           OR UPPER(LAST_NAME) LIKE '%Y%'
           OR UPPER(LAST_NAME) LIKE '%X%')
ORDER BY SALARY DESC;


SELECT *
  FROM EMPLOYEES
 WHERE    UPPER(FIRST_NAME) LIKE '%Z%'
       OR UPPER(FIRST_NAME) LIKE '%Y%'
       OR (    UPPER(FIRST_NAME) LIKE '%X%'
           AND UPPER(LAST_NAME) LIKE '%Z%')
       OR UPPER(LAST_NAME) LIKE '%Y%'
       OR UPPER(LAST_NAME) LIKE '%X%'
ORDER BY SALARY DESC;



/* From the following table, write a  SQL query to find those employees who earn
above 11000 or the seventh character in their phone number is 2. Sort the 
result-set in descending order by first name. Return full name (first name and 
last name), hire date, commission percentage, email, and telephone separated by 
'-', and salary.*/
SELECT    FIRST_NAME 
       || ' ' 
       || LAST_NAME FULL_NAME
     , HIRE_DATE
     , COMMISSION_PCT
     ,    EMAIL 
       || ' - ' 
       || PHONE_NUMBER CONTACT_INFORMATION
     , SALARY 
  FROM EMPLOYEES
 WHERE    substr(PHONE_NUMBER, 7, 1) = '2'
       OR salary > 11000
ORDER BY FIRST_NAME DESC;


/*From the following table, write a  SQL query to find those employees who 
worked more than two jobs in the past. Return employee id*/

SELECT
    employee_id,
    start_date,
    end_date,
    job_id,
    department_id
FROM
    job_history;
    
   SELECT employee_id
     FROM job_history
 group by employee_id
   having count(1) > 1;
    
SELECT distinct employee_id
  FROM job_history j1
  where (SELECT count(1)
           FROM job_history j2
          where j2.EMPLOYEE_ID = j1.EMPLOYEE_ID) > 1;
 
 /* 23. From the following table, write a SQL query to count the number of 
 employees, the sum of all salary, and difference between the highest salary 
 and lowest salaries by each job id. Return job_id, count, sum, 
 salary_difference.*/
 
  SELECT JOB_ID
       , COUNT(1) COUNT
       , SUM(SALARY) SUM
       , MAX(SALARY) - MIN(SALARY) SALARY_DIFFERENCE
    FROM EMPLOYEES
group by JOB_ID;

-- conta quante righe hanno il JOB_ID valorizzato all'interno della EMPLOYEES
SELECT COUNT(JOB_ID)
  FROM EMPLOYEES;

-- conta quanti JOB_ID differenti ci sono all'interno della EMPLOYEES
SELECT COUNT(DISTINCT JOB_ID)
  FROM EMPLOYEES;
  
  
   SELECT employee_id
     FROM job_history
 group by employee_id
   having count(distinct job_id) > 1;


/* From the following table, write a  SQL query to find each job ids where two 
or more employees worked for more than 3000 days. Return job id.*/

  SELECT JOB_ID, COUNT(1)
    FROM EMPLOYEES
   WHERE trunc(sysdate) - HIRE_DATE >= 3000
GROUP BY JOB_ID
  HAVING COUNT(1) >= 2;

select trunc(sysdate) - to_date('2025-01-01', 'yyyy-mm-dd') from dual;

select sysdate from dual;

/*From the following table, write a SQL query to count the number of employees 
worked under each manager. Return manager ID and number of employees.*/

--crea una tabella con struttura e dati della tabella employees 
CREATE TABLE EMPLOYEES_BKP AS
SELECT *
  FROM EMPLOYEES;
  
--crea una tabella con solamente la struttura della tabella employees  
CREATE TABLE EMPLOYEES_NUOVA AS
SELECT *
  FROM EMPLOYEES
 WHERE 1 = 2;

-- inserisci all'interno di una tabella a partire da una select
INSERT INTO 
    EMPLOYEES_NUOVA
SELECT
    employee_id,
    'Pippo' first_name,
    last_name,
    email,
    phone_number,
    hire_date,
    job_id,
    salary,
    commission_pct,
    manager_id,
    department_id
FROM
    employees
WHERE EMPLOYEE_ID > 200;

/*From the following tables, write a SQL query to find the first name, last name
, department number, and department name for each employee.*/

SELECT E.FIRST_NAME, E.LAST_NAME, E.DEPARTMENT_ID, D.DEPARTMENT_NAME
  FROM EMPLOYEES E
  JOIN DEPARTMENTS D
       ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;



/*From the following tables, write a SQL query to find the first name, last name
, department, city, and state province for each employee*/
SELECT E.FIRST_NAME
     , E.LAST_NAME
     , D.DEPARTMENT_NAME
     , L.CITY
     , L.STATE_PROVINCE
  FROM EMPLOYEES E
  JOIN DEPARTMENTS D
       ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
  JOIN LOCATIONS L
       ON D.LOCATION_ID = L.LOCATION_ID
 WHERE    E.FIRST_NAME = 'Ellen'
       OR L.City = 'South San Francisco';






-- Creazione della tabella
CREATE TABLE job_grade (
    grade_level VARCHAR2(1) NOT NULL,
    lowest_sal NUMBER(10, 2) NOT NULL,
    highest_sal NUMBER(10, 2) NOT NULL,
    CONSTRAINT pk_grade_level PRIMARY KEY (grade_level)
);

-- Popolamento della tabella
INSERT INTO job_grade (grade_level, lowest_sal, highest_sal) VALUES ('A', 1000, 2999);
INSERT INTO job_grade (grade_level, lowest_sal, highest_sal) VALUES ('B', 3000, 5999);
INSERT INTO job_grade (grade_level, lowest_sal, highest_sal) VALUES ('C', 6000, 9999);
INSERT INTO job_grade (grade_level, lowest_sal, highest_sal) VALUES ('D', 10000, 14999);
INSERT INTO job_grade (grade_level, lowest_sal, highest_sal) VALUES ('E', 15000, 24999);
INSERT INTO job_grade (grade_level, lowest_sal, highest_sal) VALUES ('F', 25000, 40000);

-- Conferma delle modifiche
COMMIT;

-- Visualizzazione dei dati
SELECT * FROM job_grade;