import time
cutime = time.time()
totalsec = int(cutime)
cusec = totalsec % 60
totalminu = totalsec // 60
cuminu = totalminu % 60
totalhour = totalminu // 60
offsetGMT = eval(input("Enter the time zone offset to GMT: "))
cuhour = ( totalhour + offsetGMT ) % 24
if cuhour <=12:
    print("The current time is",cuhour,":",cuminu,":",cusec,"AM")
else:
    print("The current time is",cuhour - 12,":",cuminu,":",cusec,"PM")