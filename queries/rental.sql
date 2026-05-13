SELECT
    r.rental_id,
    r.customer_id,
    r.inventory_id,
    i.film_id,

    r.rental_date,
    r.return_date,
    DATEDIFF(r.return_date, r.rental_date) AS rental_duration,

    p.payment_id,
    p.amount,
    p.payment_date,
    DATE(p.payment_date) AS payment_day

FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
WHERE r.return_date IS NOT NULL
  AND p.amount > 0
  AND r.rental_date < r.return_date;
