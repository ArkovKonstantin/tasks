CREATE TABLE crime_type
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    type TEXT
);

CREATE TABLE address_type
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    type TEXT
);

CREATE TABLE disposition
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    code TEXT
);

CREATE TABLE Crime
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Id_Crime_Type INTEGER,
    Report_Date date,
    Call_Date date,
    Offense_Date date,
    Call_Time time,
    Call_Date_Time datetime,
    Id_Disposition INTEGER,
    Address text,
    City text,
    State text,
    Agency_Id text,
    Id_Address_Type INTEGER,
    Common_Location text,
    FOREIGN KEY (Id_Crime_Type) REFERENCES crime_type(id),
    FOREIGN KEY (Id_Disposition) REFERENCES disposition(id),
    FOREIGN KEY (Id_Address_Type) REFERENCES address_type(id)
);