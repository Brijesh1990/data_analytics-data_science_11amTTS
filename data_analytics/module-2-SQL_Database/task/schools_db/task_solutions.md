**solutions**
1. create database school
2. create table tbl_department(
dep_id int primary key AUTO_INCREMENT,
depname varchar(255)
)
3. create table tbl_faculty(
faculty_id int primary key AUTO_INCREMENT,
name varchar(255)
)

4. create table tbl_country(
cid int primary key AUTO_INCREMENT,
cname varchar(255)
)

6. create table tbl_student(
student_id int primary key AUTO_INCREMENT,
studentname varchar(255),
studentage int,
phone bigint,
grade varchar(255),
address text,
faculty_id int,
dep_id int,
cid int,    
foreign key(faculty_id)  REFERENCES tbl_faculty(faculty_id),
foreign key(dep_id)  REFERENCES tbl_department(dep_id),
foreign key(cid)  REFERENCES tbl_country(cid)

)


7. select student with there countryname 

```
select tbl_student.*,cname from tbl_student join tbl_country on tbl_student.cid=tbl_country.cid

```

8. select avg(studentage) as average_student_age from tbl_student;

9. select count(student_id) as total_students from tbl_student group by cid;

10. select count(student_id),cname from tbl_student join tbl_country on tbl_student.cid=tbl_country.cid  group by cname;

11. select * from tbl_student where grade='A';

12. update tbl_student set grade='A' where student_id=6;

13. delete from  tbl_student  where student_id=6;