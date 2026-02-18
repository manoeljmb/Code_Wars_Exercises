def make_negative(number):
    return -abs(number) # <--- My solution



for n, expected in ((42,-42), (-9,-9), (0,0)):
    actual = make_negative(n)
    message = f"For n = {n}, expected {expected} but got {actual}"
    print(f"{n}: {message}")