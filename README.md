# Lab works trecker

The goal is to help track the lab work progress 

# How to use

  - Expand the database on your PC (use  [create.sql](https://github.com/DianaGumar/Lab_trecker/blob/master/DAO/create.sql) )
  - Ran Lab_trecker.exe


### Control
* mouse click - add 10%
* ctrl + mouse click  - dell 10%
* shift - open/close options


### Options panel
Add subject:
- enter name;
- set lab count; 
- ress add button;
- reload application.

Del subject:
- shouse subject name;
- press dell button;
- reload application.

Change lab count:
- shouse subject name;
- set new lab count;
- press add button;
- reload application.


# Dependences
Project use MySql database and pyQt5.
Download [mysql.connector](https://dev.mysql.com/downloads/connector/python/) and PyQt5 whels. Or ran next lines:
```sh
$ pip install mysql-connector-python
$ pip insrall pyqt5
```
Also you need expand the database on your PC by  [create.sql](https://github.com/DianaGumar/Lab_trecker/blob/master/DAO/create.sql)
