def destroyer(arr, *val_to_remove):
    return [item for item in arr if item not in val_to_remove]

#

def destroyer_fast(arr, *val_to_remove):
    remove_set = set(val_to_remove)
    return [item for item in arr if item not in remove_set]

#review


def calculate_total(*args):
    print(f"受け取ったデータ型: {type(args)}")
    return sum(args)


print(calculate_total(100, 200))        # 300
print(calculate_total(100, 200, 300))

#

def print_user_profile(**kwargs):
    print(f"受け取ったデータ型: {type(kwargs)}")

    for key, value in kwargs.items():
        print(f". {key}: {value}")

print_user_profile(name="Alice", role = "Admin", active=True)

def build_query(table_name, *conditions, **options):
    print(f"対象テーブル: {table_name}")
    print(f"検索条件 (タプル): {conditions}")
    print(f"オプション (辞書): {options}")

build_query("users","status = 'active'", "age >= 18", limit=10,sort = "ASC")

class CustomLogger:
    def log(self, message, *args, **kwargs):
        print(f"[LOG] {message}, *args, **kwargs")

#

def print_point(x,y,z):
    print(f"X:{x},Y:{y},Z:{z}")
point_list = [10,20,30]
print_point(*print_point)

#

def create_user(name, age, role):
    print(f"ユーザー登録: {name} ({age}歳) - 権限: {role}")

user_data = {"name":"Alice", "age":25,"tole":"Admin"}
create_user(**user_data)

#

list_a = [1,2]
list_b = [3,4]
combined_list = [*list_a, *list_b, 5]

dict_a = {"x":1}
dict_b = {"y":2}
combined_list ={**dict_a, **dict_b, "z":3}

#

def internal_process(a,b,c=0):
    return a+b+c

def wrapper_func(*args, **kwargs):
    print("ログ記録中...")
    return internal_process(*args, **kwargs)

print(wrapper_func(10,20,c=5))

