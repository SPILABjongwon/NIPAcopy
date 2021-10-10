const router = require('express').Router();
const { Router } = require('express');
const rectifierAPI = require('../src/models/rectifier');  // Rectifier sample data
const mongoose = require('mongoose');

// 라우터 존은 간단하게 설정
/*
  GET: get All Data
*/
router.get('/:rectId', rectifierAPI.getRectifierByTime); 

module.exports = router;