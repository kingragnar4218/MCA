
	SELECT * FROM [dbo].[STUDENT]

	-- LEB 15 :- Part – A:   1. Write a function to print "hello world"

CREATE FUNCTION PRE1()
RETURNS VARCHAR(100)
AS	
BEGIN
	RETURN 'HELLOW WORLD..........'
END
SELECT dbo.PRE1()
--- 2.Write a function which returns addition of two numbers
ALTER FUNCTION PRE2(@V1 INT , @V2 INT )
RETURNS INT
AS	
BEGIN
	RETURN (@V1 + @V2)
END

SELECT dbo.PRE2(10 , 20)

-- 3.Write a function to print a cube of a given number.
CREATE FUNCTION PRE3(@V1 INT )
RETURNS INT
AS	
BEGIN
	RETURN (@V1 * @V1 * @V1)
END

SELECT dbo.PRE3(10)
-- 4. Write a function to check whether the given number is ODD or EVEN.
ALTER FUNCTION PRE4(@V1 INT )
RETURNS VARCHAR(100)
AS	
BEGIN
	DECLARE @R VARCHAR(100)
	IF (@V1 % 2 LIKE 0)
	
		SET @R= 'NUMBER IS EVEN '
	 
	ELSE
	
		SET @R= 'NUMBER IS ODD'
	
	 RETURN @R
END
SELECT dbo.PRE4(1)

--  5.Write a function which returns a table with details of a person whose first name starts with B

CREATE FUNCTION PRE5( )
RETURNS TABLE 
AS	

	RETURN(SELECT * FROM [dbo].[STUDENT] WHERE NAME LIKE 'R%')

SELECT * FROM dbo.PRE5()
-- 6.Write a function which returns a table with unique first names from the person table.CREATE FUNCTION PRE6( )
RETURNS TABLE 
AS	

	RETURN(SELECT DISTINCT NAME  FROM [dbo].[STUDENT] )

SELECT * FROM dbo.PRE6() -- PART :- B Write a function to compare two integers and return the comparison result. (Using Case statement) CREATE FUNCTION PRE7(@N1 INT , @N2 INT )
RETURNS VARCHAR(100)
AS	
BEGIN
	DECLARE @R VARCHAR(100)= 
	CASE 
		WHEN @N1 > @N2 THEN 'N1 IS BIG '	
		WHEN @N2 > @N1 THEN 'N2 IS BIG '	
		ELSE 'NUMBER IS EQUAL '
	END
		RETURN @R
END

SELECT dbo.PRE7(100 ,20)--8.Write a function to print number from 1 to N. (Using while loop)

