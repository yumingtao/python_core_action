def pre_process(arr):
    return arr


def sort(arr):
    return arr


def post_process(arr):
    return arr


def work_process(arr):
    arr_after_pre = pre_process(arr)
    arr_after_sort = sort(arr_after_pre)
    arr_return = post_process(arr_after_sort)

    return arr_return

