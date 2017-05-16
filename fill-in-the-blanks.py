# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def generate_quiz():
    '''Create a quiz dict.

    Returns:
        a quiz dict,the key is index and the value is the list with tip, sample and answer
    '''

    tips = [u"这个八岁的女孩酷爱弹钢琴，以致于他坚持练琴三年了。",
            u"由于天气不好，校运会不得不推迟。",
            u"刘老师是位非常亲切的老师，以致于我们把她当做自己的母亲。",
            u"下定决心努力学习吧,你迟早会成功的。"]

    samples = ["The eight-year-old girl likes __1__ the piano __2__ much __3__ he "
               "has kept __4__ for three years.",
               "__1__ __2__ the bad weather, the school sports meet had to __3__ __4__ __5__.",
               "Mrs. Liu is __1__ __2__ kind teacher__3__ we __4__ her __5__ our mother.",
               "Make __1__ __2__ __3__to work hard, __4__ you‘ll succeed __5__ __6__ __7__."]

    answers = [['playing', 'so', 'that', 'practicing'],
               ['Because', 'of', 'be', 'put', 'off'],
               ['such', 'a', 'that', 'regard', 'as'],
               ['up', 'your', 'mind', 'and', 'soon', 'or', 'later']]

    quiz_zip = {index: [tip, sample, answer] for index, tip, sample, answer in
                zip(range(0, len(tips)), tips, samples, answers)}

    return quiz_zip


def get_level(quiz_num):
    '''
    Get user's choice
    :param quiz_num: user's input which need a integer
    :return: a level num
    '''

    print u'''###################################
欢迎来到单词填空挑战
0 - 简单
1 - 中等
2 - 苦难
3 - 专家级'''
    level = raw_input("请选择您要挑战的难度（请输入数字0-{quiz_num}）： ".
                      format(quiz_num=quiz_num - 1))

    while True:
        if not level.isdigit():
            level = raw_input(u"您的输入格式不正确,应该输入整数，请输入重新： ")

        elif not int(level) in range(0, quiz_num):
            level = raw_input(u"请输入数字0-{quiz_num}，请输入重新： ".format(quiz_num=quiz_num-1))

        else:
            break

    return int(level)


def get_quiz(level, quiz_zip):
    '''
    Get the quiz which user choose
    :param level: an integer,which user input
    :param quiz_zip: all quiz 
    :return: the quiz which usr choose including tip, sample and answer
    '''

    return quiz_zip[level]


def get_alllow_wrong_time():
    '''
    Get the the allowed wrong times 
    :return: an integer 
    '''

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
    '''
    Get the blanks number in the sample
    :param sample: a sample in a quiz
    :return: balnk number,an integer,
    '''

    sample_lst = sample.split()
    return len([i for i in sample_lst if "__" in i])


def fill_blank(tip, sample, answer, wrong_times):
    '''
    the function deal user's input 
    :param tip: the quiz tip
    :param sample: the quiz sample
    :param answer: the quiz answer
    :param wrong_times: allow max wrong times
    :return: if user answer the all blanks in allowed wrong times, return success or return failed
    '''

    print "###################################"
    print tip
    print sample

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
            print(u"恭喜您第{n}个单词填写正确,您还有{times}次机会".
                  format(times=wrong_times-count, n=n+1))
            sample = sample.replace("__{n}__".format(n=n+1), input_answer)
            print sample

        if count == wrong_times:
            break
        print u"恭喜您完成测试"
        break

    if count == wrong_times:
        print u"很遗憾，挑战失败，您已经没有机会再挑战了！"


def main():
    '''
    The main function which combined all functions logic
    '''

    quiz_zip = generate_quiz()
    quiz_num = len(quiz_zip)
    level = get_level(quiz_num)
    tip, sample, answer = get_quiz(level, quiz_zip)
    wrong_times = get_alllow_wrong_time()
    fill_blank(tip, sample, answer, wrong_times)


if __name__ == '__main__':
    main()





