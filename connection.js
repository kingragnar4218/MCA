const express = require('express')
const mongoose = require('mongoose')
const app=express()

try {
    mongoose.connect("mongodb://127.0.0.1/RAVI");
    console.log("Conncted...");
} catch (error) {
    console.error("Connection Failed : ",err);
}

app.listen(3000,()=>{console.log("server Start")})

const userschme = new mongoose.Schema({
    name:{type:String,require:true},
    age:{type:Number,require:true},
    email:{type:String,require:true,unique:true},
    createdAt:{type:Date,default:Date.now}
});

module.exports=mongoose.model('user',userschme);