-- List all genres not linked to the show Dexter
SELECT tg.name
FROM tv_genres AS tg
WHERE tg.id NOT IN (
    SELECT tsg.genre_id
    FROM tv_show_genres AS tsg
    JOIN tv_shows AS ts
ON tsg.show_id = ts.id
    WHERE ts.title = 'Dexter'
)
ORDER BY tg.name;
