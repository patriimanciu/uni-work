USE Music;
GO

-- emails of users who use yahoo or have created their account before 2024-01-04
SELECT Email, DateCreated
FROM Users 
WHERE Email LIKE '%yahoo.com' OR Username = 'drizzy_fanatic'

UNION

SELECT Email, DateCreated
FROM Users
WHERE DateCreated < '2024-01-04';


--  all albums created beween 2020 and 2024 that are Kpop or Are Rock before 2010
SELECT AlbumName, ReleaseDate
FROM Albums
WHERE GenreID = (SELECT GenreID FROM Genre WHERE GenreName = 'K-Pop') 
    OR ReleaseDate BETWEEN '2020-01-01' AND '2023-12-31'

UNION ALL

SELECT AlbumName, ReleaseDate
FROM Albums
WHERE GenreID = (SELECT GenreID FROM Genre WHERE GenreName = 'Rock') 
    OR ReleaseDate < '2010-01-01';

