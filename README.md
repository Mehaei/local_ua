# local_ua

# fake_useragent 是一个非常好用的随机请求头模块
# 但因为这个模块在本地运行总是会因为各种各样的原因, 报错
# 所以重新整理fake_useragent模块的所有请求头, 实现在本地获取随机请求头
# 实际上就是把所有的请求头保存到本地 😂

# ua.py 是所有的请求头
# ua_b.py 是所有的请求头按照浏览器分类
# ua_c.py 是主流的浏览器请求头

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