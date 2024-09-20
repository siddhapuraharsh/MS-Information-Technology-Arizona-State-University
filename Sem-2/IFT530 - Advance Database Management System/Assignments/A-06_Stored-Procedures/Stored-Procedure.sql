/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 02/18/2024
*/


--Exercise 1
GO
CREATE PROC spBalanceRange 
    @VendorVar varchar(50) = '%',
    @BalanceMin money = 0,
    @BalanceMax money = 0
AS
BEGIN
    IF @BalanceMax = 0
    BEGIN
        SELECT VendorName, InvoiceNumber, InvoiceTotal - CreditTotal - PaymentTotal AS Balance
        FROM Vendors
        JOIN Invoices ON Vendors.VendorID = Invoices.VendorID
        WHERE VendorName LIKE @VendorVar
            AND (InvoiceTotal - CreditTotal - PaymentTotal) > 0
            AND (InvoiceTotal - CreditTotal - PaymentTotal) >= @BalanceMin
        ORDER BY Balance DESC;
    END;
    ELSE
    BEGIN
        SELECT VendorName, InvoiceNumber, InvoiceTotal - CreditTotal - PaymentTotal AS Balance
        FROM Vendors
        JOIN Invoices ON Vendors.VendorID = Invoices.VendorID
        WHERE VendorName LIKE @VendorVar
            AND (InvoiceTotal - CreditTotal - PaymentTotal) > 0
            AND (InvoiceTotal - CreditTotal - PaymentTotal) BETWEEN @BalanceMin AND @BalanceMax
        ORDER BY Balance DESC;
    END;
END;



--Exercise 2
EXEC spBalanceRange @VendorVar='M%';
EXEC spBalanceRange @BalanceMin = 200, @BalanceMax = 1000;
EXEC spBalanceRange @VendorVar='[C,F]%', @BalanceMax=200;
EXEC spBalanceRange;



--Exercise 3
GO
CREATE PROC spDateRange 
    @DateMin varchar(50) = NULL,
    @DateMax varchar(50) = NULL
AS
BEGIN
    IF @DateMin IS NULL OR @DateMax IS NULL
    BEGIN
        RAISERROR('The DateMin and DateMax are required.',15,1)
        RETURN (@@error)       
    END

    IF NOT (ISDATE(@DateMin) = 1 AND ISDATE(@DateMax) = 1)
    BEGIN
        RAISERROR('The date format is invalid. Please use mm/dd/yy.',15,1)
        RETURN (@@error)
    END

    IF CAST(@DateMin AS datetime) > CAST(@DateMax AS datetime)
    BEGIN
        RAISERROR('The DateMin must be earlier than DateMax.',15,1)
        RETURN (@@error)
    END

    SELECT InvoiceNumber, InvoiceDate, InvoiceTotal, InvoiceTotal - CreditTotal - PaymentTotal AS Balance
    FROM Invoices
    WHERE InvoiceDate BETWEEN @DateMin AND @DateMax
    ORDER BY InvoiceDate;
END;



--Exercise 4
BEGIN TRY
    EXEC spDateRange '10/10/2022', '10/20/2022';
END TRY
BEGIN CATCH
    PRINT 'An error occurred.';
    PRINT 'Error Number: ' + CONVERT(varchar(80), ERROR_NUMBER());
    PRINT 'Error Message: ' + CONVERT(varchar(80), ERROR_MESSAGE());
END CATCH;

EXEC spDateRange;