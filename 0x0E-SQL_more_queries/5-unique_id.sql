#!/usr/bin/python3
-- script that creates the table unique_id
-- id INT must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
