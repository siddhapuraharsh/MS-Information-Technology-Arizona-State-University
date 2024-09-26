/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 03/17/2024
*/



-- Question - 1

USE MyGuitarShop;
GO

-- Create the trigger
CREATE TRIGGER Products_UPDATE
ON dbo.Products
FOR UPDATE
AS
BEGIN
    DECLARE @NewDiscountPercent MONEY;

    SELECT @NewDiscountPercent = DiscountPercent
    FROM INSERTED;

    -- Check if the new discount percent is greater than 100 or less than 0
    IF @NewDiscountPercent > 100 OR @NewDiscountPercent < 0
    BEGIN
        RAISERROR('Discount percent must be between 0 and 100.', 16, 1);
        ROLLBACK;
    END;

    -- If the new discount percent is between 0 and 1, multiply it by 100
    IF @NewDiscountPercent >= 0 AND @NewDiscountPercent <= 1
    BEGIN
        UPDATE dbo.Products
        SET DiscountPercent = @NewDiscountPercent * 100
        FROM dbo.Products
        INNER JOIN INSERTED ON dbo.Products.ProductID = INSERTED.ProductID;
    END;
END;


-- Test the trigger with an appropriate UPDATE statement
-- Example 1: Invalid discount percent (greater than 100)
UPDATE dbo.Products
SET DiscountPercent = 150
WHERE ProductID = 1;


-- Example 2: Invalid discount percent (less than 0)
UPDATE dbo.Products
SET DiscountPercent = -10
WHERE ProductID = 1;


-- Example 3: Valid discount percent (between 0 and 1)
UPDATE dbo.Products
SET DiscountPercent = 0.25
WHERE ProductID = 1;

Select * from Products;
GO




-- Question - 2

USE MyGuitarShop;
GO

-- Create the trigger
CREATE TRIGGER Products_INSERT
ON dbo.Products
FOR INSERT
AS
BEGIN
    -- Insert the current date for the DateAdded column if it is null
    UPDATE p
    SET p.DateAdded = GETDATE()
    FROM dbo.Products p
    INNER JOIN INSERTED i ON p.ProductID = i.ProductID
    WHERE p.DateAdded IS NULL;
END;



-- Test the trigger with an appropriate INSERT statement
-- Example:
INSERT INTO dbo.Products (CategoryID, ProductCode, ProductName, Description, ListPrice, DiscountPercent)
VALUES (1, 'PC555', 'Phone case', 'This is a mobile case', 49.99, 0.1);

Select * FROM Products;
