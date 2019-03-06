-- Selects all cities of California in table
SELECT id, name
FROM cities
WHERE state_id = (SELECT ID FROM states WHERE name = 'California') GROUP BY id ORDER BY id ASC;
