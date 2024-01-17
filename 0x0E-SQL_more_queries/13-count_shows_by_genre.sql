-- List genres and the number of shows linked to each
SELECT tg.name AS genre,
       COUNT(ts.id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE tsg.show_id IS NOT NULL
GROUP BY tg.name
ORDER BY number_of_shows DESC;

