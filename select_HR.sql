-- seleziona persone che si chiamano Patrik
  SELECT *
    FROM HR.EMPLOYEES
   WHERE FIRST_NAME = 'Patrik'

-- ordina nomi e cognomi in ordine alfabetico
  SELECT FIRST_NAME, LAST_NAME
    FROM HR.EMPLOYEES
   ORDER BY FIRST_NAME, LAST_NAME

-- seleziona le persone con employee_id maggiore di 200
  SELECT *
    FROM HR.EMPLOYEES
   WHERE EMPLOYEE_ID > 200

-- seleziona le persone che hanno un nome che inizia per Pat
  SELECT FIRST_NAME AS NOME
       , LAST_NAME  AS COGNOME
    FROM HR.EMPLOYEES
   WHERE FIRST_NAME LIKE 'Pat%'
ORDER BY LAST_NAME
       , FIRST_NAME

-- seleziona le persone che hanno un nome che inizia per Pat in modo piú veloce rispetto alla LIKE
  SELECT FIRST_NAME AS NOME
       , LAST_NAME  AS COGNOME
    FROM HR.EMPLOYEES
   WHERE substr(FIRST_NAME, 0, 3) = 'Pat'
ORDER BY LAST_NAME
       , FIRST_NAME

-- seleziona le persone che non hanno una T nel nome (maiuscola o minuscola)
  SELECT FIRST_NAME AS NOME
       , LAST_NAME  AS COGNOME
    FROM HR.EMPLOYEES
   WHERE UPPER(FIRST_NAME) NOT LIKE '%T%'
ORDER BY LAST_NAME
       , FIRST_NAME

-- seleziona le persone che si chiamano Grant Douglas
 SELECT * 
    FROM HR.EMPLOYEES 
   WHERE     LAST_NAME  = 'Grant' 
         AND FIRST_NAME = 'Douglas' 

-- conta quanti utenti esistono
  SELECT COUNT(*)
    FROM HR.EMPLOYEES

-- conta quanti utenti hanno le commissioni
  SELECT COUNT(COMMISSION_PCT)
    FROM HR.EMPLOYEES

-- Funzioni di gruppo
  SELECT AVG(SALARY), MIN(SALARY), MAX(SALARY), COUNT(1), SUM(SALARY)
    FROM HR.EMPLOYEES

-- group by con la media salariale maggiore di 10k
  SELECT JOB_ID, COUNT(1) AS TOTALE, AVG(SALARY) MEDIA_SALARIO 
    FROM HR.EMPLOYEES 
GROUP BY JOB_ID 
  HAVING AVG(SALARY) >= 10000 
ORDER BY 3 DESC

-- per creare le viste:
CREATE VIEW VistaBellissima1 AS
SELECT blablabla

-- visualizzare nome e job title
SELECT EMPLOYEES.FIRST_NAME, EMPLOYEES.LAST_NAME, JOBS.JOB_TITLE
  FROM HR.EMPLOYEES
  JOIN HR.JOBS
       ON EMPLOYEES.JOB_ID = JOBS.JOB_ID;

-- Uso di due join
SELECT EMPLOYEES.FIRST_NAME, EMPLOYEES.LAST_NAME, JOBS.JOB_TITLE, DEPARTMENTS.DEPARTMENT_NAME
  FROM HR.EMPLOYEES
  JOIN HR.JOBS
       ON EMPLOYEES.JOB_ID = JOBS.JOB_ID
  JOIN HR.DEPARTMENTS
       ON EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;

-- Uso di due join e degli alias delle tabelle
SELECT E.FIRST_NAME, E.LAST_NAME, J.JOB_TITLE, D.DEPARTMENT_NAME
  FROM HR.EMPLOYEES E
  JOIN HR.JOBS J
       ON E.JOB_ID = J.JOB_ID
  JOIN HR.DEPARTMENTS D
       ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;

--distinct
  select distinct first_name
    from employees
  --che equivale a:
  select first_name
    from employees
group by first_name
  

--union (sí, questo esempio non ha troppo senso, ma é per far capire il funzionamento)
select first_name colonna_strana, 'employees' tabella_di_provenienza
  from employees
where employee_id > 200
union
select JOB_TITLE, 'jobs'
  from jobs
 where min_salary > 8000;

--concat (ma é piú comodo il pipe)
select concat(concat(first_name,' '), last_name)
     , salary
  from employees 
 where salary < 6000

--pipe ||
 select first_name || ' ' || last_name full_name
     , salary
  from employees 
 where salary < 6000;