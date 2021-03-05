import csv
from pymongo import MongoClient

prevResultDic = {}
nextResultDic = {}
filterResultDic = {}

client = MongoClient("localhost", 27017)
print(client.list_database_names())

db = client['current_three_step']


def prevData2019():
    errData = 0
    cnt = 1

    f = open('상가업소정보_201912_04.csv', 'r', encoding='utf-8')
    firstLine = f.readline()
    rdr = csv.reader(f)

    for line in rdr:
        result = line[0].split('|')
        if len(result) == 39 and result[11] == '50':
            bizesId = result[0]
            bizesNm = result[1]
            brchNm = result[2]
            indsLclsCd = result[3]
            indsLclsNm = result[4]
            indsMclsCd = result[5]
            indsMclsNm = result[6]
            indsSclsCd = result[7]
            indsSclsNm = result[8]
            ksicCd = result[9]
            ksicNm = result[10]
            ctprvnCd = result[11]
            ctprvnNm = result[12]
            signguCd = result[13]
            signguNm = result[14]
            adongCd = result[15]
            adongNm = result[16]
            ldongCd = result[17]
            ldongNm = result[18]
            lnoAdr = result[24]
            rdnmAdr = result[31]
            lon = result[37]
            lat = result[38]

            prevResultDic[bizesId] = [bizesNm, brchNm, indsLclsCd, indsLclsNm, indsMclsCd, indsMclsNm, indsSclsCd,
                                      indsSclsNm, ksicCd, ksicNm, ctprvnCd, ctprvnNm, signguCd, adongCd, ldongCd,
                                      signguNm,
                                      adongNm, ldongNm, lnoAdr, rdnmAdr, lon, lat]

            print(cnt, "번", bizesId, prevResultDic[bizesId])

        cnt += 1

    f.close()


print("---------2019---------")
prevData2019()


def nextData2020():
    cnt = 1

    f = open('상가업소정보_202012_4.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)
    for line in rdr:
        if line[11] == '50':
            bizesId = line[0]
            bizesNm = line[1]

            nextResultDic[bizesId] = [bizesId, bizesNm]

            print(cnt, "번", bizesId, nextResultDic[bizesId])
        cnt += 1

    f.close()


print("---------2020---------")
nextData2020()

filterResultDic = prevResultDic

firstLen = len(filterResultDic)

# for key in errDataDic:
#     if key in filterResultDic.keys():
#         del[filterResultDic[key]]

for key in nextResultDic:
    if key in filterResultDic.keys():
        del [filterResultDic[key]]

print("----------------------------------------")

lastCnt = 1
for key in filterResultDic:
    store = {
        # 상가업소번호
        "bizesId": key,
        # 상호명
        "bizesNm": filterResultDic[key][0],
        # 지점명
        "brchNm": filterResultDic[key][1],
        # 상권업종대분류코드
        "indsLclsCd": filterResultDic[key][2],
        # 상권업종대분류명
        "indsLclsNm": filterResultDic[key][3],
        # 상권업종중분류코드
        "indsMclsCd": filterResultDic[key][4],
        # 상권업종중분류명
        "indsMclsNm": filterResultDic[key][5],
        # 상권업종소분류코드
        "indsSclsCd": filterResultDic[key][6],
        # 상권업종소분류명
        "indsSclsNm": filterResultDic[key][7],
        # 표준산업분류코드
        "ksicCd": filterResultDic[key][8],
        # 표준산업분류명
        "ksicNm": filterResultDic[key][9],
        # 시도코드
        "ctprvnCd": filterResultDic[key][10],
        # 시군구코드
        "signguCd": filterResultDic[key][12],
        # 행정동코드
        "adongCd": filterResultDic[key][13],
        # 법정동코드
        "ldongCd": filterResultDic[key][14],
        # 시도명
        "ctprvnNm": filterResultDic[key][11],
        # 시군구명
        "signguNm": filterResultDic[key][15],
        # 행정동명
        "adongNm": filterResultDic[key][16],
        # 법정동명
        "ldongNm": filterResultDic[key][17],
        # 지번주소
        "lnoAdr": filterResultDic[key][18],
        # 도로명주소
        "rdnmAdr": filterResultDic[key][19],
        # 경도
        "lon": filterResultDic[key][20],
        # 위도
        "lat": filterResultDic[key][21]
    }


    if filterResultDic[key][10] == '50':
        jeju = db.jeju
        store_id = jeju.insert_one(store).inserted_id

    print(lastCnt, filterResultDic[key])
    lastCnt += 1

# errCnt = 1
# for code in errDataDic:
#     print(errCnt, code)
#     errCode = {
#         "bizesId": code
#     }
#     errKeys = db.errCode
#     err_id = errKeys.insert_one(errCode).inserted_id
#     errCnt += 1


print("firstLen:", firstLen)
print("len(filterResultDic)", len(filterResultDic))
print(db.list_collection_names())