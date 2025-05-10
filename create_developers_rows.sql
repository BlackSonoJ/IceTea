INSERT INTO developers (id, name, department, geolocation, last_known_ip, is_available)
SELECT 
    uuid_generate_v4 (),
    (ARRAY['James', 'Mary', 'John', 'Patricia', 'Robert'])[floor(random()*5 + 1)::int] || ' ' || (ARRAY['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'])[floor(random()*5 + 1)::int],
    (ARRAY['backend', 'frontend', 'ios', 'android'])[floor(random()*4 + 1)::int],
    point(
        ROUND((random() * 180 - 90)::numeric, 6),
        ROUND((random() * 360 - 180)::numeric, 6)
    ),
    (
        (floor(random()*256)::int)::text || '.' ||
        (floor(random()*256)::int)::text || '.' ||
        (floor(random()*256)::int)::text || '.' ||
        (floor(random()*256)::int)::text
    )::inet,
    (random() > 0.5)
FROM generate_series(1, (floor(random() * 9000) + 1000)::int);