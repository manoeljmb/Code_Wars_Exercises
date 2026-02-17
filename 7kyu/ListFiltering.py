import re
l = [1, 2, 'aasf', '1', '123', 123]
newList = []
for i in l:
    if isinstance(i, int):
        newList.append(i)
    else:
        continue
print(newList)