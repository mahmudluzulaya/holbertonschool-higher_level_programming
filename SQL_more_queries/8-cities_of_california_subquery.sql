-- List all cities of California using a subquery
-- The subquery retrieves the id of California from the states table
-- The outer query selects cities that have a matching state_id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
