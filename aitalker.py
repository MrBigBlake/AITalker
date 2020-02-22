# AI talker
class ArtificialIdiot:
    nuclear_powered = 'sure'

    # 始
    def lets_talk(self):
        while self.nuclear_powered:
            get_str = self.listen()
            res_str = self.think(get_str)
            self.talk(res_str)

    # 听
    def listen(self):
        get_str = input('在听, 你说:').strip()
        return get_str

    # 思
    def think(self, get_str):
        if get_str.startswith('我') and (get_str.endswith(('吗', '?')) or '是' in get_str):
            res_str = '呵呵, 你只会BB而已'
        elif get_str.startswith('你') and get_str.endswith(('吗', '?')):
            res_str = '不, 我是谢广坤'
        elif get_str.startswith('我'):
            res_str = get_str.replace('我', '我也', 1)
        elif get_str.endswith(('吗', '?',)):
            res_str = get_str.replace('吗', '')
            res_str = res_str.replace('?', '!')
        else:
            res_str = '呵呵, 说人话, 我听得懂'
        return res_str

    # 说
    def talk(self, res_str):
        print(res_str)

