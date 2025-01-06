# WeAuth
使用微信公众号或者QQ机器人来帮助你添加白名单与管理Minecraft服务器!

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
 - [ ] CdKey生成与兑换系统
 - [ ] 从Minecraft能反向输出信息到微信公众号（仅支持rcon） 
 - [ ] 执行定时脚本  
 - [ ] https支持
### 桥梁
 - [x] 通过[Flask](https://github.com/pallets/flask)与微信公众号服务器交互     
 - [ ] 通过Flask与QQ机器人服务器交互  
 - [x] 通过[MCSManager](https://github.com/MCSManager/MCSManager)的API与Minecraft服务器交互（单向）  
 - [ ] 通过rcon协议与Minecraft服务器交互（双向）  
 - [ ] 通过[MCDReforged](https://github.com/MCDReforged/MCDReforged)插件与Minecraft服务器交互  
### 数据库
 - [x] 集成的SQLite3  
 - [ ] MySQL连接支持  

## WeAuth所需要的安装与运行环境  
```command
Python>=3.8
服务器的80端口必须可以被访问*
```   
* 微信公众号只会通过80(http)或443(https)与开发者服务器进行交互。
* **您运行WeAuth的服务器如果是在大陆境内的云服务器，只有经过备案才能使用80/443端口。**





WeAuth已上传至[Pypi](https://pypi.org/project/weauth/)，如果




 



