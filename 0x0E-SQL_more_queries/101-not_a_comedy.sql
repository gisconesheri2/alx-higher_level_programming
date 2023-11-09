-- show genres not linked to show 'Dexter'
SELECT ts.title
FROM tv_shows as ts
LEFT JOIN 
	(SELECT tsg.show_id
	FROM tv_show_genres AS tsg
	INNER JOIN tv_genres AS tg
	ON tg.id = tsg.genre_id
	WHERE tg.name = "Comedy") as comedy_shows (id)
ON ts.id = comedy_shows.id
WHERE comedy_shows.id is NULL
ORDER BY ts.title ASC;
