-- This Code Created By Mokhtar Tiouiri
-- More SQL!
-- More SQL!
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
