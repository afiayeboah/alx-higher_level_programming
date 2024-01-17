-- List genres and the number of shows linked to each
SELECT g.name AS genre,
       COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_shows_genre AS t
ON g.id = t.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
