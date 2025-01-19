仅用于微信公众号验证服务器地址
=========================

微信公众号如果要连接第三方服务器，需要先进行验证服务器地址。WeAuth提供了单独使用的“验证模式”，即一个开启一个简单的web服务器，
以完成微信验证。

本篇教程只介绍验证模式使用方法，关于微信公众号相关设置请移步下一章。

环境要求
-------

您的服务器必须拥有可以接收来自微信请求的80/443端口。如果您使用的是中国大陆境内的云服务器，完成ICP备案即可。

.. note::
    微信只会通过http或https协议的默认端口发送请求（http使用80端口，https使用443端口）。WeAuth自1.6.0版本起支持https请求。

运行验证模式
----------

如果您使用pip工具安装WeAuth。

.. code-block:: bash

    pip3 install weauth


.. code-block:: bash

    pip3 install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple weauth

下载安装完成后，WeAuth便添加进了环境变量。

您可以添加启动参数进入验证模式

http服务
~~~~~~~~

.. code-block:: bash

    weauth -w -t token123 -r /wx

其中， ``-w`` 代表进入验证模式， ``-t token123`` 代表token为token123， ``-r /wx`` 代表使用 ``/wx`` 路由，即在 ``http://0.0.0.0/wx`` 进行监听。

在微信公众号后台填写URL地址时，请填写 ``http://公网地址/wx`` 。

.. note::
    WeAuth目前仅支持“明文模式”进行传输，将在未来支持微信的“兼容模式”与“安全模式”。

https服务
~~~~~~~~

.. warning::
    使用https服务需要您配置ssl证书。

.. code-block:: bash

    weauth -w -t token123 -r /wx -cp ssl/server.crt -kp ssl/server.key

其中， ``-cp ssl/server.crt`` 代表ssl证书文件路径为 ``ssl/server.crt`` ， ``-kp ssl/server.key`` 代表ssl密钥文件路径为 ``ssl/server.key`` 。服务器将在 ``https://0.0.0.0/wx`` 进行监听。


在微信公众号后台填写URL地址时，请填写 ``https://公网地址/wx`` 。
