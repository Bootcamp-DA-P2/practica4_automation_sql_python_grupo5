SELECT
    c.customer_id,
    LOWER(TRIM(c.first_name)) AS first_name,
    LOWER(TRIM(c.last_name)) AS last_name,
    LOWER(TRIM(c.email)) AS email,
    c.active,
    LOWER(TRIM(a.address)) AS address,
    COALESCE(NULLIF(LOWER(TRIM(a.district)), ''), 'sin datos') AS district,
    a.postal_code,
    LOWER(TRIM(ci.city)) AS city,
    LOWER(TRIM(co.country)) AS country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE c.customer_id IS NOT NULL
  AND c.address_id IS NOT NULL
  AND c.email IS NOT NULL;
