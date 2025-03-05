-- Create a table called second_table with the following columns:
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
