USE Music;
GO

-- Artists who have songs both Pop (1006) and R&B (1009)
SELECT ArtistName
FROM Artists 
WHERE ArtistID IN (
    SELECT ArtistID
    FROM Albums
    WHERE GenreID = 1006
)

INTERSECT

SELECT ArtistName
FROM Artists 
WHERE ArtistID IN (
    SELECT ArtistID
    FROM Albums
    WHERE GenreID = 1009
)

-- Pop Albums released after 2020 
SELECT AlbumName, ReleaseDate
FROM Albums
WHERE ReleaseDate >= '2020-01-01'

INTERSECT

SELECT AlbumName, ReleaseDate
FROM Albums
WHERE ArtistID IN (
    SELECT ArtistID
    FROM Albums
    WHERE GenreID = 1006
);