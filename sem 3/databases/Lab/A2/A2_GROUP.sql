USE Music;
GO

-- Number of tracks in each album 
SELECT TOP 5 AlbumId, COUNT(*) AS TrackCount
FROM Tracks
GROUP BY AlbumId
ORDER BY TrackCount DESC;

-- Albums that have at least 2 tracks
SELECT AlbumID, COUNT(Track_ID) AS TrackCount, SUM(Duration) AS TotalDuration
FROM Tracks
GROUP BY AlbumID
HAVING COUNT(Track_ID) >= 2;

-- Duration of the max song of album
-- Why when addinf the name it crashes???
SELECT AlbumId, MAX(Duration) AS MaxTrackDuration, AVG(Duration) AS AverageDuration
FROM Tracks
GROUP BY AlbumId
HAVING MAX(Duration) > (
    SELECT AVG(Duration)
    FROM Tracks
);

-- Total duration in all albums
SELECT TOP 50 PERCENT AlbumId, SUM(Duration) AS TotalAlbumDuration
FROM Tracks
GROUP BY AlbumId
HAVING SUM(Duration) > (
    SELECT AVG(Duration)
    FROM Tracks
)
ORDER BY TotalAlbumDuration DESC;
