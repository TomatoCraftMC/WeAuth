WeAuth
--------

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/weauth)](https://pypi.org/project/weauth)
[![PyPI - Version](https://img.shields.io/pypi/v/weauth)](https://pypi.org/project/weauth)
[![GitHub License](https://img.shields.io/github/license/TomatoCraftMC/WeAuth)](https://github.com/TomatoCraftMC/WeAuth/blob/main/LICENSE)

<div align=center><img src="logo/long_banner.png"></div>

>使用微信公众号或者QQ机器人来帮助你添加白名单与管理Minecraft服务器!  
> [开发与问题反馈交流群](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=zZWKaVfLOLW19NRVtffSgxPZivKkK45n&authKey=cF0bEvwv%2FoHTMrXJpzkvGvZhuYdF7WCefRF4F21dqnJMSvzOCL%2FZSpGqnwEVYE7G&noverify=0&group_code=1017293626)
  
## WeAuth的作用
```command
         微信公众号            <=======(rcon)=======>
玩家<====>        <====>WeAuth                      Minecraft Server
         QQ 机器人             ==(MCSManager API)==>
```
WeAuth架起一座连接微信公众号（QQ机器人）与Minecraft服务器的桥梁。  

你可以直接在微信公众号(或者QQ机器人）对Minecraft服务器进行指令操作。  

此外，WeAuth可以单独作为微信公众号验证开发者服务器url地址使用。  

## WeAuth目前的开发路线图  

### 功能  
 - [x] 白名单添加与管理   
 - [x] 管理员直接通过公众号发送指令（单向）  
 - [x] 微信公众号验证开发者服务器URL地址  
- [x] CdKey生成与兑换系统 (1.5.0起支持)
 - [x] 从Minecraft能反向输出信息到微信公众号（仅支持rcon）(1.4.0起支持)
 - [ ] 执行定时脚本  
 - [ ] https支持
- [x] 可直接在微信公众号运行WeAuth指令
- [ ] log系统
### 桥梁
 - [x] 通过[Flask](https://github.com/pallets/flask)与微信公众号服务器交互     
 - [ ] 通过Flask与QQ机器人服务器交互  
 - [x] 通过[MCSManager](https://github.com/MCSManager/MCSManager)的API与Minecraft服务器交互（单向）  
 - [x] 通过rcon协议与Minecraft服务器交互（双向） (1.4.0起支持) 
 - [ ] 通过[MCDReforged](https://github.com/MCDReforged/MCDReforged)插件与Minecraft服务器交互  
### 数据库
 - [x] 集成的SQLite3  
 - [ ] MySQL连接支持  

## WeAuth所需要的安装与运行环境  
```command
Python>=3.8 (推荐使用Python>=3.10)
服务器的80端口必须可以被访问*
```   
* 微信公众号只会通过80(http)或443(https)与开发者服务器进行交互。
* **如果您运行WeAuth的服务器是在大陆境内的云服务器，只有经过备案才能使用80/443端口。**  
* **如果您运行WeAuth的服务器使用的家庭宽带，则80/443端口无法使用。**   
> 您可以购买一台便宜的云服务器，经过备案后专门运行WeAuth。此时，如果您的Minecraft服务器无法连接到WeAuth服务器
> （比如IPv6原因，云服务器厂商一般不提供IPv6访问），可以使用[frp](https://github.com/fatedier/frp)等工具解决。  


## 安装WeAuth
WeAuth已上传至[Pypi](https://pypi.org/project/weauth/)，您可以直接通过`pip`指令安装。  
```shell
pip3 install weauth  # 使用官方Pypi源
```   

### 推荐使用国内镜像源加速

```shell
pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple weauth  # 使用清华源加速
```   

### 建议使用Python>=3.10版本
安装完成后，此时，你已经可以直接在控制台使用`weauth`指令来运行WeAuth。但我们建议您在新建的文件夹内运行WeAuth。    
```shell
mkdir WeAuth
cd WeAuth
weauth
```   
## 配置WeAuth
首次运行WeAuth会自动生成`config.yaml`与`ops.yaml`文件。  
您需要在文件内填入合适信息才能正式运行WeAuth。  
### config.yaml  
该文件包含WeAuth连接微信/QQ服务器所需要的凭证与连接MCSManager或rcon所需要的信息。  
您可以在启动WeAuth时添加参数（见下一节），这些参数的优先级高于`config.yaml`中的内容。   
  
### ops.yaml  
该文件保存着管理员ID信息（指游戏角色ID）。  
该管理员是指可以通过微信公众号直接发送指令到游戏内执行。  
>请勿将WeAuth管理员与游戏内op混淆，但是在未来，WeAuth将支持从游戏服务器拉取op玩家ID信息。    

**只有`ops.yaml`文件支持热重载**

### gift_list.yaml

该文件储存CDKey系统的礼物元数据，每个礼物对应一个哈希值。该文件通过CDKey系统自动生成与管理，具体见[CDKey系统说明](docs/Cdkey.md)。

### cdkey.yaml

该文件储存所有未兑换的CDKeys(兑换码)。该文件本质是一个Python字典，键为礼物的哈希值(对应gift_list.yaml)
，键值为该礼物对应所有兑换码的列表。  
玩家成功兑换CDKey时会自动从该文件中删除对应兑换码。该文件通过CDKey系统自动生成与管理，具体见[CDKey系统说明](docs/Cdkey.md)。
## WeAuth启动参数(近期正在快速更新)
```shell
weauth
-v  # 查看版本信息
-h  # 查看启动参数帮助信息
-p [port]  # 启动后在port端口监听。默认为80端口
-r [route]  # web服务路由。默认为“/wx”
-w  # 微信服务器验证模式，需配合 -t指令使用
-t [token]  # 微信服务器验证用的token，也就是您在微信公众号后台输入的token内容
-g  # 进入CDKey生成系统
-op [ID]  # 将ID加入ops.yaml中的普通管理员(可以在公众号发出游戏内指令)
-sop [id] # 将ID加入ops.yaml中的超级管理员(可以在公众号中发出WeAuth指令)
-test  # 以测试模式启动，仅用于开发测试
```   
在绝大多数情况下，您无需输入任何参数，直接使用`weauth`启动即可。  
程序将在`http://127.0.0.1/wx`监听来自微信的请求。  
## [微信公众号后台配置](docs/WeChatConfig.md)
## [MCSManager后台配置](docs/MCSManagerConfig.md)
## [rcon设置](docs/Rcon.md)
## [CDKey系统使用指南](docs/Cdkey.md)

## 在微信公众号发送WeAuth指令

> WeAuth指令使用!开头, 只有超级管理员可以使用该功能

```shell
!op [ID]   # 将ID加入ops.yaml中的普通管理员(可以在公众号发出游戏内指令)
!sop [ID]  # 将ID加入ops.yaml中的超级管理员(可以在公众号中发出WeAuth指令)
!v  # 查看WeAuth版本信息
!g [mineID] [mineNum] [cdkeyNum] [comment]   # 生成礼物 暂未支持
```
## [版本更新日志](docs/UPDATE.md)  
## 贡献  
# Licence

WeAuth is released under the [GPLv3.0](LICENSE) license.   
[pyyaml](https://github.com/yaml/pyyaml) : MIT   
[tcping](https://github.com/zhengxiaowai/tcping) : MIT    
[rcon](https://github.com/conqp/rcon): GPLv3   
[Flask](https://github.com/pallets/flask/): BSD-3-Clause license  
[MCDReforged](https://github.com/MCDReforged/MCDReforged): LGPLv3









 


