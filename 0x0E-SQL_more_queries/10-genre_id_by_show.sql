-- Import the database dump from hbtn_0d_tvshows to MySQL
-- server hbtn_0d_tvshows.sql
-- lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by
-- tv_shows.title and tv_show_genres.genre_id
-- I can use only one SELECT statement.
SELECT tvs.title, tvsg.genre_id
       FROM tv_shows tvs
       LEFT JOIN tv_show_genres tvsg
       ON tvs.id = tvsg.show_id
       WHERE tvsg.genre_id IS NOT NULL
       ORDER BY tvs.title ASC, tvsg.genre_id ASC;
