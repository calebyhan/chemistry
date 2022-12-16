class Conversions:
    global metric_pre
    metric_pre = {"Y": 24, "Z": 21, "E": 18, "P": 15, "T": 12, "G": 9, "M": 6, "k": 3, "h": 2, "da": 1, "base": 0, "d": -1, "c": -2, "m": -3, "μ": -6, "mu": -6, "n": -9, "p": -12, "f": -15, "a": -18, "z": -21, "y": -24}
    def k_to_c(k):
        try:
            return float(k) - 273.15
        except:
            raise Exception("Value inputted is not a number.")
    def k_to_f(k):
        try:
            return (float(k) - 273.15) * 9/5 + 32
        except:
            raise Exception("Value inputted is not a number.")
    def c_to_k(c):
        try:
            return float(c) + 273.15
        except:
            raise Exception("Value inputted is not a number.")
    def c_to_f(c):
        try:
            return float(c) * 9/5 + 32
        except:
            raise Exception("Value inputted is not a number.")
    def f_to_k(f):
        try:
            round(((float(f) - 32) * 5/9 + 273.15), 5)
        except:
            raise Exception("Value inputted is not a number.")
    def f_to_c(f):
        try:
            return round(((float(f) - 32) * 5/9), 5)
        except:
            raise Exception("Value inputted is not a number.")
    def metric(num, pre1, pre2):
        try:
            num = float(num)
            if pre1 and pre2 in metric_pre:
                return num * (10 ** (metric_pre[pre1] - metric_pre[pre2]))
            else:
                raise Exception("Inputted prefixes are invalid. Reference [] for valid prefixes.")
        except:
            raise Exception("Value inputted is not a number.")

print(Conversions.metric(5, "M", "c"))