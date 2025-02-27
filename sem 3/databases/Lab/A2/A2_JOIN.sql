USE Music;
GO

-- a) Users, their playlists and the tracks added to them
SELECT 
    u.Username,
    p.PlaylistName,
    t.TrackName
FROM 
    Users u
INNER JOIN 
    Playlists p ON u.UserID = p.UserId
INNER JOIN 
    Playlist_Tracks pt ON p.Playlist_ID = pt.PlaylistID
INNER JOIN 
    Tracks t ON pt.TrackID = t.Track_ID;


-- b) same as a), but also users who haven't added any tracks still appear
SELECT 
    u.Username,
    p.PlaylistName,
    t.TrackName
FROM 
    Users u
LEFT JOIN 
    Playlists p ON u.UserID = p.UserId
LEFT JOIN 
    Playlist_Tracks pt ON p.Playlist_ID = pt.PlaylistID
LEFT JOIN 
    Tracks t ON pt.TrackID = t.Track_ID;


-- c) Users and they favorite tracks, all tracks appear, even if they were not favorited by anyone
SELECT 
    u.Username,
    t.TrackName
FROM 
    Tracks t
RIGHT JOIN 
    User_Favorites uf ON t.Track_ID = uf.TrackID
RIGHT JOIN 
    Users u ON uf.UserID = u.UserID;

-- d) all playlists and all tracks between them
SELECT 
    p.PlaylistName,
    t.TrackName
FROM 
    Playlists p
FULL JOIN 
    Playlist_Tracks pt ON p.Playlist_ID = pt.PlaylistID
FULL JOIN 
    Tracks t ON pt.TrackID = t.Track_ID;
