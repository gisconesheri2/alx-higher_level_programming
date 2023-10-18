select t.name 
from tv_genres as t
join tv_show_genres AS tsg
on t.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
order by t.name
