# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def param_arg(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if hash_(value):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict


def hash_(value):
    try:
        hash(value)
        return True
    except:
        return False


print(param_arg(city='Moscow', lst=[1, 2, 3]))
