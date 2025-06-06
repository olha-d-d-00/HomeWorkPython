def second_index(text, some_str):
    if text:
        ind = text.find(some_str)

        if ind == -1:
            return None

        start_index = text.find(some_str, ind + 1)

        if start_index == -1:
            return None
        return start_index
    return None



assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
