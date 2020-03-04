-- lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- I can use only one SELECT statement
SELECT tvs.title, tvsg.genre_id
       FROM tv_shows tvs
       LEFT JOIN tv_show_genres tvsg
       ON tvs.id = tvsg.show_id
       ORDER BY tvs.title ASC, tvsg.genre_id ASC;
