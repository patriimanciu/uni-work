USE Music;
GO

-- Artists released at least one Pop in 2010s
SELECT ArtistName
FROM Artists
WHERE ArtistID IN (
    SELECT ArtistID
    FROM Albums
    WHERE ReleaseDate BETWEEN '2010-01-01' AND '2019-12-31'
)

EXCEPT

SELECT ArtistName
FROM Artists
WHERE ArtistID NOT IN (
    SELECT ArtistID
    FROM Albums
    WHERE GenreID != 1006
);

-- Artists that don't have Pop or K-Pop albums

SELECT ArtistID, ArtistName
FROM Artists

EXCEPT

SELECT ArtistID, ArtistName
FROM Artists
WHERE ArtistID IN (
    SELECT ArtistID
    FROM Albums
    WHERE GenreID = 1010 OR GenreID = 1006
)