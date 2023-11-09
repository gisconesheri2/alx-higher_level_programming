-- show genres not linked to show 'Dexter'
SELECT tg.name
FROM tv_genres AS tg
LEFT JOIN 
	(SELECT tsg.genre_id
	FROM tv_show_genres AS tsg
	INNER JOIN tv_shows AS ts
	ON ts.id = tsg.show_id
	WHERE ts.title = "Dexter") AS dexter_genres (id)
ON tg.id = dexter_genres.id
WHERE dexter_genres.id IS NULL
ORDER BY tg.name ASC;
