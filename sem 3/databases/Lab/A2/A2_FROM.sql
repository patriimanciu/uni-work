USE Music;
GO

-- Most popular track with details about users
SELECT DISTINCT t.Track_ID, t.TrackName, uf.UserID, u.Username
FROM Tracks t
JOIN (
    SELECT TrackID, COUNT(UserID) as FavCnt
    FROM User_Favorites
    GROUP BY TrackID
    HAVING COUNT(UserID) > 1
) as PopularTracks on t.Track_ID = PopularTracks.TrackID
JOIN User_Favorites uf ON uf.TrackID = t.Track_ID
JOIN Users u ON uf.UserID = u.UserID


-- Users who have at least 2 common favorite tracks
SELECT DISTINCT u1.UserID AS User1ID, u1.UserName AS User1Name, u2.UserID AS User2ID, u2.UserName AS User2Name, shared_tracks.SharedTrackCount
FROM Users u1
JOIN Users u2 ON u1.UserID < u2.UserID
JOIN (
    SELECT f1.UserID AS User1ID, f2.UserID AS User2ID, COUNT(f1.TrackID) AS SharedTrackCount
    FROM User_Favorites f1
    JOIN User_Favorites f2 ON f1.TrackID = f2.TrackID AND f1.UserID < f2.UserID
    GROUP BY f1.UserID, f2.UserID
    HAVING COUNT(f1.TrackID) >= 2
) AS shared_tracks ON u1.UserID = shared_tracks.User1ID AND u2.UserID = shared_tracks.User2ID
ORDER BY shared_tracks.SharedTrackCount DESC;
