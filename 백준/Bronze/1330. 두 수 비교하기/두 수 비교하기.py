a, b = map(int, input().split())
if int(a) > int(b):
    print('>')
elif int(a) < int(b):
    print('<')
elif int(a) == int(b):
    print('==')