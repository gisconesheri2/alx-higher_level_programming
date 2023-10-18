-- create database and table 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	state_id INTEGER,
       	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL)
	AUTO_INCREMENT = 1;
