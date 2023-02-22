## documents

+ [pandas](https://pandas.pydata.org/docs/reference/io.html#)

## I/O

### read_csv

+ `keep_default_na=False` 防止将某些默认值转换成NAN



## General Function

### merge

```python
pd.merge(sdf, cid1_df, left_on='cid1', right_index=True)
```

## Dataframe

### join

```python
rule_type = sdf.apply(check_rule_type, axis=1)
rule_type.name = 'rule_type'
sdf.join(rule_type)
```



### query

+ 找到含有