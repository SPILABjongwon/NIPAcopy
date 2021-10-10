import pandas as pd
import numpy as pd
from pymongo import MongoClient
import model 


def connect_mongodb_mahcine_collection(machine):
    '''
    MongoDB machine collection에 연결하는 함수
    input : machine = collection 이름 ('compressor' or 'rectifier'), dtype = str
    output : collection에 연결된 객체
    '''
    # Client 연결 --> DB 연결 --> compressor collection 연결
    mongo_client = MongoClient('mongodb+srv://admin:admin1234@jongwon.rgiku.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    nipadb = mongo_client['NIPA']
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
    comp_collection = connect_mongodb_mahcine_collection('compressor')
    data_comp = model.result_comp()
    input_data_to_collection(comp_collection, data_comp)

    rect_collection = connect_mongodb_mahcine_collection('rectifier')
    data_rect = model.result_rect()
    input_data_to_collection(rect_collection, data_rect)
