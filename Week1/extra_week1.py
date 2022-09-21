import time

starttime = time.time_ns()



for i in range(100):
    print(f"\rProgress: {i + 1} / 100", end="")
    #time.sleep(.01)
print()

elapsed = (time.time_ns() - starttime) / 1000000000

print(f"{(elapsed / 1000000000)=}")
print(f"{(elapsed)=}")
