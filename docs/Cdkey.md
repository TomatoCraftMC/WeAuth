# CDKey系统使用指南

> CDKey仅支持WeAuth v1.5.0及以上版本

## 一、生成CDKey

```shell
weauth -g

-请输入礼物注释,并按回车确认。例如: 火把/钻石/给小张的礼物
>新年礼物
-请输入单次兑换所给予的数量,并按回车确认。例如: 6
>16
-请输入礼物,可以带有NBT标签。
>minecraft:cooked_beef
-请输入生成CDKey数量
>20
```

### 名词解释

- 礼物注释，即礼物说明，用来记录礼物的用途。在`gift_list.yaml`中记录为`gift_comment`。
- 礼物，即礼物名称，指Minecraft的物品代码（物品ID），可以带有NBT标签。在`gift_list.yaml`中记录为`gift_arg`。
- 单次兑换所给予的数量，在`gift_list.yaml`中记录为`gift_num`。即Minecraft指令中的`give @p minecraft:torch [num]`。
- 生成CDKey数量,在`gift_list.yaml`中记录为`gift_total`。也是对应在`cdkey.yaml`中生成的兑换码数量。玩家兑换成功时会自动减少。

### 生成机制

每个礼物会根据`gift_arg`、`gift_num`和`gift_total`生成唯一的哈希值`gift_hash`。  
`gift_hash`会成为`cdkey.yaml`文件中，连接兑换码和对应礼物的唯一索引。

## 二、兑换CDKey

> 在任何情况下，兑换CDKey都必须要求玩家在游戏内在线。

在微信公众号输入(没有任何空格)

```C
#[CDKey]
```

例如，输入`#tpFV-Psb5-fHPH-J10h`，即可进行兑换。

- 只有已注册白名单的玩家才能进行兑换，其他用户进行兑换会被WeAuth忽略。
- 如果使用MCSManager作为连接，WeAuth只会在核销前确认能否连接到MCSManager，不会对兑换结果进行任何验证。
- 如果使用Rcon作为连接，WeAuth会确认兑换结果，包括玩家不在线情况、物品ID不合法情况。若兑换失败，CDKey不会被消耗，且玩家在微信公众号会收到反馈。

兑换完成后，`cdkey.yaml`中的兑换码会被删除，`gift_list.yaml`中的`gift_total`会自动减1。  
若兑换时`gift_total`已小于等于0，则会提醒兑换失败。

### valid 参数（暂未上线）

你可以设置`gift_list.yaml`中的`valid`为`false`（小写，yaml文件格式要求）  
这样，该礼物对应的所有兑换码会被拒绝兑换。
