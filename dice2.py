#! /bin/python3
import random


class Dice:
    def set_dice(self, dice_text):
        # フラグ・statusを初期化
        self.lt_flag = False
        self.gt_flag = False
        self.status = None
        self.critical = 5
        self.funble = 96
        self.arotd = dice_text[1]
        self.skill = "なし"
        if len(dice_text) > 2:
            self.skill = dice_text[2]
        # dice_text[1](1d100>=50とかの部分)を>=で分割してみて、分割できるようであればif内を処理
        if len(dice_text[1].split('>=')) > 1:
            # throw_dice内の判定で使う greater than フラグをTrueにしておく
            self.gt_flag = True
            # dice_text[1]のステータス値(1d100>=[50]の部分)を取得し、statusに保存
            self.status = int(dice_text[1].split('>=')[1])
            # dice_text[1]のステータス値を保存したので、ステータス値を除外(1d100>=50→1d100)して再保存
            dice_text[1] = dice_text[1].split('>=')[0]

        elif len(dice_text[1].split('<=')) > 1:
            # throw_dice内の判定で使う less than フラグをTrueにしておく
            self.lt_flag = True
            # dice_text[1]のステータス値(1d100<=[50]の部分)を取得し、statusに保存
            self.status = int(dice_text[1].split('<=')[1])
            # dice_text[1]のステータス値を保存したので、ステータス値を除外(1d100>=50→1d100)して再保存
            dice_text[1] = dice_text[1].split('<=')[0]

        # diceを振る回数をdice_countに保存
        self.dice_count = int(dice_text[1].split('d')[0])
        # diceの面数をnum_surfaceに保存
        self.num_surface = int(dice_text[1].split('d')[1])

    def throw_dice(self):
        dice_number = []

        if self.status is not None:
            dice_number.append(random.randint(1, int(self.num_surface)))
            if self.num_surface is 100:
                if self.lt_flag:
                    if dice_number[0] <= self.status:
                        if dice_number[0] <= self.critical:
                            return str(dice_number) + ' 成功しましたわよ！ なんとクリティカルですわ！' + '\n振ったダイス：' + str(self.arotd) + ' ' + 'スキル：' + str(self.skill)
                        else:
                            return str(dice_number) + ' 成功ですわよ！!' + '\n振ったダイス：' + str(self.arotd) + ' ' + 'スキル：' + str(self.skill)
                    else:
                        if dice_number[0] >= self.funble:
                            return str(dice_number) + ' 失敗ですわよ...。 更にファンブルですわ...。' + '\n振ったダイス：' + str(self.arotd) + ' ' + 'スキル：' + str(self.skill)
                        else:
                            return str(dice_number) + '失敗ですわよ...。' + '\n振ったダイス：' + str(self.arotd) + ' ' + 'スキル：' + str(self.skill)
                else:
                    return ">=はだめですわよ～"
            else:
                return "100面ダイスを使ってくださいまし！"
        else:
            for i in range(self.dice_count):
                dice_number.append(random.randint(1, self.num_surface))
            return str(dice_number)
