-- mport in hbtn_0c_0 database file named "temperatures.sql"
-- Write a script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).
use hbtn_0c_0;
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY state ORDER BY value DESC;
