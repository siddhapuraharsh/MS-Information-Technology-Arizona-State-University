/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 03/23/2024
*/


CREATE TABLE Test (
    tid INT PRIMARY KEY,
    name CHAR(3),
    city CHAR(3),
    age INT
);

INSERT INTO Test VALUES
(1, 'abe', 'phx', 56),
(2, 'joe', 'phx', 66),
(3, 'coe', 'tuc', 41),
(4, 'doe', 'tuc', 38),
(5, 'moe', 'ajo', 40);




-- Part - A

-- Before Update
SELECT * FROM Test;

BEGIN TRANSACTION;

UPDATE Test
SET name = 'lee'
WHERE tid = 5;

-- After Update
SELECT * FROM Test;

COMMIT;




-- Part - B

-- Before Update
SELECT * FROM Test;

BEGIN TRANSACTION;

UPDATE Test
SET name = 'moe'
WHERE tid = 5;

-- After Update
SELECT * FROM Test;

-- Rollback
ROLLBACK;





-- Part - C

-- Before Insert
SELECT * FROM Test;

BEGIN TRANSACTION;

-- Insert a new row
INSERT INTO Test VALUES (6, 'tom', 'ajo', 72);

-- Set a save point
SAVE TRANSACTION insertSavePoint;

-- Delete the row with tid = 6
DELETE FROM Test WHERE tid = 6;

-- Table status after delete
SELECT * FROM Test;

-- Rollback to save point
ROLLBACK TRANSACTION insertSavePoint;

-- Commit the transaction
COMMIT;

-- Table status after rollback
SELECT * FROM Test;