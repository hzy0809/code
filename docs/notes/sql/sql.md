## 函数

### 排序

```sql
USE
AdventureWorks2012;
GO
SELECT p.FirstName
	 , p.LastName
	 , ROW_NUMBER() OVER (ORDER BY a.PostalCode) AS "Row Number"  
    ,RANK() OVER (ORDER BY a.PostalCode) AS Rank  
    ,DENSE_RANK() OVER (ORDER BY a.PostalCode) AS "Dense Rank"  
    ,NTILE(4) OVER (ORDER BY a.PostalCode) AS Quartile  
    ,s.SalesYTD
	 , a.PostalCode
FROM Sales.SalesPerson AS s
	     INNER JOIN Person.Person AS p ON s.BusinessEntityID = p.BusinessEntityID
	     INNER JOIN Person.Address AS a ON a.AddressID = p.BusinessEntityID
WHERE TerritoryID IS NOT NULL
  AND SalesYTD <> 0;  
```

#### 连续排序无跳跃DENSE_RANK
  ```sql
  DENSE_RANK ( ) OVER ( [ <partition_by_clause> ] < order_by_clause > )  
  ```
#### 连续排序跳跃RANK
  ```sql
  RANK ( ) OVER ( [ partition_by_clause ] order_by_clause )  
  ```
#### 连续排序不重复ROW_NUMBER
  ```sql
  ROW_NUMBER ( ) OVER ( [ PARTITION BY value_expression , ... [ n ] ] order_by_clause )  
  ```
#### 排序分层NTILE
  ```sql
  NTILE (integer_expression) OVER ( [ <partition_by_clause> ] < order_by_clause > ) 
  ```
  PARTITION BY：划分组的依据   
  ORDER BY：排序依据
  
### 类型转换

[DOC](https://docs.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-ver15)
#### CONVERT
```sql
CONVERT ( data_type [ ( length ) ] , expression [ , style ] ) 
```
#### CAST
```sql
CAST ( expression AS data_type [ ( length ) ] ) 
```

### 精度转换
#### ROUND
```sql
ROUND ( numeric_expression , length [ ,function ] ) 
```
