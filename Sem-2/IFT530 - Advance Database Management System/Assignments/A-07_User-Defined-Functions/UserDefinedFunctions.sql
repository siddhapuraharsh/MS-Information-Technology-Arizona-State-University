/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 02/25/2024
*/


-- Question - 5
CREATE FUNCTION fnUnpaidInvoiceID()
RETURNS INT
AS
BEGIN
    DECLARE @InvoiceID INT;
    SELECT TOP 1 @InvoiceID = InvoiceID
        FROM Invoices
    WHERE (InvoiceTotal - CreditTotal - PaymentTotal) > 0
        ORDER BY InvoiceDate ASC;
    RETURN @InvoiceID;
END;
GO


SELECT VendorName, InvoiceNumber, InvoiceDueDate,
    InvoiceTotal - CreditTotal - PaymentTotal AS Balance
FROM Vendors v
    JOIN Invoices i
        ON v.VendorID = i.VendorID
WHERE InvoiceID = dbo.fnUnpaidInvoiceID();
GO



-- Question - 6
CREATE FUNCTION fnDateRange(@StartDate DATE, @EndDate DATE)
RETURNS TABLE
AS
RETURN
(
    SELECT InvoiceNumber, InvoiceDate, InvoiceTotal, InvoiceTotal - CreditTotal - PaymentTotal AS Balance
    FROM Invoices
    WHERE InvoiceDate BETWEEN @StartDate AND @EndDate
);
GO

SELECT * FROM fnDateRange('2022-10-10', '2022-10-20');



-- Question - 7
SELECT DISTINCT v.VendorName, fn.InvoiceNumber, fn.InvoiceDate, fn.InvoiceTotal, fn.Balance
FROM Vendors v
JOIN Invoices i ON v.VendorID = i.VendorID
CROSS APPLY fnDateRange('2022-10-10', '2022-10-20') AS fn
WHERE i.InvoiceNumber = fn.InvoiceNumber;
