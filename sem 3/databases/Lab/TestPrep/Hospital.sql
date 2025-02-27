-- Create a database for a hospital management system. The entities of interest to the problem domain are: Patients, Doctors, Medications, Appointments and Prescriptions. A patient has an ID, a name, a date of birth and a gender. IDs are unique. A doctor has a name and a department. A medication has a name and a manufacturer. Names are unique. The system stores data about scheduled appointments between patients and doctors and it will store the date and time for each appointment. A prescription represents the medication that was prescribed during the appointment, including the dosage.
-- 1. Write an SQL script that creates the corresponding relational data model.
-- 2. Implement a stored procedure that receives a patient, a doctor and a date-time and creates a new appointment. If there is already an appointment for the same doctor and patient, the date of the existing appointment is updated.
-- 3. Create a view that shows the names of the doctors with scheduled appointments during the month of February, 2024.
-- 4. Implement a function that returns the total count of each medication prescribed by a doctor D across all appointments, where D is a function parameter.

USE Practical;
GO

-- 1. Write an SQL script that creates the corresponding relational data model.
-- Create a database for a hospital management system. The entities of interest to the problem domain are: 
-- Patients, Doctors, Medications, Appointments and Prescriptions. 
-- A patient has an ID, a name, a date of birth and a gender. IDs are unique. 

CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    DateOfBirth DATE,
    Gender VARCHAR(10)
);

-- A doctor has a name and a department. 

CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Department VARCHAR(25)
);

-- A medication has a name and a manufacturer. Names are unique. 

CREATE TABLE Medications (
    MedicationID INT PRIMARY KEY,
    Name VARCHAR(255) UNIQUE NOT NULL,
    Manufacturer VARCHAR(255)
);

-- The system stores data about scheduled appointments between patients and doctors and it will store the date and time for each appointment. 

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    PatientID INT,
    DoctorID INT,
    DateAndTime DATETIME,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- A prescription represents the medication that was prescribed during the appointment, including the dosage.

CREATE TABLE Prescriptions (
    PrescriptionID INT PRIMARY KEY,
    AppointmentID INT,
    MedicationID INT,
    Dosage VARCHAR(50),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID),
    FOREIGN KEY (MedicationID) REFERENCES Medications(MedicationID)
); 

-- 2. Implement a stored procedure that receives a patient, a doctor and a date-time and creates a new appointment. 
-- If there is already an appointment for the same doctor and patient, the date of the existing appointment is updated.

DROP PROCEDURE IF EXISTS ScheduleAppointment;
GO

CREATE PROCEDURE ScheduleAppointment (
    @DoctorID INT,
    @PatientID INT,
    @DateAndTime DATETIME
) 
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Appointments WHERE DoctorID = @DoctorID AND PatientID = @PatientID)
    BEGIN
        UPDATE Appointments
        SET DateAndTime = @DateAndTime
        WHERE DoctorID = @DoctorID AND PatientID = @PatientID
    END
    ELSE
    BEGIN
        INSERT INTO Appointments (PatientID, DoctorID, DateAndTime)
        VALUES (@PatientID, @DoctorID, @DateAndTime)
    END
END;
GO

-- 3. Create a view that shows the names of the doctors with scheduled appointments during the month of February, 2024.

DROP VIEW [ScheduledDoctors];
GO

CREATE VIEW ScheduledDoctors AS
SELECT DISTINCT
    D.Name AS DoctorName
FROM Doctors D
JOIN Appointments A ON D.DoctorID = A.DoctorID
WHERE YEAR(A.DateAndTime) = 2024 AND MONTH(A.DateAndTime) = 2;
GO

-- 4. Implement a function that returns the total count of each medication prescribed by a doctor D across all appointments, where D is a function parameter.
DROP FUNCTION IF EXISTS PrescriptionCount;
GO

CREATE FUNCTION PrescriptionCount (
    @DoctorID INT
)
RETURNS TABLE
AS
RETURN (
    SELECT
        M.Name AS MedicationName,
        COUNT(P.MedicationID) AS PrescriptionCount
    FROM Medications M
    LEFT JOIN Prescriptions P ON M.MedicationID = P.MedicationID
    LEFT JOIN Appointments A ON P.AppointmentID = A.AppointmentID
    WHERE A.DoctorID = @DoctorID
    GROUP BY M.Name
);
GO