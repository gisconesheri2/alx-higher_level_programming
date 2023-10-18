-- show all comedy shows
SELECT ts.title
FROM tv_show_genres AS tsg
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
JOIN tv_genres AS tg 
ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
