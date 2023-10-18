-- show all comedy shows
SELECT ts.title
FROM tv_show_genres AS tsg
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE tsg.genre_id = 
	(SELECT id
	 FROM tv_genres
	 WHERE name = 'Comedy')
ORDER BY ts.title ASC;
