score = input("Enter Score:")
s = float(score)
if s >= 0.9:
    g ="A"
elif s >= 0.8:
    g ="B"
elif s >= 0.7:
    g="C"
elif s>= 0.6:
    g="D"
else:
    g="F"
print(g)