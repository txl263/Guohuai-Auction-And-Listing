# coding: utf-8
from __future__ import unicode_literals
# author: haofly
#
# fun: 生成随机姓名、随机电话号码、随机字符串，目前仅支持Python2

import random


def generateName(first_len=0, last_len=0):
    surnames = [
        u'赵', u'钱', u'孙', u'李', u'周', u'吴', u'郑', u'王', u'冯', u'陈',
        u'褚', u'卫', u'蒋', u'沈', u'韩', u'杨', u'朱', u'秦', u'尤', u'许',
        u'何', u'吕', u'施', u'张', u'孔', u'曹', u'严', u'华', u'金', u'魏',
        u'陶', u'姜', u'戚', u'谢', u'邹', u'喻', u'柏', u'窦', u'章',
        u'云', u'苏', u'潘', u'葛', u'奚', u'范', u'彭', u'郎', u'鲁', u'韦',
        u'昌', u'马', u'苗', u'凤', u'花', u'方', u'俞', u'任', u'袁', u'柳',
        u'鲍', u'史', u'唐', u'费', u'廉', u'薛', u'雷', u'贺',
        u'倪', u'汤', u'滕', u'殷', u'罗', u'毕', u'郝', u'邬', u'安', u'常',
        u'乐', u'于', u'时', u'傅', u'皮', u'齐', u'康', u'伍', u'余',
        u'元', u'卜', u'顾', u'孟', u'平', u'黄', u'和', u'穆', u'萧', u'尹',
        u'姚', u'邵', u'湛', u'汪', u'祁', u'毛', u'禹', u'狄', u'米', u'贝',
        u'明', u'臧', u'计', u'伏', u'成', u'戴', u'谈', u'宋', u'茅', u'庞',
        u'熊', u'纪', u'舒', u'屈', u'项', u'祝', u'董', u'粱', u'杜', u'阮',
        u'蓝', u'闵', u'席', u'季', u'麻', u'强', u'贾', u'路', u'娄', u'危',
        u'江', u'童', u'颜', u'郭', u'梅', u'盛', u'林', u'刁', u'钟', u'徐',
        u'邱', u'骆', u'高', u'夏', u'蔡', u'田', u'樊', u'胡', u'凌', u'霍',
        u'虞', u'万', u'支', u'柯', u'咎', u'管', u'卢', u'莫', u'经', u'房',
        u'缪', u'干', u'解', u'应', u'宗', u'宣', u'丁', u'贲', u'邓',
        u'郁', u'单', u'杭', u'洪', u'包', u'诸', u'左', u'石', u'崔', u'吉',
        u'龚', u'程', u'嵇', u'邢', u'裴', u'陆', u'荣', u'翁',
        u'荀', u'羊', u'於', u'惠', u'加', u'封', u'芮', u'羿',
        u'松', u'井', u'段', u'富', u'巫', u'乌',
        u'焦', u'巴', u'牧', u'山', u'谷',  u'车', u'侯',
        u'全', u'秋', u'仲', u'伊', u'宫', u'宁',
        u'甘', u'钭', u'厉', u'戎', u'祖', u'武', u'符',
        u'刘', u'景', u'詹', u'束', u'龙', u'叶', u'幸', u'司',
        u'黎', u'蓟', u'薄', u'宿', u'白', u'怀', u'蒲', u'台', u'从',
        u'鄂', u'索', u'咸', u'赖', u'卓', u'蔺', u'屠', u'胥', u'能',
        u'苍', u'闻', u'莘', u'翟', u'谭', u'贡', u'劳', u'逄',
        u'姬', u'申', u'冉', u'宰', u'郦', u'雍',
        u'桑', u'桂', u'牛', u'寿', u'通', u'边', u'燕', u'冀',
        u'浦', u'尚', u'农', u'温', u'别', u'庄', u'晏', u'柴',
        u'阎', u'充', u'慕', u'连', u'茹', u'习', u'宦', u'艾', u'鱼', u'容',
        u'向', u'古', u'易', u'慎', u'戈', u'廖', u'庚', u'终', u'暨', u'居',
        u'衡', u'步', u'都', u'耿', u'满', u'弘', u'匡', u'国', u'文', u'寇',
        u'广', u'禄', u'阙', u'东', u'殴', u'沃', u'利', u'蔚', u'越',
        u'隆', u'师', u'巩', u'厍', u'聂', u'晁', u'勾', u'敖', u'融',
        u'冷', u'辛', u'那', u'简', u'饶', u'空', u'曾', u'毋',
        u'沙', u'养', u'鞠', u'须', u'丰', u'关', u'蒯', u'相',
        u'查', u'后', u'荆', u'红', u'游',
        u'桓', u'公', u'万', u'俟', u'司', u'马', u'上官', u'欧阳',u'东方',u'西门',
    ]
    first_name = ''
    last_name = ''
    if first_len == 0:
        first_name = random.choice(surnames)
    else:
        while len(first_name) != first_len:
            first_name = random.choice(surnames)

    length = random.randint(1, 2) if last_len == 0 else last_len

    while len(last_name) != length:
        try:
            head = random.randint(0xB0, 0xDF)
            body = random.randint(0xA, 0xF)
            tail = random.randint(0, 0xF)
            val = (head << 0x8) | (body << 0x4) | tail
            string = '%x' % val
            last_name += string.decode('hex').decode('gb2312')
        except:
            pass

    return first_name + unicode(last_name)

def generateString(min_length=0, max_length=0, digital=True, characters=True, uppercase=True, lowercase=True, repeat=True):
    digital_char = '0123456789'
    characters_char = 'abcdefghijklmnopqrstuvwxyz'
    characters_CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    char_set = ''
    result = ''
    if digital:
        char_set += digital_char

    if characters:
        if uppercase:
            char_set += characters_CHAR
        elif lowercase:
            char_set = characters_char
        else:
            char_set += characters_char + characters_CHAR

    length = random.randint(min_length, max_length)
    if repeat:
        while len(result) < length:
            result += random.choice(char_set)
    else:
        result = random.sample(char_set, length)
    return result


def generatePhone():
    begin = random.choice(['13', '15', '18'])
    return begin + generateString(9, 9, True, False, False, False, True)

if __name__ == "__main__":
    name = generateName(0, 0)
    print(name)
    car_num = generateString(3, 3, True, True, True, False, True) + generateString(2, 2, True, False, True, False, True)
    print(car_num)
    phone = generatePhone()
    print(phone)