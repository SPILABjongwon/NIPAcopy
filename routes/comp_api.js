const router = require('express').Router();
const { Router } = require('express');
const compressorAPI = require('../src/models/compressor');  // Rectifier sample data
const mongoose = require('mongoose');

// 라우터 존은 간단하게 설정
/*
  GET: get All Data
*/
router.get('/:compId', compressorAPI.getCompressorByTime);

//router.get('/:compId/:anomaly', compressorAPI.getCompressorByAnomaly);
module.exports = router;