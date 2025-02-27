USE Music;
GO

SELECT * FROM Playlist_Tracks

 /*
a table with a single-column primary key and no foreign keys; - Genre (1PK, no FK -> PK: GenreID)
a table with a single-column primary key and at least one foreign key; - Albums (one pk + 1 PK + FK -> AlbumID)
a table with a multicolumn primary key; - Playlist_Tracks (2 PK -> (PlaylistID, TrackID))
 */

 /*
a view with a SELECT statement operating on one table;
a view with a SELECT statement that operates on at least 2 different tables and contains at least one JOIN operator;
a view with a SELECT statement that has a GROUP BY clause, operates on at least 2 different tables and contains at least one JOIN operator.
 */
drop procedure addToViews
drop procedure addToTests
drop procedure addToTables
drop procedure connectTableToTest
drop procedure connectViewsToTest
drop procedure if exists runTest
go

CREATE TABLE Tables (
    TableID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Views (
    ViewID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Tests (
    TestID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE TestTables (
    TestID INT,
    TableID INT,
    NoOfRows INT,
    Position INT,
    PRIMARY KEY (TestID, TableID),
    FOREIGN KEY (TestID) REFERENCES Tests(TestID),
    FOREIGN KEY (TableID) REFERENCES Tables(TableID)
);

CREATE TABLE TestViews (
    TestID INT,
    ViewID INT,
    PRIMARY KEY (TestID, ViewID),
    FOREIGN KEY (TestID) REFERENCES Tests(TestID),
    FOREIGN KEY (ViewID) REFERENCES Views(ViewID)
);

CREATE TABLE TestRuns (
    TestRunID INT IDENTITY(1,1) PRIMARY KEY,
    Description VARCHAR(255),
    StartAt DATETIME,
    EndAt DATETIME
);

CREATE TABLE TestRunTables (
    TestRunID INT,
    TableID INT,
    StartAt DATETIME,
    EndAt DATETIME,
    PRIMARY KEY (TestRunID, TableID),
    FOREIGN KEY (TestRunID) REFERENCES TestRuns(TestRunID),
    FOREIGN KEY (TableID) REFERENCES Tables(TableID)
);

CREATE TABLE TestRunViews (
    TestRunID INT,
    ViewID INT,
    StartAt DATETIME,
    EndAt DATETIME,
    PRIMARY KEY (TestRunID, ViewID),
    FOREIGN KEY (TestRunID) REFERENCES TestRuns(TestRunID),
    FOREIGN KEY (ViewID) REFERENCES Views(ViewID)
);
GO

CREATE PROCEDURE addToTables(@tableName varchar(255))
AS
    -- check if the table exists or is already in the Tables
    if @tableName not in (select TABLE_NAME from INFORMATION_SCHEMA.Tables)
    BEGIN
        print 'Table does not exist'
        return
    END
    if @tableName in (select Name from Tables)
    BEGIN
        print 'Table already in Tables'
        return
    END
    -- insert it into Tables
    INSERT into Tables (Name) values (@tableName) 
GO

CREATE PROCEDURE addToViews(@viewName varchar(255))
AS
    -- check if the view exists or is already in the Views
    if @viewName not in (select TABLE_NAME from INFORMATION_SCHEMA.VIEWS)
    BEGIN
        print 'View does not exist'
        return 
    END
    if @viewName in (select Name from Views)
    BEGIN
        print 'View already in Views'
        return 
    END
    -- insert it into Views
    insert into Views (Name) values (@viewName)
GO

create procedure addToTests(@testName varchar(255))
AS
    -- check if it exists already
    if @testName in (select Name from Tests)
    BEGIN
        print 'Test already exists'
        return 
    end
    insert into Tests (Name) values (@testName)
go

create procedure connectTableToTest(@tableName varchar(255), @testName varchar(255), @rows int, @pos int)
AS
    -- check if the table and test exist
    if @tableName not in (select Name from Tables)
    BEGIN   
        print 'Table does not exist'
        return 
    END
    if @testName not in (SELECT Name from Tests)
    BEGIN
        print 'Test does not exist'
        RETURN
    END
    -- get the IDs
    declare @tableID int
    declare @testID INT
    set @tableID = (select TableID from Tables where Name=@tableName)
    set @testID = (select TestID from Tests where Name=@testName)
    -- check if we already have this pair
    if exists (select * from TestTables
        where TestID=@testID and TableID=@tableID)
    BEGIN   
        print 'the connection is already in the TestTable'
        return 
    END
    -- insert it
    insert into TestTables values (@testID, @tableID, @rows, @pos)
go

create procedure connectViewsToTest(@viewName varchar(255), @testName varchar(255))
AS
    -- check if the table and test exist
    if @viewName not in (select Name from Views)
    BEGIN   
        print 'View does not exist'
        return 
    END
    if @testName not in (SELECT Name from Tests)
    BEGIN
        print 'Test does not exist'
        RETURN
    END
    -- get the IDs
    declare @viewID int
    declare @testID INT
    set @viewID = (select ViewID from Views where Name=@viewName)
    set @testID = (select TestID from Tests where Name=@testName)
    -- check if we already have this pair
    if exists (select * from TestViews
        where TestID=@testID and ViewID=@viewID)
    BEGIN   
        print 'the connection is already in the TestView'
        return 
    END
    -- insert it
    insert into TestViews values (@testID, @viewID)
go

CREATE PROCEDURE runTest(@testName VARCHAR(255), @description VARCHAR(255))
AS
BEGIN
    -- Validate if the test exists
    IF NOT EXISTS (SELECT 1 FROM Tests WHERE Name = @testName)
    BEGIN
        PRINT 'Test not in Tests';
        RETURN;
    END

    -- Variables
    DECLARE @testID INT, @testRunID INT;
    DECLARE @tableID INT, @tableName NVARCHAR(255), @rows INT, @pos INT;
    DECLARE @viewID INT, @viewName NVARCHAR(255);
    DECLARE @startTime DATETIME, @endTime DATETIME;

    -- Get the TestID
    SET @testID = (SELECT TestID FROM Tests WHERE Name = @testName);

    -- Log the test run
    SET @startTime = SYSDATETIME();
    INSERT INTO TestRuns (Description, StartAt, EndAt) VALUES (@description, @startTime, NULL);
    SET @testRunID = SCOPE_IDENTITY();

    -- Deletion in reverse dependency order
    DECLARE deletionCursor CURSOR FOR
    SELECT T1.Name, T1.TableID
    FROM Tables T1
    INNER JOIN TestTables T2 ON T1.TableID = T2.TableID
    WHERE T2.TestID = @testID
    ORDER BY T2.Position DESC;

    OPEN deletionCursor;
    FETCH NEXT FROM deletionCursor INTO @tableName, @tableID;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        BEGIN TRY
            EXEC('DELETE FROM ' + @tableName);
        END TRY
        BEGIN CATCH
            PRINT 'Error deleting from table ' + @tableName + ': ' + ERROR_MESSAGE();
        END CATCH;

        FETCH NEXT FROM deletionCursor INTO @tableName, @tableID;
    END;

    CLOSE deletionCursor;
    DEALLOCATE deletionCursor;

    -- Insertion in forward dependency order
    DECLARE insertionCursor CURSOR FOR
    SELECT T1.Name, T1.TableID, T2.NoOfRows
    FROM Tables T1
    INNER JOIN TestTables T2 ON T1.TableID = T2.TableID
    WHERE T2.TestID = @testID
    ORDER BY T2.Position ASC;

    OPEN insertionCursor;
    FETCH NEXT FROM insertionCursor INTO @tableName, @tableID, @rows;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @startTime = SYSDATETIME();
        BEGIN TRY
            EXEC('EXEC populateTable ' + @tableName + ', ' + @rows);
        END TRY
        BEGIN CATCH
            PRINT 'Error populating table ' + @tableName + ': ' + ERROR_MESSAGE();
        END CATCH;
        SET @endTime = SYSDATETIME();

        -- Log performance for table insertion
        INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt) VALUES (@testRunID, @tableID, @startTime, @endTime);

        FETCH NEXT FROM insertionCursor INTO @tableName, @tableID, @rows;
    END;

    CLOSE insertionCursor;
    DEALLOCATE insertionCursor;

    -- Evaluate views
    DECLARE viewCursor CURSOR FOR
    SELECT V.Name, V.ViewID
    FROM Views V
    INNER JOIN TestViews TV ON V.ViewID = TV.ViewID
    WHERE TV.TestID = @testID;

    OPEN viewCursor;
    FETCH NEXT FROM viewCursor INTO @viewName, @viewID;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @startTime = SYSDATETIME();
        BEGIN TRY
            EXEC('SELECT * FROM ' + @viewName);
        END TRY
        BEGIN CATCH
            PRINT 'Error executing view ' + @viewName + ': ' + ERROR_MESSAGE();
        END CATCH;
        SET @endTime = SYSDATETIME();

        -- Log performance for view execution
        INSERT INTO TestRunViews (TestRunID, ViewID, StartAt, EndAt) VALUES (@testRunID, @viewID, @startTime, @endTime);

        FETCH NEXT FROM viewCursor INTO @viewName, @viewID;
    END;

    CLOSE viewCursor;
    DEALLOCATE viewCursor;

    -- End the test run
    SET @endTime = SYSDATETIME();
    UPDATE TestRuns SET EndAt = @endTime WHERE TestRunID = @testRunID;

    PRINT 'Test run completed successfully.';
END;
GO

-- create procedure dropExistingProcedure(@tableName varchar(255))
-- AS
--     if exists(select * from INFORMATION_SCHEMA.ROUTINES
--     where ROUTINE_NAME=@tableName)
--     BEGIN
--         exec('drop procedure '+@tableName)
--     END
-- GO

-- create procedure dropExistingView(@viewName varchar(255))
-- AS
--     if exists(select * from INFORMATION_SCHEMA.ROUTINES
--     where ROUTINE_NAME=@viewName)
--     BEGIN
--         exec('drop view '+@viewName)
--     END
-- GO

create PROCEDURE populateTableGenre(@rows int)
AS
    declare @idx INT
    set @idx=0
    while @idx<@rows BEGIN
        insert into Genre (GenreName) 
        VALUES('Genre'+cast(@idx as varchar(255)))
        set @idx=@idx+1
    END
GO

drop PROCEDURE populateTableAlbums
go 

create PROCEDURE populateTableAlbums(@rows int)
AS
BEGIN
    declare @idx INT
    declare @artistCount INT
    declare @artistID INT
    declare @currentArtistIdx INT
    declare @currentGenIdx INT
    declare @gen INT
    declare @genCount INT

    set @idx = 0
    set @currentArtistIdx = 0
    set @currentGenIdx = 0
    set @artistCount = (select COUNT(*) from Artists)
    set @genCount = (select COUNT(*) from Genre)

    IF @artistCount = 0
    BEGIN
        PRINT 'Error: No artists exist in the Artists table. Cannot populate Albums.'
        RETURN
    END

    while @idx < @rows 
    BEGIN
        set @artistID = (select ArtistID from Artists 
                        ORDER BY ArtistID 
                        OFFSET @currentArtistIdx ROWS FETCH NEXT 1 ROWS ONLY)
        set @gen = (select GenreID from Genre
                    ORDER BY GenreID
                    OFFSET @currentGenIdx ROWS FETCH NEXT 1 ROWS ONLY)
        insert into Albums (AlbumName, ReleaseDate, ArtistID, GenreID) 
        VALUES ('Album' + cast(@idx as varchar(255)), 
                '2020-01-01', 
                @artistID, 
                @gen)

        set @currentArtistIdx = (@currentArtistIdx + 1) % @artistCount
        set @currentGenIdx = (@currentGenIdx + 1) % @genCount
        set @idx = @idx + 1
    END
END
GO


DELETE from User_Favorites
DELETE From Tracks
delete from Albums
delete from Genre
delete from Playlist_Tracks

exec populateTableGenre 5
select * from Genre

exec populateTableAlbums 100
select * from Albums
go

drop PROCEDURE populateTableTracks
go

create PROCEDURE populateTableTracks(@rows int)
AS
    declare @idx INT
    declare @album INT
    DECLARE @albumIdx INT
    DECLARE @albumCount INT

    set @albumCount = (select COUNT(*) from Albums)
    set @idx=0
    set @albumIdx = 0
    while @idx<@rows BEGIN
        set @album = (select AlbumID from Albums
                    ORDER BY AlbumID
                    OFFSET @albumIdx ROWS FETCH NEXT 1 ROWS ONLY)
        insert into Tracks (TrackName, Duration, AlbumId) 
        VALUES('Track'+cast(@idx as varchar(255)), 300, @album)
        set @idx=@idx+1
        set @albumIdx = (@albumIdx + 1) % @albumCount
    END
GO

-- drop PROCEDURE populateTablePlaylistTracks
-- go

CREATE PROCEDURE populateTablePlaylistTracks(@rows int)
as 
    declare @playlistIdx INT
    declare @trackIdx INT
    declare @playlistCnt INT
    declare @trackCnt INT

    set @playlistIdx=0
    set @trackIdx=0

    set @playlistCnt=(select count(*) from Playlists)
    set @trackCnt=(select count(*) from Tracks)

    while @playlistIdx<@playlistCnt and @rows>0
    begin 
        set @trackIdx=0
        while @trackIdx<@trackCnt and @rows>0
        BEGIN
            insert into Playlist_Tracks (PlaylistID, TrackID)
            values(@playlistIdx, @trackIdx)
            set @trackIdx=@trackIdx+1
            set @rows=@rows-1
        END
        set @playlistIdx=@playlistIdx+1
    END
GO

create VIEW GenreView
AS
    select * from Genre
GO

-- view with select that operates on 2 tables and at least one join
drop view PlaylistUserView
go
create view PlaylistUserView
AS
    select p.UserId, p.PlaylistName, u.Username
    from Playlists p join Users u on p.UserId=u.UserID
go
select * from PlaylistUserView
go

-- view with a select statement that has a GROUP BY clause, operates on at least 2 different tables and contains at least one join operator
create or alter view PlaylistUserGroupedView
AS
    select p.UserId, p.PlaylistName, u.Username
    from Playlists p join Users u on p.UserId=u.UserID
    group by p.UserId,  p.PlaylistName, u.Username
go
select * from PlaylistUserGroupedView

-- delete procedure populateTable if exists
IF EXISTS (SELECT *
FROM INFORMATION_SCHEMA.ROUTINES
WHERE ROUTINE_NAME = 'populateTable') BEGIN
	EXEC ('DROP PROCEDURE populateTable')
END
GO

-- create procedure to poplate tables, generally
CREATE PROCEDURE populateTable(@tableName VARCHAR(255), @rows INT)
AS
    IF @tableName NOT IN (SELECT Name
    FROM Tables) BEGIN
        PRINT 'Table not in Tables'
        RETURN
    END
    DECLARE @i INT
    SET @i = 0


    PRINT 'Populating table ' + @tableName + ' with ' + CAST(@rows AS VARCHAR(255)) + ' rows'

    -- -- get the columns of the table
    DECLARE @columns TABLE (
        ColumnName VARCHAR(255),
        DataType VARCHAR(255),
        OrdinalPosition INT
    )
    if @tableName='Genre'
    BEGIN
        exec populateTableGenre @rows
    END
    if @tableName='Albums'
    BEGIN
        exec populateTableAlbums @rows
    END
    if @tableName='Tracks'
    BEGIN
        exec populateTableTracks @rows
    END
    if @tableName='Playlist_Tracks'
    BEGIN
        exec populateTablePlaylistTracks @rows
    END
GO

delete from Genre
delete from Albums
delete from Tracks
delete from Playlist_Tracks
delete from TestTables
go

exec addToTables 'Genre'
exec addToTables 'Albums'
exec addToTables 'Tracks'
exec addToTables 'Playlist_Tracks'


exec addToViews 'GenreView'
exec addToViews 'PlaylistUserView'
exec addToViews 'PlaylistUserGroupedView'

-- test1
exec addToTests 'MainTest'

exec connectTableToTest 'Genre', 'MainTest', 5, 1
exec connectTableToTest 'Albums', 'MainTest', 5, 2
exec connectTableToTest 'Tracks', 'MainTest', 5, 3
exec connectTableToTest 'Playlist_Tracks', 'MainTest', 5, 4

exec connectViewsToTest 'GenreView', 'MainTest'
exec connectViewsToTest 'PlaylistUserView', 'MainTest'
exec connectViewsToTest 'PlaylistUserGroupedView', 'MainTest'

EXEC runTest 'MainTest', 'Test1'
GO

-- test2
exec addToTests 'MainTest2'

exec connectTableToTest 'Genre', 'MainTest2', 100, 1
exec connectTableToTest 'Albums', 'MainTest2', 100, 2
exec connectTableToTest 'Tracks', 'MainTest2', 100, 3
exec connectTableToTest 'Playlist_Tracks', 'MainTest2', 100, 4

exec connectViewsToTest 'GenreView', 'MainTest2'
exec connectViewsToTest 'PlaylistUserView', 'MainTest2'
exec connectViewsToTest 'PlaylistUserGroupedView', 'MainTest2'

EXEC runTest 'MainTest2', 'Test2'
GO

-- test3
exec addToTests 'MainTest3'

exec connectTableToTest 'Genre', 'MainTest3', 500, 1
exec connectTableToTest 'Albums', 'MainTest3', 500, 2
exec connectTableToTest 'Tracks', 'MainTest3', 500, 3
exec connectTableToTest 'Playlist_Tracks', 'MainTest3', 500, 4

exec connectViewsToTest 'GenreView', 'MainTest3'
exec connectViewsToTest 'PlaylistUserView', 'MainTest3'
exec connectViewsToTest 'PlaylistUserGroupedView', 'MainTest3'

EXEC runTest 'MainTest3', 'Test3'
GO

delete from TestRuns
delete from TestRunTables
delete from TestRunViews

select * from TestRuns
select * from TestRunTables
select * from TestRunViews

select * from Genre
select * from Albums
select * from Tracks
select * from Playlist_Tracks

delete from Tracks
delete from Albums
exec populateTableAlbums 5
exec populateTableTracks 10

delete from TestRuns
delete from TestRunTables
delete from TestRunViews
delete from TestTables
delete from TestViews
delete from Views
delete from Tables
delete from Tests


SELECT * FROM TestRuns


SELECT tr.TestRunID, t.Name AS TableName, trt.StartAt, trt.EndAt
FROM TestRunTables trt
JOIN TestRuns tr ON trt.TestRunID = tr.TestRunID
JOIN Tables t ON trt.TableID = t.TableID


SELECT tr.TestRunID, v.Name AS ViewName, trv.StartAt, trv.EndAt
FROM TestRunViews trv
JOIN TestRuns tr ON trv.TestRunID = tr.TestRunID
JOIN Views v ON trv.ViewID = v.ViewID