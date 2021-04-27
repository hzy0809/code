## 函数

### 排序
```sql
USE AdventureWorks2012;  
GO  
SELECT p.FirstName, p.LastName  
    ,ROW_NUMBER() OVER (ORDER BY a.PostalCode) AS "Row Number"  
    ,RANK() OVER (ORDER BY a.PostalCode) AS Rank  
    ,DENSE_RANK() OVER (ORDER BY a.PostalCode) AS "Dense Rank"  
    ,NTILE(4) OVER (ORDER BY a.PostalCode) AS Quartile  
    ,s.SalesYTD  
    ,a.PostalCode  
FROM Sales.SalesPerson AS s   
    INNER JOIN Person.Person AS p   
        ON s.BusinessEntityID = p.BusinessEntityID  
    INNER JOIN Person.Address AS a   
        ON a.AddressID = p.BusinessEntityID  
WHERE TerritoryID IS NOT NULL AND SalesYTD <> 0;  
```
+ 连续排序无跳跃
  ```sql
  DENSE_RANK ( ) OVER ( [ <partition_by_clause> ] < order_by_clause > )  
  ```
+ 连续排序跳跃
  ```sql
  RANK ( ) OVER ( [ partition_by_clause ] order_by_clause )  
  ```
+ 连续排序不重复
  ```sql
  ROW_NUMBER ( ) OVER ( [ PARTITION BY value_expression , ... [ n ] ] order_by_clause )  
  ```
+ 排序分层
  ```sql
  NTILE (integer_expression) OVER ( [ <partition_by_clause> ] < order_by_clause > ) 
  ```
    PARTITION BY：划分组的依据   
    ORDER BY：排序依据