-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- I can use only one SELECT statement.
SELECT tvs.title, tvg.name
       FROM tv_shows tvs
       LEFT JOIN tv_show_genres tvsg
       ON tvs.id = tvsg.show_id
       LEFT JOIN tv_genres tvg
       ON tvsg.genre_id = tvg.id
       ORDER BY tvs.title ASC;
