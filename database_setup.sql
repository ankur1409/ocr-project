-- SQL script to create the database schema for storing patient assessment data

CREATE TABLE IF NOT EXISTS patient_assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    age INTEGER,
    assessment_date DATE,
    symptoms TEXT,  
    diagnosis TEXT,
    medication TEXT  
);
