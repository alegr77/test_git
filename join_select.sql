-- ES 3
select FIRST_NAME, LAST_NAME, DEPARTMENT_ID
  from employees
 where LAST_NAME = 'McEwen';
 
-- ES 4
select employee_id
      , first_name
      , last_name
      , email
      , phone_number
      , hire_date
      , job_id
      , salary
      , commission_pct
      , manager_id
      , department_id
  from employees
 where department_id = null;

-- ES 5
select *
  from departments
 where DEPARTMENT_NAME = 'Marketing';
 
-- ES 6
  select first_name || ' ' || last_name full_name
       , hire_date
       , salary
       , department_id  
    from employees
   where UPPER(first_name) not like '%M%'
         AND UPPER(last_name) not like '%M%'
order by department_id;

-- ES 7
select *
  from employees
 where salary >= 8000 
   and salary <= 12000
   and COMMISSION_PCT is not null
   and HIRE_DATE <= TO_DATE('05-06-2015', 'DD-MM-YYYY')
   and DEPARTMENT_ID <> 80;

-- ES 10
select FIRST_NAME, LAST_NAME, SALARY
  from employees
 where UPPER(substr(FIRST_NAME, -1)) <> 'M';

-- ES 12
select first_name || ' ' || last_name full_name
     , JOB_ID
     , HIRE_DATE
  from employees
 where HIRE_DATE BETWEEN TO_DATE('05-06-2015', 'DD-MM-YYYY') 
                     and TO_DATE('05-06-2017', 'DD-MM-YYYY');

-- ES 18
select first_name || ' ' || last_name full_name
     , hire_date
     , commission_pct
     , email || ' - ' || phone_number contact_details
     , salary
  from employees
 where salary > 11000
       or substr(phone_number, 5, 1) = 5
order by first_name DESC;
     
-- ES 1J
 select E.FIRST_NAME
      , E.LAST_NAME
      , E.DEPARTMENT_ID 
      , D.DEPARTMENT_NAME
   from employees E
   join departments D
        on E.DEPARTMENT_ID = D.DEPARTMENT_ID;
        
-- ES 2J
select E.FIRST_NAME
     , E.LAST_NAME
     , D.DEPARTMENT_NAME
     , L.CITY
     , L.STATE_PROVINCE 
  from employees E
  join departments D
        on E.DEPARTMENT_ID = D.DEPARTMENT_ID
  join locations L
        on D.LOCATION_ID = L.LOCATION_ID;
 
-- ES 4J
 select E.FIRST_NAME
      , E.LAST_NAME
      , E.DEPARTMENT_ID 
      , D.DEPARTMENT_NAME
   from employees E
   join departments D
        on E.DEPARTMENT_ID = D.DEPARTMENT_ID
  where E.DEPARTMENT_ID in (80, 40);
        
-- ES 5J
select E.FIRST_NAME
     , E.LAST_NAME
     , D.DEPARTMENT_NAME
     , L.CITY
     , L.STATE_PROVINCE 
  from employees E
  join departments D
        on E.DEPARTMENT_ID = D.DEPARTMENT_ID
        and lower(E.First_name) LIKE '%z%'
  join locations L
        on D.LOCATION_ID = L.LOCATION_ID;
        
   select E.FIRST_NAME
        , E.LAST_NAME
        , D.DEPARTMENT_ID 
        , D.DEPARTMENT_NAME
     from departments D
Left join employees E
          on D.DEPARTMENT_ID = E.DEPARTMENT_ID;

-- ES 7J
select R.FIRST_NAME
     , R.LAST_NAME
     , R.SALARY
  from employees E
  join    employees R
       on E.SALARY   > R.SALARY 
 where E.EMPLOYEE_ID = 182
 
-- oppure
select R.FIRST_NAME
     , R.LAST_NAME
     , R.SALARY
     , R.EMPLOYEE_ID ID_R
     , E.EMPLOYEE_ID ID_E
  from employees E
  join    employees R
       on R.SALARY < E.SALARY
 where E.EMPLOYEE_ID IN (182, 135);

--oppure       
select FIRST_NAME
     , LAST_NAME
     , SALARY
  from employees
 where SALARY < (select min(salary) 
                   from employees
                  where EMPLOYEE_ID = 182);

