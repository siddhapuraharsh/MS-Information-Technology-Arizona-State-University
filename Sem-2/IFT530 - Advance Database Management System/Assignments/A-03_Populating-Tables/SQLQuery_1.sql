/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 01/28/2024
*/


-- Populate Course Table
INSERT INTO Course (CourseID, CourseDescription, CourseFee)
VALUES
    ('C000', null, 0.00),
    ('C001', 'Introduction to Programming', 1500.00),
    ('C002', 'Database Management', 1200.00),
    ('C003', 'Data Structures and Algorithms', 1800.00);


-- Populate Faculty Table
INSERT INTO Faculty (FacultyID, FirstName, LastName, PrimaryEmail, DateOfJoining, WorkPhone)
VALUES
    ('F000', null, null, null, null, null),
    ('F001', 'John', 'Doe', 'john.doe@email.com', '2022-01-01', '123-456-7890'),
    ('F002', 'Jane', 'Smith', 'jane.smith@email.com', '2022-02-01', '987-654-3210');


-- Populate Class Table
INSERT INTO Class (ClassID, CourseID, StartDate, EndDate, Location)
VALUES
    ('CL000', 'C000', null, null, null),
    ('CL001', 'C001', '2022-03-01', '2022-05-01', 'Room A'),
    ('CL002', 'C002', '2022-03-15', '2022-05-15', 'Room B'),
    ('CL003', 'C003', '2022-04-01', '2022-06-01', 'Room C');


-- Populate Student Table
INSERT INTO Student (StudentID, FirstName, LastName, State, Zip, Degree, NoOfClasses)
VALUES
    -- Students from California (CA)
    ('S001', 'Alice', 'Johnson', 'CA', '90001', 'Undergraduate', 3),
    ('S004', 'David', 'Lee', 'CA', '90002', 'Bachelor', 2),
    ('S007', 'Grace', 'Davis', 'CA', '90003', 'Undergraduate', 1),
    ('S010', 'Jack', 'Chen', 'CA', '90004', 'Bachelor', 3),

    -- Students from New York (NY)
    ('S002', 'Bob', 'Williams', 'NY', '10001', 'Bachelor', 3),
    ('S005', 'Eva', 'Miller', 'NY', '10002', 'Undergraduate', 1),
    ('S008', 'Henry', 'Johnson', 'NY', '10003', 'Bachelor', 2),

    -- Students from Texas (TX)
    ('S003', 'Charlie', 'Smith', 'TX', '75001', 'Masters', 3),
    ('S006', 'Frank', 'Brown', 'TX', '75002', 'Masters', 0),
    ('S009', 'Ivy', 'Wang', 'TX', '75003', 'Masters', 1);


-- Populate StudentGrade Table
INSERT INTO StudentGrade (StudentID, ClassID, CourseID, FacultyID, Grade)
VALUES
    ('S001', 'CL001', 'C001', 'F001', 3.75),
    ('S001', 'CL002', 'C002', 'F002', 3.95),
    ('S001', 'CL003', 'C003', 'F001', 2.75),

    ('S002', 'CL001', 'C001', 'F001', 3.0),
    ('S002', 'CL002', 'C002', 'F001', 4.0),
    ('S002', 'CL003', 'C003', 'F002', 2.0),

    ('S003', 'CL001', 'C001', 'F002', 2.9),
    ('S003', 'CL002', 'C002', 'F001', 3.2),
    ('S003', 'CL003', 'C003', 'F001', 3.2),

    ('S004', 'CL001', 'C001', 'F001', 3.8),
    ('S004', 'CL002', 'C002', 'F002', 2.8),

    ('S005', 'CL002', 'C002', 'F002', 3.2),

    ('S006', 'CL000', 'C000', 'F000', 0.0),

    ('S007', 'CL003', 'C003', 'F001', 3.6),

    ('S008', 'CL003', 'C003', 'F001', 3.1),
    ('S008', 'CL002', 'C002', 'F002', 3.9),

    ('S009', 'CL003', 'C003', 'F001', 4.0),

    ('S010', 'CL001', 'C001', 'F001', 3.1),
    ('S010', 'CL002', 'C002', 'F002', 3.5),
    ('S010', 'CL003', 'C003', 'F001', 3.7);



-- Test script to show that tables are populated

-- Display data from Course Table
SELECT * FROM Course;

-- Display data from Faculty Table
SELECT * FROM Faculty;

-- Display data from Class Table
SELECT * FROM Class;

-- Display data from Student Table
SELECT * FROM Student;

-- Display data from StudentGrade Table
SELECT * FROM StudentGrade;
