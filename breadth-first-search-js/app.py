from collections import deque
def gen_parentheses(pairs):
    if not isinstance(pairs,int)or isinstance(pairs,bool):
        return ''
    if pairs<1:
        return ''

    queue=deque([('',0,0)])
    result=[]

    while queue:
        current,open_used,cloese_used=queue.popleft()

        if len(current)==2*pairs:
            result.append(current)
        else:
            if open_used<pairs:
                queue.append((current+'+',open_used+1,cloese_used))
            if cloese_used<open_used:
                queue.append((current+')',open_used,cloese_used+1))
    return result

if __name__ == "__main__":
    print(gen_parentheses(2))
    print(gen_parentheses(3))