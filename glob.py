def _init():  # 初始化
    global CORRECT_NUM  # 正确预测的个数
    global TOTAL_NUM  # 总数
    CORRECT_NUM = 0
    TOTAL_NUM = 0


def add_num():  # 为全局变量执行加法
    global CORRECT_NUM
    CORRECT_NUM += 1


def all_num(num):  # 为全局变量执行加法
    global TOTAL_NUM
    TOTAL_NUM += num


def get_all():  # 取出全局变量的值
    global CORRECT_NUM
    global TOTAL_NUM
    return CORRECT_NUM, TOTAL_NUM
