启动参数与命令
============
WeAuth可依靠启动参数，或者超级管理员在微信直接输入指令，实现丰富的游戏管理功能。

启动参数
-------

直接启动服务器
~~~~~~~~~~~~

.. code-block:: bash

    weauth

这是当您配置完成所有设置后，正式进入运行的方式。

WeAuth会开始监听来自微信服务器的消息，您可以使用screen工具将WeAuth放入后台，这样您退出终端也不会停止WeAuth运行。

.. code-block:: bash

    screen -S wa
    weauth
    # 此时，同时敲击键盘ctrl 和 A ， 然后再敲击 D ，便可将WeAuth放入后台

    screen -r wa
    # 即可回到运行WeAuth的终端

测试模式
~~~~~~~

.. code-block:: bash

    # 仅供开发使用
    weauth -test

    # 用于测试与微信服务器连接
    weauth -wtest

    # 用于测试与游戏服务器连接
    weauth -gtest

    # 查看版本
    weauth -v

    # 查看启动参数帮助信息
    weauth -h


CDKey生成
~~~~~~~~

.. code-block:: bash

    weauth -g

    -请输入礼物注释,并按回车确认。例如: 火把/钻石/给小张的礼物
    >新年礼物
    -请输入单次兑换所给予的数量,并按回车确认。例如: 6
    >16
    -请输入礼物,可以带有NBT标签。
    >minecraft:cooked_beef
    -请输入生成CDKey数量
    >20

礼物信息会保存在 ``gift_list.yaml`` ， CDKeys会保存在 ``cdkey.yaml`` 。

名词解释
^^^^^^^

- 礼物注释，即礼物说明，用来记录礼物的用途。在 ``gift_list.yaml`` 中记录为 ``gift_comment`` 。

- 礼物，即礼物名称，指Minecraft的物品代码（物品ID），可以带有NBT标签。在 ``gift_list.yaml`` 中记录为 ``gift_arg`` 。

- 单次兑换所给予的数量，在 ``gift_list.yaml`` 中记录为 ``gift_num`` 。即Minecraft指令中的 ``give @p minecraft:torch [num]`` 。

- 生成CDKey数量,在 ``gift_list.yaml`` 中记录为 ``gift_total`` 。也是对应在 ``cdkey.yaml`` 中生成的兑换码数量。玩家兑换成功时会自动减少。

生成机制
^^^^^^^

每个礼物会根据 ``gift_arg`` 、 ``gift_num`` 和 ``gift_total`` 生成唯一的哈希值 ``gift_hash`` 。

``gift_hash`` 会成为 ``cdkey.yaml`` 文件中，连接兑换码和对应礼物的唯一索引。

你可以设置 ``gift_list.yaml`` 中的 ``valid`` 为 ``false`` （小写，yaml文件格式要求）。
这样，该礼物对应的所有兑换码会被拒绝兑换。

管理员与超级管理员设置
~~~~~~~~~~~~~~~~~~

管理员与超级管理员的ID会保存在 ``ops.yaml`` 中。

管理员是指可以在微信公众号直接发送游戏指令的用户。

超级管理员是指在管理员基础上，可以在微信公众号直接发送WeAuth指令的用户。

.. code-block:: bash

    weauth -op [ID]
    # 将ID加入ops.yaml中的普通管理员(可以在公众号发出游戏内指令)


    weauth -sop [id]
    # 将ID加入ops.yaml中的超级管理员(可以在公众号中发出WeAuth指令)


数据库操作
~~~~~~~~

可以使用启动参数来对数据库 ``WeAuth.db`` 进行查、删、改。但在目前版本，不同于在微信公众号执行指令，在启动参数上进行查、删、改不会同步到游戏服务器。

.. code-block:: bash

    weauth -list
    # 显示所有用户ID

    weauth -search [play_id]
    # 显示该用户ID的封禁、订阅情况

    weauth -ban [player_id]
    # 封禁该用户(仅本地数据库)

    weauth -unban [player_id]
    # 移出封禁(仅本地数据库)

    weauth -del [player_id]
    # 在数据库中删除该玩家信息(仅本地数据库)

    weauth -update [player_id] -b -s
    # 手动更新该玩家是否封禁标志与是否订阅标志(仅本地数据库)

微信公众号指令
------------

目前可在微信公众号直接发送四类文字指令：白名单注册申请指令、游戏指令、WeAuth指令和CDKey兑换指令。

白名单注册申请指令使用 ``#``作为前缀。

游戏指令使用 ``@`` 作为前缀，仅管理员和超级管理员可以使用。

WeAuth指令使用 ``!`` 作为前缀，仅超级管理员可以使用。（英文的半角感叹号）

CDKey兑换指令使用 ``$`` 作为前缀。

白名单注册申请指令
~~~~~~~~~~~~~~~

所有用户均可使用 ``#myid`` 运行白名单注册申请指令，若该ID被封禁则会提示“被封禁”。

游戏指令
~~~~~~~

管理员和超级管理员可以使用 ``@`` 作为前缀，发送Minecraft Server的游戏指令。

例如：``@time set 1000`` , ``@kill player_id`` , ``@give @a minecraft:torch 64`` 。

.. note::
    如果您使用MCSManager作为连接服务器方式，则不会收到发送指令后的反馈。

WeAuth指令
~~~~~~~~~

超级管理员可以使用 ``!`` 作为前缀（英文的半角感叹号），发送WeAuth程序的指令。

.. code-block:: python

    !op [ID]
    # 将ID加入ops.yaml中的普通管理员(可以在公众号发出游戏内指令)

    !sop [ID]
    # 将ID加入ops.yaml中的超级管理员(可以在公众号中发出WeAuth指令)

    !v
    # 查看WeAuth版本信息

    !g [mineID] [mineNum] [cdkeyNum] [comment]
    # 生成礼物

    !l
    # 显示所有用户ID

    !s [player_id]
    # 显示该用户ID的封禁、订阅情况

    !b [player_id]
    # 封禁该用户，同时会移出白名单

    !ub [player_id]
    # 移出封禁

    !d [player_id]
    # 在数据库中删除该玩家信息，会自动移出白名单

    !u [player_id] [is_ban] [is_sub]
    # 手动更新该玩家是否封禁标志与是否订阅标志 （会自动同步到游戏服务器）

.. note::
    WeAuth指令不同于启动参数，其不仅会更改WeAuth本地数据，还会同步至MC Server。

CDKey兑换
~~~~~~~~~

CDKey兑换指令使用 ``$`` 作为前缀。例如，输入 ``#tpFV-Psb5-fHPH-J10h`` ，即可进行兑换。

- 只有已注册白名单的玩家才能进行兑换，其他用户进行兑换会被WeAuth忽略。

- 如果使用MCSManager作为连接，WeAuth只会在核销前确认能否连接到MCSManager，不会对兑换结果进行任何验证。

- 如果使用Rcon作为连接，WeAuth会确认兑换结果，包括玩家不在线情况、物品ID不合法情况。若兑换失败，CDKey不会被消耗，且玩家在微信公众号会收到反馈。

兑换完成后， ``cdkey.yaml`` 中的兑换码会被删除， ``gift_list.yaml`` 中的 ``gift_total`` 会自动减1。

若兑换时 ``gift_total`` 已小于等于0，则会提醒兑换失败。

