counter = 0

def greeting(func):
    def inner(*args):
        global counter
        n = func()
        counter += 1
        if counter % 5 == 0:
            wrapped_text = f"Привет, {n}!  Вы получаете бесплатную плюшку!"
        else:
            wrapped_text = f"Привет, {n}!"
        return wrapped_text

    return inner


counter1 = 0

@greeting
def read_file():
    with open('client.txt', encoding='utf-8') as c:
        global counter1
        d = c.readlines()[counter1].rstrip()
        counter1 += 1
        return d


@greeting
def input_name():
    return input()


print(read_file())
print(read_file())
print(read_file())
print(input_name())
print(input_name())
