import sqlite3 
  
connection = sqlite3.connect("myTable.db") 
  
crsr = connection.cursor() 
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE StudentDB (
Student_Name CHAR(20),
Student_Number INTEGER PRIMARY KEY,  
Student_Address VARCHAR(30));

CREATE TABLE EXAMS (
Exam_Code INTEGER PRIMARY KEY,
Exam_Subject CHAR(20),
Exam_Location CHAR(20));

CREATE TABLE WROTE_EXAM (
Student_Number_ID INTEGER,
Exam_Code_ID INTEGER,
Date VARCHAR(10),
FOREIGN KEY(STUDENT_NUMBER_ID) REFERENCES STUDENT(STUDENT_NUMBER),
FOREIGN KEY(EXAM_CODE_ID) REFERENCES EXAMS(EXAM_CODE));
)"""
  
# execute the statement 
crsr.execute(sql_command) 
  
# SQL command to insert the data in the table 
sql_command = """INSERT INTO StudentDB VALUES ("Jason Crabtree", "778272", "Santa Clara University");"""
crsr.execute(sql_command) 
sql_command = """INSERT INTO StudentDB VALUES ("Alan Hanson", "839972", "UCSC");"""
crsr.execute(sql_command) 
sql_command = """INSERT INTO StudentDB VALUES ("Mikka Hakkinnen", "1291023", "UCLA");"""
crsr.execute(sql_command) 
  
# another SQL command to insert the data in the table 
sql_command = """INSERT INTO EXAMS VALUES ("2331231", "CIS47B", "GC302");"""
crsr.execute(sql_command) 
sql_command = """INSERT INTO EXAMS VALUES ("3231992", "CIS39", "GC231");"""
crsr.execute(sql_command) 
sql_command = """INSERT INTO EXAMS VALUES ("9827737", "CIS47A", "GC489");"""
crsr.execute(sql_command) 

 
connection.commit() 
  
# close the connection 
connection.close() 