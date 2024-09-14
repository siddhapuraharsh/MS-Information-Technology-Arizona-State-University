/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 01/19/2024
*/



-- CREATING TABLES

-- Create Course Table
CREATE TABLE Course (
    CourseID VARCHAR(255) PRIMARY KEY,
    CourseDescription VARCHAR(255),
    CourseFee DECIMAL(10,2)
);

--Create Faculty Table
CREATE TABLE Faculty (
    FacultyID VARCHAR(255) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    PrimaryEmail VARCHAR(100),
    DateOfJoining DATE,
    WorkPhone VARCHAR(15),
);

-- Create Student table
CREATE TABLE Student (
    StudentID VARCHAR(50) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    State VARCHAR(50),
    Zip VARCHAR(10),
    Degree VARCHAR(50),
    NoOfClasses INT
);

-- Create Class table
CREATE TABLE Class (
    ClassID VARCHAR(50),
    CourseID VARCHAR(255),
    StartDate DATE,
    EndDate DATE,
    Location VARCHAR(255),
    PRIMARY KEY (ClassID, CourseID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- Create StudentGrade table
CREATE TABLE StudentGrade (
    StudentID VARCHAR(50),
    ClassID VARCHAR(50),
    CourseID VARCHAR(255),
    FacultyID VARCHAR(255),
    Grade NUMERIC(3, 2),
    PRIMARY KEY (StudentID, ClassID, CourseID, FacultyID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClassID, CourseID) REFERENCES Class(ClassID, CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
);



-- =========================================================================



-- Test Script to Check if Tables are Created

-- Check if Course table exists
IF OBJECT_ID('Course', 'U') IS NOT NULL
    PRINT 'Course table exists.';
ELSE
    PRINT 'Course table does not exist.';

-- Check if Faculty table exists
IF OBJECT_ID('Faculty', 'U') IS NOT NULL
    PRINT 'Faculty table exists.';
ELSE
    PRINT 'Faculty table does not exist.';

-- Check if Student table exists
IF OBJECT_ID('Student', 'U') IS NOT NULL
    PRINT 'Student table exists.';
ELSE
    PRINT 'Student table does not exist.';

-- Check if Class table exists
IF OBJECT_ID('Class', 'U') IS NOT NULL
    PRINT 'Class table exists.';
ELSE
    PRINT 'Class table does not exist.';

-- Check if StudentGrade table exists
IF OBJECT_ID('StudentGrade', 'U') IS NOT NULL
    PRINT 'StudentGrade table exists.';
ELSE
    PRINT 'StudentGrade table does not exist.';



-- =========================================================================



-- Drop tables script
DROP TABLE IF EXISTS StudentGrade;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Course;