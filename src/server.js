const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const mongoose = require('mongoose')
/*
  body-parser
  : 요청의 본문을 해석해주는 미들웨어이다.
    보통 폼 데이터나 AJAX요청의 데이터를 처리한다
*/
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

/*
  그런데 이전에 express미들웨어에서의 app.js에서는 body-parser를 사용하지 않았다.
  익스프레스 4.16.0버전 부터 body-parser의 일부 기능이 익스프레스에 내장되었기 때문이다.
*/
app.use(express.urlencoded({ extended: true }))   ;
app.use(express.json());

/*
  Raw는 본문이 버퍼 데이터일 때, Text는 본문이 텍스트 데이터일 때  해석하는 미들웨어이다.
  서비스에 적용하고 싶다면 body-parser를 설치한 후 다음과 같이 추가한다.
*/
app.use(bodyParser.text());

// Web Server's PORT Number
const PORT = 3000;


// env 환경변수 안에 DEV_MONGO_URI 넣음
const { DEV_MONGO_URI } = process.env;  

// 환경변수에 DEV_MONGO_URI가 있음을 명시
if (!DEV_MONGO_URI) console.error("DEV_MONGO_URI is required!!!")
// console.log(DEV_MONGO_URI)


// 비동기 처리 : 몽고디비 연결 후 서버 접속
const server = async() => {
  // CONNECT to MongoDB
  let mongodbConnection = await mongoose.connect(DEV_MONGO_URI,{useNewUrlParser: true, useUnifiedTopology: true})
  console.log({mongodbConnection})    

  // ROUTERS
  app.use('/data/ai/rect', require('../routes/rect_api'));
  app.use('/data/ai/comp', require('../routes/comp_api'));

  // Web server listening on port
  app.listen(PORT, () => console.log(`Server lisetening on port ${PORT}`));   

}
server();

