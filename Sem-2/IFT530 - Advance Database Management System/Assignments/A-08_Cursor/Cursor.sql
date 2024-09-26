/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 03/02/2024
*/


-- Question - 1
DECLARE GuitarCursor CURSOR FOR
    SELECT LastName, AVG(ShipAmount) AS ShipAmountAvg
    FROM Customers JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
    GROUP BY LastName;

-- Open the cursor
OPEN GuitarCursor

-- Fetch each row
WHILE @@FETCH_STATUS = 0
BEGIN
    FETCH NEXT FROM GuitarCursor
END

-- Close and deallocate the cursor
CLOSE GuitarCursor
DEALLOCATE GuitarCursor




-- Question - 2

DECLARE GuitarShopCursor CURSOR FOR
    SELECT LastName, AVG(ShipAmount) AS ShipAmountAvg
    FROM Customers JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
    GROUP BY LastName;

-- Declare local variables
DECLARE @LocalLastName VARCHAR(255);
DECLARE @LocalShipAmountAvg DECIMAL(10, 2);

-- Open the cursor
OPEN GuitarShopCursor;

-- Fetch each row into local variables
FETCH NEXT FROM GuitarShopCursor INTO @LocalLastName, @LocalShipAmountAvg;

-- Loop through the result set
WHILE @@FETCH_STATUS = 0
BEGIN
PRINT @LocalLastName + ', $' + CAST(@LocalShipAmountAvg AS NVARCHAR(20)) ;
FETCH NEXT FROM GuitarShopCursor INTO @LocalLastName, @LocalShipAmountAvg;
END

-- Close and deallocate the cursor
CLOSE GuitarShopCursor;
DEALLOCATE GuitarShopCursor;
