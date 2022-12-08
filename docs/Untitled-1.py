

def sub_lists(num):
    if num == []:
        return[[]]
    n = sub_lists(num[1:])
    return n + [[num[0]] + new_num for new_num in n]

def sub_list_new_size(num,num_of_set):
    return [n for n in sub_lists(num) if len(n) == num_of_set]


if __name__ == '__main__':

    num = [1,3,5,7,9,11]
    num_of_set = 2

    print(sub_list_new_size(num,num_of_set))
