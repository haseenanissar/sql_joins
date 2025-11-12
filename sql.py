/*1.INNER JOIN */
SELECT C.CustomerID,P.FirstName,P.LastName,O.SalesOrderID AS OrderID,O.OrderDate
FROM Sales.Customer C
INNER JOIN Sales.SalesOrderHeader O
ON C.CustomerID = O.CustomerID
LEFT JOIN Person.Person P
ON P.BusinessEntityID = O.CustomerID;

SELECT P.Name AS [Product Name],PC.Name AS [Product Category Name]
FROM Production.[Product] P
INNER JOIN Production.ProductSubcategory PS
ON P.ProductID = PS.ProductSubcategoryID
INNER JOIN Production.ProductCategory PC
ON PC.ProductCategoryID =PS.ProductSubcategoryID
/* PART 2 LEFT JOIN */
SELECT P.Name AS [Product Name], SOD.[SalesOrderID] AS [Order ID],SOH.OrderDate AS
[Order Date]
FROM Production.[Product] P
LEFT JOIN Sales.[SalesOrderDetail] SOD
ON p.ProductID = SOD.ProductID
LEFT JOIN Sales.[SalesOrderHeader] SOH
ON SOD.SalesOrderID = SOH.SalesOrderID
/*PART 3 RIGHT JOIN*/
SELECT ST.Name AS [Territory Name],SP.BusinessEntityID AS [Sales ID]
FROM Sales.SalesTerritory ST
RIGHT JOIN Sales.SalesPerson SP
ON ST.TerritoryID = SP.TerritoryID

/*PART 4 FULL OUTER JOIN*/
SELECT P.Name AS [Product Name],SOD.SalesOrderID AS [Order ID],SOD.OrderQty AS
[Order Quantity]
FROM Production.[Product] AS P
FULL OUTER JOIN Sales.SalesOrderDetail AS SOD
ON P.ProductID = SOD.ProductID
/*PART 5 CROSS JOIN*/
SELECT P.Name AS [Product Name],ST.Name AS [Territory Name]
FROM Production.[Product] P
CROSS JOIN Sales.SalesTerritory ST

SELECT P.FirstName AS [Employee Name],E.JobTitle AS [Job Title]
FROM HumanResources.Employee E
CROSS JOIN HumanResources.EmployeeDepartmentHistory EDH
INNER JOIN Person.Person P
ON P.BusinessEntityID = EDH.BusinessEntityID

/*6.INNER JOIN, LEFT JOIN, and FULL OUTER JOIN*/
SELECT P.FirstName AS [Customer Name],SOH.SalesOrderID AS [Order ID],SOH.OrderDate
AS [Order Date],PRO.Name AS [Product Name],ST.Name AS [Sales Territory Name]
FROM Sales.Customer C
RIGHT JOIN Person.Person P
ON C.CustomerID =P.BusinessEntityID
LEFT JOIN Sales.SalesOrderHeader SOH
ON C.CustomerID =SOH.CustomerID
LEFT JOIN Sales.SalesOrderDetail SOD
ON SOH.SalesOrderID = SOD.SalesOrderID
FULL OUTER JOIN Production.[Product] PRO
ON PRO.ProductID = SOD.ProductID
INNER JOIN Sales.SalesTerritory ST
ON ST.TerritoryID =C.TerritoryID
