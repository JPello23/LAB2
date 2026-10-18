GROWTH = 0.06
usage = float(input("usage:"))
usage = usage * (1 + GROWTH)
print("Month 1=" , round(usage, 2))
usage = usage * (1 + GROWTH)
print("Month 2=" , round(usage, 2))
usage = usage * (1 + GROWTH)
print("Month 3=" , round(usage, 2))