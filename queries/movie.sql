SELECT
    f.film_id,
    f.title,
    f.release_year,
    f.length,
    f.rating,
    cat.name AS category,
    l.name AS language
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
JOIN language l ON f.language_id = l.language_id;