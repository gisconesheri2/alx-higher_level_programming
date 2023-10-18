-- show tv_shows with at least one genre
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
