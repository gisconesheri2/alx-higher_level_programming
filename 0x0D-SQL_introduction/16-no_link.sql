-- list all records in second_table which have a name attribute
SELECT score, name
	FROM second_table
	WHERE name != "" 
	ORDER BY score DESC
