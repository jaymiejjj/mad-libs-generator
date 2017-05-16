# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def generate_quiz():
    tips0 = u"这个八岁的男孩酷爱弹钢琴，以致于他坚持练琴三年了。"
    sample0 = "The eight-year-old girl likes playing the piano __1__ much __2__ he has kept __3__ for three years."
    answer0 = ['so', 'that', 'practicing']

    tips1 = u"由于天气不好，校运会不得不推迟。"
    sample1 = "__1__ __2__ the bad weather, the school sports meet had to __3__ __4__ __5__."
    answer1 = ['Because', 'of', 'be', 'put', 'off']

    tips2 = u"刘老师是位非常亲切的老师，以致于我们把她当做自己的母亲。"
    sample2 = "Mrs. Liu is __1__ __2__ kind teacher__3__ we __4__ her __5__ our mother."
    answer2 = ['such', 'a', 'that', 'regard', 'as']

    tips3 = u"下定决心努力学习吧,你迟早会成功的。"
    sample3 = "Make __1__ __2__ __3__to work hard, __4__ you‘ll succeed __5__ __6__ __7__."
    answer3 = ['up', 'your', 'mind', 'and', 'soon', 'or', 'later']

    tips = [tips0, tips1, tips2, tips3]
    samples = [sample0, sample1, sample2, sample3]
    answers = [answer0, answer1, answer2, answer3]

    quiz_zip = {}
    index = 0
    for tip, sample, answer in zip(tips, samples, answers):
        quiz_zip[index] = [tip, sample, answer]
        index += 1

    return quiz_zip


def get_level(quiz_num):
    print u'''###################################
欢迎来到单词填空挑战,如果中途您想退出游戏，请输入end
0 - 简单
1 - 中等
2 - 苦难
3 - 专家级'''
    level = raw_input(u"请选择您要挑战的难度（请输入数字0-{quiz_num}）： ".format(quiz_num=quiz_num - 1))

    while True:
        if not level.isdigit():
            level = raw_input(u"您的输入格式不正确,应该输入整数，请输入重新： ")

        elif not int(level) in range(0, quiz_num):
            level = raw_input(u"请输入数字0-{quiz_num}，请输入重新： ".format(quiz_num=quiz_num-1))

        else:
            break

    return int(level)


def get_quiz(level, quiz_zip):
    return quiz_zip[level]


def get_alllow_wrong_time():

    wrong_times = raw_input(u"请输入您可以允许自己回答错误的次数（1-10）")

    while True:
        if not wrong_times.isdigit():
            wrong_times = raw_input(u"您的输入格式不正确,应该输入整数，请输入重新： ")

        elif not int(wrong_times) in range(1, 11):
            wrong_times = raw_input(u"请输入数字1-10，请输入重新： ")

        else:
            break

    return int(wrong_times)


def get_blank_num(sample):
    sample_lst = sample.split()
    return len([i for i in sample_lst if "__" in i])


def fill_blank(tip, sample, answer, wrong_times):
    print "###################################"
    print u"{tip}".format(tip=tip)
    print "{sample}".format(sample=sample)

    count = 0
    while True:
        blank_num = get_blank_num(sample)
        for n in range(0, blank_num):
            input_answer = raw_input(u"请输入第{n}个空的单词: ".format(n=n+1))
            while not input_answer == answer[n]:
                count += 1
                if count == wrong_times:
                    break
                input_answer = raw_input(u"您的回答错误，您还有{times}次机会，"
                                         u"请重新输入第{n}个空的单词: ".format(times=wrong_times-count,n=n + 1))

            if count == wrong_times:
                break
            print(u"恭喜您第{n}个单词填写正确,您还有{times}次机会".format(times=wrong_times-count, n=n+1))
            sample = sample.replace("__{n}__".format(n=n+1), input_answer)
            print sample
        if count == wrong_times:
            break
        print u"恭喜您完成测试"

    print u"很遗憾，挑战失败，您已经没有机会再挑战了！"


def main():
    quiz_zip = generate_quiz()
    quiz_num = len(quiz_zip)
    level = get_level(quiz_num)
    tip, sample, answer = get_quiz(level, quiz_zip)
    wrong_times = get_alllow_wrong_time()
    fill_blank(tip, sample, answer, wrong_times)


if __name__ == '__main__':
    main()





