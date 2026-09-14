def diff_array(arr1,arr2):
    diff1 = [item for item in arr1 if item not in arr2]
    diff2 = [item for item in arr2 if item not in arr1]
    return diff1+ diff2

#variant

def diff_array_set(arr1,arr2):
    return list(set(arr1) ^ set(arr2))

#

set_a = {"apple", "banana","orange"}
set_b = {"banana", "grape","orange"}

result = set_a | set_b #a.untion(b)
result = set_a & set_b #a.intersection(b)
result = set_a - set_b #a.difference(b)
result = set_a ^ set_b #a.symmetric_difference(b)

#

my_set =[1,2,3]
my_list = [3,4,5]

print(my_set.union(my_list))

# 実務でよくある重複混じりのメールアドレスリスト
free_users_list = [
    "alice@example.com",
    "bob@example.com",
    "charlie@example.com",
    "alice@example.com",  # 重複データ
    "david@example.com",
]

premium_users_list = [
    "charlie@example.com",
    "david@example.com",
    "eve@example.com",
    "frank@example.com",
    "eve@example.com",  # 重複データ
]

free_users = set(free_users_list)
premium_users = set(premium_users_list)

print("--- [1. 重複除去後のユーザー数] ---")
print(f"無料ユーザー(ユニーク): {len(free_users)}人")  # 4人
print(f"有料ユーザー(ユニーク): {len(premium_users)}人")  # 4人

converted_users = free_users & premium_users
print("\n--- [2. 無料・有料の両方に登録しているユーザー (積集合)] ---")
print(converted_users)

free_only_users = free_users - premium_users
print("\n--- [3. 無料プランのみ利用中のユーザー (差集合)] ---")
print(free_only_users)

all_inique_users = free_users | premium_users
print("\n--- [4. 全サービス合計のユニークユーザー数 (和集合)] ---")
#print(f"全ユーザー数: {len(all_unique_users)}人")  # 6人

single_plan_users = free_users ^ premium_users
print("\n--- [5. どちらか1つのプランのみ契約しているユーザー (対称差)] ---")
print(single_plan_users)

active_user_emails = {user["email"] for user in active_user_data}
banned_user_emails = {user["email"] for user in banned_users_data}

#
config_old = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "timeout": 30
}

config_new = {
    "host": "localhost",
    "port": 9000,       # 値を変更
    "debug": True,
    "use_ssl": True     # 新規追加
}

common_keys = config_old.keys() & config_new.keys()
print(common_keys)

#

removed_keys = config_old.keys() = config_new.keys()
print(removed_keys)

added_keys = config_new.keys() - config_old.keys()
print(added_keys)

#

same_pairs = config_old.items() & config_new.items()
print(same_pairs)
same_dict = dict(same_pairs)
print(same_dict)

#

changed_values = {
    k: (config_old[k], config_new[k])
    for k in (config_old.keys() & config_new.keys())
    if config_old[k] != config_new[k]
}
print(changed_values)