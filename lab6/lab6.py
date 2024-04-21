import re
import random
import string


def add_unused_code(code):
    # Словарь для хранения "бесполезного" кода с ключами - числами и строками - кодом
    unused_code_dict = {
        1: """
    def binary_search(self, arr, x):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1
""",
        2: """
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
""",
        3: """
    def sliding_window(arr, k):
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(len(arr) - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(max_sum, window_sum)
        return max_sum
""",
        4: """    
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)
        """
    }

    # Выбор случайных чисел для ключей словаря
    random_keys = random.choices(list(unused_code_dict.keys()), k=2)

    # Получение "бесполезного" кода из словаря по случайно выбранным ключам
    unused_code_1 = unused_code_dict[random_keys[0]]
    unused_code_2 = unused_code_dict[random_keys[1]]

    # Поиск мест для вставки "бесполезного" кода перед функциями
    code = re.sub(r'def\s+authenticate_user', f'{unused_code_1}\n    def authenticate_user', code, count=1)
    code = re.sub(r'def\s+process_file_input', f'{unused_code_2}\n    def process_file_input', code, count=1)

    return code

def add_useless_comments(code):
    lines = code.split('\n')
    with_comments = []
    for line in lines:
        comment_probability = random.randint(1, 4)
        if comment_probability == 3:
            tab_size = random.randint(1, 20)
            spaces = ' ' * tab_size
            useless_comment = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))
            with_comments.append(f'{spaces}# {useless_comment}')
        with_comments.append(line)
    return '\n'.join(with_comments)


def replace_tabs(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    code = re.sub(r'def\s+(\w+)\s*\(([^)]+)\):', lambda match: replace_args_tabs(match), code)

    code = re.sub(r'(?<=\s)(\w+)\s*=', lambda match: replace_variable_tabs(match), code)

    code = replace_variable_names(code)

    code = add_useless_comments(code)

    code = add_unused_code(code)

    with open("/home/panton8/PycharmProjects/ИСОБ/lab4_5/modified_code.py", 'w') as file:
        file.write(code)

    print("Tab replacement complete. Modified code saved as 'modified_code.py'.")


def replace_args_tabs(match):
    func_name = match.group(1)
    args = match.group(2)
    args_list = args.split(',')
    replaced_args = []
    for arg in args_list:
        spaces = ' ' * random.randint(1, 20)
        replaced_args.append(f"{spaces}{arg.strip()}")
    return f'def {func_name}({", ".join(replaced_args)}):'


def replace_variable_tabs(match):
    variable = match.group(1)
    spaces = ' ' * random.randint(1, 20)  # Случайное количество пробелов от 1 до 10
    return f'{variable}{spaces}='


def replace_variable_names(code):
    variable_names = {
        'user_data': ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))),
        'file_path': ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))),
        'input_entry': ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))),
        'current_user': ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))),
        'data_list': ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    }
    for old_name, new_name in variable_names.items():
        code = re.sub(rf'\b{old_name}\b', new_name, code)
    return code


if __name__ == "__main__":
    file_path = "test"
    replace_tabs(file_path)
