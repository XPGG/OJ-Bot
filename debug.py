#! /bin/python
import dice2
dice = dice2.Dice()
dice.set_dice('!dice 1d100<=50'.split(' '))
print dice.throw_dice()
