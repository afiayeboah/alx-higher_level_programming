-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_shows AS ts
WHERE ts.id NOT IN (
    SELECT tsg.show_id
    FROM tv_show_genres AS tsg
    JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
    WHERE tg.name = 'Comedy'
)
ORDER BY ts.title;
