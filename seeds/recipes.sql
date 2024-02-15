-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name text,
  average_cooking_time INTERVAL,
  rating numeric(2,1)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Spaghetti Carbonara', '30 minutes', 4.0);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Beef Stew', '4 hours', 3.2);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Roast Chicken', '2 hours 30 minutes', 3.8);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Lamb & Beef Lasanga', '2 hours', 4.5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Bengali Chicken Curry', '1 hour 15 minutes', 5.0);
