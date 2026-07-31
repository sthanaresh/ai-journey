# Exercise C (finally drill): Write a function safe_divide(a: float, b: float) -> float that:

# Tries to divide a / b
# Catches ZeroDivisionError and returns 0.0
# In finally, prints "Division attempted" regardless of outcome


def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0
    finally:
        print("Division attempted")


result = safe_divide(10, 0)
print(result)
