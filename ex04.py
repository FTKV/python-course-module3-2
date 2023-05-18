print(globals())

x = 10

def some_fnc():
    def inner_fnc():
        print("Hello from inner")
    print(locals())
    return "Hello"

some_fnc()

print(globals())