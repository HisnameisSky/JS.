def steamroll_array(arr):
    flattened = []

    def flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                flatten(sub_item)  # 再帰呼び出し
        else:
            flattened.append(item)

    for element in arr:
        flatten(element)

    return flattened

#Alt

def steamroll_array_gen(arr):
    def flatten_gen(item):
        if isinstance(item, list):
            for sub_item in item:
                yield from flatten_gen(sub_item)
        else:
            yield item

    return list(flatten_gen(arr))

#yield from

def steamroll_gen(arr):
    for item in arr:
        if isinstance(item, list):
            # サブジェネレータに処理を丸投げ（委譲）
            yield from steamroll_gen(item)
        else:
            yield item

nested_list = [1,[2,[3,4]],5]
gen = steamroll_gen(nested_list)
for val in gen:
    print(val, end=" ")

###if isinstance(item,list):
    ###for sub_item in streamroll_gen(item):
       ### yield sub_item

###if isinstance(item,list):
   ### yield from streamroll_gen(item)

#

def streamroll_array_stack(arr):
    stack=list(arr)
    result =[]

    while stack:
        item = stack.pop()

        if isinstance(item,list):
            stack.extend(item)
        else:
            result.append(item)
    result.reverse()
    return result

print(streamroll_array_stack([1,{},[3,[[4]]]]))

#

def read_hug_file(file_path):
    with open(file_path,"r")as f:
        for line in f:
            yield line

#for line in read_hug_file("huge_file.txt"):
#    process(line)

    
import tracemalloc

tracemalloc.start()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
for stat in top_stats[:5]:
    print(stat)