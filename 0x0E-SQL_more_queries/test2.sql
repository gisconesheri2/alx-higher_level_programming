
	SELECT tsg.show_id
	FROM tv_show_genres AS tsg
	INNER JOIN tv_genres AS tg
	ON tg.id = tsg.genre_id
	WHERE tg.name = "Comedy";
