import csv

my_list = []

def prevData2018():
    cnt = 1

    f = open('상가업소정보_201812_4.csv', 'r', encoding='euc_kr')
    firstLine = f.readline()
    rdr = csv.reader(f)
    for line in rdr:
        print(cnt)
        ctprvnCd = line[11]
        ctprvnNm = line[12]


        my_list.append(ctprvnCd + ctprvnNm)
        cnt += 1

    f.close()

prevData2018()

my_set = set(my_list)
print("my_set", my_set)