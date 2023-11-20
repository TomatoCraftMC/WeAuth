# Rcon设置指南  

### Minecraft服务器后台中的server.properties文件
```yaml
enable-rcon=true  # 必须设置为true
rcon.password=password   # 自行输入密码
rcon.port=9876    # 不建议使用默认的端口号
```

### WeAuth的config.yaml文件
```yaml
server_connect: 1  # 1 代表使用rcon连接Minecraft服务器  0 代表使用MCSManager连接
rcon_host_adr: 127.0.0.1  # 连接rcon所用IP地址或者域名，详细见下方介绍
rcon_port: 9876  # 端口号
rcon_password: password # 密码
```
## rcon连接的几种形式
由于rcon协议的特殊性，将其直接暴露在公网会对您的MC服务器造成潜在的风险。  
根据是否暴露公网与WeAuth位置的不同，有以下三种rcon连接方式供参考。  
### WeAuth与Minecraft Server在同一个服务器上运行  
由于是在同一个主机，防火墙无需开放rcon端口到公网，WeAuth便能连接。  
具体操作：`server.properties`设置好rcon端口后，`config.yaml`的`rcon_host_adr`使用`127.0.0.1`即可  
>注：如果您是在Docker内运行，请设置好端口转发规则。如果您的MC服务器和WeAuth服务器是同一个云服务提供商的不同服务器实例，可以通过云服务商后台搭建内网实现类似功能。  
  
### WeAuth与Minecraft Server通过[frp工具](https://github.com/fatedier/frp)连接
这种情况适用于WeAuth与MC不在同一个服务器的情况。如果直接通过MC服务器暴露rcon端口来连接，会增加被攻击的风险。    
操作方法为：在WeAuth服务器安装frp服务端，在MC服务器安装frp客户端。  
WeAuth服务器只需要开放一个供frp连接的端口，MC服务器不需要开放任何端口。    
在MC服务器中设置frp配置文件，将rcon的端口设置为localPort，再设置一个remotePort。   
WeAuth只需要连接`127.0.0.1`的remotePort便可以连接到MC服务器rcon服务。  
具体请自行查阅frp相关文档。  

### WeAuth服务器与Minecraft服务器直接连接
不推荐这种方法，会增加服务器的风险。  
>注：当前无法连接IPv6的rcon地址，但仍可通过frp工具解决。
