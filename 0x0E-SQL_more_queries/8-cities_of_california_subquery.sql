-- This Code Created By Mokhtar Tiouiri
-- More SQL!
-- More SQL!
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
