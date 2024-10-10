SELECT
    p.package_type as package_type,
    SUM(CASE WHEN MONTH(b.booking_date) BETWEEN 1 AND 3 THEN 1 ELSE 0 END) AS spring_bookings,
    SUM(CASE WHEN MONTH(b.booking_date) BETWEEN 4 AND 6 THEN 1 ELSE 0 END) AS summer_bookings,
    SUM(CASE WHEN MONTH(b.booking_date) BETWEEN 7 AND 9 THEN 1 ELSE 0 END) AS autumn_bookings,
    SUM(CASE WHEN MONTH(b.booking_date) BETWEEN 10 AND 12 THEN 1 ELSE 0 END) AS winter_bookings,
    ROUND(AVG(c.rating_score), 2) AS average_rating
FROM
    tourism_packages p
LEFT JOIN
    bookings b ON p.package_id = b.package_id
LEFT JOIN
    customer_ratings c ON b.booking_id = c.booking_id
GROUP BY
    p.package_type
ORDER BY
    MIN(p.package_id)