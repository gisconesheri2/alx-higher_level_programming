-- Database + tables to test
DROP DATABASE IF EXISTS test_1;
CREATE DATABASE IF NOT EXISTS test_1;
USE test_1;

CREATE TABLE IF NOT EXISTS states ( 
	    id INT NOT NULL AUTO_INCREMENT, 
	    name VARCHAR(256) NOT NULL,
	    PRIMARY KEY (id)
	);

	CREATE TABLE IF NOT EXISTS cities ( 
		    id INT NOT NULL AUTO_INCREMENT, 
		    state_id INT NOT NULL,
		    name VARCHAR(256) NOT NULL,
		    PRIMARY KEY (id),
		    FOREIGN KEY(state_id) REFERENCES states(id)
		);
