# WeAuth
WeAuth is a bridge between WeChat Official Accounts and your Minecraft server.

## Requirement

Requires python >= 3.8

```
pip3 install -r requirements.txt
```
Your Minecraft server should've been installed with [MCManager](https://github.com/MCSManager/MCSManager).
WeAuth uses the api of MCManager to connect with game server.

Later on, WeAuth will support Rcon to connect Minecraft server.
## Installation
```
pip3 install weauth
```
## Quick start
```
mkdir WeAuth
cd WeAuth
weauth
```
`config.yaml` and `ops.yaml` will be generated after first-time running.

```commandline
vi config.yaml
```
You can configure your WeChatDeveloper information and game server in `config.yaml`.
```commandline
vi ops.yaml
```
You should also fill in the IDs of In-Game admins in `ops.yaml`.
For example:
```commandline
ops: [Zi_min, Pink_fish, jsdkj2m999]
```
After configuration, run WeAuth again.



## WeChat Command
### Add an ID into Whitelist
```commandline
#ID
#Zi_min
#bjwefbjw
```
### Send a Command
```commandline
@command
@tell @a hello,world
@give @a minecraft:torch 1
```
Only those whose ID in `ops.yaml` can use this function.

## [Homepage](https://github.com/TomatoCraftMC/WeAuth)
For more guide and 中文介绍.