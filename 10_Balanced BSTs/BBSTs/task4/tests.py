from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from random import shuffle
from random import randint
from task import func as func
from task_copy import func as func_judge

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()

def test_generator(n):
    li = []
    a_and_b_s = set()
    h_s = set()
    for i in range(n):
        a = randint(1, 100000)
        b = randint(1, 100000)
        h = randint(1, 100000)
        if a in a_and_b_s or b in a_and_b_s or h in h_s or a == b:
            continue
        a_and_b_s.append(a)
        a_and_b_s.append(b)
        h_s.append(h)
        if a > b:
            a, b = b, a
        li.append((a, h, b))
    return li

if __name__ == '__main__':
    test_nums = [10, 10, 100, 1000]
    for test_num in test_nums:
        li = test_generator(test_num)
        assert func(li) == func_judge(li)
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call


