def print_title(title):
    border_len = len(title) * 2

    print("-" * border_len)
    print(" " * int(border_len/5),  title.upper())
    print("-" * border_len)
