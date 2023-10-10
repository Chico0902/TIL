-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

SELECT
FirstName AS '이름'

FROM employees;

-- 02. Sorting data
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC
  City ASC;

SELECT
  Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시

SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering dataz
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company is NULL
  AND Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
Bytes BETWEEN 10000 <= Bytes <= 500000;


SELECT
  Name, Bytes
FROM
  tracks
WHERE
Bytes BETWEEN 10000 <= Bytes <= 500000
ORDER BY
  Bytes BETWEEN 10000 AND400000;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country = 'Canada'
  OR Country = 'Geramny'
  Or Country = 'France';


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada','Geramny','France')

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '___a';

SELECT
  TrackId, Namem, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3,4;
-- LIMIT 4 OFFSET 3;


-- 04. Grouping data

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
  Composer
FROM
  tracks
GROUP BY
  Composer
ORDER BY
AVG(bytes) DESC;


SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;


-- 에러


-- 에러 해결
