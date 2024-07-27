def wish_decor(func):
    def inner(name):
        if name == 'Aishwarya':
            print(f"Hey You are amazing, Good Morning {name}")
        else:
            func(name)

@wish_decor
def wish(name):
    print(f"Good Morning {name}")

while True:
    name = input("Please enter your name")
    if name == 'Aishwarya':
        wish(name)
    else:
        break

