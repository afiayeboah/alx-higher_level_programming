-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT ts.title, COALESCE(SUM(rate), 0) AS rating
FROM tv_shows AS ts
LEFT JOIN tv_show_ratings AS tr
ON ts.id = tr.show_id
GROUP BY ts.title
ORDER BY rating DESC;
