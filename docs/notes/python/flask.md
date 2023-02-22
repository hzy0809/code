
## 时序图
```mermaid
gantt
    title      flask process
    dateFormat HH
    axisFormat %H
    
    section    Flask
    begin            : milestone, m1, 00, 0h
    process          : m2, 00, 24h
		app context      : done, m3, 01, 22h
		request context  : done, 02, 20h
		process request  : crit, done, 03, 18h
		end              : milestone, 24, 0h
		
```