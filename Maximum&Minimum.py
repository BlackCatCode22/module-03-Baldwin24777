maxi = None
mini = None

while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        fvalue = float(value)
        if maxi is None or fvalue > maxi:
            maxi = fvalue
        if mini is None or fvalue < mini:
            mini = fvalue
    except:
        print("Error")

print("Maximum number: ", maxi)
print("Minimum number: ", mini)














