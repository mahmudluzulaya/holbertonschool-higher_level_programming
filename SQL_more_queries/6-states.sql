-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to using the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table 'states' if it does not exist
-- Columns:
--   id: INT, primary key, unique, auto-increment, cannot be null
--   name: VARCHAR(256), cannot be null
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
