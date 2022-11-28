ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
+ solution
> sudo pip3 install --upgrade pip setuptools wheel

ERROR: 导入的包不能调试
+ solution
  > pip uninstall pydantic  
  > export SKIP_CYTHON=1   
  > pip install --no-cache-dir --no-binary :all: pydantic  