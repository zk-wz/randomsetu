# A random picture sending python script for mirai

使用本项目之前，你需要先安装好`mirai`和最新版的`mirai-api-http` 插件

#### 下载本项目时请直接下载两个代码文件，不要下载整个项目！！！（因为有个文件夹是放图的，你下了也没用，当然你想下也没问题）

## 安装依赖

```bash
pip install graia-application-mirai
pip install graia-broadcast --upgrade
```

## 必要的设置

```python
host="http://0.0.0.0:8080", # 填入 httpapi 服务运行的地址
authKey="123456", # 填入 authKey
account=123456789, # 你的机器人的 qq 号
websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
```

### 网络图片脚本

进入项目文件夹，运行代码

```bash
python random setu-from internet.py
```

显示运行成功后，输入“色图”或以“色图”开头的文字即可触发色图发送

默认触发关键字为“色图”，你可以通过修改`message.asDisplay().startswith("")`以修改关键字

默认图库来自本仓库的piccache(图片太se可能有一半qq都发不出来)，你可以通过修改`Image.fromNetworkAddress(）`的值来修改图库

### 本地图片脚本

进入项目文件夹，运行代码

```bash
python random setu-from local.py
```

显示运行成功后，输入“本地”或以“本地”开头的文字即可触发色图发送

默认触发关键字为“本地”，你可以通过修改`message.asDisplay().startswith("")`以修改关键字

你可以通过修改`az`这个变量来修改图片路径