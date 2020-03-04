-- The script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- I can use only one SELECT statement
SELECT tvg.name AS name
       FROM tv_genres tvg
       LEFT JOIN tv_show_genres tvsg
       ON tvsg.genre_id = tvg.id
       WHERE tvsg.show_id = 8
       ORDER BY tvg.name ASC;
