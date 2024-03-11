passed = False

def unitTest():
    global passed  # Declare 'passed' as a global variable
    try:
        time = int(input("Please enter the time of pickup 1 in session 1:"))
        passed = True
    except ValueError:
        passed = False

    return passed

print("Test result:", unitTest())

def unitTest2():
    global passed  # Declare 'passed' as a global variable
    try:
        time = int(input("Please enter the time of pickup 1 in session 2:"))
        passed = True
    except ValueError:
        passed = False

    return passed

print("Test result:", unitTest2())

def unitTest3():
    global passed
    totalTime=int(input("Please enter the total time of session 1:"))
    if totalTime<7200:
        passed=True
    else:
        passed=False
    return passed
print("Test result:",unitTest3())

def unitTest4():
    global passed
    totalTime=int(input("Please enter the total time of session 2:"))
    if totalTime<7200:
        passed=True
    else:
        passed=False
    return passed
print("Test result:",unitTest4())