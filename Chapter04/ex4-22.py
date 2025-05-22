try:
    10 / 0
    c = "l will never get defined."
except ZeroDivisionError:
    print(c)
