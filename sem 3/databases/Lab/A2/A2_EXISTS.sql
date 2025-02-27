USE Music;
GO

-- Albums that have more favorite users
SELECT DISTINCT a.AlbumName, art.ArtistName, a.ReleaseDate
FROM Albums a
JOIN Tracks t ON a.AlbumID = t.AlbumId
JOIN Artists art ON art.ArtistID = a.ArtistID
WHERE EXISTS (
    SELECT 1
    FROM User_Favorites f
    JOIN User_Favorites f2 ON f.TrackID=f2.TrackID AND f.UserID <> f2.UserID -- different users
    WHERE f.TrackID = t.Track_ID
);

-- Users who have Playlists that contain Drake tracks
SELECT u.Username, u.Email
FROM Users u
WHERE EXISTS (
    SELECT 1
    FROM Playlists p
    JOIN Playlist_Tracks pt ON p.Playlist_ID = pt.PlaylistID
    JOIN Tracks t ON pt.TrackID = t.Track_ID
    JOIN Albums a ON t.AlbumId = a.AlbumID
    JOIN Artists ar ON a.ArtistID = ar.ArtistID
    WHERE p.UserId = u.UserID AND ar.ArtistID = 1022
);
