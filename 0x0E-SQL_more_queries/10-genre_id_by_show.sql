-- This Code Created By Mokhtar Tiouiri
-- More SQL!
-- More SQL!
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities JOIN states WHERE cities.state_id = states.id ORDER BY cities.id ASC;

