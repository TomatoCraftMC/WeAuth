# 更新日志

### 2025-01-12 v1.5.3

- WeAuth现在已只支持通过微信公众号发送WeAuth指令

### 2025-01-11 v1.5.1-rc1
- WeAuth现在对管理员ID大小写不敏感
- gift的valid参数现在有效了
### 2025-01-11 v1.5.0-release

* WeAuth现在支持CDKey生成与兑换功能
* 使用`weauth -g`便可进入CDKey生成程序
* CDKey的兑换在微信公众号发送`$[CDKey]`即可
* 只有注册了白名单的玩家才可以使用CDKey兑换功能
* Rcon模式下，可以检测是否兑换成功。若玩家ID不在线等情况，CDKey不会被核销
* MCSM模式下，若游戏服务器连接正常则默认核销CDKey。玩家不在线则会损失CDKey。

### 2025-01-09 v1.4.1-release

* 修复了微信公众号回复文字不换行的问题

### 2025-01-09 v1.4.1-rc1
* 修复了微信公众号回复文字不换行的问题

### 2025-01-08 v1.4.0-release
* WeAuth现在支持使用[rcon](https://github.com/conqp/rcon)协议连接Minecraft服务器
* `config.yaml`文件现在支持设置rcon相关信息
* `config.yaml`文件现在会随版本自动更新
* 使用rcon情况下，在微信公众号发送消息可以收到来自游戏服务器的回复信息
* 修复了取消订阅事件的报错
* WeAuth管理员的ID不再区分大小写


### 2025-01-07 v1.3.9-release
* 新增对[rcon](https://github.com/conqp/rcon)模块的依赖,Python<3.10版本最高支持rcon v2.1.1  
> rcon项目使用GPLv3协议开源  

### 2025-01-07 v1.3.8-release
* 现在可以通过`weauth -r [/route] `来自定义程序监听路由地址  
* 现在可以在`config.yaml`中自定义程序监听路由地址  
* `weauth -r [/route]`优先级高于`config.yaml`中的路由地址  
* bug fix: 修复了游戏服务器中断情况下程序崩溃的问题  
### 2025-01-07 v1.3.7-release
- WeAuth现已支持使用`weauth -op [ID]`来实时添加管理员  
### 2025-01-06 v1.3.6-release
- WeAuth现已支持单独作为微信验证开发者服务器地址使用  
