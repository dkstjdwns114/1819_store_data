from pymongo import MongoClient

client = MongoClient('localhost', 27017)

prev_data = client['threestep']
next_data = client['current_three_step']

same_coordinates = client['same_coordinates']

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
            lon = exist_store['lon']
            lat = exist_store['lat']

            next_store_list.append(exist_store['_id'])

            next_cnt += 1
            total_cnt += 1

        if is_exist:
            info = {
                "rdmAdr": rdnmAdr,
                "lon": lon,
                "lat": lat,
                "same_locations": next_store_list
            }
            same_id = same.insert_one(info).inserted_id

    print("Jeju total :", total_cnt)


jeju_compare()