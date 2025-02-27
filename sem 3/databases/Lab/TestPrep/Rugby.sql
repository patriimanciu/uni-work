USE Practical;
GO

-- 1. Write a SQL script that creates the corresponding relational data model.
-- Create a database for managing the 2023 Rugby World Cup. The entities of interest to the problem
-- domain are: Cities, Stadiums, National Teams, Players, Coaches and Games. 
-- Cities have a name. Names must be unique.

CREATE TABLE Cities (
    CityID INT PRIMARY KEY,
    Name VARCHAR(100) UNIQUE NOT NULL
);

-- Stadiums have a name and belong to a city. 

CREATE TABLE Stadiums (
    StadiumID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    CityID INT,
    FOREIGN KEY (CityID) REFERENCES Cities(CityID)
);

-- National teams belong to a country and have a list of players and a list of coaches. There can be only one national team per country. 

CREATE TABLE NationalTeams (
    NationalTeamID INT PRIMARY KEY,
    Country VARCHAR(100) NOT NULL,
)

-- Players have a name, birth date, nationality, position and a flag indicating if the player is captain. 

CREATE TABLE Players (
    PlayerID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Birthdate DATE,
    Nationality VARCHAR(100),
    Position VARCHAR(100),
    IsCapitan BIT
);

-- Coaches have a name and nationality. 

CREATE TABLE Coaches (
    CoachID INT PRIMARY KEY,
    Name VARCHAR(100),
    Nationality VARCHAR(100)
);

-- The system stores information about all the games played during the World Cup: the date, the two teams involved, stadium, final score, winner and a
-- flag indicating if the final score was decided in overtime.

CREATE TABLE Games (
    GameID INT PRIMARY KEY,
    DateOfGame DATE,
    Team1ID INT FOREIGN KEY REFERENCES NationalTeams(NationalTeamID),
    Team2ID INT FOREIGN KEY REFERENCES NationalTeams(NationalTeamID),
    StadiumID INT FOREIGN KEY REFERENCES Stadiums(StadiumID),
    FinalScore VARCHAR(20),
    Winner INT FOREIGN KEY REFERENCES NationalTeams(NationalTeamID),
    Overtime BIT
);


-- 2. Implement a stored procedure that receives the details of a game and stores the game in the
-- database. If the two teams already played against each other on the same date, then the final score is
-- updated.

DROP PROCEDURE IF EXISTS LogGame;
GO

CREATE PROCEDURE LogGame (
    @Team1 INT,
    @Team2 INT,
    @DateOfGame DATE,
    @Stadium INT,
    @FinalScore VARCHAR(20),
    @Winner INT,
    @Overtime BIT
)
AS
BEGIN
    DECLARE @ExistingGame INT;
    SELECT @ExistingGame = GameID
    FROM Games 
    WHERE (@Team1 = Team1ID AND @Team2 = Team2ID AND @DateOfGame = DateOfGame) OR
        (@Team2 = Team1ID AND @Team1 = Team2ID AND @DateOfGame = DateOfGame);

    IF @ExistingGame IS NOT NULL
        BEGIN
            UPDATE Games
            SET FinalScore = @FinalScore
            WHERE @ExistingGame = GameID;
        END
    ELSE
        BEGIN
            INSERT INTO Games (DateOfGame, Team1ID, Team2ID, StadiumID, FinalScore, Winner, Overtime) 
            VALUES (@DateOfGame, @Team1, @Team2, @Stadium, @FinalScore, @Winner, @Overtime);
        END
END
GO


-- 3. Create a view that shows the names of the stadiums where all games played were decided in
-- overtime.

CREATE VIEW OvertimeStadiums AS
SELECT DISTINCT S.Name AS StadiumName
FROM Stadiums S
JOIN Games G ON G.StadiumID = S.StadiumID
WHERE G.Overtime = 1;
GO

-- 4. Implement a function that returns the number of teams that won all the games played on a
-- stadium S with a score difference greater than R. where S and R are function parameters.

CREATE FUNCTION TeamsThatWonByR (
    @Stadium VARCHAR(255),
    @R INT
)
RETURNS INT
AS
BEGIN 
    DECLARE @Count INT;
    SELECT @Count = COUNT(S.Winner)
    FROM Stadiums S 
    JOIN Games G ON S.StadiumID = G.StadiumID
    WHERE S.Name = @Stadium AND
    ABS(CONVERT(INT, SUBSTRING(G.FinalScore, 1, CHARINDEX('-', G.FinalScore) - 1)) -
              CONVERT(INT, SUBSTRING(G.FinalScore, CHARINDEX('-', G.FinalScore) + 1, LEN(G.FinalScore)))) > @R;
    RETURN @Count;
END;
GO