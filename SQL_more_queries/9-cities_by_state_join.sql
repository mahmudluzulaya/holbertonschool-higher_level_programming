-- List all cities with their state names
-- Output: cities.id - cities.name - states.name
-- Sorted by cities.id ascending
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
