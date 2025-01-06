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
* **如果您运行WeAuth的服务器是在大陆境内的云服务器，只有经过备案才能使用80/443端口。**  
* **如果您运行WeAuth的服务器使用的家庭宽带，则80/443端口无法使用。**   
> 您可以购买一台便宜的云服务器，经过备案后专门运行WeAuth。此时，如果您的Minecraft服务器无法连接到WeAuth服务器
（比如IPv6原因，云服务器厂商一般不提供IPv6访问），可以使用[frp](https://github.com/fatedier/frp)等工具解决。  


## 安装WeAuth
WeAuth已上传至[Pypi](https://pypi.org/project/weauth/)，您可以直接通过`pip`指令安装。  
```command
pip3 install weauth  # 使用官方Pypi源
```   
```command 
pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple weauth  # 使用清华源加速
```   
安装完成后，此时，你已经可以直接在控制台使用`weauth`指令来运行WeAuth。但我们建议您在新建的文件夹内运行WeAuth。    
```command
mkdir WeAuth
cd WeAuth
weauth
```   
## 配置WeAuth
首次运行WeAuth会自动生成`config.yaml`与`ops.yaml`文件。  
您需要在文件内填入合适信息才能正式运行WeAuth。  
### config.yaml  
该文件包含WeAuth连接微信/QQ服务器所需要的凭证与连接MCSManager所需要的信息。  
您可以在启动WeAuth时添加参数（见下一节），这些参数的优先级高于`config.yaml`中的内容。   
  

### ops.yaml  
该文件保存着管理员ID信息（指游戏角色ID）。  
该管理员是指可以通过微信公众号直接发送指令到游戏内执行。  
>请勿将WeAuth管理员与游戏内op混淆，但是在未来，WeAuth将支持从游戏服务器拉取op玩家ID信息。    

**只有`ops.yaml`文件支持热重载**  
## WeAuth启动参数(近期正在快速更新)
```command
weauth
-v  # 查看版本信息
-h  # 查看启动参数帮助信息
-p [port]  # 启动后在port端口监听。默认为80端口。
#-r [route]  # web服务路由。默认为“/wx”。待开发。
-w  # 微信服务器验证模式，需配合 -t指令使用
-t [token]  # 微信服务器验证用的token，也就是您在微信公众号后台输入的token内容
-op [ID]  # 将ID加入ops.yaml中
-test  # 以测试模式启动，仅用于开发测试
```   
在绝大多数情况下，您无需输入任何参数，直接使用`weauth`启动即可。  
程序将在`http://127.0.0.1/wx`监听来自微信的请求。  
## 微信公众号后台配置
待更新  
## MCSManager后台配置
待更新  
  
# 版本更新日志  
### 2025-01-05 v1.3.6-release
- WeAuth现在可作为微信公众号验证开发者服务器工具使用  










 


