# def inner():
#     if (2==2):
#         return("in end")
#
# def test():
#     print("start")
#     inner()
#     return("out end")
#
# if __name__ == "__main__":
#     answer = test()
#     print(answer)

import inspect

def permutation(list, start, end):
    print("start" + str(len(inspect.stack(0))))
    '''This prints all the permutations of a given list
       it takes the list,the starting and ending indices as input'''
    if (start == end):
        print("hm" + str(len(inspect.stack(0))))
        print(list)
    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]  # The swapping
            print("swap" + str(len(inspect.stack(0)))+ str(list))
            permutation(list, start + 1, end)
            list[start], list[i] = list[i], list[start]  # Backtracking
            print("revert" + str(len(inspect.stack(0))) + str(list))


permutation([1, 2, 3], 0, 2)  # The first index of a list is zero
