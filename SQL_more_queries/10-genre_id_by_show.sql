-- List all shows with at least one genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Sorted by tv_shows.title ASC, then genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
