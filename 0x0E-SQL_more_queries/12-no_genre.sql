-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- I can use only one SELECT statement.
SELECT tvs.title, tvsg.genre_id
       FROM tv_shows tvs
       LEFT JOIN tv_show_genres tvsg
       ON tvs.id = tvsg.show_id
       WHERE tvsg.show_id IS NULL
       ORDER BY tvs.title ASC, tvsg.show_id ASC;
