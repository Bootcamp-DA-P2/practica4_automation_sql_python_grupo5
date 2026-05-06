USE sakila;

SELECT 
    f.film_id, f.title, f.description, f.release_year, f.length, f.rating,
    fc.category_id, cat.name AS category_name,
    l.name AS language_name,
    i.inventory_id
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
JOIN language l ON f.language_id = l.language_id
LEFT JOIN inventory i ON f.film_id = i.film_id;