SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    c.active,

    a.address,
    a.district,
    a.postal_code,

    ci.city,
    co.country,

    r.rental_id,
    r.rental_date,
    r.return_date,

    p.payment_id,
    p.payment_date,
    p.amount
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id;