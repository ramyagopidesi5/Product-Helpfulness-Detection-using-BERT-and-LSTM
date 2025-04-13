drop database if exists amazontweet;
create database amazontweet;
use amazontweet;

CREATE TABLE User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL,
    age INT,
    contact VARCHAR(20)
);