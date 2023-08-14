# create a table
1. need to assign fields with datatypes
2. Must set a primary key with not null
3. Foreign key is optional

`CMD`  
CREATE TABLE student
roll INT NOT NULL
name VARCHAR(50) NOT NULL
age INT

PRIMARY KEY (roll);


# create a table with foreign key

`CMD`
CREATE TABLE student
roll INT NOT NULL
name VARCHAR(50) NOT NULL
age INT
class_id INT    `need to create the filed`

PRIMARY KEY(roll)
FORIGN KEY (class_id) REFERENCE CLASS(class_id);  `make it as foreign key use the parent table target key`