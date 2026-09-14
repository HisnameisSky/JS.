def pyramid(pattern, rows, inverted):
    lines = []

    for i in range(rows):
        row_num = rows - i if inverted else i + 1

        space_count = rows - row_num
        pattern_count = 2 * row_num - 1

        line = " " * space_count + pattern * pattern_count
        lines.append(line)

    return "\n" + "\n".join(lines) + "\n"

#ex

print("o"*4)
print(" "*3)
print("ABC"*2)