USE Music;
GO

DROP PROCEDURE IF EXISTS changeTypeOfGenreNameTypeChar
DROP PROCEDURE IF EXISTS changeTypeOfGenreNameTypeVarchar
DROP PROCEDURE IF EXISTS addPriceToSubscription
DROP PROCEDURE IF EXISTS removePriceFromSubscription
DROP PROCEDURE IF EXISTS addDefaultPlanDesc
DROP PROCEDURE IF EXISTS removeDefaultPlanDesc
DROP PROCEDURE IF EXISTS createSongAwards
DROP PROCEDURE IF EXISTS dropSongAwards
DROP PROCEDURE IF EXISTS addPrimaryKey
DROP PROCEDURE IF EXISTS removePrimaryKey
DROP PROCEDURE IF EXISTS addCandidateSubscription
DROP PROCEDURE IF EXISTS removeCandidateSubscription
DROP PROCEDURE IF EXISTS addForeignKey
DROP PROCEDURE IF EXISTS removeForeignKey
DROP PROCEDURE IF EXISTS createTables
DROP PROCEDURE IF EXISTS dropTables
DROP PROCEDURE IF EXISTS goToVersion
GO

-- modify the type of a column
CREATE PROCEDURE changeTypeOfGenreNameTypeChar AS
    ALTER TABLE Genre ALTER COLUMN GenreName char(10)
    PRINT 'GenreNameType changed'
GO

CREATE PROCEDURE changeTypeOfGenreNameTypeVarchar AS
    ALTER TABLE Genre ALTER COLUMN GenreName varchar(100)
    PRINT 'GenreNameType changed back'
GO

-- add / remove column
CREATE PROCEDURE addPriceToSubscription AS
    ALTER TABLE Subscriptions ADD Price INT
    PRINT 'Price added to Subscriptions'
GO

CREATE PROCEDURE removePriceFromSubscription AS
    ALTER TABLE Subscriptions DROP COLUMN Price
    PRINT 'Priced dropped from Subscriptions'
GO

-- add remove a default constraint
CREATE PROCEDURE addDefaultPlanDesc AS
    ALTER TABLE Subscriptions ADD CONSTRAINT Price DEFAULT 0 FOR Price
    PRINT 'add default 0 for price'
GO

CREATE PROCEDURE removeDefaultPlanDesc AS
    ALTER TABLE Subscriptions DROP CONSTRAINT Price
    PRINT 'dropped default price'
GO

-- add / remove primary key
CREATE PROCEDURE createSongAwards AS
BEGIN
    CREATE TABLE Songs_Awards(
        SongID int NOT NULL,
        SongName VARCHAR(100) NOT NULL,
        Awards INT
    );
    PRINT 'Created songAwards'
END;
GO

CREATE PROCEDURE dropSongAwards AS
BEGIN
    DROP TABLE IF EXISTS Songs_Awards;
    PRINT 'Dropped songAwards'
END;
GO

CREATE PROCEDURE addPrimaryKey AS
BEGIN
    ALTER TABLE Songs_Awards
    ADD CONSTRAINT PK_Songs_Awards PRIMARY KEY (SongName);
    PRINT 'add primary key'
END;
GO

CREATE PROCEDURE removePrimaryKey AS
BEGIN
    ALTER TABLE Songs_Awards
    DROP CONSTRAINT PK_Songs_Awards;
    PRINT 'dropped primary key'
END;
GO


-- add / remove candidate key
CREATE PROCEDURE addCandidateSubscription AS
    ALTER TABLE Subscriptions
    ADD CONSTRAINT SubUser UNIQUE (SubscriptionID, UserID)
    PRINT 'add candidate key'
GO

CREATE PROCEDURE removeCandidateSubscription AS
    ALTER TABLE Subscriptions
    DROP CONSTRAINT SubUser
    PRINT 'drop candidate key'
GO

-- add / remove foreign key
CREATE PROCEDURE addForeignKey AS
    ALTER TABLE Songs_Awards
    ADD CONSTRAINT SongID FOREIGN KEY (SongID) REFERENCES Tracks(Track_ID)
    PRINT 'foreign key added'
GO

CREATE PROCEDURE removeForeignKey AS
    ALTER TABLE Songs_Awards
    DROP CONSTRAINT SongID
    PRINT 'foreign key removed'
GO

-- create and drop table 
CREATE PROCEDURE createTables AS
    CREATE TABLE MockTable(
        value int,
        PRIMARY KEY(value)
    );
    INSERT INTO MockTable VALUES(0);
    PRINT 'Table created'
GO

-- CREATE TABLE PROCEDURES_TABLE(
-- 	fromVersion INT,
-- 	toVersion INT,
-- 	nameProc VARCHAR(255),
-- 	PRIMARY KEY(fromVersion, toVersion)
-- );
-- GO

CREATE PROCEDURE dropTables AS
    DROP TABLE IF EXISTS MockTable;
    -- DROP TABLE IF EXISTS PROCEDURES_TABLE;
    PRINT 'Table dropped'
GO

CREATE PROCEDURE goToVersion(@newVersion INT) AS
BEGIN
    DECLARE @currentVersion INT;
    DECLARE @procName VARCHAR(255);
    SELECT @currentVersion = version FROM VERSION_TABLE;

    IF @newVersion > (SELECT MAX(toVersion) FROM PROCEDURES_TABLE)
    BEGIN
        RAISERROR('Invalid version', 16, 1);
        RETURN;
    END;

    IF @currentVersion = @newVersion
    BEGIN
        PRINT 'Already at the requested version.';
        RETURN;
    END;

    IF @newVersion < (SELECT MIN(fromVersion) FROM PROCEDURES_TABLE)
    BEGIN
        RAISERROR('Invalid version', 16, 1);
        RETURN;
    END;

    WHILE @currentVersion < @newVersion 
    BEGIN
        SELECT @procName = nameProc 
        FROM PROCEDURES_TABLE 
        WHERE fromVersion = @currentVersion AND toVersion = @currentVersion + 1;

        -- Safely execute the procedure
        BEGIN TRY
            PRINT 'Executing: ' + @procName;
            EXEC(@procName);
            SET @currentVersion = @currentVersion + 1;
            UPDATE VERSION_TABLE SET version = @currentVersion;
        END TRY
        BEGIN CATCH
            PRINT 'Error executing procedure: ' + @procName;
            PRINT ERROR_MESSAGE();
            RETURN;
        END CATCH;
    END;

    WHILE @currentVersion > @newVersion 
    BEGIN
        SELECT @procName = nameProc 
        FROM PROCEDURES_TABLE 
        WHERE fromVersion = @currentVersion AND toVersion = @currentVersion - 1;

        BEGIN TRY
            PRINT 'Executing: ' + @procName;
            EXECUTE @procName;
            SET @currentVersion = @currentVersion - 1;
            UPDATE VERSION_TABLE SET version = @currentVersion;
        END TRY
        BEGIN CATCH
            PRINT 'Error executing procedure: ' + @procName;
            PRINT ERROR_MESSAGE();
            RETURN;
        END CATCH;
    END;
END;
GO

-- EXECUTE dropTables;
-- GO

-- EXECUTE createTables;
-- GO

-- SELECT * FROM VERSION_TABLE
-- SELECT * FROM PROCEDURES_TABLE

EXECUTE goToVersion 2;
GO

-- ALTER TABLE Subscriptions DROP COLUMN Price
-- SELECT * FROM Subscriptions
