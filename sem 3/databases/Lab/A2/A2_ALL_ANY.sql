USE Music;
GO

-- duration of any track is greater than the average duration of all tracks
SELECT AlbumId, TrackName, Duration
FROM Tracks
WHERE Duration > ANY (
    SELECT AVG(Duration)
    FROM Tracks
);

SELECT AlbumId, TrackName, Duration
FROM Tracks
WHERE Duration > (
    SELECT AVG(Duration)
    FROM Tracks
);


-- Albums for which the average duration of tracks is greater than the total average
SELECT AlbumId, SUM(Duration) AS TotalAlbumDuration, AVG(Duration) AS AlbumAverage
FROM Tracks
GROUP BY AlbumId
HAVING AVG(Duration) > ALL (
    SELECT AVG(Duration)
    FROM Tracks
);

SELECT AlbumId, SUM(Duration) AS TotalAlbumDuration, AVG(Duration) AS AlbumAverage
FROM Tracks
GROUP BY AlbumId
HAVING AVG(Duration) > (
    SELECT AVG(Duration)
    FROM Tracks
);

-- Tracks that are not the longest in their album
SELECT TrackName, Duration
FROM Tracks
WHERE Duration != ALL (
    SELECT MAX(Duration)
    FROM Tracks
    GROUP BY AlbumId
);

SELECT TrackName, Duration
FROM Tracks
WHERE Duration NOT IN (
    SELECT MAX(Duration)
    FROM Tracks
    GROUP BY AlbumId
);


-- All tracks greater than all duration from album 52
SELECT AlbumId, TrackName, Duration
FROM Tracks
WHERE Duration > ALL (
    SELECT Duration
    FROM Tracks
    WHERE AlbumId = 52
);

SELECT AlbumId, TrackName, Duration
FROM Tracks t1
WHERE NOT EXISTS (
    SELECT 1
    FROM Tracks t2
    WHERE t2.AlbumId = 52 AND t1.Duration <= t2.Duration
);
