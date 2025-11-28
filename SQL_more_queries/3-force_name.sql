-- This script creates the table 'force_name' in the specified database.
-- The table has two columns: 
--   1. id INT
--   2. name VARCHAR(256) which cannot be NULL
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
