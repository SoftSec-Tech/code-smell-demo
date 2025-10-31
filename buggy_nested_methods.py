def method_c(index):
    my_list = [1, 2, 3, 4]
    return my_list[index] + method_b()

def method_d():
    my_dict = {"a": 1, "b": 2}
    return my_dict["c"] + method_c(2)

def method_e(value):
    number = int(value)
    return number / method_d()
def method_a():
    result = "Hello" + 1122
    return result

def method_b():
    result = method_a() + undefined_variable
    return result



except Exception as e:
    print(f"程序执行出错: {type(e).__name__} - {e}")
