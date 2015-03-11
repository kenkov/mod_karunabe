#! /usr/bin/env python
# coding:utf-8

from mod import Mod
from datetime import datetime
import random


class ModKarunabe(Mod):
    def __init__(
        self,
        logger=None,
    ):
        Mod.__init__(self, logger)

        self.basetime = datetime.now()
        self.time_flag = True

    def is_fire(self, message, master) -> bool:
        """
        3600秒以上ツイートしていなかったら発動する
        """
        screen_name = message["user"]["screen_name"]
        # flags
        name_flag = screen_name == "karubabu"

        if not self.time_flag:
            time_diff = (datetime.now() - self.basetime).seconds
            if time_diff > 3600:
                self.time_flag = True

        if self.time_flag and name_flag:
            # basetime の更新
            self.basetime = datetime.now()
            self.time_flag = False
            self.logger.debug("time passed")

            return True
        else:
            return False

    def reses(self, message, master):
        base = (
            "うおおおおおおおおおおおおあああああああああ"
            "あああああああああああああああああああああ！！！"
            "！！！！！！！！！(ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！"
            "！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁ"
        )

        texts = [base + "ｯ"*i for i in range(3)] + \
            ["".join(random.choice(["ﾌﾞ"] + list("ﾁﾐﾘ")) for _ in range(100))]

        random.shuffle(texts)
        formated_texts = ["@{} {}".format("karubabu", text) for text in texts]

        return [
            (1.0, text.format("karubabu"), "karunabe",
             {"in_reply_to_status_id": message["id"]}
             )
            for text in formated_texts
        ]
