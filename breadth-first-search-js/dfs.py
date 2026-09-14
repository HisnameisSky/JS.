def gen_parentheses_dfs(pairs):
    if not isinstance(pairs,int)or isinstance(pairs,bool):
        return ''
    if pairs<1:
        return ''
    result = []

    def backtrack(current_str, open_used, closes_used):
        if len(current_str)==2 * pairs:
            result.append(current_str)
            return

        if open_used<pairs:
            backtrack(current_str+'(',open_used+1,closes_used)
        if closes_used<open_used:
            backtrack(current_str+')',open_used,closes_used+1)
    backtrack('',0,0)
    return result

if __name__ == "__main__":
    print(gen_parentheses_dfs(2))
    print(gen_parentheses_dfs(3))