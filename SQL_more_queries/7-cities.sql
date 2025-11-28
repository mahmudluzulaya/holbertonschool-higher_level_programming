-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to using the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table 'cities' if it does not exist
-- Columns:
--   id: INT, primary key, unique, auto-increment, cannot be null
--   state_id: INT, cannot be null, foreign key referencing states(id)
--   name: VARCHAR(256), cannot be null
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id)
        REFERENCES states(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
