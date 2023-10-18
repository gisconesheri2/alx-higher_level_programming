-- show tv_shows with no genre
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
LEFT OUTER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
WHERE tsg.genre_id is NULL
ORDER BY ts.title, tsg.genre_id;
