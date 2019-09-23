def normalize_name(input):
    for symbol in input:
        if symbol == "_":
            input = input.replace(symbol, " ")
    for symbol in input:
        if symbol.isalpha() == False and symbol.isdigit() == False and symbol != " ":
            input = input.replace(symbol, "")
    input = input.strip().lower().replace(" ", "_")
    return input


def cumsum(lst):
    total = 0
    new_lst = []
    for num in lst:
        total += num
        new_lst.append(total)
    return new_lst
