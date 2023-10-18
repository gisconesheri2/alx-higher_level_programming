-- create a table that does not accept NULL values
CREATE TABLE IF NOT EXISTS force_name(
	id INTEGER,
	name VARCHAR(256) NOT NULL);
