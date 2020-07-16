#!/usr/bin/python3
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to them
SELECT tv_genres.name genre, COUNT(*) number_of_shows
    FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre.id
    GROUP BY tv_show_genres.genre_id 
    ORDER BY number_of_shows DESC;
