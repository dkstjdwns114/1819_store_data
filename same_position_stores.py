from pymongo import MongoClient
from multiprocessing import Process

client = MongoClient('localhost', 27017)

prev_data = client['threestep']
next_data = client['current_three_step']

same_coordinates = client['same_coordinates2222']


def seoul_compare():
    prev_stores = prev_data['seoul']
    next_stores = next_data['seoul']

    same = same_coordinates['seoul']

    prev_seoul_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_seoul_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Seoul total :", total_cnt)


def busan_compare():
    prev_stores = prev_data['busan']
    next_stores = next_data['busan']

    same = same_coordinates['busan']

    prev_busan_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_busan_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Busan total :", total_cnt)


def chungcheongbukdo_compare():
    prev_stores = prev_data['chungcheongbukdo']
    next_stores = next_data['chungcheongbukdo']

    same = same_coordinates['chungcheongbukdo']

    prev_chungcheongbukdo_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_chungcheongbukdo_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Chungcheongbukdo total :", total_cnt)


def chungcheongnamdo_compare():
    prev_stores = prev_data['chungcheongnamdo']
    next_stores = next_data['chungcheongnamdo']

    same = same_coordinates['chungcheongnamdo']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Chungcheongnamdo total :", total_cnt)


def daegu_compare():
    prev_stores = prev_data['daegu']
    next_stores = next_data['daegu']

    same = same_coordinates['daegu']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id


def daejeon_compare():
    prev_stores = prev_data['daejeon']
    next_stores = next_data['daejeon']

    same = same_coordinates['daejeon']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Daejeon total :", total_cnt)


def gangwondo_compare():
    prev_stores = prev_data['gangwondo']
    next_stores = next_data['gangwondo']

    same = same_coordinates['gangwondo']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Gangwondo total :", total_cnt)


def gwangju_compare():
    prev_stores = prev_data['gwangju']
    next_stores = next_data['gwangju']

    same = same_coordinates['gwangju']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Gwangju total :", total_cnt)


def gyeonggido_compare():
    prev_stores = prev_data['gyeonggido']
    next_stores = next_data['gyeonggido']

    same = same_coordinates['gyeonggido']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Gyeonggido total :", total_cnt)


def gyeongsangbukdo_compare():
    prev_stores = prev_data['gyeongsangbukdo']
    next_stores = next_data['gyeongsangbukdo']

    same = same_coordinates['gyeongsangbukdo']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Gyeongsangbukdo total :", total_cnt)


def gyeongsangnamdo_compare():
    prev_stores = prev_data['gyeongsangnamdo']
    next_stores = next_data['gyeongsangnamdo']

    same = same_coordinates['gyeongsangnamdo']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Gyeongsangnamdo total :", total_cnt)


def incheon_compare():
    prev_stores = prev_data['incheon']
    next_stores = next_data['incheon']

    same = same_coordinates['incheon']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Incheon total :", total_cnt)


def jeollabukdo_compare():
    prev_stores = prev_data['jeollabukdo']
    next_stores = next_data['jeollabukdo']

    same = same_coordinates['jeollabukdo']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Jeolabukdo total :", total_cnt)


def jeollanamdo_compare():
    prev_stores = prev_data['jeollanamdo']
    next_stores = next_data['jeollanamdo']

    same = same_coordinates['jeollanamdo']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Jeolanamdo total :", total_cnt)


def sejong_compare():
    prev_stores = prev_data['sejong']
    next_stores = next_data['sejong']

    same = same_coordinates['sejong']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Sejong total :", total_cnt)


def ulsan_compare():
    prev_stores = prev_data['ulsan']
    next_stores = next_data['ulsan']

    same = same_coordinates['ulsan']

    prev_stores_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_stores_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon': store['lon']}, {'lat': store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Ulsan total :", total_cnt)


def jeju_compare():
    prev_stores = prev_data['jeju']
    next_stores = next_data['jeju']

    same = same_coordinates['jeju']

    prev_seoul_cnt = prev_stores.count_documents({})

    total_cnt = 0
    prev_cnt = 1
    for store in prev_stores.find({}):
        next_store_list = []
        rdnmAdr = ""
        lon = ""
        lat = ""
        is_exist = False

        print(prev_cnt, "/", prev_seoul_cnt)
        prev_cnt += 1

        next_cnt = 1
        for exist_store in next_stores.find({'$and': [{'lon':store['lon']}, {'lat':store['lat']}]}):
            is_exist = True
            print(next_cnt, exist_store)

            rdnmAdr = exist_store['rdnmAdr']
            ctprvnCd = exist_store['ctprvnCd']
            signguCd = exist_store['signguCd']
            ctprvnNm = exist_store['ctprvnNm']
            signguNm = exist_store['signguNm']
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "ctprvnCd": ctprvnCd,
                "signguCd": signguCd,
                "ctprvnNm": ctprvnNm,
                "signguNm": signguNm,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Jeju total :", total_cnt)


if __name__ == "__main__":
    p1 = Process(target=seoul_compare)
    p2 = Process(target=busan_compare)
    p3 = Process(target=chungcheongbukdo_compare)
    p4 = Process(target=chungcheongnamdo_compare)
    p5 = Process(target=daegu_compare)
    p6 = Process(target=daejeon_compare)
    p7 = Process(target=gangwondo_compare)
    p8 = Process(target=gwangju_compare)
    p9 = Process(target=gyeonggido_compare)
    p10 = Process(target=gyeongsangbukdo_compare)
    p11 = Process(target=gyeongsangnamdo_compare)
    p12 = Process(target=incheon_compare)
    p13 = Process(target=jeollabukdo_compare)
    p14 = Process(target=jeollanamdo_compare)
    p15 = Process(target=sejong_compare)
    p16 = Process(target=ulsan_compare)
    p17 = Process(target=jeju_compare)

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
    p17.start()

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
    p17.join()

