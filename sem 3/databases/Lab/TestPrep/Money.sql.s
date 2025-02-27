-- Create a database to manage services offered by a crypto exchange. 
-- The database will store data about all the intermediaries involved in trading. 
-- The entities of interest to the problem domain are : Clients, Accounts, Cryptos, Transactions and Statistics. 
-- A client has a name and unique identification number called ClientID, also each client can only one account. 

CREATE TABLE Clients (
    ClientID INT PRIMARY KEY,
    
)

-- An account has a client identification number (ClientID) and another field call investing moneythe amount of 
-- money added by the client to the account, waiting to be invested). 
-- An account can have multiple types of cryptos bought(Bitcoin, Ethereum and Dodgecoin) and a price to each one of the cryptos mentioned. 
-- An account can have multiple transactions, 3 rowsfields) registered(on Bitcoin, Ethereum or Dodgecoin, also there are two different 
-- transaction types (BUY or SELL, two other rows(fields)).
-- An account can have as well multiple statistics related(number of buy orders, number of sell orders, total number of operations 
-- buy + sell and the amount of money left for investing(initial amount - spent amount(invested money))) .
-- 1. Write a SQL script that creates the corresponding relational data model.
-- 2. Implement a stored procedure that receives a Client and returns all the crypto's names bought by the client and the investing 
-- amount left in his accountinitial amount - invested money).
-- 3. Create a view that shows all the Clients with their identification number and the amount of SELL and BUY transactions performed.
-- 4. Implement a function that lists the identification numbers of the clients which are investing only in Bitcoin and the number of transactions made.
