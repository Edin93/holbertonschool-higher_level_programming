-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement.
SELECT tvg.name AS name
       FROM tv_genres tvg
       LEFT JOIN tv_show_genres tvsg
       ON tvsg.genre_id = tvg.id
       LEFT JOIN tv_shows tvs
       ON tvs.id = tvsg.show_id
       WHERE NOT EXISTS (
       	     SELECT tvsg.show_id
	     FROM tv_show_genres tvsg
	     WHERE tvs.title = 'Dexter'
       )
       GROUP BY tvg.name
       ORDER BY tvg.name ASC;
