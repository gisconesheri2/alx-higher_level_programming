-- shows that are not comedies
SELECT ts.title
FROM tv_shows AS ts
LEFT JOIN 
	(SELECT tsg.show_id
	FROM tv_show_genres AS tsg
	INNER JOIN tv_genres AS tg
	ON tg.id = tsg.genre_id
	WHERE tg.name = "Comedy") AS comedy_shows (id)
ON ts.id = comedy_shows.id
WHERE comedy_shows.id IS NULL
ORDER BY ts.title ASC;
