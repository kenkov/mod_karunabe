#! /usr/bin/env python
# coding:utf-8

from mod import Mod
from datetime import datetime
import random


class ModKarunabe(Mod):
    def __init__(
        self,
        screen_name="karubabu",
        logger=None,
    ):
        Mod.__init__(self, logger)

        self.screen_name = screen_name
        self.basetime = datetime.now()
        self.time_flag = False

    def can_utter(self, message, master) -> bool:
        """
        3600 秒後のツイートでﾌﾞﾁﾐﾘする。
        """
        screen_name = message["user"]["screen_name"]
        # flags
        name_flag = screen_name == self.screen_name

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

    def utter(self, message, master):
        base = (
            "うおおおおおおおおおおおおあああああああああ"
            "あああああああああああああああああああああ！！！"
            "！！！！！！！！！(ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！"
            "！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁ"
        )

        texts = [base + "ｯ"*i for i in range(3)] + \
            ["".join(random.choice(["ﾌﾞ"] + list("ﾁﾐﾘ")) for _ in range(100))]
        texts += [
            "青菜に塩なう😔（悪い印象を与えた）",
            "早く3月にならないかな（´-`）.｡oO",
        ]

        random.shuffle(texts)
        formated_texts = [
            "@{} {}".format(self.screen_name, text) for text in texts
        ]

        return [
            (1.0, text, "karunabe",
             {"in_reply_to_status_id": message["id"]}
             )
            for text in formated_texts
        ]
