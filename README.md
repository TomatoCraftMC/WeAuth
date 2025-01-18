WeAuth
--------

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/weauth)](https://pypi.org/project/weauth)
[![PyPI - Version](https://img.shields.io/pypi/v/weauth)](https://pypi.org/project/weauth)
[![GitHub License](https://img.shields.io/github/license/TomatoCraftMC/WeAuth)](https://github.com/TomatoCraftMC/WeAuth/blob/main/LICENSE)
[![docs](https://readthedocs.org/projects/mcdreforged/badge/)](https://weauth.readthedocs.io/)

<div align=center><img src="logo/long_banner.png"></div>

>使用微信公众号或者QQ机器人来帮助你添加白名单与管理Minecraft服务器!  
> [开发与问题反馈交流群](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=zZWKaVfLOLW19NRVtffSgxPZivKkK45n&authKey=cF0bEvwv%2FoHTMrXJpzkvGvZhuYdF7WCefRF4F21dqnJMSvzOCL%2FZSpGqnwEVYE7G&noverify=0&group_code=1017293626)
  
## WeAuth的作用

![原理图](docs/assets/pic11.png)

WeAuth架起一座连接微信公众号（QQ机器人）与Minecraft服务器的桥梁。  

你可以直接在微信公众号（或者QQ机器人）对Minecraft服务器进行指令操作。

此外，WeAuth可以单独作为微信公众号验证开发者服务器url地址使用。  

## 浏览WeAuth[使用手册](https://weauth.readthedocs.io/)

## WeAuth目前的开发路线图  

### 功能  
 - [x] 白名单添加与管理   
 - [x] 管理员直接通过公众号发送指令（单向）  
 - [x] 微信公众号验证开发者服务器URL地址  
- [x] CdKey生成与兑换系统 (1.5.0起支持)
 - [x] 从Minecraft能反向输出信息到微信公众号（仅支持rcon）(1.4.0起支持)
 - [ ] 执行定时脚本  
 - [ ] https支持
- [x] 可直接在微信公众号运行WeAuth指令 (1.5.3起支持)
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

## 安装WeAuth
WeAuth已上传至[Pypi](https://pypi.org/project/weauth/)，您可以直接通过`pip`指令安装。  
```shell
pip3 install weauth  # 使用官方Pypi源
```   

### 推荐使用国内镜像源加速

```shell
pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple weauth  # 使用清华源加速
```

## 在微信公众号发送WeAuth指令

> WeAuth指令使用!开头, 只有超级管理员可以使用该功能

```shell
!op [ID]   # 将ID加入ops.yaml中的普通管理员(可以在公众号发出游戏内指令)
!sop [ID]  # 将ID加入ops.yaml中的超级管理员(可以在公众号中发出WeAuth指令)
!v  # 查看WeAuth版本信息
!g [mineID] [mineNum] [cdkeyNum] [comment]   # 生成礼物 
!l # 显示所有用户ID
!s [player_id]  # 显示该用户ID的封禁、订阅情况
!b [player_id]  # 封禁该用户，同时会移出白名单
!ub [player_id]  # 移出封禁
!d [player_id]  # 在数据库中删除该玩家信息，会自动移出白名单
!u [player_id] [is_ban] [is_sub]  # 手动更新该玩家是否封禁标志与是否订阅标志 （会自动同步到游戏服务器）
```
## [版本更新日志](docs/UPDATE.md)  
## 贡献  

欢迎大家参与WeAuth的开发！请发起PR时选择`dev`
branch。如有任何问题欢迎在[Issues](https://github.com/TomatoCraftMC/WeAuth/issues)中提出。

# Licence

WeAuth is released under the [GPLv3.0](LICENSE) license.   
[pyyaml](https://github.com/yaml/pyyaml) : MIT   
[tcping](https://github.com/zhengxiaowai/tcping) : MIT    
[rcon](https://github.com/conqp/rcon): GPLv3   
[Flask](https://github.com/pallets/flask/): BSD-3-Clause license  
[MCDReforged](https://github.com/MCDReforged/MCDReforged): LGPLv3









 


