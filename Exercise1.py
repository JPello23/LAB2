seconds = int(input("Seconds: "))
secondsTotal = seconds
days =  seconds // 86400
seconds = seconds % 86400
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(f"{secondsTotal} seconds are {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")
