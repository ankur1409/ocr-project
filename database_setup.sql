-- SQL script to create the database schema for storing patient assessment data

CREATE TABLE IF NOT EXISTS patient_assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
