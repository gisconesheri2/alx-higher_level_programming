-- create a table that does not accept NULL values
CREATE TABLE IF NOT EXISTS id_not_null(
	id INTEGER DEFAULT 1,
	name VARCHAR(256));
