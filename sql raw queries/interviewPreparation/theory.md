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


# diffrence beetween primary key and unique key

`primary key`
1. only one primary key can present in a row
2. can not accept NULL values
3. creactes clustered index
4. creation: `PRIMARY KEY(roll)`

`unique key`
1. multiple unique key can present in a row
2. can accept 1 NULL values (only 1 row of the table can contain NULL value)
3. creactes clustered index
4. creation: `UNIQUE(roll)`

# diffrence beetween DROP , Delete, Truncate
`DROP`
1. it is used to delete : entire table or database
`cmd` : 
a. DROP DATABASE database_name;   to delete database
b. DROP TABLE table_name;


`DELETE`
1. it is used to delete : one or more rows of a table
`cmd` : DELETE FROM customer_table WHERE name='sumit';

`Truncate`
1. it is used to delete all the data inside the table
`cmd` : TRUNCATE TABLE table_name;

# what are the diffrent types of languages are available in DBMS
`1) Data Definition Language (DDL)`:
CREATE, ALTER, DROP, TRUNCATE

`2)Data-Manipulation Language (DML)`
INSERT, UPDATE, DELETE

`3) Data Control Language (DCL)`
REVOKE, GRANT

`4) Transaction Control Language (TCL)`
COMMIT, ROLLBACK, SHAREPOINT

`5) Data Query Language (DQL)`
SELECT

# diffrence beetween 'UNION' and 'UNION ALL'

`UNION`: used to combain the results of two select statements, `without returning any duplicate rows`

cmd: 
SELECT CITY FROM customer_table
UNION
SELECT CITY FROM supplier_table
ORDER BY City;


`UNION ALL`: used to combain the results of two select statements, `including duplicate rows`

cmd: 
SELECT CITY FROM customer_table
UNION ALL
SELECT CITY FROM supplier_table
ORDER BY City;


# What are ACID properties in DBMS

`A -> Atomicity` : Either all success or fails then rollback/ restart. No other condition is there.

`C -> Consistency`: Data is consistence before and after a transaction. 
transaction is success : Database will go to a new stable stage
transaction is failed : Database will go to a previous stable stage because of roll-back.

`I-> Isolation` : Multiple transaction is going on in a time but without interfering to each other.

`D -> Durability` : It ensures that committed changes are saved successfully and data base will survive even after system crash.

# what are the different types of relation in the DBMS

`one to one` : where one row of table1 is related with another row of table2 or vice versa.
-> Here the foreign_key filed must be Unique-Key

`one to many` : where one row of table1 is related with multiple rows of table2 or vice versa.

`many to many` : where multiple rows of table1 is related with multiple row of table2 or vice versa.

# what is super key ?
Super key combination of 2 keys.
note** : `First key ill always be a candidate key`

# what is candidate key ?
In a table it is possible to have more than one unique key.
So apart from the primary key, other keys are called candidate key.

# what are the constraints?

Helps to specify the limits on the datatype,

NOT NULL, DEFAULT, INDEX, UNIQUE, CHECK

# Clustered Index vs non-Clustered Index

`Clustered Index`:
1. to use easy retrieval of data from database but it is fast.
2. it alters the way the records are stored in the database.
3. one table can have only one clustered index.

`non-Clustered Index`:
1. to use easy retrieval of data from database but it is slow.
2. it not alters the way the records are stored in the database.
3. one table can have multiple clustered index.

# how to print date in sql
SQL comes with in-build function called GetDate()
`cmd:  SELECT GETDATE();`


