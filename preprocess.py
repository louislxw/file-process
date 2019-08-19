import re

from itertools import zip_longest


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


f1 = open("results/result_cam1_RAW_bus_stop.txt", 'r')
f3 = open("data/coco.names", 'r')
f4 = open("summary/cam1_RAW_bus_stop.txt", 'wt')

list1 = []
list3 = []

for lines in f1:
    for word in lines.split(":"):
        list1.append(word)
for lines in f3:
    for word in lines.split(" "):
        list3.append(word)

f1 = open("results/result_cam1_RAW_bus_stop.txt", 'r')

# string1 = f1.read().replace('\n', '')
# raw_f1 = re.findall(r'=\d+', string1)
# raw_f2 = str(raw_f1).strip('[]')
# fr1 = [int(s) for s in re.findall(r'\d+', raw_f2)]
# fr2 = list(grouper(4, fr1))
# print(fr2[0])

for i in list3:
    i = i.strip()
    count_object_raw = 0
    count_frame_raw = 0
    k = 0
    for j in list1:
        j = j.strip()
        # print(j)
        if j == "Enter Image Path":
            count_frame_raw += 1
            count_object_raw = 0
        elif j == i:
            count_object_raw += 1
            if re.search(r'Left+', list1[k+3]):
                print("RAW", count_frame_raw, i, list1[k+3], file=f4)
            else:
                print("RAW", count_frame_raw, i, list1[k+5], file=f4)
        k += 1

f1.close()
f3.close()
f4.close()
