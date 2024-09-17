@echo off

:: Define paths for PostgreSQL and the data directory
SET PGPATH="C:\Program Files\PostgreSQL\17\bin"
SET PGDATA="C:\Program Files\PostgreSQL\17\data"
SET PGUSER="postgres"
SET PGPORT=6899

:: Installing Python library
pip install -r "requirements.txt"

:: Step 1: Start PostgreSQL server if it's not already running
echo Starting PostgreSQL server...
net start postgresql-17 || echo PostgreSQL server is already running

:: Step 2: Run the setup SQL script to create database and tables
echo Running setup.sql...
%PGPATH%\psql -U %PGUSER% -p %PGPORT% -f "setup.sql" 
::"C:\path\to\your\setup.sql"

:: Step 3: Confirmation
echo Database setup complete!
pause
