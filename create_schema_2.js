const express = require('express')
const mongoose = require('mongoose')
const app=express()

try {
    mongoose.connect("mongodb://127.0.0.1/RAVI");
    console.log("Conncted...");
} catch (error) {
    console.error("Connection Failed : ",err);
}

const userschme = new mongoose.Schema({
    Name:{type:String,require:true},
    Salary:{type:Number,require},
    City:{type:String,require:true},
    Age:{type:Date,require:true}
});

module.exports=mongoose.model('faculty',userschme);

app.listen(3000,()=>{console.log("server Start")})