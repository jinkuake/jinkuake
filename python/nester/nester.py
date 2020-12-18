"# Author:guangqing"
''' 这是 "nester" 模块，提供了一个名为print_lol()的函数，这个函数的作用是打印列表，其中有可能包含（也有可能不包含嵌套列表的类别）嵌套列表 '''
def print_lol(the_list):
    '''这个函数取一个位置参数，名为 'the_list'这可以是任何python列表（也可以是包含嵌套列表的列表）。所指定的列表中的每个数据项会（递归的）输出到屏幕上，各个数据各占一行 '''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)