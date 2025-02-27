-- Write your own SQL object definition here, and it'll be included in your package.
CREATE DATABASE Music;
GO

USE Music;
GO

CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY,
    Username VARCHAR(50) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    PasswordHash VARCHAR(50) NOT NULL,
    DateCreated DATE
);

CREATE TABLE Artists (
    ArtistID INT PRIMARY KEY IDENTITY,
    ArtistName VARCHAR(100) NOT NULL,
    Bio VARCHAR(500),
    DateAdded DATE
);

CREATE TABLE Genre (
    GenreID INT PRIMARY KEY IDENTITY,
    GenreName VARCHAR(100) NOT NULL
);

CREATE TABLE Albums (
    AlbumID INT PRIMARY KEY IDENTITY,
    AlbumName VARCHAR(100) NOT NULL,
    ReleaseDate DATE,
    ArtistID INT FOREIGN KEY REFERENCES Artists(ArtistID),
    GenreID INT FOREIGN KEY REFERENCES Genre(GenreID)
);

CREATE TABLE Tracks (
    Track_ID INT PRIMARY KEY IDENTITY,
    TrackName VARCHAR(100),
    Duration INT,
    AlbumId INT,
    FOREIGN KEY (AlbumId) REFERENCES Albums(AlbumID)
);

CREATE TABLE Playlists (
    Playlist_ID INT PRIMARY KEY IDENTITY,
    PlaylistName VARCHAR(100),
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES Users(UserID)
);

CREATE TABLE Playlist_Tracks (
    PlaylistID INT,
    TrackID INT,
    PRIMARY KEY (PlaylistID, TrackID),
    FOREIGN KEY (PlaylistID) REFERENCES Playlists(Playlist_ID),
    FOREIGN KEY (TrackID) REFERENCES Tracks(Track_ID)
);

CREATE TABLE User_Favorites (
    UserID INT,
    TrackID INT,
    PRIMARY KEY (UserID, TrackID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (TrackID) REFERENCES Tracks(Track_ID)
);

CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY IDENTITY,
    UserID INT,
    AlbumID INT,
    Rating INT,
    ReviewText VARCHAR(500),
    DateReview DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (AlbumID) REFERENCES Albums(AlbumID)
);

CREATE TABLE Subscriptions (
    SubscriptionID INT PRIMARY KEY IDENTITY,
    UserID INT,
    PlanName VARCHAR(100),
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
