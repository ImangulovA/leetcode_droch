SELECT 
    ROUND(AVG(lat_n), 4) AS median
FROM
(
    SELECT lat_n, ROW_NUMBER() OVER (ORDER BY lat_n) AS rn
    FROM station
) AS subq
WHERE
    rn = (SELECT CEIL((COUNT(rn)+1)/2) FROM station)
    OR
    rn = (SELECT FLOOR((COUNT(rn)+1)/2) FROM station)