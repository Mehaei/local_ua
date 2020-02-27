# local_ua

# fake_useragent 是一个非常好用的随机请求头模块
# 但因为这个模块在本地运行总是会因为各种各样的原因, 报错
# 所以重新整理fake_useragent模块的所有请求头, 实现在本地获取随机请求头
# 实际上就是把所有的请求头保存到本地 😂

# ua.py 是所有的请求头
# ua_b.py 是所有的请求头按照浏览器分类
# ua_c.py 是主流的浏览器请求头

# 安装方法
# 以windows系统为例，其他操作系统操作过程类似。
# 提前正确安装好fake_userage，然后执行下面操作完成安装。
# 1. clone local_ua的压缩包到本地  
# 2. 解压并找到里面的user_agent文件夹，文件夹内包含__init__.py、main.py、ua.py、ua_b.py、ua_c.py等5个文件
# 3. 找到python第三方模块安装目录，一般在X:\XXX\Anaconda3\Lib\site-packages\fake_useragent路径下
# 4. 将user_agent文件夹5个附件复制并覆盖fake_useragent，安装完毕

# 使用方法
```python
from user_agent import UserAgent
# 获取所有浏览器的随机请求头
ua = UserAgent()
ua.rget

# 获取chrome随机请求头
ua = UserAgent("chrome")
ua.rget
```

# 测试用例
```
import requests
from fake_useragent import UserAgent

ua = UserAgent().rget
headers = {'User-agent': ua}
url ='https://www.baidu.com'
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
print(response.text)
```
