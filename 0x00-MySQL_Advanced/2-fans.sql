-- ranks the country origins of bands
-- ordered by the number of (non-unique) fans

-- create temporary table to hold the number of fans per country
CREATE TEMPORARY TABLE IF NOT EXISTS country_fans (
    origin VARCHAR(255),
    nb_fans INT
);

-- insert the number of fans per country
INSERT INTO country_fans (origin, nb_fans)
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin;

-- rank the countries by the number of fans
SELECT origin, nb_fans
FROM country_fans
ORDER BY nb_fans DESC;

-- drop the temporary table
DROP TABLE IF EXISTS country_fans;
