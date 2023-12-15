

def question1():
    # https://www.youtube.com/live/tfvm2k5c9JI?si=cmLTO9K62hNWQ63F&t=2032
    lst = [-6, -4, -3, 2, 4, 5]

    """
    O(n)
    Дан массив в порядке возрастания 
    нужно вернуть массив квадратов в порядке возрастания
    """

    """
    0 5
    0 -> 36
    1 5
    5 -> 25
    1 4
    4 -> 16
    1 3
    1 -> 16
    2 3
    2 -> 9 
    3 3
    3 -> 4
    while left <= right:
        if lst[left]**2 <= lst[right]**2:
            new_lst.append(lst[right]**2)
            right -= 1

        else:
            new_lst.append(lst[left]**2)
            left += 1
    """

    new_lst = []
    left = 0
    right = len(lst) - 1

    while left <= right:
        if lst[left]**2 <= lst[right]**2:
            new_lst.append(lst[right]**2)
            right -= 1

        else:
            new_lst.append(lst[left]**2)
            left += 1

    print(new_lst[::-1], lst)

question1()