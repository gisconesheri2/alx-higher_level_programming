-- show genres for a specif show
SELECT tg.name
FROM tv_show_genres AS tsg
INNER JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
WHERE tsg.show_id = -- get id for dexter 
	(SELECT id
	 FROM tv_shows
	 WHERE title = 'Dexter')
ORDER BY tg.name;
