
//const express = require('express')
const mongoose = require('mongoose')
//const app=express()

// try {
//     mongoose.connect("mongodb://127.0.0.1/RAVI");
//     console.log("Conncted...");
// } catch (error) {
//     console.error("Connection Failed : ",err);
// }

const userschme = new mongoose.Schema({
    Name:{type:String},
    Salary:{type:Number},
    City:{type:String},
    Age:{type:Number}
});

module.exports=mongoose.model('faculty',userschme);

//app.listen(3000,()=>{console.log("server Start")})