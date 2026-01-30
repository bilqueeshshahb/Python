#12.write a program to display the use of local,global and nonlocal variables.

message = "I  am a global variable."

def outer_function():
    message = "I am a nonlocal variable."

    def inner_function():
        message = "I am a local variable."

        print("1. inside inner_function:", message)

    inner_function()
    print("2. inside outer_function:", message)

outer_function()
print("3. in the main body:", message)
