-- Lists the scores and number of instances sorted by frequency
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
