使用rcon连接游戏服务器
===================

`rcon <https://developer.valvesoftware.com/wiki/Source_RCON_Protocol>`__ 是一种允许服务器管理员远程执行游戏命令的协议。

配置rcon
-------

Minecraft Server自1.9版本起已原生支持rcon协议，您可以在 ``server.properties`` 文件中配置开启rcon。

.. code-block:: toml

    enable-rcon=true  # 必须设置为true
    rcon.password=password   # 自行输入密码
    rcon.port=9876    # 不建议使用默认的端口号

然后再设置WeAuth的 ``config,yaml`` 文件。

.. code-block:: yaml

    server_connect: 1  # 1 代表使用rcon连接Minecraft服务器  0 代表使用MCSManager连接
    rcon_host_adr: 127.0.0.1  # 连接rcon所用IP地址或者域名，详细见下方介绍
    rcon_port: 9876  # 端口号
    rcon_password: password # 密码


