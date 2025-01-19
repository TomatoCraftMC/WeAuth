配置连接游戏服务器
===============
WeAuth提供两种连接Minecraft Server的方式。即使您的MC Server没有固定公网IP，也可以借助frp工具搭建隧道实现与WeAuth服务器的连接。

.. list-table::
    :header-rows: 1

    * - 项目
      - `rcon <https://baike.baidu.com/item/RCON/23218655>`__
      - `MCSManager <https://mcsmanager.com>`__
    * - 使用条件
      - MC服务端 ``server.properties`` 中开启rcon相关配置
      - MC服务端运行在MCSManager框架内
    * - 连接方式
      - 直接向MC服务器发送指令
      - 通过MCSM向MC服务器控制台发送指令
    * - 缺点
      - 需要其他工具来保护rcon端口暴露（若WeAuth安装在另一台服务器）
      - 无法收到来自MC控制台的反馈消息
    * - 优点
      - 无需安装MCSM
      - 无需开启rcon端口（若WeAuth安装在另一台服务器）

以下是WeAuth团队给出的建议

.. list-table::
    :header-rows: 1

    * - 情况
      - 推荐模式
      - 说明
    * - WeAuth与MC服务端同在一个服务器
      - rcon
      - rcon端口无需向外界暴露
    * - WeAuth与MC服务端不在同一个服务器
      - rcon + frp
      - 使用 `frp <https://github.com/fatedier/frp>`__ 将rcon端口隐藏，提高了安全性


.. toctree::
   :maxdepth: 2

    使用MCSM连接游戏服务器<MCSManager.rst>
    使用rcon连接游戏服务器<rcon.rst>
