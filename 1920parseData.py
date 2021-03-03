from pymongo import MongoClient
from multiprocessing import Process
import pprint

client = MongoClient('localhost', 27017)

db = client['threestep']

Qq = db['Q']
Pp = db['P']
Rr = db['R']
Dd = db['D']
Nn = db['N']
Ss = db['S']
Ff = db['F']
Oo = db['O']
Ll = db['L']

def seoulDB():
    seoul20 = db['seoul']

    seoulCnt = seoul20.count_documents({})

    print(seoulCnt)

    # qCnt = 1
    # for store in seoul20.find({"indsLclsCd": "Q"}):
    #     print(qCnt, "seoul",store)
    #     insertData = Qq.insert_one(store)
    #     qCnt += 1

    pCnt = 1
    for store in seoul20.find({"indsLclsCd": "P"}):
        print(pCnt, "seoul", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in seoul20.find({"indsLclsCd": "R"}):
        print(rCnt, "seoul", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in seoul20.find({"indsLclsCd": "D"}):
        print(dCnt, "seoul", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in seoul20.find({"indsLclsCd": "N"}):
        print(nCnt, "seoul", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in seoul20.find({"indsLclsCd": "S"}):
        print(sCnt, "seoul", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in seoul20.find({"indsLclsCd": "F"}):
        print(fCnt, "seoul", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in seoul20.find({"indsLclsCd": "O"}):
        print(oCnt, "seoul", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in seoul20.find({"indsLclsCd": "L"}):
        print(lCnt, "seoul", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def busanDB():
    busan20 = db['busan']

    busanCnt = busan20.count_documents({})

    print(busanCnt)

    qCnt = 1
    for store in busan20.find({"indsLclsCd": "Q"}):
        print(qCnt, "busan", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in busan20.find({"indsLclsCd": "P"}):
        print(pCnt, "busan", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in busan20.find({"indsLclsCd": "R"}):
        print(rCnt, "busan", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in busan20.find({"indsLclsCd": "D"}):
        print(dCnt, "busan", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in busan20.find({"indsLclsCd": "N"}):
        print(nCnt, "busan", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in busan20.find({"indsLclsCd": "S"}):
        print(sCnt, "busan", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in busan20.find({"indsLclsCd": "F"}):
        print(fCnt, "busan", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in busan20.find({"indsLclsCd": "O"}):
        print(oCnt, "busan", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in busan20.find({"indsLclsCd": "L"}):
        print(lCnt, "busan", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def chungcheongbukdoDB():
    chungcheongbukdo20 = db['chungcheongbukdo']

    chungcheongbukdoCnt = chungcheongbukdo20.count_documents({})

    print(chungcheongbukdoCnt)

    qCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "chungcheongbukdo", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "P"}):
        print(pCnt, "chungcheongbukdo", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "R"}):
        print(rCnt, "chungcheongbukdo", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "D"}):
        print(dCnt, "chungcheongbukdo", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "N"}):
        print(nCnt, "chungcheongbukdo", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "S"}):
        print(sCnt, "chungcheongbukdo", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "F"}):
        print(fCnt, "chungcheongbukdo", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "O"}):
        print(oCnt, "chungcheongbukdo", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in chungcheongbukdo20.find({"indsLclsCd": "L"}):
        print(lCnt, "chungcheongbukdo", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def chungcheongnamdoDB():
    chungcheongnamdo20 = db['chungcheongbukdo']

    chungcheongnamdoCnt = chungcheongnamdo20.count_documents({})

    print(chungcheongnamdoCnt)

    qCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "충남", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "P"}):
        print(pCnt, "충남", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "R"}):
        print(rCnt, "충남", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "D"}):
        print(dCnt, "충남", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "N"}):
        print(nCnt, "충남", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "S"}):
        print(sCnt, "충남", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "F"}):
        print(fCnt, "충남", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "O"}):
        print(oCnt, "충남", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in chungcheongnamdo20.find({"indsLclsCd": "L"}):
        print(lCnt, "충남", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def daeguDB():
    daegu20 = db['daegu']

    daeguCnt = daegu20.count_documents({})

    print(daeguCnt)

    qCnt = 1
    for store in daegu20.find({"indsLclsCd": "Q"}):
        print(qCnt, "daegu20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in daegu20.find({"indsLclsCd": "P"}):
        print(pCnt, "daegu20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in daegu20.find({"indsLclsCd": "R"}):
        print(rCnt, "daegu20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in daegu20.find({"indsLclsCd": "D"}):
        print(dCnt, "daegu20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in daegu20.find({"indsLclsCd": "N"}):
        print(nCnt, "daegu20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in daegu20.find({"indsLclsCd": "S"}):
        print(sCnt, "daegu20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in daegu20.find({"indsLclsCd": "F"}):
        print(fCnt, "daegu20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in daegu20.find({"indsLclsCd": "O"}):
        print(oCnt, "daegu20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in daegu20.find({"indsLclsCd": "L"}):
        print(lCnt, "daegu20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def daejeonDB():
    daejeon20 = db['daejeon']

    daejeonCnt = daejeon20.count_documents({})

    print(daejeonCnt)

    qCnt = 1
    for store in daejeon20.find({"indsLclsCd": "Q"}):
        print(qCnt, "daejeon20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in daejeon20.find({"indsLclsCd": "P"}):
        print(pCnt, "daejeon20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in daejeon20.find({"indsLclsCd": "R"}):
        print(rCnt, "daejeon20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in daejeon20.find({"indsLclsCd": "D"}):
        print(dCnt, "daejeon20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in daejeon20.find({"indsLclsCd": "N"}):
        print(nCnt, "daejeon20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in daejeon20.find({"indsLclsCd": "S"}):
        print(sCnt, "daejeon20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in daejeon20.find({"indsLclsCd": "F"}):
        print(fCnt, "daejeon20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in daejeon20.find({"indsLclsCd": "O"}):
        print(oCnt, "daejeon20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in daejeon20.find({"indsLclsCd": "L"}):
        print(lCnt, "daejeon20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def gangwondoDB():
    gangwondo20 = db['gangwondo']

    gangwondoCnt = gangwondo20.count_documents({})

    print(gangwondoCnt)

    qCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "gangwondo20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "P"}):
        print(pCnt, "gangwondo20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "R"}):
        print(rCnt, "gangwondo20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "D"}):
        print(dCnt, "gangwondo20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "N"}):
        print(nCnt, "gangwondo20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "S"}):
        print(sCnt, "gangwondo20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "F"}):
        print(fCnt, "gangwondo20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "O"}):
        print(oCnt, "gangwondo20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in gangwondo20.find({"indsLclsCd": "L"}):
        print(lCnt, "gangwondo20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def gwangjuDB():
    gwangju20 = db['gwangju']

    gwangjuCnt = gwangju20.count_documents({})

    print(gwangjuCnt)

    qCnt = 1
    for store in gwangju20.find({"indsLclsCd": "Q"}):
        print(qCnt, "gwangju20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in gwangju20.find({"indsLclsCd": "P"}):
        print(pCnt, "gwangju20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in gwangju20.find({"indsLclsCd": "R"}):
        print(rCnt, "gwangju20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in gwangju20.find({"indsLclsCd": "D"}):
        print(dCnt, "gwangju20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in gwangju20.find({"indsLclsCd": "N"}):
        print(nCnt, "gwangju20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in gwangju20.find({"indsLclsCd": "S"}):
        print(sCnt, "gwangju20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in gwangju20.find({"indsLclsCd": "F"}):
        print(fCnt, "gwangju20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in gwangju20.find({"indsLclsCd": "O"}):
        print(oCnt, "gwangju20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in gwangju20.find({"indsLclsCd": "L"}):
        print(lCnt, "gwangju20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def gyeonggidoDB():
    gyeonggido20 = db['gyeonggido']

    qCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "Q"}):
        print(qCnt, "gyeonggido20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "P"}):
        print(pCnt, "gyeonggido20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "R"}):
        print(rCnt, "gyeonggido20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "D"}):
        print(dCnt, "gyeonggido20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "N"}):
        print(nCnt, "gyeonggido20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "S"}):
        print(sCnt, "gyeonggido20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "F"}):
        print(fCnt, "gyeonggido20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "O"}):
        print(oCnt, "gyeonggido20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in gyeonggido20.find({"indsLclsCd": "L"}):
        print(lCnt, "gyeonggido20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def gyeongsangbukdoDB():
    gyeongsangbukdo20 = db['gyeongsangbukdo']

    qCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "gyeongsangbukdo20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "P"}):
        print(pCnt, "gyeongsangbukdo20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "R"}):
        print(rCnt, "gyeongsangbukdo20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "D"}):
        print(dCnt, "gyeongsangbukdo20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "N"}):
        print(nCnt, "gyeongsangbukdo20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "S"}):
        print(sCnt, "gyeongsangbukdo20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "F"}):
        print(fCnt, "gyeongsangbukdo20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "O"}):
        print(oCnt, "gyeongsangbukdo20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in gyeongsangbukdo20.find({"indsLclsCd": "L"}):
        print(lCnt, "gyeongsangbukdo20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def gyeongsangnamdoDB():
    gyeongsangnamdo20 = db['gyeongsangnamdo']

    qCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "gyeongsangnamdo20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "P"}):
        print(pCnt, "gyeongsangnamdo20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "R"}):
        print(rCnt, "gyeongsangnamdo20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "D"}):
        print(dCnt, "gyeongsangnamdo20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "N"}):
        print(nCnt, "gyeongsangnamdo20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "S"}):
        print(sCnt, "gyeongsangnamdo20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "F"}):
        print(fCnt, "gyeongsangnamdo20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "O"}):
        print(oCnt, "gyeongsangnamdo20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in gyeongsangnamdo20.find({"indsLclsCd": "L"}):
        print(lCnt, "gyeongsangnamdo20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def incheonDB():
    incheon20 = db['incheon']

    qCnt = 1
    for store in incheon20.find({"indsLclsCd": "Q"}):
        print(qCnt, "incheon20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in incheon20.find({"indsLclsCd": "P"}):
        print(pCnt, "incheon20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in incheon20.find({"indsLclsCd": "R"}):
        print(rCnt, "incheon20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in incheon20.find({"indsLclsCd": "D"}):
        print(dCnt, "incheon20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in incheon20.find({"indsLclsCd": "N"}):
        print(nCnt, "incheon20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in incheon20.find({"indsLclsCd": "S"}):
        print(sCnt, "incheon20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in incheon20.find({"indsLclsCd": "F"}):
        print(fCnt, "incheon20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in incheon20.find({"indsLclsCd": "O"}):
        print(oCnt, "incheon20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in incheon20.find({"indsLclsCd": "L"}):
        print(lCnt, "incheon20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def jeolabukdoDB():
    jeolabukdo20 = db['jeolabukdo']

    qCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "jeolabukdo20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "P"}):
        print(pCnt, "jeolabukdo20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "R"}):
        print(rCnt, "jeolabukdo20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "D"}):
        print(dCnt, "jeolabukdo20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "N"}):
        print(nCnt, "jeolabukdo20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "S"}):
        print(sCnt, "jeolabukdo20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "F"}):
        print(fCnt, "jeolabukdo20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "O"}):
        print(oCnt, "jeolabukdo20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in jeolabukdo20.find({"indsLclsCd": "L"}):
        print(lCnt, "jeolabukdo20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def jeolanamdoDB():
    jeolanamdo20 = db['jeolanamdo']

    qCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "Q"}):
        print(qCnt, "jeolanamdo20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "P"}):
        print(pCnt, "jeolanamdo20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "R"}):
        print(rCnt, "jeolanamdo20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "D"}):
        print(dCnt, "jeolanamdo20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "N"}):
        print(nCnt, "jeolanamdo20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "S"}):
        print(sCnt, "jeolanamdo20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "F"}):
        print(fCnt, "jeolanamdo20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "O"}):
        print(oCnt, "jeolanamdo20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in jeolanamdo20.find({"indsLclsCd": "L"}):
        print(lCnt, "jeolanamdo20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def sejongDB():
    sejong20 = db['sejong']

    qCnt = 1
    for store in sejong20.find({"indsLclsCd": "Q"}):
        print(qCnt, "sejong20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in sejong20.find({"indsLclsCd": "P"}):
        print(pCnt, "sejong20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in sejong20.find({"indsLclsCd": "R"}):
        print(rCnt, "sejong20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in sejong20.find({"indsLclsCd": "D"}):
        print(dCnt, "sejong20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in sejong20.find({"indsLclsCd": "N"}):
        print(nCnt, "sejong20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in sejong20.find({"indsLclsCd": "S"}):
        print(sCnt, "sejong20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in sejong20.find({"indsLclsCd": "F"}):
        print(fCnt, "sejong20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in sejong20.find({"indsLclsCd": "O"}):
        print(oCnt, "sejong20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in sejong20.find({"indsLclsCd": "L"}):
        print(lCnt, "sejong20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

def ulsanDB():
    ulsan20 = db['ulsan']

    qCnt = 1
    for store in ulsan20.find({"indsLclsCd": "Q"}):
        print(qCnt, "ulsan20", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in ulsan20.find({"indsLclsCd": "P"}):
        print(pCnt, "ulsan20", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in ulsan20.find({"indsLclsCd": "R"}):
        print(rCnt, "ulsan20", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in ulsan20.find({"indsLclsCd": "D"}):
        print(dCnt, "ulsan20", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in ulsan20.find({"indsLclsCd": "N"}):
        print(nCnt, "ulsan20", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in ulsan20.find({"indsLclsCd": "S"}):
        print(sCnt, "ulsan20", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in ulsan20.find({"indsLclsCd": "F"}):
        print(fCnt, "ulsan20", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in ulsan20.find({"indsLclsCd": "O"}):
        print(oCnt, "ulsan20", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in ulsan20.find({"indsLclsCd": "L"}):
        print(lCnt, "ulsan20", store)
        insertData = Ll.insert_one(store)
        lCnt += 1


if __name__ == "__main__":
    p1 = Process(target=seoulDB)
    p2 = Process(target=busanDB)
    p3 = Process(target=chungcheongbukdoDB)
    p4 = Process(target=chungcheongnamdoDB)
    p5 = Process(target=daeguDB)
    p6 = Process(target=daejeonDB)
    p7 = Process(target=gangwondoDB)
    p8 = Process(target=gwangjuDB)
    p9 = Process(target=gyeonggidoDB)
    p10 = Process(target=gyeongsangbukdoDB)
    p11 = Process(target=gyeongsangnamdoDB)
    p12 = Process(target=incheonDB)
    p13 = Process(target=jeolabukdoDB)
    p14 = Process(target=jeolanamdoDB)
    p15 = Process(target=sejongDB)
    p16 = Process(target=ulsanDB)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
