Use Practical;
GO

-- Create a database to manage services offered by a Tax management company. The database will store data about all the intermediaries involved. 
-- The entities of interest to the problem domain are: TaxCompany, Clients, Assets and SRLs(companies opened by the Tax company for their clients).
-- A tax company has a name, number of clients and number of opened SRLs(each client has a number of companies(SRLs) opened in his name).
-- A tax company can have multiple clients, a client can work only with one tax company. 
CREATE TABLE TaxCompanies (
    TaxCompanyID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    NumOfClients INT DEFAULT 0,
    OpenedSRLs INT DEFAULT 0
); 

-- A client has an ID, identification number and the amount of money sent to the tax company(money at his disposal). 
-- Furthermore, a client can have multiple assets and multiple SRLs opened. 

CREATE TABLE Clients (
    ClientID INT PRIMARY KEY,
    TaxCompanyID INT,
    IdentificationNumber VARCHAR(25) UNIQUE NOT NULL,
    MoneyForTax INT,
    FOREIGN KEY (TaxCompanyID) REFERENCES TaxCompanies(TaxCompanyID)
);

-- Assets have a name, number of assets for each client and a location (the location of the SRL to which the assets were added). 

CREATE TABLE Assets (
    AssetID INT PRIMARY KEY,
    ClientID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    NumOfAssets INT DEFAULT 1,
    Location VARCHAR(255),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- SRLs have a name, an activity and a location (place where the company is established).

CREATE TABLE SRLs (
    SRLID INT PRIMARY KEY,
    ClientID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Activity VARCHAR(255),
    Location VARCHAR(255),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) 
);

-- Mock Data for TaxCompanies
INSERT INTO TaxCompanies (TaxCompanyID, Name, NumOfClients, OpenedSRLs)
VALUES 
(1, 'Alpha Tax Solutions', 2, 3),
(2, 'Beta Tax Services', 1, 1);

-- Mock Data for Clients
INSERT INTO Clients (ClientID, TaxCompanyID, IdentificationNumber, MoneyForTax)
VALUES 
(1, 1, '123456789', 10000),
(2, 1, '987654321', 15000),
(3, 2, '456789123', 5000);

-- Mock Data for SRLs
INSERT INTO SRLs (SRLID, ClientID, Name, Activity, Location)
VALUES 
(1, 1, 'Alpha Innovations', 'Technology', 'New York'),
(2, 1, 'Alpha Trading', 'Retail', 'San Francisco'),
(3, 2, 'Beta Ventures', 'Consulting', 'Chicago'),
(4, 3, 'Gamma Enterprises', 'Logistics', 'Houston');

-- Mock Data for Assets
INSERT INTO Assets (AssetID, ClientID, Name, NumOfAssets, Location)
VALUES 
(1, 1, 'Office Building', 1, 'New York'),
(2, 1, 'Delivery Trucks', 5, 'New York'),
(3, 2, 'Warehouse', 1, 'Chicago'),
(4, 3, 'Fleet Vehicles', 10, 'Houston');


-- 1. Write a SQL script that creates the corresponding relational data model.
-- 2. Implement a stored procedure that receives a client and returns the number of assets owned and the number of SRLs opened in his name.

DROP PROCEDURE IF EXISTS ClientAssetsAndSRLs;
GO

CREATE PROCEDURE ClientAssetsAndSRLs (
    @ClientID INT
)
AS
BEGIN
    DECLARE @AssetsCount INT;
    DECLARE @SRLsCount INT;

    SELECT @AssetsCount = SUM(A.NumOfAssets)
    FROM Assets A
    WHERE A.ClientID = @ClientID;

    SELECT @SRLsCount = COUNT(*)
    FROM SRLs S
    WHERE S.ClientID  = @ClientID

    BEGIN
        PRINT 'ClientID: ' + CAST(@ClientID AS VARCHAR(10)) + ' | Assets: ' + CAST(@AssetsCount AS VARCHAR(10)) + ' | SRLs: ' + CAST(@SRLsCount AS VARCHAR(10))
    END
END

EXEC ClientAssetsAndSRLs @ClientID = 1;
EXEC ClientAssetsAndSRLs @ClientID = 2;
EXEC ClientAssetsAndSRLs @ClientID = 3;
GO
-- 3. Create a view that shows client's identification number and amount of money owned, also the name and activity of all the SRLs opened in his name.
DROP VIEW [ClientActivity];
GO

CREATE VIEW ClientActivity AS
    SELECT
        C.ClientID,
        C.IdentificationNumber,
        C.MoneyForTax,
        S.Activity
    FROM Clients C
    JOIN SRLs S ON S.ClientID = C.ClientID
GROUP BY C.IdentificationNumber, C.ClientID, C.MoneyForTax, S.Activity
GO

SELECT * FROM ClientActivity;
GO

-- 4. Implement a function that lists the identification numbers of the clients and the location of all the SRLs opened 
-- in his name and in addition the number of assets for each SRL.
DROP FUNCTION ClientsLocation;
GO

CREATE FUNCTION ClientsLocation ()
RETURNS @Result TABLE (
    ClientID INT,
    IdentificationNumber VARCHAR(25),
    SRLLocation VARCHAR(255),
    NumAssets INT
)
AS
BEGIN
    INSERT INTO @Result
        SELECT
            C.ClientID,
            C.IdentificationNumber,
            S.Location as SRLLocation,
            COALESCE(SUM(A.NumOfAssets), 0) AS NumAssets
        FROM Clients C 
        LEFT JOIN SRLs S ON S.ClientID = C.ClientID
        LEFT JOIN Assets A ON A.Location = S.Location
        GROUP BY C.ClientID, C.IdentificationNumber, S.Location;
    RETURN;
END
GO

SELECT dbo.ClientsLocation();
