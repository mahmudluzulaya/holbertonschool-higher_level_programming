-- This script creates the table 'id_not_null' in the specified database.
-- The table has two columns:
--   1. id INT with a default value of 1
--   2. name VARCHAR(256)
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
