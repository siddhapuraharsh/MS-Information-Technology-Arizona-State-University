/*
** Group Name: Final Project 41
** Project: Hospital Management System
** Group Members: Harsh Siddhapura & Jhansi Alugoju
** Course: IFT530 - Advanced Database Management System
** Date: 04/23/2024
*/



-- Create database

IF EXISTS (
    SELECT name FROM master.dbo.sysdatabases 
    WHERE name = 'HospitalManagementSystem'
)
DROP DATABASE HospitalManagementSystem;
GO

CREATE DATABASE HospitalManagementSystem;
GO

USE HospitalManagementSystem;
GO


----------------------------------------------------------------------------------------


-- Create the tables using SQL script you have defined in the Final project.

-- Table 1: Patients
CREATE TABLE Patients (
    PatientID INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    DOB DATE NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Address VARCHAR(200) NOT NULL
);

-- Table 2: Departments
CREATE TABLE Departments (
    DepartmentID INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
);

-- Table 3: Doctors
CREATE TABLE Doctors (
    DoctorID INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Specialty VARCHAR(50) NOT NULL,
    DepartmentID INTEGER NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Table 4: Nurses
CREATE TABLE Nurses (
    NurseID INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    DepartmentID INTEGER NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Table 5: Bills
CREATE TABLE Bills (
    BillID INTEGER NOT NULL PRIMARY KEY,
    PatientID INTEGER NOT NULL,
    TotalAmount FLOAT NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- Table 6: Appointments
CREATE TABLE Appointments (
    AppointmentID INTEGER NOT NULL PRIMARY KEY,
    PatientID INTEGER NOT NULL,
    DoctorID INTEGER NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Table 7: MedicalRecords
CREATE TABLE MedicalRecords (
    RecordID INTEGER NOT NULL PRIMARY KEY,
    PatientID INTEGER NOT NULL,
    DoctorID INTEGER NOT NULL,
    Diagnosis VARCHAR(200) NOT NULL,
    Prescription VARCHAR(200) NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Table 8: Payments
CREATE TABLE Payments (
    PaymentID INTEGER NOT NULL PRIMARY KEY,
    BillID INTEGER NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount FLOAT NOT NULL,
    FOREIGN KEY (BillID) REFERENCES Bills(BillID)
);

-- Table 9: Insurance
CREATE TABLE Insurance (
    InsuranceID INTEGER NOT NULL PRIMARY KEY,
    PatientID INTEGER NOT NULL,
    InsuranceCompany VARCHAR(100) NOT NULL,
    PolicyNumber VARCHAR(50) NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- Table 10: PatientInsurance
CREATE TABLE PatientInsurance (
    PatientID INTEGER NOT NULL,
    InsuranceID INTEGER NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (InsuranceID) REFERENCES Insurance(InsuranceID)
);


----------------------------------------------------------------------------------------


-- Populate the table with 10 rows for dimension tables, 20 – 50 rows for transactional tables.

-- Table 1: Patients
INSERT INTO Patients (PatientID, Name, DOB, Gender, Address)
VALUES
    (1, 'John Doe', '1990-05-15', 'Male', '123 Main St'),
    (2, 'Jane Smith', '1985-09-20', 'Female', '456 Elm St'),
    (3, 'Michael Johnson', '1978-03-10', 'Male', '789 Oak St'),
    (4, 'Emily Davis', '1992-11-25', 'Female', '101 Pine St'),
    (5, 'Christopher Wilson', '1983-07-08', 'Male', '234 Maple St'),
    (6, 'Jessica Taylor', '1995-02-18', 'Female', '567 Cedar St'),
    (7, 'William Brown', '1970-12-30', 'Male', '890 Walnut St'),
    (8, 'Amanda Martinez', '1988-06-05', 'Female', '111 Birch St'),
    (9, 'Daniel Miller', '1982-04-14', 'Male', '222 Spruce St'),
    (10, 'Sarah Garcia', '1998-08-22', 'Female', '333 Ash St'),
    (11, 'Matthew Rodriguez', '1975-01-12', 'Male', '444 Sycamore St'),
    (12, 'Ashley Hernandez', '1991-10-07', 'Female', '555 Willow St'),
    (13, 'David Lopez', '1980-09-03', 'Male', '666 Oak St'),
    (14, 'Jennifer Gonzalez', '1987-07-19', 'Female', '777 Maple St'),
    (15, 'James Perez', '1994-04-28', 'Male', '888 Elm St');

-- Table 2: Departments
INSERT INTO Departments (DepartmentID, Name)
VALUES
    (1, 'Cardiology'),
    (2, 'Neurology'),
    (3, 'Orthopedics'),
    (4, 'Oncology'),
    (5, 'Pediatrics'),
    (6, 'Emergency Medicine'),
    (7, 'Radiology'),
    (8, 'Dermatology'),
    (9, 'Ophthalmology'),
    (10, 'Gynecology'),
    (11, 'Urology'),
    (12, 'Anesthesiology'),
    (13, 'Pathology'),
    (14, 'Physical Therapy'),
    (15, 'Psychiatry');

-- Table 3: Doctors
INSERT INTO Doctors (DoctorID, Name, Specialty, DepartmentID)
VALUES
    (1, 'Dr. John Smith', 'Cardiologist', 1),
    (2, 'Dr. Emily Brown', 'Neurologist', 2),
    (3, 'Dr. Michael Johnson', 'Orthopedic Surgeon', 3),
    (4, 'Dr. Sarah Lee', 'Oncologist', 4),
    (5, 'Dr. David Clark', 'Pediatrician', 5),
    (6, 'Dr. Jessica Taylor', 'Emergency Medicine Physician', 6),
    (7, 'Dr. Robert Martinez', 'Radiologist', 7),
    (8, 'Dr. Jennifer Wilson', 'Dermatologist', 8),
    (9, 'Dr. Andrew Garcia', 'Ophthalmologist', 9),
    (10, 'Dr. Samantha White', 'Gynecologist', 10),
    (11, 'Dr. James Carter', 'Urologist', 11),
    (12, 'Dr. Michelle Adams', 'Anesthesiologist', 12),
    (13, 'Dr. Daniel Thompson', 'Pathologist', 13),
    (14, 'Dr. Elizabeth Harris', 'Physical Therapist', 14),
    (15, 'Dr. Christopher Allen', 'Psychiatrist', 15);

-- Table 4: Nurses
INSERT INTO Nurses (NurseID, Name, DepartmentID)
VALUES
    (1, 'Alice Johnson', 1),
    (2, 'Bob Smith', 2),
    (3, 'Catherine Brown', 3),
    (4, 'David Miller', 4),
    (5, 'Emily Wilson', 5),
    (6, 'Frank Davis', 6),
    (7, 'Grace Taylor', 7),
    (8, 'Henry Clark', 8),
    (9, 'Isabella Martinez', 9),
    (10, 'John Anderson', 10),
    (11, 'Kate Garcia', 11),
    (12, 'Liam Thomas', 12),
    (13, 'Mia Lee', 13),
    (14, 'Nathan Jackson', 14),
    (15, 'Olivia White', 15);

-- Table 5: Bills (Fact Table / Transactional Table)
INSERT INTO Bills (BillID, PatientID, TotalAmount)
VALUES
    (1, 3, 125.75),
    (2, 8, 357.20),
    (3, 5, 489.50),
    (4, 12, 220.00),
    (5, 2, 180.25),
    (6, 7, 312.80),
    (7, 10, 145.90),
    (8, 9, 275.60),
    (9, 14, 198.75),
    (10, 6, 432.10),
    (11, 4, 510.30),
    (12, 11, 325.40),
    (13, 1, 150.00),
    (14, 15, 267.85),
    (15, 13, 390.75),
    (16, 3, 215.20),
    (17, 8, 177.40),
    (18, 5, 301.60),
    (19, 12, 425.30),
    (20, 2, 350.00),
    (21, 7, 175.90),
    (22, 10, 290.75),
    (23, 9, 175.20),
    (24, 14, 398.50),
    (25, 6, 220.80),
    (26, 4, 160.25),
    (27, 11, 270.40),
    (28, 1, 190.60),
    (29, 15, 312.75),
    (30, 13, 255.00),
    (31, 3, 330.25),
    (32, 8, 275.40),
    (33, 5, 190.80),
    (34, 12, 410.60),
    (35, 2, 325.25),
    (36, 7, 150.40),
    (37, 10, 390.75),
    (38, 9, 215.20),
    (39, 14, 175.60),
    (40, 6, 301.40),
    (41, 4, 210.25),
    (42, 11, 280.80),
    (43, 1, 335.00),
    (44, 15, 175.75),
    (45, 13, 295.20),
    (46, 3, 220.40),
    (47, 8, 180.75),
    (48, 5, 380.00),
    (49, 12, 412.25),
    (50, 2, 305.60);

-- Table 6: Appointments (Fact Table / Transactional Table)
INSERT INTO Appointments (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime)
VALUES
    (1, 1, 1, '2024-04-01', '09:00:00'),
    (2, 2, 2, '2024-04-01', '10:00:00'),
    (3, 3, 3, '2024-04-02', '11:00:00'),
    (4, 4, 4, '2024-04-02', '12:00:00'),
    (5, 5, 5, '2024-04-03', '13:00:00'),
    (6, 6, 6, '2024-04-03', '14:00:00'),
    (7, 7, 7, '2024-04-04', '15:00:00'),
    (8, 8, 8, '2024-04-04', '16:00:00'),
    (9, 9, 9, '2024-04-05', '09:00:00'),
    (10, 10, 10, '2024-04-05', '10:00:00'),
    (11, 11, 11, '2024-04-06', '11:00:00'),
    (12, 12, 12, '2024-04-06', '12:00:00'),
    (13, 13, 13, '2024-04-07', '13:00:00'),
    (14, 14, 14, '2024-04-07', '14:00:00'),
    (15, 15, 15, '2024-04-08', '15:00:00'),
    (16, 1, 2, '2024-04-08', '16:00:00'),
    (17, 2, 3, '2024-04-09', '09:00:00'),
    (18, 3, 4, '2024-04-09', '10:00:00'),
    (19, 4, 5, '2024-04-10', '11:00:00'),
    (20, 5, 6, '2024-04-10', '12:00:00'),
    (21, 6, 7, '2024-04-11', '13:00:00'),
    (22, 7, 8, '2024-04-11', '14:00:00'),
    (23, 8, 9, '2024-04-12', '15:00:00'),
    (24, 9, 10, '2024-04-12', '16:00:00'),
    (25, 10, 11, '2024-04-13', '09:00:00'),
    (26, 11, 12, '2024-04-13', '10:00:00'),
    (27, 12, 13, '2024-04-14', '11:00:00'),
    (28, 13, 14, '2024-04-14', '12:00:00'),
    (29, 14, 15, '2024-04-15', '13:00:00'),
    (30, 15, 1, '2024-04-15', '14:00:00'),
    (31, 1, 3, '2024-04-16', '15:00:00'),
    (32, 2, 4, '2024-04-16', '16:00:00'),
    (33, 3, 5, '2024-04-17', '09:00:00'),
    (34, 4, 6, '2024-04-17', '10:00:00'),
    (35, 5, 7, '2024-04-18', '11:00:00'),
    (36, 6, 8, '2024-04-18', '12:00:00'),
    (37, 7, 9, '2024-04-19', '13:00:00'),
    (38, 8, 10, '2024-04-19', '14:00:00'),
    (39, 9, 11, '2024-04-20', '15:00:00'),
    (40, 10, 12, '2024-04-20', '16:00:00'),
    (41, 11, 13, '2024-04-21', '09:00:00'),
    (42, 12, 14, '2024-04-21', '10:00:00'),
    (43, 13, 15, '2024-04-22', '11:00:00'),
    (44, 14, 1, '2024-04-22', '12:00:00'),
    (45, 15, 2, '2024-04-23', '13:00:00'),
    (46, 1, 4, '2024-04-23', '14:00:00'),
    (47, 2, 5, '2024-04-24', '15:00:00'),
    (48, 3, 6, '2024-04-24', '16:00:00'),
    (49, 4, 7, '2024-04-25', '09:00:00'),
    (50, 5, 8, '2024-04-25', '10:00:00');

-- Table 7: MedicalRecords (Fact Table / Transactional Table)
INSERT INTO MedicalRecords (RecordID, PatientID, DoctorID, Diagnosis, Prescription)
VALUES
    (1, 1, 1, 'Hypertension', 'Lisinopril'),
    (2, 2, 2, 'Migraine', 'Sumatriptan'),
    (3, 3, 3, 'Fractured leg', 'Painkillers and rest'),
    (4, 4, 4, 'Breast cancer', 'Chemotherapy'),
    (5, 5, 5, 'Pneumonia', 'Antibiotics'),
    (6, 6, 6, 'Heart attack', 'Aspirin and beta blockers'),
    (7, 7, 7, 'Lung cancer', 'Radiation therapy'),
    (8, 8, 8, 'Eczema', 'Topical corticosteroids'),
    (9, 9, 9, 'Cataracts', 'Surgery'),
    (10, 10, 10, 'Endometriosis', 'Oral contraceptives'),
    (11, 11, 11, 'Prostate cancer', 'Surgery and radiation therapy'),
    (12, 12, 12, 'Anesthesia complications', 'Monitoring and supportive care'),
    (13, 13, 13, 'Pancreatic cancer', 'Chemotherapy and radiation therapy'),
    (14, 14, 14, 'Sprained ankle', 'RICE therapy'),
    (15, 15, 15, 'Depression', 'Selective serotonin reuptake inhibitors'),
    (16, 1, 2, 'High cholesterol', 'Atorvastatin'),
    (17, 2, 3, 'Asthma', 'Inhaled corticosteroids'),
    (18, 3, 4, 'Diabetes', 'Insulin therapy'),
    (19, 4, 5, 'Bronchitis', 'Bronchodilators'),
    (20, 5, 6, 'Stroke', 'Antiplatelet medication'),
    (21, 6, 7, 'Kidney stones', 'Pain management and fluid intake'),
    (22, 7, 8, 'Psoriasis', 'Phototherapy'),
    (23, 8, 9, 'Glaucoma', 'Eye drops'),
    (24, 9, 10, 'Infertility', 'In vitro fertilization'),
    (25, 10, 11, 'Urinary tract infection', 'Antibiotics'),
    (26, 11, 12, 'Gallstones', 'Cholecystectomy'),
    (27, 12, 13, 'Liver cirrhosis', 'Diuretics and lifestyle changes'),
    (28, 13, 14, 'Torn ligament', 'Physical therapy'),
    (29, 14, 15, 'Bipolar disorder', 'Mood stabilizers'),
    (30, 15, 1, 'Osteoporosis', 'Calcium and vitamin D supplements'),
    (31, 1, 3, 'Sinusitis', 'Nasal decongestants'),
    (32, 2, 4, 'Arthritis', 'Nonsteroidal anti-inflammatory drugs'),
    (33, 3, 5, 'Anemia', 'Iron supplements'),
    (34, 4, 6, 'Gastritis', 'Antacids'),
    (35, 5, 7, 'Schizophrenia', 'Antipsychotic medications'),
    (36, 6, 8, 'Hyperthyroidism', 'Thyroid hormone therapy'),
    (37, 7, 9, 'Glomerulonephritis', 'Immunosuppressants'),
    (38, 8, 10, 'Menopause', 'Hormone replacement therapy'),
    (39, 9, 11, 'Epilepsy', 'Antiepileptic drugs'),
    (40, 10, 12, 'COPD', 'Bronchodilators and corticosteroids'),
    (41, 11, 13, 'Crohn''s disease', 'Immunomodulators and biologic therapy'),
    (42, 12, 14, 'Concussion', 'Rest and observation'),
    (43, 13, 15, 'Hypothyroidism', 'Levothyroxine'),
    (44, 14, 1, 'Rheumatoid arthritis', 'Disease-modifying antirheumatic drugs'),
    (45, 15, 2, 'Obesity', 'Diet and exercise'),
    (46, 1, 4, 'Allergic rhinitis', 'Antihistamines'),
    (47, 2, 5, 'Pancreatitis', 'Pain relief and IV fluids'),
    (48, 3, 6, 'Hepatitis', 'Antiviral medications'),
    (49, 4, 7, 'Celiac disease', 'Gluten-free diet'),
    (50, 5, 8, 'Fibromyalgia', 'Physical therapy and medications');

-- Table 8: Payments (Fact Table / Transactional Table)
INSERT INTO Payments (PaymentID, BillID, PaymentDate, Amount)
VALUES
    (1, 1, '2023-01-05', 100.00),
    (2, 2, '2023-01-10', 150.00),
    (3, 3, '2023-01-15', 200.00),
    (4, 4, '2023-01-20', 125.00),
    (5, 5, '2023-01-25', 180.00),
    (6, 6, '2023-02-01', 90.00),
    (7, 7, '2023-02-05', 220.00),
    (8, 8, '2023-02-10', 175.00),
    (9, 9, '2023-02-15', 130.00),
    (10, 10, '2023-02-20', 195.00),
    (11, 11, '2023-02-25', 240.00),
    (12, 12, '2023-03-01', 85.00),
    (13, 13, '2023-03-05', 210.00),
    (14, 14, '2023-03-10', 165.00),
    (15, 15, '2023-03-15', 150.00),
    (16, 16, '2023-03-20', 200.00),
    (17, 17, '2023-03-25', 100.00),
    (18, 18, '2023-04-01', 175.00),
    (19, 19, '2023-04-05', 185.00),
    (20, 20, '2023-04-10', 145.00),
    (21, 21, '2023-04-15', 135.00),
    (22, 22, '2023-04-20', 220.00),
    (23, 23, '2023-04-25', 130.00),
    (24, 24, '2023-05-01', 250.00),
    (25, 25, '2023-05-05', 110.00),
    (26, 26, '2023-05-10', 160.00),
    (27, 27, '2023-05-15', 195.00),
    (28, 28, '2023-05-20', 170.00),
    (29, 29, '2023-05-25', 140.00),
    (30, 30, '2023-06-01', 180.00),
    (31, 31, '2023-06-05', 125.00),
    (32, 32, '2023-06-10', 205.00),
    (33, 33, '2023-06-15', 190.00),
    (34, 34, '2023-06-20', 150.00),
    (35, 35, '2023-06-25', 220.00),
    (36, 36, '2023-07-01', 135.00),
    (37, 37, '2023-07-05', 165.00),
    (38, 38, '2023-07-10', 200.00),
    (39, 39, '2023-07-15', 145.00),
    (40, 40, '2023-07-20', 175.00),
    (41, 41, '2023-07-25', 230.00),
    (42, 42, '2023-08-01', 120.00),
    (43, 43, '2023-08-05', 250.00),
    (44, 44, '2023-08-10', 135.00),
    (45, 45, '2023-08-15', 195.00),
    (46, 46, '2023-08-20', 180.00),
    (47, 47, '2023-08-25', 160.00),
    (48, 48, '2023-09-01', 210.00),
    (49, 49, '2023-09-05', 170.00),
    (50, 50, '2023-09-10', 140.00);

-- Table 9: Insurance
INSERT INTO Insurance (InsuranceID, PatientID, InsuranceCompany, PolicyNumber)
VALUES
    (1, 1, 'ABC Insurance', 'ABC123456'),
    (2, 2, 'XYZ Insurance', 'XYZ789012'),
    (3, 3, 'DEF Insurance', 'DEF345678'),
    (4, 4, 'GHI Insurance', 'GHI901234'),
    (5, 5, 'JKL Insurance', 'JKL567890'),
    (6, 6, 'MNO Insurance', 'MNO123456'),
    (7, 7, 'PQR Insurance', 'PQR789012'),
    (8, 8, 'STU Insurance', 'STU345678'),
    (9, 9, 'VWX Insurance', 'VWX901234'),
    (10, 10, 'YZA Insurance', 'YZA567890'),
    (11, 11, 'BCD Insurance', 'BCD123456'),
    (12, 12, 'EFG Insurance', 'EFG789012'),
    (13, 13, 'HIJ Insurance', 'HIJ345678'),
    (14, 14, 'KLM Insurance', 'KLM901234'),
    (15, 15, 'NOP Insurance', 'NOP567890');


-- Table 10: PatientInsurance
INSERT INTO PatientInsurance (PatientID, InsuranceID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15);


----------------------------------------------------------------------------------------


/*
** Create three queries and convert them into views. Explain why you think would be
** useful to the user. All queries must be joined to one or more tables. Make sure you restrict
** the data by using a where clause for each of the queries.
*/

-- Query 1
SELECT P.PatientID, P.Name AS PatientName, P.DOB, P.Gender, 
    P.Address, A.AppointmentID, A.DoctorID, A.AppointmentDate, A.AppointmentTime
FROM Patients P
INNER JOIN Appointments A ON P.PatientID = A.PatientID
INNER JOIN Doctors D ON A.DoctorID = D.DoctorID
INNER JOIN Departments Dept ON D.DepartmentID = Dept.DepartmentID
WHERE Dept.Name = 'Cardiology';
GO

-- View 1
CREATE VIEW PatientsInCardiologyView AS
SELECT P.PatientID, P.Name AS PatientName, P.DOB, P.Gender, 
    P.Address, A.AppointmentID, A.DoctorID, A.AppointmentDate, A.AppointmentTime
FROM Patients P
INNER JOIN Appointments A ON P.PatientID = A.PatientID
INNER JOIN Doctors D ON A.DoctorID = D.DoctorID
INNER JOIN Departments Dept ON D.DepartmentID = Dept.DepartmentID
WHERE Dept.Name = 'Cardiology';
GO

-- Query 2
SELECT MR.RecordID, MR.PatientID, P.Name AS PatientName, MR.DoctorID, D.Name 
    AS DoctorName, MR.Diagnosis, MR.Prescription
FROM MedicalRecords MR
INNER JOIN Patients P ON MR.PatientID = P.PatientID
INNER JOIN Doctors D ON MR.DoctorID = D.DoctorID
WHERE P.Gender = 'Female';
GO

-- View 2
CREATE VIEW MedicalRecordsForFemalesView AS
SELECT MR.RecordID, MR.PatientID, P.Name AS PatientName, MR.DoctorID, D.Name 
    AS DoctorName, MR.Diagnosis, MR.Prescription
FROM MedicalRecords MR
INNER JOIN Patients P ON MR.PatientID = P.PatientID
INNER JOIN Doctors D ON MR.DoctorID = D.DoctorID
WHERE P.Gender = 'Female';
GO

-- Query 3
SELECT B.BillID, B.PatientID, B.TotalAmount, P.PaymentID, P.PaymentDate, P.Amount
FROM Bills B
LEFT JOIN Payments P ON B.BillID = P.BillID
WHERE B.PatientID = 3;
GO

-- View 3
CREATE VIEW PatientBillView AS
SELECT B.BillID, B.PatientID, B.TotalAmount, P.PaymentID, P.PaymentDate, P.Amount
FROM Bills B
LEFT JOIN Payments P ON B.BillID = P.BillID
WHERE B.PatientID = 3;
GO


----------------------------------------------------------------------------------------


/*
** Create an audit table for one of the lookup tables and demonstrate data saved to that audit
** table when data in the original table is inserted, modified, or deleted. Include an
** additional column in the audit table that will have a datetime field when the data was
** changed in the original table. Include the script to test all the operations
*/

-- Step 1: Create the audit table
CREATE TABLE PatientsAudit (
    AuditID INT IDENTITY(1,1) PRIMARY KEY,
    PatientID INT,
    Name VARCHAR(100),
    DOB DATE,
    Gender VARCHAR(10),
    Address VARCHAR(200),
    ChangeDateTime DATETIME
);
GO

-- Step 2: Create trigger for INSERT operation
CREATE TRIGGER trg_Patients_Insert
ON Patients
AFTER INSERT
AS
BEGIN
    INSERT INTO PatientsAudit (PatientID, Name, DOB, Gender, Address, ChangeDateTime)
    SELECT PatientID, Name, DOB, Gender, Address, GETDATE()
    FROM inserted;
END;
GO

-- Create trigger for UPDATE operation
CREATE TRIGGER trg_Patients_Update
ON Patients
AFTER UPDATE
AS
BEGIN
    INSERT INTO PatientsAudit (PatientID, Name, DOB, Gender, Address, ChangeDateTime)
    SELECT PatientID, Name, DOB, Gender, Address, GETDATE()
    FROM inserted;
END;
GO

-- Create trigger for DELETE operation
CREATE TRIGGER trg_Patients_Delete
ON Patients
AFTER DELETE
AS
BEGIN
    INSERT INTO PatientsAudit (PatientID, Name, DOB, Gender, Address, ChangeDateTime)
    SELECT PatientID, Name, DOB, Gender, Address, GETDATE()
    FROM deleted;
END;
GO

-- Step 3: Test the functionality
-- Insert
INSERT INTO Patients (PatientID, Name, DOB, Gender, Address)
VALUES (16, 'John D', '1990-05-15', 'Male', '123 Main St');

-- Update
UPDATE Patients
SET Name = 'Jane Smit'
WHERE PatientID = 16;

-- Delete
DELETE FROM Patients
WHERE PatientID = 16;

-- View audit table
SELECT * FROM PatientsAudit;



----------------------------------------------------------------------------------------


/*
** Demonstrate a use of the one stored procedures and User Defined Function (UDF) for
** your database. Include create and drop scripts.
*/

-- Stored Procedure

-- Drop procedure if exists
IF EXISTS (SELECT * FROM sys.objects WHERE type = 'P' AND name = 'usp_GetPatientAppointments')
    DROP PROCEDURE usp_GetPatientAppointments;
GO

-- Create procedure
CREATE PROCEDURE usp_GetPatientAppointments
    @PatientID INT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT A.AppointmentID, A.PatientID, A.DoctorID, D.Name AS DoctorName, 
           A.AppointmentDate, A.AppointmentTime
    FROM Appointments A
    INNER JOIN Doctors D ON A.DoctorID = D.DoctorID
    WHERE A.PatientID = @PatientID;
END;
GO

-- Call Procedure
EXEC usp_GetPatientAppointments @PatientID = 1;
GO


-- User Defined Functions

-- Drop the User Defined Function if it already exists
IF EXISTS (SELECT * FROM sys.objects WHERE type = 'FN' AND name = 'CalculatePatientAge')
    DROP FUNCTION dbo.CalculatePatientAge;
GO

-- Create the User Defined Function
CREATE FUNCTION dbo.CalculatePatientAge (@DOB DATE)
RETURNS INT
AS
BEGIN
    DECLARE @Age INT

    SET @Age = DATEDIFF(YEAR, @DOB, GETDATE()) -
               CASE
                   WHEN DATEADD(YEAR, DATEDIFF(YEAR, @DOB, GETDATE()), @DOB) > GETDATE() THEN 1
                   ELSE 0
               END

    RETURN @Age
END;
GO

SELECT Name, DOB, dbo.CalculatePatientAge(DOB) AS Age
FROM Patients;


----------------------------------------------------------------------------------------


-- Demonstrate the use of one cursor for your database. Create and drop script for cursor.

-- Declare the cursor
DECLARE @PaymentCursor CURSOR;  

-- Set the cursor
SET @PaymentCursor = CURSOR FOR  
SELECT P.PatientID, P.Name, SUM(B.TotalAmount) AS TotalPaid
FROM Patients P
JOIN Bills B ON P.PatientID = B.PatientID
JOIN Payments Pay ON B.BillID = Pay.BillID
GROUP BY P.PatientID, P.Name;

-- Open the cursor
OPEN @PaymentCursor;  

-- Declare variables to hold the data
DECLARE @PatientID INTEGER, @Name VARCHAR(100), @TotalPaid FLOAT;

-- Fetch the first row
FETCH NEXT FROM @PaymentCursor INTO @PatientID, @Name, @TotalPaid;

-- Fetch and print all rows
WHILE @@FETCH_STATUS = 0  
BEGIN  
    PRINT 'Patient ID: ' + CAST(@PatientID AS VARCHAR(10)) + ', Name: ' + @Name + ', Total Paid: ' + CAST(@TotalPaid AS VARCHAR(20));

    -- Fetch the next row
    FETCH NEXT FROM @PaymentCursor INTO @PatientID, @Name, @TotalPaid;
END;

-- Close and deallocate the cursor
CLOSE @PaymentCursor;  
DEALLOCATE @PaymentCursor;


