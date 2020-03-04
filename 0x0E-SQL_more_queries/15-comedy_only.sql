-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- I can use only one SELECT statement.
SELECT tvs.title
       FROM tv_shows tvs
       LEFT JOIN tv_show_genres tvsg
       ON tvsg.show_id = tvs.id
       LEFT JOIN tv_genres tvg
       ON tvsg.genre_id = tvg.id
       WHERE tvg.name = 'Comedy'
       ORDER BY tvs.title ASC;
