/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 02/11/2024
*/

--Exercise 1
DECLARE @IncCount INT;
DECLARE @TotalDue INT;

SELECT @IncCount = COUNT(CreditTotal), @TotalDue = SUM(CreditTotal) FROM Invoices 
WHERE CreditTotal > 0.0;

IF @TotalDue >= 30000.0
BEGIN
    PRINT 'Invoice count: ' + CAST(@IncCount AS VARCHAR);
    PRINT 'Total Due: ' + CAST(@TotalDue AS VARCHAR);
END
ELSE
BEGIN
    PRINT 'Total balance due is less than $30,000';
END


--Exercise 2
DECLARE @TotalBal INT

SELECT @TotalBal = SUM(i.CreditTotal)
FROM Invoices i
JOIN Vendors v ON i.VendorID = v.VendorID
WHERE i.CreditTotal > 0;

IF @TotalBal > 10000.00
BEGIN
    SELECT v.VendorName, i.InvoiceNumber, i.InvoiceDueDate, i.CreditTotal
    FROM Invoices i
    JOIN Vendors v ON i.VendorID = v.VendorID
    WHERE i.CreditTotal > 0
    ORDER BY i.InvoiceDueDate;
END
ELSE
BEGIN
    PRINT 'Balance due is less than $10,000.00'
END


--Exercise 3
USE AP;

IF OBJECT_ID('tempdb..#TempFirstInvoice') IS NOT NULL
    DROP TABLE #TempFirstInvoice;

CREATE TABLE #TempFirstInvoice
(
    VendorID INT,
    FirstInvoiceDate DATE
);

INSERT INTO #TempFirstInvoice (VendorID, FirstInvoiceDate)
SELECT VendorID, MIN(InvoiceDate) AS FirstInvoiceDate
FROM Invoices
GROUP BY VendorID;

SELECT v.VendorName, tfi.FirstInvoiceDate, i.InvoiceTotal
FROM Invoices i 
JOIN #TempFirstInvoice tfi ON i.VendorID = tfi.VendorID AND i.InvoiceDate = tfi.FirstInvoiceDate
JOIN Vendors v ON i.VendorID = v.VendorID
ORDER BY v.VendorName, tfi.FirstInvoiceDate;

DROP TABLE #TempFirstInvoice;