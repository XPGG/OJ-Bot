#! /bin/python3
class Dice:
	def set_dice(self, dice_text):
		# フラグ・statusを初期化
		self.lt_flag = False
		self.gt_flag = False
		self.status = None

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
			# dice_text[1]のステータス値(1d100>=[50]の部分)を取得し、statusに保存
			self.status = int(dice_text[1].split('<=')[1])
			# dice_text[1]のステータス値を保存したので、ステータス値を除外(1d100>=50→1d100)して再保存
			dice_text[1] = dice_text[1].split('<=')[0]

		# diceを振る回数をdice_countに保存
		self.dice_count = int(dice_text[1].split('d')[0])
		# diceの面数をnum_surfaceに保存
		self.num_surface = int(dice_text[1].split('d')[1])

	def throw_dice(self):
		import random
		dice_number = []

		if self.status is not None:
			dice_number.append(random.randint(1, int(self.num_surface)))
			if self.lt_flag and dice_number[0] <= self.status or self.gt_flag and dice_number[0] >= self.status:
				return str(dice_number) + ' 成功ですわよ！!'

			else:
				return str(dice_number) + ' 失敗ですわよ...。'

			elif self.lt_flag and dice_number[0] <= self.status and self.num_surface is 100 and dice_number[0] <= 5:
				dice_number = str(dice_number) + ' 成功しましたわよ！　なんとクリティカルですわ！'

			elif self.lt_flag and dice_number[0] <= self.status and self.num_surface is 100 and dice_number[0] >= 95:
				dice_number = str(dice_number) + ' 失敗しましたわよ...　しかもファンブルですわ...!'

			return str(dice_number)
		#else:
			#for i in range(self.dice_count):
				#dice_number.append(random.randint(1, self.num_surface))

			#if self.num_surface is 100 and dice_number[0] <= 5:
				# dice_number = str(dice_number) + ' Critical!'

			#elif self.num_surface is 100 and dice_number[0] >= 95:
				# dice_number = str(dice_number) + ' Fumble!'

			#return str(dice_number)
