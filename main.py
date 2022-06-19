# numbers count down

print("\n== Number Count Down == ")
start = int(input("Input a number to start: "))
finish = int(input("Input a number to finish: "))
step = -1                            # -1 means count from behind/the back

for i in range(start,finish-1,step):  # -1 means to include the finish point/number
    print(i)

print("\n== Display String in Reverse == ")
word = input("Input word/s to be diplayed in reverse: ")
i = int(len(word))
reserveStr = []

while i != 0:
    reserveStr += word[i - 1]            # value is saved in reservestr
    i = i -1                            # decrement i

print(reserveStr)
