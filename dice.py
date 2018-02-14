import random
import re


def get_dice(throw):
    result = []

    if re.search(r'(.*)(?=d)', throw):
        throw_count = re.search(r'(.*)(?=d)', throw)
        throw_dice = re.search(r'(?<=d)(.*)', throw)
    elif re.search(r'(.*)(?=D)', throw):
        throw_count = re.search(r'(.*)(?=D)', throw)
        throw_dice = re.search(r'(?<=D)(.*)', throw)
    else:
        return "エラー 例`3d6` `2D10`"

    isdigit_count = throw_count.group(1).isdigit()
    isdigit_dice = throw_dice.group(1).isdigit()
    if isdigit_count is False or isdigit_dice is False:
        return "整数でよろしくね～"

    count = int(throw_count.group(1))
    dice = int(throw_dice.group(1))

    if count > 100:
        return "100d?が上限だよー"
    elif dice > 100:
        return "?d100が上限だよー"

    if count == 1 and dice == 100:
        num = random.randint(1, 100)
        if num > 95:
            return "[%d] マジですの！？　ファンブルですわよ...。" % num

        elif num <= 5:
            return "[%d] やりましたわ！　クリティカルですわよ!" % num
        else:
            return "[%d]" % num

    for i in range(count):
        result.append(random.randint(1, dice))

    return result
