------------------------------------- LEB 13 PART :- A -------------------------
---------------------------- 1-------------
Create Table Person2
(
	PersonID Int Primary Key,
	PersonName Varchar(100) Not Null,
	Salary Decimal(8,2) Not Null,
	JoiningDate Datetime Not Null,
	City Varchar(100) Not Null,
	Age Int Null,
	BirthDate Datetime Not Null
);
Create Table PersonLog
(
	PLogID Int Primary Key identity(1,1),
	PersonID Int Not Null,
	PersonName Varchar(250) Not Null,
	Operation Varchar(50) Not Null,
	UpdateDate Datetime Not Null
);

INSERT INTO Person2 VALUES(8,'RAJ',10000,'1-1-22','RAJKOT',21,'1-1-2000')
INSERT INTO Person2 VALUES(5,'Meet',10000,'1-1-22','RAJKOT',23,'1-1-2002')
INSERT INTO Person2 VALUES(10,'DHARMIK',0000,'1-1-22','JAMNAGAR',23,'1-1-1999')

UPDATE Person2
SET Salary=40000
WHERE PersonName='DEEP'

Delete from Person2
where PersonName='DHARMIK'

SELECT * FROM PERSON2

ALTER TRIGGER TR_IN
ON PERSON2
FOR INSERT , UPDATE ,DELETE
AS 
BEGIN 
	PRINT('DATA INSERTED IN TABLLE......')
END


----------------------2--------------------
-- THIS CREATE INSERT AND UPDATE DATA RECODE IN PERSONLOG TABLE --
CREATE TRIGGER TR_IN_PersonLog
ON PERSON2
FOR INSERT , UPDATE 
AS 
BEGIN 
	INSERT INTO PersonLog  (	PersonID ,	PersonName ,Operation ,	UpdateDate )
	SELECT PersonID , PersonName,'INSERTED',GETDATE() FROM inserted
END
SELECT * FROM[dbo].[PersonLog]
SELECT * FROM PERSON2
CREATE TRIGGER TR_DEL_PersonLog
ON PERSON2
FOR DELETE 
AS 
BEGIN 
	INSERT INTO PersonLog  (	PersonID ,	PersonName ,Operation ,	UpdateDate )
	SELECT PersonID , PersonName,'DELETE DATA ',GETDATE() FROM deleted
END

------------------------------------- LEB 13 PART :- B -------------------------
ALTER TRIGGER TR_IN_PersonLog
ON PERSON2
INSTEAD OF INSERT , UPDATE 
AS 
BEGIN 
	INSERT INTO PersonLog  (	PersonID ,	PersonName ,Operation ,	UpdateDate )
	SELECT PersonID , PersonName,'INSERTED',GETDATE() FROM inserted
END

