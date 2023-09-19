def spell(*args):
    return {i[0].lower(): len(i) for i in sorted(args, key=len)}


words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
