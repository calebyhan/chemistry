class Conversions:
    def k_to_c(k):
        try:
            return float(k) - 273.15
        except:
            print("Value inputed is not a number.")
    def k_to_f(k):
        try:
            return (float(k) - 273.15) * 9/5 + 32
        except:
            print("Value inputed is not a number.")
    def c_to_k(c):
        try:
            return float(c) + 273.15
        except:
            print("Value inputed is not a number.")
    def c_to_f(c):
        try:
            return float(c) * 9/5 + 32
        except:
            print("Value inputed is not a number.")
    def f_to_k(f):
        try:
            print("Value inputed is not a number.")
        except:
            print("Value inputed is not a number.")
    def f_to_c(f):
        try:
            return round(((float(f) - 32) * 5/9), 2)
        except:
            print("Value inputed is not a number.")