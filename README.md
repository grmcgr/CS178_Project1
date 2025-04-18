# CS 178 Project 1
#### Grace McGrane
### Due 4/17/2025

# CS178 Project 1: Full-Stack Web Application

## Overview

This project replaces an in-class exam and reinforces the skills we've covered in the first part of the course. You will build a self-contained web application using Flask that connects to both a relational (SQL via AWS RDS) and a non-relational (NoSQL via AWS DynamoDB) database.

### Your project must:
- ✅ Be built and run locally using Visual Studio Code  
- ✅ Be deployed via Flask as a web application  
- ✅ Use both an RDS (MySQL) and DynamoDB database with a consistent theme  
- ✅ Be version-controlled using GitHub  
- ✅ Be accessible entirely through a browser interface (no terminal interaction)  

---

## 🔗 What to Submit

### ✅ GitHub Repository  
[GitHub Repository Link](https://github.com/grmcgr/CS178_Project1)

### ✅ Project Report  
- Screenshots of your working project  
    - `Project 1 Demo.mp4`  
- Description of how SQL and DynamoDB are integrated  
- Any challenges you encountered  

---

## 📊 Proposed Grade

### 🔧 Technical Requirements

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
