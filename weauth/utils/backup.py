#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/21 15:41
# ide： PyCharm
# file: backup.py
from crontab import CronTab
from datetime import datetime
import time
import warnings
import os
import shutil


class BackUp:
    def __init__(self, cron: str):
        self.entry = CronTab(cron)
        self.__flag = False
        os.makedirs("backup", exist_ok=True)

    def next(self) -> float:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return self.entry.next()

    def run(self):
        while True:
            next = self.next()
            if next < 60.0 and not self.__flag:
                try:
                    self.backup()
                    self.__flag = True
                except FileNotFoundError:
                    print("-未找到备份文件!")
            elif next >= 60.0:
                self.__flag = False
            time.sleep(40)

    def backup(self):
        print("-准备开始备份...")
        now = datetime.now().strftime("%Y_%m_%d_%H%M")
        path = "backup/" + now
        os.makedirs(path, exist_ok=True)
        self.copy("config.yaml", path)
        self.copy("WeAuth.db", path)
        self.copy("ops.yaml", path)
        self.copy("cdkey.yaml", path)
        self.copy("gift_list.yaml", path)
        print("-备份完成，./backup/" + path)

    def copy(self, filename: str, path: str) -> None:
        try:
            shutil.copyfile(filename, path + "/" + filename)
        except FileNotFoundError:
            print(f"-未找到{filename}!")


if __name__ == "__main__":
    backup = BackUp("* * * * *")
    backup.backup()
