-- This file is used to generate the 16-no_link.sql file which contains the SQL query to get the top 10 scores from the second_table where the name is not null and not empty.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
