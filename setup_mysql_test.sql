--a script that prepares a MySQL server for the project:
create database if not exist hbnb_test_db;
create user if not exist 'hbnb_test'@'localhost' identified by hbnb_test_pwd;
grant all privilages on hbnb_test_db . * to 'hbnb_test'@'localhost';
grant select on performance_schema . * to 'hbnb_test'@'localhost';
