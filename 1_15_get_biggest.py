def get_biggest(numbers):
    if len(numbers) < 1:
        return -1
    else:
        return  int(''.join(sorted(map(str, numbers), key=lambda x: x*len(max(map(str, numbers), key=len)), reverse=True)))
