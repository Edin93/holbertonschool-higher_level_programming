#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            i > a
        except:
            raise
            result = a ** b / i
        finally:
            result = b + a

    return result



from dis import dis
dis(magic_calculation)
