f1 = open("results/result_cam6_RAW_still.txt", 'r')
f2 = open("data/coco.names", 'r')
f3 = open("summary/summary_cam6_RAW_still.txt", 'wt')

list1 = []
list2 = []
list3 = []

for lines in f1:
    for word in lines.split(":"):
        list1.append(word)
# print(list1)
for lines in f2:
    for word in lines.split(":"):
        list2.append(word)
# print(list2)
for i in list2:
    i = i.strip()
    count_object = 0
    count_frame = 0
    for j in list1:
        j = j.strip()
        if j == "Enter Image Path":
            if count_object != 0:
                print("Frame\t", count_frame, "\tdetect\t", i, "\t", count_object, "\ttimes", file=f3)
            count_frame += 1
            count_object = 0
        elif j == i:
            count_object += 1

    # print("Frame", count_frame, ":", i, count_object, file=f3)
f1.close()
f2.close()
f3.close()
