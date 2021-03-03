from pymongo import MongoClient
from multiprocessing import Process
import csv


client = MongoClient('localhost', 27017)

db = client['current_three_step']

def compareData1():
    seoul19 = db['seoul']
    busan19 = db['busan']

    cnt = 1

    # 1. 서울, 부산
    prevSeoulCnt = seoul19.count_documents({})
    prevBusanCnt = busan19.count_documents({})

    f = open('상가업소정보_202012_1.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)
    for line in rdr:
        bizeId = line[0]
        seoul19.find_one_and_delete({"bizesId": bizeId})
        busan19.find_one_and_delete({"bizesId": bizeId})

        print("1. 서울 부산", cnt)
        cnt += 1

    f.close()

    afterSeoulCnt = seoul19.count_documents({})
    afterBusanCnt = busan19.count_documents({})

    print("prevSeoul:", prevSeoulCnt, "afterSeoul", afterSeoulCnt)
    print("prevBusan:", prevBusanCnt, "afterBusan", afterBusanCnt)


def compareData2():
    daegu19 = db['daegu']
    incheon19 = db['incheon']
    gwangju19 = db['gwangju']
    daejeon19 = db['daejeon']
    ulsan19 = db['ulsan']
    sejong19 = db['sejong']

    cnt = 1

    # 2. 대구, 인천, 광주, 대전, 울산, 세종
    prevDaeguCnt = daegu19.count_documents({})
    prevIncheonCnt = incheon19.count_documents({})
    prevGwangjuCnt = gwangju19.count_documents({})
    prevDaejeonCnt = daejeon19.count_documents({})
    prevUlsanCnt = ulsan19.count_documents({})
    prevSejongCnt = sejong19.count_documents({})

    f = open('상가업소정보_202012_2.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)
    for line in rdr:
        bizeId = line[0]
        daegu19.find_one_and_delete({"bizesId": bizeId})
        incheon19.find_one_and_delete({"bizesId": bizeId})
        gwangju19.find_one_and_delete({"bizesId": bizeId})
        daejeon19.find_one_and_delete({"bizesId": bizeId})
        ulsan19.find_one_and_delete({"bizesId": bizeId})
        sejong19.find_one_and_delete({"bizesId": bizeId})

        print("2. 대구, 인천, 광주, 대전, 울산, 세종", cnt)
        cnt += 1

    f.close()

    afterDaeguCnt = daegu19.count_documents({})
    afterIncheonCnt = incheon19.count_documents({})
    afterGwangjuCnt = gwangju19.count_documents({})
    afterDaejeonCnt = daejeon19.count_documents({})
    afterUlsanCnt = ulsan19.count_documents({})
    afterSejongCnt = sejong19.count_documents({})

    print("prevDaeguCnt:", prevDaeguCnt, "afterDaeguCnt", afterDaeguCnt)
    print("prevIncheonCnt:", prevIncheonCnt, "afterIncheonCnt", afterIncheonCnt)
    print("prevGwangjuCnt:", prevGwangjuCnt, "afterGwangjuCnt", afterGwangjuCnt)
    print("prevDaejeonCnt:", prevDaejeonCnt, "afterDaejeonCnt", afterDaejeonCnt)
    print("prevUlsanCnt:", prevUlsanCnt, "afterUlsanCnt", afterUlsanCnt)
    print("prevSejongCnt:", prevSejongCnt, "afterSejongCnt", afterSejongCnt)


def compareData3():
    gyeonggido19 = db['gyeonggido']
    gangwondo19 = db['gangwondo']
    chungcheongbukdo19 = db['chungcheongbukdo']

    cnt = 1

    # 3. 경기도, 강원도, 충청북도
    prevGyeonggidoCnt = gyeonggido19.count_documents({})
    prevGangwondoCnt = gangwondo19.count_documents({})
    prevChungcheongbukdoCnt = chungcheongbukdo19.count_documents({})

    f = open('상가업소정보_202012_3.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)
    for line in rdr:
        bizeId = line[0]
        gyeonggido19.find_one_and_delete({"bizesId": bizeId})
        gangwondo19.find_one_and_delete({"bizesId": bizeId})
        chungcheongbukdo19.find_one_and_delete({"bizesId": bizeId})

        print("3. 경기도, 강원도, 충청북도", cnt)
        cnt += 1

    f.close()

    afterGyeonggidoCnt = gyeonggido19.count_documents({})
    afterGangwondoCnt = gangwondo19.count_documents({})
    afterChungcheongbukdoCnt = chungcheongbukdo19.count_documents({})

    print("prevGyeonggidoCnt:", prevGyeonggidoCnt, "afterGyeonggidoCnt", afterGyeonggidoCnt)
    print("prevGangwondoCnt:", prevGangwondoCnt, "afterGangwondoCnt", afterGangwondoCnt)
    print("prevChungcheongbukdoCnt:", prevChungcheongbukdoCnt, "afterChungcheongbukdoCnt", afterChungcheongbukdoCnt)


def compareData4():
    chungcheongnamdo19 = db['chungcheongnamdo']
    jeollabukdo19 = db['jeollabukdo']
    jeollanamdo19 = db['jeollanamdo']
    gyeongsangbukdo19 = db['gyeongsangbukdo']
    gyeongsangnamdo19 = db['gyeongsangnamdo']
    jeju19 = db['jeju']

    cnt = 1

    # 4. 충남, 전북, 전남, 경북, 경남, 제주
    prevChungcheongnamdoCnt = chungcheongnamdo19.count_documents({})
    prevJeollabukdoCnt = jeollabukdo19.count_documents({})
    prevJeollanamdoCnt = jeollanamdo19.count_documents({})
    prevGyeongsangbukdoCnt = gyeongsangbukdo19.count_documents({})
    prevGyeongsangnamdoCnt = gyeongsangnamdo19.count_documents({})
    prevJejuCnt = jeju19.count_documents({})

    f = open('상가업소정보_202012_4.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)
    for line in rdr:
        bizeId = line[0]
        chungcheongnamdo19.find_one_and_delete({"bizesId": bizeId})
        jeollabukdo19.find_one_and_delete({"bizesId": bizeId})
        jeollanamdo19.find_one_and_delete({"bizesId": bizeId})
        gyeongsangbukdo19.find_one_and_delete({"bizesId": bizeId})
        gyeongsangnamdo19.find_one_and_delete({"bizesId": bizeId})
        jeju19.find_one_and_delete({"bizesId": bizeId})

        print("4. 충남, 전북, 전남, 경북, 경남, 제주", cnt)
        cnt += 1

    f.close()

    afterChungcheongnamdoCnt = chungcheongnamdo19.count_documents({})
    afterJeollabukdoCnt = jeollabukdo19.count_documents({})
    afterJeollanamdoCnt = jeollanamdo19.count_documents({})
    afterGyeongsangbukdoCnt = gyeongsangbukdo19.count_documents({})
    afterGyeongsangnamdoCnt = gyeongsangnamdo19.count_documents({})
    afterJejuCnt = jeju19.count_documents({})

    print("prevChungcheongnamdoCnt:", prevChungcheongnamdoCnt, "afterChungcheongnamdoCnt", afterChungcheongnamdoCnt)
    print("prevJeollabukdoCnt:", prevJeollabukdoCnt, "afterJeollabukdoCnt", afterJeollabukdoCnt)
    print("prevJeollanamdoCnt:", prevJeollanamdoCnt, "afterJeollanamdoCnt", afterJeollanamdoCnt)
    print("prevGyeongsangbukdoCnt:", prevGyeongsangbukdoCnt, "afterGyeongsangbukdoCnt", afterGyeongsangbukdoCnt)
    print("prevGyeongsangnamdoCnt:", prevGyeongsangnamdoCnt, "afterGyeongsangnamdoCnt", afterGyeongsangnamdoCnt)
    print("prevJejuCnt:", prevJejuCnt, "afterJejuCnt", afterJejuCnt)


def allCollectionTotal():
    seoul19 = db['seoul']
    busan19 = db['busan']

    daegu19 = db['daegu']
    incheon19 = db['incheon']
    gwangju19 = db['gwangju']
    daejeon19 = db['daejeon']
    ulsan19 = db['ulsan']
    sejong19 = db['sejong']

    gyeonggido19 = db['gyeonggido']
    gangwondo19 = db['gangwondo']
    chungcheongbukdo19 = db['chungcheongbukdo']

    chungcheongnamdo19 = db['chungcheongnamdo']
    jeollabukdo19 = db['jeollabukdo']
    jeollanamdo19 = db['jeollanamdo']
    gyeongsangbukdo19 = db['gyeongsangbukdo']
    gyeongsangnamdo19 = db['gyeongsangnamdo']
    jeju19 = db['jeju']

    totalCnt = 0

    totalCnt += seoul19.count_documents({})
    totalCnt += busan19.count_documents({})

    totalCnt += daegu19.count_documents({})
    totalCnt += incheon19.count_documents({})
    totalCnt += gwangju19.count_documents({})
    totalCnt += daejeon19.count_documents({})
    totalCnt += ulsan19.count_documents({})
    totalCnt += sejong19.count_documents({})

    totalCnt += gyeonggido19.count_documents({})
    totalCnt += gangwondo19.count_documents({})
    totalCnt += chungcheongbukdo19.count_documents({})

    totalCnt += chungcheongnamdo19.count_documents({})
    totalCnt += jeollabukdo19.count_documents({})
    totalCnt += jeollanamdo19.count_documents({})
    totalCnt += gyeongsangbukdo19.count_documents({})
    totalCnt += gyeongsangnamdo19.count_documents({})
    totalCnt += jeju19.count_documents({})

    print(totalCnt)

'''
if __name__ == "__main__":
    p1 = Process(target=compareData1)
    p2 = Process(target=compareData2)
    p3 = Process(target=compareData3)
    p4 = Process(target=compareData4)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
'''
# compareData1()


allCollectionTotal()