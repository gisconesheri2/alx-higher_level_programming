-- show genres for a specif show
SELECT t.name 
FROM tv_genres AS t
JOIN tv_show_genres AS tsg
ON t.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
ORDER BY t.name
