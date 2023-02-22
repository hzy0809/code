
# CODE   

---
> 笔记  

## PROJECT STRUCTURE   
   

---
[code](.)/  
├── [const.py](const.py)                                                   # 项目常量                                              
├── [README.md](README.md)                                                                                                     
├── [requirements.txt](requirements.txt)                                                                                       
├── [docs](docs)/                                                                                                              
│   └── [notes](docs/notes)/                                                                                                       
│       ├── [docker](docs/notes/docker)/                                                                                               
│       │   └── [command.md](docs/notes/docker/command.md)                                                                                 
│       ├── [elasticsearch](docs/notes/elasticsearch)/                                                                                 
│       │   └── [elasticsearch.md](docs/notes/elasticsearch/elasticsearch.md)                                                              
│       ├── [git](docs/notes/git)/                                                                                                     
│       │   ├── [command.md](docs/notes/git/command.md)                                                                                    
│       │   └── [git.md](docs/notes/git/git.md)                                                                                            
│       ├── [linux](docs/notes/linux)/                                                                                                 
│       │   ├── [crontab.md](docs/notes/linux/crontab.md)                                                                                  
│       │   ├── [linux.md](docs/notes/linux/linux.md)                                                                                      
│       │   └── [shell.md](docs/notes/linux/shell.md)                                                                                      
│       ├── [minio](docs/notes/minio)/                                                                                                 
│       │   ├── [error.md](docs/notes/minio/error.md)                                                                                      
│       │   ├── [mc.md](docs/notes/minio/mc.md)                                                                                            
│       │   └── [pyminio.md](docs/notes/minio/pyminio.md)                                                                                  
│       ├── [mongo](docs/notes/mongo)/                                                                                                 
│       │   ├── [MongoDB.md](docs/notes/mongo/MongoDB.md)                                                                                  
│       │   └── [MongoDB权威指南（第2版）.pdf](docs/notes/mongo/MongoDB权威指南（第2版）.pdf)                                                              
│       ├── [neo4j](docs/notes/neo4j)/                                                                                                 
│       │   └── [neo4j.ipynb](docs/notes/neo4j/neo4j.ipynb)                                                                                
│       ├── [pycharm](docs/notes/pycharm)/                                                                                             
│       │   ├── [pycharm_error.md](docs/notes/pycharm/pycharm_error.md)                                                                    
│       │   └── [pycharm_setting.md](docs/notes/pycharm/pycharm_setting.md)                                                                
│       ├── [python](docs/notes/python)/                                                                                               
│       │   └── [requests.md](docs/notes/python/requests.md)                                                                               
│       ├── [redis](docs/notes/redis)/                                                                                                 
│       │   └── [redis.md](docs/notes/redis/redis.md)                                                                                      
│       ├── [shortcut](docs/notes/shortcut)/                                                                                           
│       │   └── [zsh.md](docs/notes/shortcut/zsh.md)                                                                                       
│       └── [sql](docs/notes/sql)/                                                                                                     
│           ├── [sql.md](docs/notes/sql/sql.md)                                                                                            
│           └── [sqlserver](docs/notes/sql/sqlserver)/                                                                                     
│               └── [sqlserver.md](docs/notes/sql/sqlserver/sqlserver.md)                                                                      
├── [python](python)/                                                                                                          
│   ├── [__init__.py](python/__init__.py)                                                                                          
│   ├── [EXTENTIONLIBRARY.md](python/EXTENTIONLIBRARY.md)                                                                          
│   ├── [README.MD](python/README.MD)                                                                                              
│   ├── [STANDARDLIBRARY.md](python/STANDARDLIBRARY.md)                                                                            
│   ├── [cookbook](python/cookbook)/                                                                                               
│   │   ├── [class_object.ipynb](python/cookbook/class_object.ipynb)                                                                   
│   │   ├── [dataStructure_algorithm.ipynb](python/cookbook/dataStructure_algorithm.ipynb)                                                     
│   │   ├── [express_evaluator.py](python/cookbook/express_evaluator.py)                                                               
│   │   ├── [file_io.ipynb](python/cookbook/file_io.ipynb)                                                                             
│   │   ├── [function.ipynb](python/cookbook/function.ipynb)                                                                           
│   │   ├── [Metaprogramming.ipynb](python/cookbook/Metaprogramming.ipynb)                                                             
│   │   ├── [module_package.ipynb](python/cookbook/module_package.ipynb)                                                               
│   │   ├── [multitask.ipynb](python/cookbook/multitask.ipynb)                                                                         
│   │   ├── [network_web.ipynb](python/cookbook/network_web.ipynb)                                                                     
│   │   ├── [number&date&time.ipynb](python/cookbook/number&date&time.ipynb)                                                           
│   │   ├── [script_system.ipynb](python/cookbook/script_system.ipynb)                                                                 
│   │   ├── [str&text.ipynb](python/cookbook/str&text.ipynb)                                                                           
│   │   └── [数据编码和处理.ipynb](python/cookbook/数据编码和处理.ipynb)                                                                             
│   ├── [design_patterns](python/design_patterns)/                                                                                 
│   │   ├── [abstract_factory.py](python/design_patterns/abstract_factory.py)                                                          
│   │   ├── [builder.py](python/design_patterns/builder.py)                                                                            
│   │   ├── [factory.py](python/design_patterns/factory.py)                                                                            
│   │   ├── [prototype.py](python/design_patterns/prototype.py)                                                                        
│   │   ├── [README.MD](python/design_patterns/README.MD)                                                                              
│   │   └── [singleton.py](python/design_patterns/singleton.py)                                                                        
│   ├── [elasticsearch](python/elasticsearch)/                                                                                     
│   │   ├── [elasticsearch_basic.py](python/elasticsearch/elasticsearch_basic.py)                                                      
│   │   ├── [es_count.py](python/elasticsearch/es_count.py)                                                                            
│   │   └── [mysql-replication.py](python/elasticsearch/mysql-replication.py)                                                          
│   ├── [flask](python/flask)/                                                                                                     
│   │   ├── [01_migrate.py](python/flask/01_migrate.py)                                                                                
│   │   └── [flask.md](python/flask/flask.md)                                                                                          
│   ├── [mongo](python/mongo)/                                                                                                     
│   │   ├── [01_pymongo.py](python/mongo/01_pymongo.py)                                                                                
│   │   ├── [context_diff.ipynb](python/mongo/context_diff.ipynb)                                                                      
│   │   ├── [delete_mongo_doc.ipynb](python/mongo/delete_mongo_doc.ipynb)                                                              
│   │   ├── [text.txt](python/mongo/text.txt)                                                                                          
│   │   ├── [Untitled.ipynb](python/mongo/Untitled.ipynb)                                                                              
│   │   └── [Untitled1.ipynb](python/mongo/Untitled1.ipynb)                                                                            
│   ├── [pandas](python/pandas)/                                                                                                   
│   │   ├── [data_structures.ipynb](python/pandas/data_structures.ipynb)                                                               
│   │   ├── [essential_basic_functionality.ipynb](python/pandas/essential_basic_functionality.ipynb)                                                     
│   │   ├── [excel_split.py](python/pandas/excel_split.py)                                                                             
│   │   ├── [io_tools.ipynb](python/pandas/io_tools.ipynb)                                                                             
│   │   └── [test.ipynb](python/pandas/test.ipynb)                                                                                     
│   ├── [redis](python/redis)/                                                                                                     
│   │   ├── [00_connetc_redis.py](python/redis/00_connetc_redis.py)                                                                    
│   │   └── [__init__.py](python/redis/__init__.py)                                                                                    
│   └── [usage](python/usage)/                                                                                                     
│       ├── [__init__.py](python/usage/__init__.py)                                                                                    
│       ├── [README.MD](python/usage/README.MD)                                                                                        
│       ├── [domain_modeling](python/usage/domain_modeling)/                                                                           
│       │   └── [test.ipynb](python/usage/domain_modeling/test.ipynb)                                                                      
│       ├── [function](python/usage/function)/                                                                                         
│       │   └── [builtin.ipynb](python/usage/function/builtin.ipynb)                                                                       
│       ├── [function_tools](python/usage/function_tools)/                                                                             
│       │   ├── [cache.py](python/usage/function_tools/cache.py)                                                                           
│       │   └── [README.MD](python/usage/function_tools/README.MD)                                                                         
│       ├── [multiTask](python/usage/multiTask)/                                                                                       
│       │   ├── [00_gevent.py](python/usage/multiTask/00_gevent.py)                                                                        
│       │   └── [__init__.py](python/usage/multiTask/__init__.py)                                                                          
│       ├── [OOP](python/usage/OOP)/                                                                                                   
│       │   ├── [00_magic.py](python/usage/OOP/00_magic.py)                                                                                
│       │   ├── [01_class_decorator.py](python/usage/OOP/01_class_decorator.py)                                                            
│       │   ├── [02_metaclass.py](python/usage/OOP/02_metaclass.py)                                                                        
│       │   ├── [03_inherit.ipynb](python/usage/OOP/03_inherit.ipynb)                                                                      
│       │   ├── [__init__.py](python/usage/OOP/__init__.py)                                                                                
│       │   ├── [bound_method.py](python/usage/OOP/bound_method.py)                                                                        
│       │   ├── [contextManager.py](python/usage/OOP/contextManager.py)                                                                    
│       │   ├── [decorator.py](python/usage/OOP/decorator.py)                                                                              
│       │   ├── [operation_overload.py](python/usage/OOP/operation_overload.py)                                                            
│       │   └── [opp.md](python/usage/OOP/opp.md)                                                                                          
│       ├── [os](python/usage/os)/                                                                                                     
│       │   ├── [00_basic.py](python/usage/os/00_basic.py)                                                                                 
│       │   └── [__init__.py](python/usage/os/__init__.py)                                                                                 
│       ├── [protocol](python/usage/protocol)/                                                                                         
│       │   ├── [generator.py](python/usage/protocol/generator.py)                                                                         
│       │   └── [iterator.py](python/usage/protocol/iterator.py)                                                                           
│       ├── [tools](python/usage/tools)/                                                                                               
│       │   └── [logging_usage.py](python/usage/tools/logging_usage.py)                                                                    
│       └── [transitions](python/usage/transitions)/                                                                                   
│           ├── [machine.ipynb](python/usage/transitions/machine.ipynb)                                                                    
│           └── [my_state_diagram](python/usage/transitions/my_state_diagram)                                                              
└── [scripts](scripts)/                                                                                                        
    ├── [jupyter.sh](scripts/jupyter.sh)                                                                                           
    └── [personal](scripts/personal)/                                                                                              
        ├── [scheduler.py](scripts/personal/scheduler.py)                                                                              
        ├── [send_email.py](scripts/personal/send_email.py)                                                                            
        ├── [structure.py](scripts/personal/structure.py)                                                                              
        └── [minio](scripts/personal/minio)/                                                                                           
            ├── [delete_object.ipynb](scripts/personal/minio/delete_object.ipynb)                                                          
            ├── [minio.ipynb](scripts/personal/minio/minio.ipynb)                                                                          
            └── [upload.ipynb](scripts/personal/minio/upload.ipynb)                                                                        
