# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : string_sort2.py
@Time    : 2018/11/15 18:17
'''


def two_d_list_sort2(sort_index="0,1,2"):  # 动态的根据传入的元素索引进行排序
    list = [["1", "c++", "demo"], ["1", "c", "test"], ["2", "java", ""], ["8", "golang", "google"],
            ["4", "python", "gil"], ["5", "swift", "apple"]]
    key_set = ""
    for item in sort_index.split(","):
        key_set += "ele[" + item + "]+"
    key_set = key_set.rstrip("+")
    list.sort(key=lambda ele: eval(key_set))
    print("排序索引:", sort_index, list)


if __name__ == "__main__":
    two_d_list_sort2("0")
    two_d_list_sort2("1")
    two_d_list_sort2("2")
    two_d_list_sort2("1,0")