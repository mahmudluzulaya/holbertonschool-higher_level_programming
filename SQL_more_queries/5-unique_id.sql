-- This script creates the table 'unique_id' in the specified database.
-- The table has two columns:
--   1. id INT with a default value of 1 and a UNIQUE constraint to prevent duplicate IDs
--   2. name VARCHAR(256)
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
