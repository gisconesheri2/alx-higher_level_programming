-- show tv_shows with at least one genre
SELECT ts.title, tg.name
FROM tv_genres AS tg
RIGHT JOIN
	(tv_shows AS ts LEFT OUTER JOIN tv_show_genres AS tsg
	ON ts.id = tsg.show_id)
ON tg.id = tsg.genre_id
ORDER BY ts.title ASC, tg.name ASC;
