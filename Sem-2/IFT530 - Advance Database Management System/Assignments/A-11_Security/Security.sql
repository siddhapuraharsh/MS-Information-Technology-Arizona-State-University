/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 03/23/2024
*/



USE AP;
GO

-- Create user-defined database role
CREATE ROLE PaymentEntry;
GO

-- Grant UPDATE permission for Invoices table
GRANT UPDATE ON dbo.Invoices TO PaymentEntry;
GO

-- Grant UPDATE and INSERT permissions for InvoiceLineItems table
GRANT UPDATE, INSERT ON dbo.InvoiceLineItems TO PaymentEntry;
GO

-- Add PaymentEntry role to db_datareader role
EXEC sp_addrolemember 'db_datareader', 'PaymentEntry';
GO




-- 1.Created a login named "AAaron" with password "AAar99999"
USE master;
GO
CREATE LOGIN AAaron WITH PASSWORD = 'AAar99999';
GO


-- 2. Set the default database for the login to the "AP" database
ALTER LOGIN AAaron WITH DEFAULT_DATABASE = AP;
GO



-- 3.Created a user named "AAaron" for the login
USE AP;
GO
CREATE USER AAaron FOR LOGIN AAaron;
GO


-- 4.Assign the user to the "PaymentEntry" role
EXEC sp_addrolemember 'PaymentEntry', 'AAaron';
GO




CREATE TABLE NewLogins (LoginName varchar(128));
INSERT INTO NewLogins VALUES ('BBrown'), ('CChaplin'), ('DDyer'),('EEbbers');

DECLARE @LoginName varchar(128);
DECLARE @SQL nvarchar(max);

DECLARE CursorLogin CURSOR FOR
SELECT LoginName FROM NewLogins;

OPEN CursorLogin;

FETCH NEXT FROM CursorLogin INTO @LoginName;

WHILE @@FETCH_STATUS = 0
BEGIN
    
    DECLARE @Password nvarchar(128) = LEFT(@LoginName, 4) + '99999';
    
    SET @SQL = N'
        USE master;
        CREATE LOGIN ' + QUOTENAME(@LoginName) + ' WITH PASSWORD = N''' + @Password + ''', CHECK_POLICY = OFF;
        ALTER LOGIN ' + QUOTENAME(@LoginName) + ' WITH DEFAULT_DATABASE = AP;
        USE AP;
        CREATE USER ' + QUOTENAME(@LoginName) + ' FOR LOGIN ' + QUOTENAME(@LoginName) + ';
        EXEC sp_addrolemember ''PaymentEntry'', ' + QUOTENAME(@LoginName) + ';
    ';
    EXEC sp_executesql @SQL;
    FETCH NEXT FROM CursorLogin INTO @LoginName;
END

CLOSE CursorLogin;
DEALLOCATE CursorLogin;