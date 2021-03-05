from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['current_three_step']

Qq = db['Q']
Pp = db['P']
Rr = db['R']
Dd = db['D']
Nn = db['N']
Ss = db['S']
Ff = db['F']
Oo = db['O']
Ll = db['L']

def jejuDB():
    jeju20 = db['jeju']

    jejuCnt = jeju20.count_documents({})

    print(jejuCnt)

    qCnt = 1
    for store in jeju20.find({"indsLclsCd": "Q"}):
        print(qCnt, "jeju", store)
        insertData = Qq.insert_one(store)
        qCnt += 1

    pCnt = 1
    for store in jeju20.find({"indsLclsCd": "P"}):
        print(pCnt, "jeju", store)
        insertData = Pp.insert_one(store)
        pCnt += 1

    rCnt = 1
    for store in jeju20.find({"indsLclsCd": "R"}):
        print(rCnt, "jeju", store)
        insertData = Rr.insert_one(store)
        rCnt += 1

    dCnt = 1
    for store in jeju20.find({"indsLclsCd": "D"}):
        print(dCnt, "jeju", store)
        insertData = Dd.insert_one(store)
        dCnt += 1

    nCnt = 1
    for store in jeju20.find({"indsLclsCd": "N"}):
        print(nCnt, "jeju", store)
        insertData = Nn.insert_one(store)
        nCnt += 1

    sCnt = 1
    for store in jeju20.find({"indsLclsCd": "S"}):
        print(sCnt, "jeju", store)
        insertData = Ss.insert_one(store)
        sCnt += 1

    fCnt = 1
    for store in jeju20.find({"indsLclsCd": "F"}):
        print(fCnt, "jeju", store)
        insertData = Ff.insert_one(store)
        fCnt += 1

    oCnt = 1
    for store in jeju20.find({"indsLclsCd": "O"}):
        print(oCnt, "jeju", store)
        insertData = Oo.insert_one(store)
        oCnt += 1

    lCnt = 1
    for store in jeju20.find({"indsLclsCd": "L"}):
        print(lCnt, "jeju", store)
        insertData = Ll.insert_one(store)
        lCnt += 1

jejuDB()