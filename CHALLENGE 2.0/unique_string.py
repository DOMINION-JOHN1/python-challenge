def remove_duplicates(string_list):
    set_strings = set(string_list)
    return "".join(set_strings)

print(remove_duplicates('namedominionjohneleojo'))
