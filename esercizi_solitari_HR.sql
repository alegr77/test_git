LEGENDA:
(S) = Esercizi sulla select
(J) = Esercizi sulla join

es.1(S)
select first_name || ' ' || last_name full_name
	 , salary
from hr.employees
where salary < 6000;

es.2(S)
select first_name
	, last_name
	, department_id
	, salary
from hr.employees
where salary > 8000;

es.3(S)
select first_name, last_name, department_id
from hr.employees
where last_name = 'McEwen';

es.4(S)
select first_name
     , last_name
     , email
     , phone_number
     , hire_date
     , job_id
     , salary,commission_pct
     , manager_id
     , department_id
from hr.employees
where department_id = NULL;

es.5(S)
SELECT *
FROM hr.departments
WHERE department_name = 'Marketing';

es.6(S)
SELECT first_name || ' ' || last_name full_name
	 , hire_date
     , salary
     , department_id
FROM hr.employees
WHERE UPPER(first_name) NOT LIKE '%M%'
ORDER BY department_id;

es.7(S)
SELECT *
FROM hr.employees
WHERE SALARY >= 8000
    AND
		SALARY <= 12000
    AND 
    	commission_pct is not null
    AND 
    	hire_date <= TO_DATE('05-06-2015', 'DD-MM-YYYY')
    AND
		department_id != 40
	AND
		department_id != 70
	AND
		department_id != 120;

es.8(S)
SELECT first_name || ' ' || last_name full_name
     , salary
FROM hr.employees
WHERE commission_pct IS NULL;

es.9(S)
select first_name || ' ' || last_name full_name
	 , email || ' - ' || phone_number contact_details
	 , salary remuneration
from hr.employees
where salary BETWEEN 9000 AND 17000;

es.10(S)
select first_name
     , last_name 
	 , salary 
from hr.employees
where UPPER(first_name) LIKE '%M';
#ANCHE COSÌ
where UPPER(substr(FIRST_NAME, -1)) <> 'M';

es.11(S)
select first_name || ' ' || last_name full_name
     , salary 
from hr.employees
where salary NOT BETWEEN 7000 AND 15000
ORDER BY full_name

es.12(S)
select first_name || ' ' || last_name full_name
     , job_id
     , hire_date
from hr.employees
WHERE hire_date BETWEEN TO_DATE('2007-11-05', 'YYYY-MM-DD')
    		AND TO_DATE('2009-07-05', 'YYYY-MM-DD');

es.13(S)
 select first_name || ' ' || last_name full_name
     , department_id
from hr.employees
WHERE department_id = 70
	OR
	  department_id = 90;

es.14(S)
select first_name || ' ' || last_name full_name
     , salary
     , manager_id
from hr.employees
WHERE manager_id IS NOT NULL;

es.15(S)
select *
from hr.employees
WHERE hire_date < TO_DATE('2002-06-21', 'YYYY-MM-DD');

es.28(S)
select first_name
     , last_name
     , hire_date
from hr.employees
WHERE job_id = 'SA_MAN'
	OR
	  job_id = 'SA_REP';

es.1(J)
 select E.FIRST_NAME
      , E.LAST_NAME
      , E.DEPARTMENT_ID 
      , D.DEPARTMENT_NAME
   from hr.employees E
   join hr.departments D
        on E.DEPARTMENT_ID = D.DEPARTMENT_ID;

es.2(J)
select e.first_name
	 , e.last_name
	 , d.department_name
     , l.city
     , l.state_province
from hr.employees e
join hr.departments d
	on e.department_id = d.department_id
join hr.locations l
	on d.location_id = l.location_id;

es.3(J)
select e.first_name
	 , e.last_name
	 , e.salary
	 , j.grade_level
FROM employees e
JOIN job_grades j
	ON e.salary BETWEEN j.lowest_sal AND j.highest_sal;

es.4 (J)
select e.first_name
	 , e.last_name
	 , e.department_id
	 , d.department_name
FROM employees e
JOIN departments d
	ON e.department_id = d.department_id
AND e.department_id IN (80,40)
order by e.first_name

es.5(J)
SELECT e.first_name
	 , e.last_name
	 , d.department_name
	 , l.city
	 , l.state_province
FROM employees e
join departments d
	on e.department_id = d.department_id
JOIN locations l
	on d.location_id = l.location_id
where e.first_name LIKE '%z%'

es.6(J)
SELECT e.first_name
	 , e.last_name
     , e.department_id
	 , d.department_name
from departments d
left join employees e
	on d.department_id = e.department_id

  es.7(J)
SELECT e.first_name
	 , e.last_name
	 , e.salary
from hr.employees e
join hr.employees e2
	on e.salary < e2.salary
	AND e2.employee_id = 182;

es.8(J)
SELECT e.FIRST_NAME || ' ' || E.LAST_NAME NomeCompletoImpiegato
     , M.FIRST_NAME || ' ' || M.LAST_NAME NomeCompletomanager
FROM HR.EMPLOYEES E
JOIN HR.EMPLOYEES M
	ON E.MANAGER_ID = M.EMPLOYEE_ID

es.9(J)
SELECT D.DEPARTMENT_NAME
	 , L.CITY
	 , L.STATE_PROVINCE
FROM HR.DEPARTMENTS D
JOIN HR.LOCATIONS L
	ON D.LOCATION_ID = L.LOCATION_ID

ES.10(J)
SELECT E.FIRST_NAME
	 , E.LAST_NAME
	 , D.DEPARTMENT_ID
 	 , D.DEPARTMENT_NAME
FROM HR.EMPLOYEES E
LEFT JOIN HR.DEPARTMENTS D
	ON E.DEPARTMENT_ID = D.DEPARTMENT_ID

es.11(J)
SELECT E.FIRST_NAME NOME_IMPIEGATO
	 , EM.FIRST_NAME NOME_MANAGER
FROM HR.EMPLOYEES E
LEFT OUTER JOIN HR.EMPLOYEES EM
	ON E.MANAGER_ID = EM.EMPLOYEE_ID;

ES.12(J)
SELECT E.FIRST_NAME
	 , E.LAST_NAME
	 , E.DEPARTMENT_ID
FROM HR.EMPLOYEES E
JOIN HR.EMPLOYEES EM
	ON E.DEPARTMENT_ID = EM.DEPARTMENT_ID
	AND EM.LAST_NAME = 'Taylor';

es.13(J)
SELECT J.JOB_TITLE
	 , D.DEPARTMENT_NAME
	 , E.FIRST_NAME || ' ' || E.LAST_NAME FULL_NAME
	 , JH.START_DATE
FROM HR.JOB_HISTORY JH
JOIN HR.JOBS J
	ON JH.JOB_ID = J.JOB_ID
JOIN HR.DEPARTMENTS D
	ON JH.DEPARTMENT_ID = D.DEPARTMENT_ID
JOIN HR.EMPLOYEES E
	ON JH.JOB_ID = E.JOB_ID
WHERE START_DATE <= TO_DATE('1997-08-31', 'YYYY-MM-DD') 
	AND START_DATE >= TO_DATE('1993-01-01', 'YYYY-MM-DD')

ES.14(J)
SELECT J.JOB_TITLE
	 , E.FIRST_NAME || ' ' || E.LAST_NAME EMPLOYEE_NAME
	 , J.MAX_SALARY - E.SALARY SALARY_DIFFERENCE
FROM HR.EMPLOYEES E
JOIN HR.JOBS J
	ON E.JOB_ID = J.JOB_ID
ORDER BY SALARY_DIFFERENCE DESC;

ES.15(J)
SELECT D.DEPARTMENT_NAME
	 , AVG(E.SALARY) AVERAGE_SALARY
	 , COUNT(E.COMMISSION_PCT) COMMISSION_COUNT
FROM HR.DEPARTMENTS D
JOIN HR.EMPLOYEES E
	ON D.DEPARTMENT_ID = E.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_NAME;
ORDER BY COMMISSION_COUNT DESC

ES.16(J)
SELECT J.JOB_TITLE
	 , E.FIRST_NAME || ' ' || E.LAST_NAME EMPLOYEE_NAME
	 , J.MAX_SALARY - E.SALARY SALARY_DIFFERENCE
FROM HR.EMPLOYEES E
JOIN HR.JOBS J
	ON E.JOB_ID = J.JOB_ID
WHERE E.DEPARTMENT_ID = 80
ORDER BY SALARY_DIFFERENCE DESC

ES.17(J)
SELECT C.COUNTRY_NAME
	 , L.CITY
	 , D.DEPARTMENT_NAME
FROM HR.COUNTRIES C
JOIN HR.LOCATIONS L
	ON C.COUNTRY_ID = L.COUNTRY_ID
JOIN HR.DEPARTMENTS D
	ON L.LOCATION_ID = D.LOCATION_ID

 ES.18(J)    
 SELECT D.DEPARTMENT_NAME
	 , E.FIRST_NAME || ' ' || E.LAST_NAME MANAGER_NAME
FROM HR.DEPARTMENTS D
JOIN HR.EMPLOYEES E
	ON E.EMPLOYEE_ID = D.MANAGER_ID

ES.19(J)
SELECT J.JOB_TITLE
	 , AVG(E.SALARY) AVERAGE_SALARY
FROM HR.EMPLOYEES E
JOIN HR. JOBS J
	ON E.JOB_ID = J.JOB_ID
GROUP BY J.JOB_TITLE
ORDER BY AVERAGE_SALARY DESC

ES.20(J)
SELECT E.EMPLOYEE_ID
     , E.FIRST_NAME || ' ' || E.LAST_NAME FULL_NAME
	 , J.START_DATE
 	 , J.END_DATE
 	 , J.JOB_ID
 	 , J.DEPARTMENT_ID
FROM HR.EMPLOYEES E
JOIN HR.JOB_HISTORY J
	ON E.EMPLOYEE_ID = J.EMPLOYEE_ID
WHERE SALARY >= 12000;

ES.21(J)
SELECT C.COUNTRY_NAME
 	 , L.CITY
 	 , COUNT(D.DEPARTMENT_ID)
FROM HR.COUNTRIES C
JOIN HR.LOCATIONS L
	ON C.COUNTRY_ID = L.COUNTRY_ID
JOIN HR.DEPARTMENTS D
	ON L.LOCATION_ID = D.LOCATION_ID
WHERE D.DEPARTMENT_ID IN(
    SELECT DEPARTMENT_ID
    FROM HR.EMPLOYEES E
    GROUP BY DEPARTMENT_ID
    HAVING COUNT (DEPARTMENT_ID) >= 2
)
GROUP BY C.COUNTRY_NAME, L.CITY;

ES.22(J)
SELECT D.DEPARTMENT_NAME
	 , FIRST_NAME || ' ' || LAST_NAME MANAGER_FULL_NAME
 	 , L.CITY
FROM HR.LOCATIONS L
JOIN HR.DEPARTMENTS D
	ON L.LOCATION_ID = D.LOCATION_ID
JOIN HR.EMPLOYEES E
	ON D.DEPARTMENT_ID = E.DEPARTMENT_ID
ORDER BY L.CITY

ES.23(J)
SELECT JH.EMPLOYEE_ID
 	 , J.JOB_TITLE
 	 , JH.END_DATE - JH.START_DATE AS DAYS_WORKED
FROM HR.JOB_HISTORY JH
JOIN HR.JOBS J
	ON JH.JOB_ID = J.JOB_ID
WHERE JH.DEPARTMENT_ID = 80
ORDER BY DAYS_WORKED DESC;

ES.24(J)
SELECT E.FIRST_NAME || ' ' || E.LAST_NAME FULL_NAME
 	 , E.SALARY
FROM HR.LOCATIONS L
JOIN HR.DEPARTMENTS D
	ON L.LOCATION_ID = D.LOCATION_ID
JOIN HR.EMPLOYEES E
	ON D.DEPARTMENT_ID = E.DEPARTMENT_ID
WHERE L.CITY LIKE 'London'

ES.25(J)
SELECT E.FIRST_NAME || ' ' || E.LAST_NAME EMPLOYEE_NAME
 	 , J.JOB_TITLE
 	 , JH.START_DATE
 	 , JH.END_DATE
FROM HR.JOBS J
JOIN HR.JOB_HISTORY JH
	ON J.JOB_ID = JH.JOB_ID
JOIN HR.EMPLOYEES E
	ON JH.EMPLOYEE_ID = E.EMPLOYEE_ID
WHERE E.COMMISSION_PCT IS NULL;

es.26(J)
select d.department_name
 	 , d.department_id
 	 , count(e.first_name) employees_number
from hr.departments d
left join hr.employees e
	on d.department_id = e.department_id
group by d.department_id, d.department_name
order by department_id;

es.27(J)
SELECT E.EMPLOYEE_ID  
     , E.FIRST_NAME || ' ' || E.LAST_NAME FULL_NAME
	 , C.COUNTRY_NAME
FROM HR.EMPLOYEES E
JOIN HR.DEPARTMENTS D
	ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
JOIN HR.LOCATIONS L
	ON D.LOCATION_ID = L.LOCATION_ID
JOIN HR.COUNTRIES C
	ON L.COUNTRY_ID = C.COUNTRY_ID;

/*
selezionare l'elenco delle persone che lavorano in America.
Di ogni persona selezionare il nome, il cognome e il lavoro che fa.
Inoltre selezionare il nome, il cognome e il lavoro che fa il suo manager.
*/

SELECT R.REGION_NAME
        , E.FIRST_NAME
        , E.LAST_NAME
        , J.JOB_TITLE
        , M.FIRST_NAME || ' ' || M.LAST_NAME AS NAME_OF_MANAGER
        , JM.JOB_TITLE
FROM EMPLOYEES E
JOIN EMPLOYEES M
ON E.MANAGER_ID = M.MANAGER_ID
JOIN JOBS J
 ON E.JOB_ID = J.JOB_ID
JOIN JOBS JM
 ON M.JOB_ID = JM.JOB_ID
JOIN DEPARTMENTS D
 ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
JOIN LOCATIONS L
 ON D.LOCATION_ID = L.LOCATION_ID
JOIN COUNTRIES C
 ON L.COUNTRY_ID = C.COUNTRY_ID
JOIN REGIONS R
 ON C.REGION_ID = R.REGION_ID
 
WHERE UPPER(REGION_NAME) = 'AMERICAS';

/* per ogni cittá visualizzare:
    numero di dipendenti
    somma degli stipendi di tutti i dipendenti
    numero di dipartimenti
    numero di managerss
*/
SELECT 
    L.CITY,
    COUNT(E.EMPLOYEE_ID) AS NUM_DIPENDENTI,
    SUM(E.SALARY) AS SOMMA_STIPENDI,
    COUNT(DISTINCT E.DEPARTMENT_ID) AS NUM_DIPARTIMENTI,
    COUNT(DISTINCT E.MANAGER_ID) AS NUM_MANAGER
FROM 
    HR.EMPLOYEES E
JOIN 
    HR.DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
JOIN 
    HR.LOCATIONS L ON D.LOCATION_ID = L.LOCATION_ID
WHERE 
    L.CITY IS NOT NULL
GROUP BY 
    L.CITY
ORDER BY 
    L.CITY;



