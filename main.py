import csv
from pymongo import MongoClient

prevResultDic = {}
nextResultDic = {}
filterResultDic = {}

client = MongoClient("localhost", 27017)
print(client.list_database_names())

db = client['threestep']

collection = db['test1819']

errDataDic = []


def nextData2019():
    errData = 0
    cnt = 1

    f = open('상가업소정보_201912_04.csv', 'r', encoding='utf-8')
    firstLine = f.readline()
    rdr = csv.reader(f)

    for line in rdr:
        result = line[0].split('|')
        if len(result) == 39:
            bizesId = result[0]
            bizesNm = result[1]
            brchNm = result[2]
            indsLclsCd = result[3]
            indsLclsNm = result[4]
            ctprvnCd = result[11]
            ctprvnNm = result[12]
            signguCd = result[13]
            signguNm = result[14]
            adongCd = result[15]
            adongNm = result[16]
            ldongCd = result[17]
            ldongNm = result[18]
            lon = result[37]
            lat = result[38]

            nextResultDic[bizesId] = [bizesNm, brchNm, indsLclsCd, indsLclsNm, ctprvnCd, signguCd, adongCd, ldongCd, ctprvnNm, signguNm, adongNm, ldongNm, lon, lat]
            print(cnt)
            print(bizesId, nextResultDic[bizesId])
        else:
            errDataDic.append(result[0])
            errData += 1
        cnt += 1

    print("errorData : ", errData)

    f.close()

print("---------2019---------")
nextData2019()

def prevData2018():
    cnt = 1

    f = open('상가업소정보_201812_4.csv', 'r', encoding='euc_kr')
    firstLine = f.readline()
    rdr = csv.reader(f)
    for line in rdr:
        bizesId = line[0]
        bizesNm = line[1]
        brchNm = line[2]
        indsLclsCd = line[3]
        indsLclsNm = line[4]
        ctprvnCd = line[11]
        ctprvnNm = line[12]
        signguCd = line[13]
        signguNm = line[14]
        adongCd = line[15]
        adongNm = line[16]
        ldongCd = line[17]
        ldongNm = line[18]
        lon = line[37]
        lat = line[38]

        prevResultDic[bizesId] = [bizesNm, brchNm, indsLclsCd, indsLclsNm, ctprvnCd, signguCd, adongCd, ldongCd, ctprvnNm, signguNm, adongNm, ldongNm, lon, lat]

        print(cnt)
        print(bizesId, prevResultDic[bizesId])
        cnt += 1


    f.close()

print("---------2018---------")
prevData2018()


filterResultDic = prevResultDic


print("len(filterResultDic)", len(filterResultDic))

for key in errDataDic:
    if key in prevResultDic.keys():
        del[filterResultDic[key]]

for key in nextResultDic:
    if key in prevResultDic.keys():
        del[filterResultDic[key]]

print("----------------------------------------")

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
        # 시도코드
        "ctprvnCd": filterResultDic[key][4],
        # 시군구코드
        "signguCd": filterResultDic[key][5],
        # 행정동코드
        "adongCd": filterResultDic[key][6],
        # 법정동코드
        "ldongCd": filterResultDic[key][7],
        # 시도명
        "ctprvnNm": filterResultDic[key][8],
        # 시군구명
        "signguNm": filterResultDic[key][9],
        # 행정동명
        "adongNm": filterResultDic[key][10],
        # 법정동명
        "ldongNm": filterResultDic[key][11],
        # 경도
        "lon": filterResultDic[key][12],
        # 위도
        "lat": filterResultDic[key][13]
    }
    if filterResultDic[key][4] == '44':
        chungcheongnamdo = db.chungcheongnamdo
        store_id = chungcheongnamdo.insert_one(store).inserted_id
    elif filterResultDic[key][4] == '45':
        jeollabukdo = db.jeollabukdo
        store_id = jeollabukdo.insert_one(store).inserted_id
    elif filterResultDic[key][4] == '46':
        jeollanamdo = db.jeollanamdo
        store_id = jeollanamdo.insert_one(store).inserted_id
    elif filterResultDic[key][4] == '47':
        gyeongsangbukdo = db.gyeongsangbukdo
        store_id = gyeongsangbukdo.insert_one(store).inserted_id
    elif filterResultDic[key][4] == '48':
        gyeongsangnamdo = db.gyeongsangnamdo
        store_id = gyeongsangnamdo.insert_one(store).inserted_id
    elif filterResultDic[key][4] == '49':
        jeju = db.jeju
        store_id = jeju.insert_one(store).inserted_id

    print(filterResultDic[key])

print("len(filterResultDic)", len(filterResultDic))
print(db.list_collection_names())
