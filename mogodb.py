import pandas as pd
import numpy as pd
from pymongo import MongoClient
import model 


def connect_mongodb_mahcine_collection(url, machine, machineId, what=None):
    '''
    MongoDB machine collection에 연결하는 함수
    input
        machine = collection 이름 ('compressor' or 'rectifier'), dtype = str
        machine_id = machine_id : compressorId, rectifierId, dtype = int
    output : collection에 연결된 객체
    what : anomaly or regression
    '''
    # Client 연결 --> DB 연결 --> compressor collection 연결
    mongo_client = MongoClient(url)
    nipadb = mongo_client['NIPAcopy']
    
    # machine = "compressor364", "rectifier365"
    if what == None :
        machine = machine+str(machineId)
        collection = nipadb[machine]
        return collection
    else :
        machine = machine+str(machineId)+"_"+what
        collection = nipadb[machine]
        return collection

def input_data_to_collection(collection, data):
    '''
    연결된 collection에 데이터를 input하는 함수
    collection : collection에 연결된 객체
    data : json type, 10분 단위 데이터의 결과 저장.
    [{'edgeId':'2', 'compressorId':'364', 'anomaly_score':0.34, 'anomaly':0}, 
            {'edgeId':'2', 'compressorId':'365', 'anomaly_score':7.66, 'anomaly':1}]
    '''
    collection.insert_many(data)
    print(f'{collection.name} Data가 입력 되었습니다.')


if __name__ == '__main__' :
    
    
    NIPA_copy_url = 'mongodb+srv://admin:WkxsEv7zubZ66grH@nipacopy.5yjg7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    rect_regression_collection = connect_mongodb_mahcine_collection(NIPA_copy_url, 'rectifier', 1, 'regression')
    data_rect_reg = model.result_rect(model.data_rect_regression)
    input_data_to_collection(rect_regression_collection, data_rect_reg)
