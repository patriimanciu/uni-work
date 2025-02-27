USE Practical;
GO

-- Create a database for a health tracking system. The entities of interest to the problem domain are:
-- Users, Activities, Meals, Health Metrics and User Activities Journal. 
-- A user has a name, an age and a gender. Names are unique. 

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(25) UNIQUE NOT NULL,
    Age INT,
    Gender VARCHAR(10)
);

-- An activity has a name and a number of calories burned per hour. Names are unique. 

CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY,
    Name VARCHAR(255) UNIQUE NOT NULL,
    CalsPerHour INT
);

-- A meal has a name and a number of calories per serving. Names are unique. 

CREATE TABLE Meals (
    MealID INT PRIMARY KEY,
    Name VARCHAR(255) UNIQUE NOT NULL,
    CalsPerServing INT
);

-- The system stores data about health metrics: user, date of recording, weight, blood pressure and heart rate. 

CREATE TABLE HealthMetrics (
    MetricID INT PRIMARY KEY,
    UserID INT,
    DateOfRecording DATE,
    Weight DECIMAL(5, 2),
    BloodPressure VARCHAR(10),
    HeartRate INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Users can perform multiple activities. The system will store the date when the activity was performed and the duration (in minutes).

CREATE TABLE UserActivity (
    EntryID INT PRIMARY KEY,
    UserID INT,
    ActivityID INT,
    DatePerformed DATE,
    Duration INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
);

-- Inserting data into Users table
INSERT INTO Users (UserID, Name, Age, Gender) VALUES
    (1, 'John Doe', 30, 'Male'),
    (2, 'Jane Smith', 25, 'Female');

-- Inserting data into Activities table
INSERT INTO Activities (ActivityID, Name, CalsPerHour) VALUES
    (1, 'Running', 500),
    (2, 'Cycling', 300),
    (3, 'Swimming', 400);

-- Inserting data into Meals table
INSERT INTO Meals (MealID, Name, CalsPerServing) VALUES
    (1, 'Chicken Salad', 350),
    (2, 'Vegetable Stir Fry', 250),
    (3, 'Salmon with Quinoa', 400);

-- Inserting data into HealthMetrics table
INSERT INTO HealthMetrics (MetricID, UserID, DateOfRecording, Weight, BloodPressure, HeartRate) VALUES
    (1, 1, '2024-01-15', 75.0, '120/80', 72),
    (2, 1, '2024-02-01', 74.5, '118/78', 70),
    (3, 2, '2024-01-20', 62.5, '110/75', 65),
    (4, 2, '2024-02-05', 63.0, '112/76', 68);

-- Inserting data into UserActivitiesJournal table
INSERT INTO UserActivity (EntryID, UserID, ActivityID, DatePerformed, Duration) VALUES
    (1, 1, 1, '2024-01-16', 45),
    (2, 1, 2, '2024-01-17', 30),
    (3, 2, 3, '2024-01-21', 60),
    (4, 2, 1, '2024-02-06', 40);

SELECT * FROM Users
SELECT * FROM Activities
SELECT * FROM Meals
SELECT * FROM HealthMetrics
SELECT * FROM UserActivity


-- 2. Implement a stored procedure that receives the details of a health metric and adds the metric
-- in the database. If the date of recording is in the future (e.g. today is 05-01-2024 and the date of
-- recording for the health metric is 06-01-2024), the system will display an error message and it
-- will not save the health metric in the database.

DROP PROCEDURE IF EXISTS AddHealthMetric;
GO

CREATE PROCEDURE AddHealthMetric (
    @HealthMetricID INT,
    @UserID INT,
    @DateOfRecording DATE,
    @Weight DECIMAL(5, 2),
    @BloodPressure VARCHAR(10),
    @HeartRate INT
) AS 
BEGIN
    IF @DateOfRecording > GETDATE()
    BEGIN
        PRINT 'Error: Date is in the future';
        RETURN;
    END

    INSERT INTO HealthMetrics (MetricID, UserID, DateOfRecording, Weight, BloodPressure, HeartRate) 
    VALUES (@HealthMetricID, @UserID, @DateOfRecording, @Weight, @BloodPressure, @HeartRate);
END;
GO

-- good
EXEC AddHealthMetric @HealthMetricID = 100, @UserID = 1, @DateOfRecording = '2025-01-04', @Weight = 50.9, @BloodPressure = '120/80', @HeartRate = 84;
-- error
EXEC AddHealthMetric @HealthMetricID = 30, @UserID = 2, @DateOfRecording = '2025-01-01', @Weight = 65.2, @BloodPressure = '110/75', @HeartRate = 80;
EXEC AddHealthMetric @HealthMetricID = 301, @UserID = 2, @DateOfRecording = '2025-01-01', @Weight = 65.2, @BloodPressure = '115/79', @HeartRate = 80;

GO

-- 3. Create a view that displays the average weight and the maximum blood pressure for each user
-- based on the data recorded during the last year (2023).

DROP VIEW [UserAverage];
GO

CREATE VIEW UserAverage AS
SELECT
    UserID,
    AVG(Weight) AS AverageWeight,
    MAX(BloodPressure) AS MaxBloodPressure
FROM HealthMetrics
WHERE DateOfRecording BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY UserID;
GO

SELECT * FROM UserAverage;
GO

-- 4. Implement a function that returns the average duration of a specific activity A for a given user
-- U, where A and U are function parameters.

CREATE FUNCTION GetAverageDuration (
    @UserID INT,
    @ActivityID INT
)
RETURNS DECIMAL(5, 2)
AS
    BEGIN
        DECLARE @AverageDuration DECIMAL(5, 2);

        SELECT @AverageDuration = AVG(Duration) FROM UserActivity
        WHERE UserID = @UserID AND ActivityID = @ActivityID;
        RETURN @AverageDuration;
    END;
GO

DECLARE @AverageDuration DECIMAL(5, 2);
DECLARE @UserID INT = 1; -- Replace with the desired user ID
DECLARE @ActivityID INT = 1; -- Replace with the desired activity ID
SELECT @AverageDuration = dbo.GetAverageDuration(@UserID, @ActivityID);

PRINT 'Average Duration for User ' + CAST(@UserID AS VARCHAR) +
      ' and Activity ' + CAST(@ActivityID AS VARCHAR) +
      ': ' + CAST(@AverageDuration AS VARCHAR);
