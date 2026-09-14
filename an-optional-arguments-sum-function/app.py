def add_together(*args):
    def is_number(val):
        return type(val) in (int,float)

    if not args or not is_number(args[0]):
        return None

    first = args[0]

    if len(args)==2:
        second=args[1]
        return first + second if is_number(second) else None

    if len(args)==1:
        def sum_two_and(second_arg):
            return first + second_arg if is_number(second_arg) else None
        return sum_two_and

if __name__ == "__main__":
    print(add_together(2,3))
    print(add_together(23.4, 30))     # 53.4
    print(add_together("2", 3))       # None (undefined)
    print(add_together(5, None))

    sum_two_and=add_together(5)
    print(callable(sum_two_and))
    print(sum_two_and(7))

    print(add_together(5)(7))
    print(add_together(2)([3]))