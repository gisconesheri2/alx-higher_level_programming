-- create a table that does not accept NULL values
CREATE TABLE IF NOT EXISTS unique_id(
	id INTEGER DEFAULT 1 UNIQUE,
	name VARCHAR(256));
