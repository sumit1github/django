# install

  sudo apt install mysql-client-core-8.0 
  docker pull mysql

# run the container
  docker run -d --name=mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql

# connect with mysql server
  mysql -h 127.0.0.1 -u root -p

# create database
  CREATE DATABASE yourdbname;
  SHOW DATABASES;


# stop and delete
docker stop mysql-container
docker rm mysql-container
