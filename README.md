Grace McGrane
Due 4/17/2025

# CS178 Project 1: Full-Stack Web Application

## Overview

This project replaces an in-class exam and reinforces the skills we've covered in the first part of the course. You will build a self-contained web application using Flask that connects to both a relational (SQL via AWS RDS) and a non-relational (NoSQL via AWS DynamoDB) database.

### Your project must:
- [x] Be built and run locally using Visual Studio Code  
- [x] Be deployed via Flask as a web application  
- [x] Use both an RDS (MySQL) and DynamoDB database with a consistent theme  
- [x] Be version-controlled using GitHub  
- [x] Be accessible entirely through a browser interface (no terminal interaction)  

---

## What to Submit

### GitHub Repository  
[GitHub Repository Link](https://github.com/grmcgr/CS178_Project1)

### Project Report  
#### Screenshots of your working project  
Please see the video attached for a full demo of the capabilities of this site.
[Project 1 Video Demo](https://1drv.ms/v/c/331a865ca5d07667/Ed-lupMSuKNPpHixjW54UmsBUUF9ENb93u8Hd6WMgJ1_fA?e=o31eEZ)

#### Description of how SQL and DynamoDB are integrated  
As a user of the site, you need to have a username and date of birth in the system to access the movie data. To begin, you enter in your username and date of birth, DynamoDB looks it up in the system, and if you're there, you can see the next page of movies! If you are not in the system, it will take you to the Add User page so you can add yourself. Then you go back home and log in. The other aspects of CRUD are available in the Users database as you can see in the Demo video and are used as needed. 
SQL is used with the movies database. You can look at all the genres that are available right on the movies page. Looking at the other two queries, you can either look at all the movies in the database in order of popularity or you can be taken to a new page where you can pick a genre to search by. There is a drop down of genres you can pick through and return a list of the top 25 most popular movies by the genre you picked.

#### Any challenges you encountered  
1. I wanted to build my own RDS and my own SQL schema and I worked for the two weeks on it. I unfortunately had to give up today since it was due and just accept the fact I had to lose those 5 points. 
2. I had simliar issues to many other students where mysql would say it doesn't exist or pymysql not being defined. I have no idea how I got it fixed but ChatGPT was a huge help. 
3. I lost all my code from previous labs and had to start over originally and go through the labs again. Then, all my code was messed up and I couldn't figure out what was right and wrong so I restarted the entire project on Tuesday of this week. 

---

## Proposed Grade

### Technical Requirements

- [x] A working Flask application with a functioning web interface  
- [x] A MySQL database hosted on AWS RDS  
- [x] A DynamoDB table hosted on AWS  
- [x] At least one JOIN query in your SQL usage  
- [x] CRUD (Create, Read, Update, Delete) functionality for at least one entity  
- [x] A consistent theme that connects the relational and non-relational data  

---

### 🧮 Rubric

#### Part 1: Core Functionality

| Points Earned | Points Available | Criteria |
|---------------|------------------|----------|
| 10 | 10 | Website uses Flask and runs independently from VS Code |
| 15 | 15 | Relational database (MySQL/RDS) is correctly used in the project |
| 10 | 10 | Non-relational database (DynamoDB) is correctly used (e.g., user info stored/retrieved) |
| 10 | 10 | Implements full CRUD operations (Create, Read, Update, Delete) |
| 5  | 5  | Incorporates at least one SQL JOIN query |
| 0  | 5  | Uses own RDS instance inside student’s VPC |
| 5  | 5  | Uses own IAM account (e.g., ProjectOneUser) |
| 5  | 5  | Application avoids storing credentials in public GitHub (e.g., `creds.py` is excluded via `.gitignore`) |

#### Part 2: Code Quality and GitHub Submission

| Points Earned | Points Available | Criteria |
|---------------|------------------|----------|
| 10 | 10 | Code is organized across multiple files (e.g., `flaskapp.py`, `dbCode.py`) |
| 10 | 10 | Good software practices (clear naming, comments, error handling with `try/except`, modular functions) |
| 5  | 5  | GitHub repository is submitted with a clear commit history and a `README.md` file |

#### Part 3: Checkpoint Completion

| Points Earned | Points Available | Criteria |
|---------------|------------------|----------|
| 10 | 10 | Checkpoint submitted on time with a working Flask app that connects to RDS and renders dynamic data |

---







## Let's try code
``` python
print("hello world!")
```

**bolded**
*italics*
- bullet list
1. numbered list
--- horizontal line
