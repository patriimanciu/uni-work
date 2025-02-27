USE Music;
GO 

-- Users that have pop tracks as favorite
SELECT u.Username, u.Email
FROM Users u
WHERE u.UserID IN (
    SELECT uf.UserID
    FROM User_Favorites uf
    WHERE TrackID IN (
        SELECT t.Track_ID
        FROM Tracks t
        JOIN Albums a ON t.AlbumID = a.AlbumID
        JOIN Genre g ON a.GenreID = g.GenreID
        WHERE g.GenreID = 1006
    )
)

-- Tracks realeased after 2015 from american singers
SELECT TrackName, Duration
FROM Tracks
WHERE AlbumId IN (
    SELECT AlbumId
    FROM Albums
    WHERE ReleaseDate > '2015-01-01'
    AND ArtistID IN (
        SELECT ArtistID
        FROM Artists
        WHERE Bio LIKE 'American%'
    )
);