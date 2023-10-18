-- count shows by genre
SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
