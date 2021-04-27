import csv

my_list = []
def nextData2019():
    errData = 0
    cnt = 1

    f = open('상가업소정보_201912_04.csv', 'r', encoding='utf-8')
    firstLine = f.readline()
    rdr = csv.reader(f)

    for line in rdr:
        result = line[0].split('|')
        print(cnt)
        if len(result) == 39:
            # print(result)
            indsMclsCd = result[5]
            indsMclsNm = result[6]

            my_list.append(indsMclsCd + indsMclsNm)

        else:
            errData += 1
            print(result)
        cnt += 1

    print("errorData : ", errData)

    f.close()

nextData2019()

my_set = set(my_list)

print("my_set", my_set)