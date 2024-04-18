
-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time VARCHAR(255),
    rating INTEGER
    );

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Spaghetti Bolognaise', '1 hour', 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chicken Tikka Masala', '45 minutes', 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Stir Fry', '25 minutes', 1);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pizza', '15 minutes', 2);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Lemon Garlic Salmon', '20 minutes', 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Beef Stew', '2 hours', 5);
