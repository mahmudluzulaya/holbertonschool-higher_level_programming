-- This script creates the database 'hbtn_0d_2' if it doesn't exist
-- and creates the MySQL user 'user_0d_2' with password 'user_0d_2_pwd'.
-- The user is granted only SELECT privilege on the 'hbtn_0d_2' database.
-- If the database or user already exists, the script will not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
