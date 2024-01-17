-- List genres and the number of shows linked to each
SELECT g.genre AS genre,
       COUNT(s.id) AS number_of_shows
FROM tv_show_genres AS g
INNER JOIN tv_shows AS s ON g.show_id = s.id
GROUP BY g.genre
ORDER BY number_of_shows DESC;
