### 数据库迁移（migrate）
[migrate](../core/my_04_flask/01_migrate.py)  

命令行命令
```shell
# 初始化数据库配置
python core/my_04_flask/database.py db init

# 生成迁移文件 -m 操作信息
python core/my_04_flask/database.py db migrate -m 'info'

# 执行迁移操作
python core/my_04_flask/database.py db upgrade

# 查看迁移历史
python core/my_04_flask/database.py db history 

# 版本回滚
python core/my_04_flask/database.py db downgrade 4b421931e79e
```



### flask调试

```python
from werkzeug.middleware.profiler import ProfilerMiddleware
from flask import Flask


app = Flask(__name__)

# 打印SQL查询语句
app.config['SQLALCHEMY_ECHO'] = True

# 打印调用函数耗时信息
app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[100], sort_by=('cumtime',))

app.run(host='0.0.0.0', port=8881, debug=False)
```

