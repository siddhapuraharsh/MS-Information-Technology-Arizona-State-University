/*
** Name: Harsh Siddhapura
** Enrollment No.: 1230169813
** Course: IFT530 - Advanced Database Management System
** Date: 02/04/2024
*/


-- Query 1: Retrieve Student Information with Course Details
SELECT
    S.StudentID,
    S.FirstName,
    S.LastName,
    S.State,
    S.Degree,
    C.CourseID,
    C.CourseDescription,
    SG.Grade
FROM
    Student S
JOIN
    StudentGrade SG ON S.StudentID = SG.StudentID
JOIN
    Class CL ON SG.ClassID = CL.ClassID AND SG.CourseID = CL.CourseID
JOIN
    Course C ON CL.CourseID = C.CourseID
WHERE
    SG.Grade > 0.0;


-- View 1: StudentCourseGradeView
GO
CREATE VIEW StudentCourseGradeView AS
SELECT
    S.StudentID,
    S.FirstName,
    S.LastName,
    S.State,
    S.Degree,
    C.CourseID,
    C.CourseDescription,
    SG.Grade
FROM
    Student S
JOIN
    StudentGrade SG ON S.StudentID = SG.StudentID
JOIN
    Class CL ON SG.ClassID = CL.ClassID AND SG.CourseID = CL.CourseID
JOIN
    Course C ON CL.CourseID = C.CourseID
WHERE
    SG.Grade > 0.0;
GO

-- Query to select and print data from the view
SELECT * FROM StudentCourseGradeView;



--------------------------------------------------------------------------------



-- Query 2: Retrieve Faculty and Class Information
SELECT
    F.FacultyID,
    F.FirstName,
    F.LastName,
    C.ClassID,
    C.CourseID,
    C.StartDate,
    C.EndDate,
    C.Location
FROM
    Faculty F
JOIN
    StudentGrade SG ON F.FacultyID = SG.FacultyID
JOIN
    Class C ON SG.CourseID = C.CourseID
WHERE
    F.FacultyID != 'F000';


-- View 2: FacultyClassView
GO
CREATE VIEW FacultyClassView AS
SELECT
    F.FacultyID,
    F.FirstName,
    F.LastName,
    C.ClassID,
    C.CourseID,
    C.StartDate,
    C.EndDate,
    C.Location
FROM
    Faculty F
JOIN
    StudentGrade SG ON F.FacultyID = SG.FacultyID
JOIN
    Class C ON SG.CourseID = C.CourseID
WHERE
    F.FacultyID != 'F000';
GO

-- Query to select and print data from the view
SELECT * FROM FacultyClassView;