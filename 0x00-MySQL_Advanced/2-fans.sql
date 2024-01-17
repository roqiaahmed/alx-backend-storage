-- ranks country origins of bands
-- Script that creates a table bands
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;