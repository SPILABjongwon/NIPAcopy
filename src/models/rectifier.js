// compressor 데이터에 대한 정보 및 Shcema 설정
const mongoose = require('mongoose');
mongoose.set('debug', true)

// Schema 정보 입력
const rectSchema = new mongoose.Schema({
    _id : {type : Object},
    rectifierId : {type : String},
    time : {type : Number},
    anomaly_score : {type : Number},
    anomaly : {type : Number}
  }
);

const rectIdList = ['364', '365', '366']

let rectifier = {}

rectIdList.forEach((id)=>{
  let model = mongoose.model(`rectifier${id}`, rectSchema, `rectifier${id}`)
  rectifier[`rectifier${id}`] = model;
})

function getRectifierModel(rectId){
  return rectifier[`rectifier${rectId}`]
}

exports.getRectifierByTime = (req,res) =>{
  const {rectId} = req.params;
  const startTime = req.query.startTime;
  const endTime = req.query.endTime;

  var Rectifier = getRectifierModel(rectId)
  Rectifier
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
