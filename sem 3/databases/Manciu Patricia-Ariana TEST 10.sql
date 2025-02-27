USE Practical;
GO

CREATE TABLE Children (
    ChildID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    Gender VARCHAR(10),
    DateOfBirth DATE
);

CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    Country VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL
);

CREATE TABLE Chocolate (
    ChocolateID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    ChocoWeight INT,
    Stars INT, 
    ChildID INT,
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID)
);

CREATE TABLE Contest (
    ContestID INT PRIMARY KEY,
    Name VARCHAR(100),
    DateOfContest DATE,
    LocationOfContest INT,
    FOREIGN KEY (LocationOfContest) REFERENCES Location(LocationID)
);

CREATE TABLE ChildrenToContests (
    ChildrenToContestsID INT PRIMARY KEY IDENTITY(1,1),
    ChildID INT,
    ContestID INT,
    DateOfPatricipation DATE,
    NumOfChoco INT,
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID),
    FOREIGN KEY (ContestID) REFERENCES Contest(ContestID),
);
DROP TABLE ChildrenToContests

INSERT INTO Children (ChildID, Name, Surname, Gender, DateOfBirth) VALUES
(1, 'Emily', 'Smith', 'Female', '2012-04-15'),
(2, 'Liam', 'Johnson', 'Male', '2011-06-23'),
(3, 'Sophia', 'Brown', 'Female', '2013-02-11');

INSERT INTO Location (LocationID, Country, City) VALUES
(1, 'USA', 'New York'),
(2, 'Canada', 'Toronto'),
(3, 'UK', 'London');

INSERT INTO Chocolate (ChocolateID, Name, ChocoWeight, Stars, ChildID) VALUES
(1, 'Milk Delight', 120, 5, 1),
(2, 'Choco Bliss', 150, 4, 2),
(3, 'Dark Temptation', 200, 5, 3);

INSERT INTO Contest (ContestID, Name, DateOfContest, LocationOfContest) VALUES
(1, 'National Choco Festival', '2023-05-12', 1),
(2, 'Sweet Tooth Contest', '2023-06-18', 2),
(3, 'Choco Masters Championship', '2023-07-25', 3);

INSERT INTO ChildrenToContests (ChildID, ContestID, DateOfPatricipation, NumOfChoco) VALUES
(1, 1, '2023-05-12', 3),
(2, 1, '2023-06-18', 2),
(3, 3, '2023-07-25', 4);



DROP PROCEDURE IF EXISTS GetChildToContest;
GO

CREATE PROCEDURE GetChildToContest (
    @ChildID INT,
    @ContestID INT,
    @ParticipationDate DATE,
    @NumOfChoco INT
) AS
BEGIN
    IF EXISTS (SELECT 1 FROM ChildrenToContests WHERE @ChildID = ChildID AND @ContestID = ContestID)
    BEGIN
        -- relation exists, update
        UPDATE ChildrenToContests
        SET DateOfPatricipation = @ParticipationDate, NumOfChoco = @NumOfChoco
        WHERE @ChildID = ChildID AND @ContestID = ContestID
    END
    ELSE
    BEGIN
        INSERT INTO ChildrenToContests VALUES
        (@ChildID, @ContestID, @ParticipationDate, @NumOfChoco)
    END
END;

EXEC GetChildToContest @ChildID = 1, @ContestID = 2, @ParticipationDate = '2025-01-04', @NumOfChoco = 4;
EXEC GetChildToContest @ChildID = 2, @ContestID = 1, @ParticipationDate = '2025-01-04', @NumOfChoco = 1;
SELECT * FROM ChildrenToContests




INSERT INTO Location (LocationID, Country, City) VALUES
(4, 'Romania', 'Cluj'),
(5, 'Romania', 'Oradea')

INSERT INTO Contest (ContestID, Name, DateOfContest, LocationOfContest) VALUES
(4, 'Romanian Fav Choco', '2024-12-24', 4),
(5, 'Only RO CHOCO', '2025-02-14', 5);
GO

DROP VIEW [RomanianChocolate];
GO

CREATE VIEW RomanianChocolate AS
SELECT 
    C.ContestID,
    C.Name,
    C.DateOfContest,
    L.Country,
    L.City
FROM Contest C 
JOIN Location L ON L.LocationID = C.LocationOfContest
WHERE L.Country = 'Romania';
GO

SELECT * FROM dbo.RomanianChocolate;
GO

DROP FUNCTION ChildrenAtAllContests;
GO

CREATE FUNCTION ChildrenAtAllContests () 
RETURNS TABLE
AS
RETURN (
        SELECT 
            C.ChildID AS ChildID,
            C.Name AS Name,
            C.Surname AS Surname
        FROM ChildrenToContests CC
        JOIN Children C ON C.ChildID = CC.ChildID
        GROUP BY C.Name, C.Surname, C.ChildID
        HAVING COUNT(*) = (SELECT COUNT(*) FROM Contest)
    );
GO

INSERT INTO ChildrenToContests (ChildID, ContestID, DateOfPatricipation, NumOfChoco) VALUES
(1, 3, '2024-05-12', 1),
(1, 4, '2025-06-18', 2),
(1, 5, '2024-07-25', 3);

SELECT * FROM ChildrenToContests;
SELECT * FROM ChildrenAtAllContests();

