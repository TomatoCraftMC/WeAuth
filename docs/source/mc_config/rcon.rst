使用rcon连接游戏服务器
===================

`rcon <https://developer.valvesoftware.com/wiki/Source_RCON_Protocol>`__ 是一种允许服务器管理员远程执行游戏命令的协议。

配置rcon
-------

Minecraft Server自1.9版本起已原生支持rcon协议，您可以在 ``server.properties`` 文件中配置开启rcon。

.. code-block:: toml

    # 必须设置为true
    enable-rcon=true

    # 自行输入密码
    rcon.password=password

    # 不建议使用默认的端口号
    rcon.port=9876

然后再设置WeAuth的 ``config,yaml`` 文件。

.. code-block:: yaml

    # 1 代表使用rcon连接Minecraft服务器  0 代表使用MCSManager连接
    server_connect: 1

    # 连接rcon所用IP地址或者域名，详细见下方介绍
    rcon_host_adr: 127.0.0.1

    # 端口号
    rcon_port: 9876

    # 密码
    rcon_password: password

连接rcon的几种情况
----------------

.. warning::
    将rcon端口直接开放至公网会给您的MC server带来不可控的风险。因此，我们提供了几种更加安全的连接方式供您参考。



1. WeAuth与MC Sever在同一个服务器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

如果WeAuth与Minecraft Server在同一个服务器，您无需将rcon端口开放至公网。

.. code-block:: yaml

    # 固定使用127.0.0.1
    rcon_host_adr: 127.0.0.1

.. note::
    如果您的MC服务器和WeAuth服务器是同一个云服务提供商的不同服务器实例，可以通过云服务商后台搭建内网实现类似功能。

2. WeAuth与MC Sever不在同一个服务器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

我们推荐使用 `frp工具 <https://baike.baidu.com/item/RCON/23218655>`__ 搭建隧道，WeAuth通过隧道连接MC Server rcon。

这样既避免了rcon端口直接暴露至公网的风险，也可用于无固定公网IP情况下的连接。

下载frp
^^^^^^^

https://github.com/fatedier/frp/releases/

解压后会需要四个文件。

.. list-table::
    :header-rows: 1

    * - 文件名
      - 用途
    * - frps
      - frp的服务端程序
    * - frpc
      - frp的客户端程序
    * - frps.toml
      - frp服务端配置文件
    * - frpc.toml
      - frp客户端配置文件

请将服务端及配置文件上传到运行WeAuth的服务器，客户端及配置文件上传到运行MC Server的服务器。

配置frp服务端
^^^^^^^^^^^^

打开并编辑 ``frps.toml``

.. code-block:: toml

    bindPort = 1234
    token = "token123321"

``bindPort`` 是frp服务端与客户端进行联系的端口，请在防火墙设置放行。

``token`` 请自行设置并与客户端配置文件保持一致。

运行frp服务端
^^^^^^^^^^^^

.. code-block:: bash

    ./frps -c ./frps.toml

配置frp客户端
^^^^^^^^^^^^

打开并编辑 ``frpc.toml``

.. code-block:: toml

    serverAddr = "8.8.8.8"
    serverPort = 1234
    token = "token123321"


    [[proxies]]

    name = "rcon"
    type = "tcp"
    localIP = "127.0.0.1"
    localPort = 9876
    remotePort = 5432

其中 ``serverAddr`` 是frp服务端，即WeAuth运行服务器的公网地址。

``serverPort`` 与 ``bindPort`` 一致。

``token`` 与服务端一致。

``localIP`` 使用 ``127.0.0.1``。

``localPort`` 与 ``server.properties`` 中的 ``rcon.port`` 保持一致。

``remotePort`` 即在WeAuth服务器上访问rcon服务的端口，不冲突即可，且请勿设置防火墙放行（因为我们的目的就是不让rcon端口暴露到公网）。

配置config.yaml
^^^^^^^^^^^^^^^

.. code-block:: yaml

    # 固定使用127.0.0.1，会自动通过frp连接到MC Server
    rcon_host_adr: 127.0.0.1

    # 端口号，使用前文提到的remotePort
    rcon_port: 5432

测试连接
~~~~~~~

您可以运行WeAuth的游戏端测试模式。（1.6.1起支持）

在测试之前，请开启MC Server。

.. code-block:: bash

    weauth -gtest

如果配置正确，则会提示连接成功。MC Server的控制台也会提示有rcon连接。
