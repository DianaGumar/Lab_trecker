create database treckerh;
use treckerh;

create table Subjects (
	SubjectID int primary key AUTO_INCREMENT not null,
    SubjectName nvarchar(40) not null,
    LabCount int);
    
    

create table Labs
(
	LabID int primary key AUTO_INCREMENT not null,
	SubjectID int not null,
    LabNumber int not null,
    IsMaked int
);


alter table Labs add foreign key (SubjectID)
	references Subjects (SubjectID) on delete cascade;
    

       
       
       
       
       
       
       