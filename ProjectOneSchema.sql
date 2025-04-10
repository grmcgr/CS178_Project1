/* create database */
-- Create the database
CREATE DATABASE IF NOT EXISTS ProjectOneDog;
USE ProjectOneDog;

-- Create the Breed table
CREATE TABLE Breed (
    breedID INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Create the Dog table
CREATE TABLE Dog (
    dogID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    breedID INT,
    friendlyRating INT,
    kidsRating INT,
    cuteRating INT,
    overallRating FLOAT GENERATED ALWAYS AS (
        ROUND((friendlyRating + kidsRating + cuteRating) / 3, 2)
    ) STORED,
    lifeExpectancy INT,
    sizeID INT,
    FOREIGN KEY (breedID) REFERENCES Breed(breedID)
);

-- Insert breeds
INSERT INTO Breed (
    breedID, 
    name) 
        VALUES
            (1, 'Golden Retriever'),
            (2, 'French Bulldog'),
            (3, 'Border Collie'),
            (4, 'Chihuahua'),
            (5, 'Labrador Retriever'),
            (6, 'German Shepherd'),
            (7, 'Poodle'),
            (8, 'Beagle'),
            (9, 'Rottweiler'),
            (10, 'Yorkshire Terrier'),
            (11, 'Dachshund'),
            (12, 'Boxer'),
            (13, 'Siberian Husky'),
            (14, 'Australian Shepherd'),
            (15, 'Cavalier King Charles Spaniel'),
            (16, 'Great Dane'),
            (17, 'Shih Tzu'),
            (18, 'Doberman Pinscher'),
            (19, 'Boston Terrier');


-- Insert 10 dogs
INSERT INTO Dog (
    name, 
    breedID, 
    friendlyRating, 
    kidsRating, 
    cuteRating, 
    lifeExpectancy, 
    sizeID) 
        VALUES
            ('Buddy',   1, 10, 10, 9, 12, 2),
            ('Sunny',   1, 9, 10, 8, 13, 2),
            ('Luna',    2, 8, 7, 9, 11, 1),
            ('Bruno',   2, 9, 8, 10, 10, 1),
            ('Zoe',     3, 9, 9, 8, 14, 2),
            ('Dash',    3, 8, 8, 7, 13, 2),
            ('Tiny',    4, 7, 6, 9, 15, 0),
            ('Pixie',   4, 8, 7, 10, 14, 0),
            ('Bailey',  1, 10, 10, 8, 12, 2),
            ('Koda',    3, 9, 9, 7, 13, 2);


/*  */
/*  */
/*  */