def method_a():
    # 类型错误：尝试将字符串和整数相加
    result = "Hello" + 123
    return result

def method_b():
    # 名称错误：使用未定义的变量
    result = method_a() + undefined_variable
    return result

def method_c(index):
    # 索引错误：访问列表中不存在的索引
    my_list = [1, 2, 3]
    return my_list[index] + method_b()

def method_d():
    # 键错误：访问字典中不存在的键
    my_dict = {"a": 1, "b": 2}
    return my_dict["c"] + method_c(2)

def method_e(value):
    # 值错误：尝试将非数字字符串转换为整数
    number = int(value)
    return number / method_d()

def method_f():
    # 除零错误：除以零（当method_e返回0时）
    return 100 / method_e("10")

def method_g():
    # 逻辑错误：计算错误（应该是加法但写成了乘法）
    return method_f() * 2  # 应该是 + 2

# 调用最外层方法，触发嵌套调用链
try:
    print(method_g())
except Exception as e:
    print(f"程序执行出错: {type(e).__name__} - {e}")
