// compressor 데이터에 대한 정보 및 Shcema 설정
const mongoose = require('mongoose');
// mongoose.set('debug', true)

// Schema 정보 입력
const compSchema = new mongoose.Schema({
    _id :{type : Object},
    compressorId : {type : String},
    time : {type : Number},
    anomaly_score : {type : Number},
    anomaly : {type : Number}
    }
);

const compIdList = ['364','365','366']

let compressor = {}

compIdList.forEach((id)=>{
  let model = mongoose.model(`compressor${id}`, compSchema, `compressor${id}`);
  compressor[`compressor${id}`] = model;
})

function getCompressorModel(compId){
    return compressor[`compressor${compId}`]
}


exports.getCompressorByTime = (req,res) =>{
    const {compId} = req.params;
    const startTime = req.query.startTime;
    const endTime = req.query.endTime;

    var Compressor = getCompressorModel(compId)
    Compressor
        .find()
        .where('time')
        .gte(startTime)
        .lte(endTime)
        .then((datas)=>{
            console.log(datas.length)
            if (!datas.length){
                return res.status(404).send({ err: 'Data not found' });
            }else {
                return res.status(200).json(datas);
            }
        })
        .catch(e => res.status(500).send(e));
}

//exports.getCompressorByAnomaly = (req, res) => {
//    const {compId} = req.params;
//    const {anomaly} = req.params;
//   var Compressor = getCompressorModel(compId)
    
//    Compressor
//    .find()
//    .where('anomaly')
//    .equals(anomaly)
//    .then((datas)=>{
//        console.log(datas.length)
//        if (!datas.length){
//            return res.status(404).send({ err: 'Data not found' });
//        }else {
//            return res.status(200).json(datas);
//        }
//    })
//    .catch(e => res.status(500).send(e));
//}