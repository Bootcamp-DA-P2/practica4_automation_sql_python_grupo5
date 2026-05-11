SELECT
    f.film_id,
    LOWER(TRIM(f.title)) AS title,
    f.release_year,
    f.length,
    f.rating,
    LOWER(TRIM(cat.name)) AS category,
    LOWER(TRIM(l.name)) AS language
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
JOIN language l ON f.language_id = l.language_id
WHERE f.film_id IS NOT NULL
  AND f.release_year IS NOT NULL
  AND f.length > 0
  AND f.rating IS NOT NULL;
