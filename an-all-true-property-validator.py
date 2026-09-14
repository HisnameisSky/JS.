def truth_check(collection,pre):
    return all(bool(obj.get(pre)) for obj in collection)

print(
    truth_check(
        [
            {"name": "Quincy", "role": "Founder", "isBot": False},
            {"name": "Naomi", "role": "", "isBot": False},
            {"name": "Camperbot", "role": "Bot", "isBot": True},
        ],
        "isBot",
    )
)

#

my_list = []

if not my_list:
    print("Python: リストが空です！")


#

import math

if math.nan:
    print("Python: NaN でも True に評価される！")

if math.isnan(val):
    pass