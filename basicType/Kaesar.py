
# while True:
#     anum = (ord(input()) - 96) *3 + 5
#     num = anum % 27 + 96
#     print(chr(num))


# str = input()
# for i in range(0, len(str)):
#     if(str[i]) == " ":
#         print("e", end="")
#         continue
#     anum = (ord(str[i]) - 96) * 3 + 5
#     num = anum % 27 + 96
#     print(chr(num), end="")

str = "ANKYODKYUREPFJBYOJDSPLREYIUNOFDOIUERFPLUYTS"
test = "MR MUSTARD WITH THE CANDLESTICK IN THE HALL"
for i in range(0, len(str)):
    ming = ord(test[i]) - 96
    mi = ord(str[i]) - 96
    if test[i].isspace():
        print(str[i], end="")
        continue
    if mi < ming:
        mi = mi + 27
    n = mi - ming
    n += 96
    print(chr(n), end="")