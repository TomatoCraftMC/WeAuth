下载与安装
=========

WeAuth使用Python开发，并已上传至 `Pypi <https://pypi.org/project/weauth/>`__ 。您可以直接使用pip工具下载安装，
安装完成后，WeAuth便可直接使用 ``weauth`` 指令启动。

由 `Fallen_Breath <https://github.com/Fallen-Breath>`__
为 `MCDReforged <https://github.com/MCDReforged/MCDReforged>`__
编写的 `下载与安装指南 <https://docs.mcdreforged.com/zh-cn/latest/quick_start/install.html>`__ 已相当详尽，您可以进行参考。以下是WeAuth与MCDReforged安装过程中的不同之处。

系统要求
-------
WeAuth目前仅在Linux环境进行过测试，您可以将Windows环境的运行情况反馈至 `Issues <https://github.com/TomatoCraftMC/WeAuth/issues>`__ 。

Python版本
---------
WeAuth支持的最低 Python 版本为 3.8。但建议您使用 3.10 及以上版本运行WeAuth。

.. note::
    `Python基金会 <https://devguide.python.org/versions/>`__ 已于2024年10月17日结束对Python 3.8的支持，Python 3.9的支持也将于2025年10月结束。

使用pip安装
-----------

.. code-block:: bash

    pip3 install weauth

推荐使用 `清华大学镜像 <https://mirrors.tuna.tsinghua.edu.cn/help/pypi/>`__ 加速

.. code-block:: bash

    pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple weauth

使用Docker
~~~~~~~~~~

WeAuth暂未制作与发布Docker镜像。

检验是否安装成功
--------------

当您使用pip下载安装WeAuth后，程序入口已添加至您的环境变量。您可以运行以下指令

.. code-block:: bash

    weauth -v

如果安装成功，则会显示WeAuth版本信息。

.. code-block:: bash

    WeAuth version 1.5.6
    Build time: 2025-01-15 07:44:36z
    LICENSE: GPLv3
    Project Homepage: https://github.com/TomatoCraftMC/WeAuth

首次运行
-------

WeAuth在运行中会生成和读取众多文件，您需要新建一个专供WeAuth运行的文件夹，然后再初始化WeAuth

.. code-block:: bash

    mkdir ~/WeAuth
    cd ~/WeAuth

初始化WeAuth，会自动生成配置文件。

.. code-block:: bash

    weauth

然后您会在文件夹中看见配置文件 ``config.yaml`` 与数据库文件 ``WeAuth.db`` 。

``config.yaml`` 保存着您连接微信服务器与MC服务器的各种配置。

``WeAuth.db``  保存着玩家信息，包括玩家ID、微信OpenID、是否封禁与是否注册。

第二章与第三章教程会继续介绍如何填写 ``config.yaml`` 中的内容。
