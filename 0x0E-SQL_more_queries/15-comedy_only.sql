#!/usr/bin/python3
-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM
    tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
    ORDER BY tv_shows.title;
