create table employee (
emp_Id int,
emp_name varchar(225),
emp_age int,
emp_sal varchar(225), 
emp_Vehical varchar(225));

insert into employee values (1, "sandy", 32, 130000, "Honda Activa");
insert into employee values (2, "harsha", 34, 200000, "Aprilla");
insert into employee values (3, "salim", 29, 190000, "Brezza");
insert into employee values (4, "chandu", 28, 110000, "Pulsar");
insert into employee values (5, "mudda", 26, 145000, "Honda Activa");
insert into employee values (6,"Venky", 27, 250000 , "Brezza");

#select * from employee;
#select * from employee where emp_Vehical == "Brezza" and not emp_sal == 250000;
-- select * from employee order by emp_sal desc;
-- select * from employee order by emp_sal ;
-- update employee set emp_sal = 250000 where emp_name == "salim";
-- select * from employee;
-- delete from employee where emp_name == "chandu";
-- select * from employee;
-- select * from employee limit 4;
-- select min(emp_sal) from employee;
-- select count(emp_sal) from employee where emp_sal <150000;
-- select avg(emp_sal) from employee where emp_sal <150000;
-- select sum(emp_sal) from employee where emp_sal <150000;
-- select * from employee where emp_Vehical in ("Brezza");
-- select * from employee where emp_sal between 100000 and 150000;
-- select * from employee where emp_sal between 100000 and 150000 and emp_Id not in (3, 4, 5);
-- select * from employee where emp_sal between 100000 and 199999 order by emp_age;



