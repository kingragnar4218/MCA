const mongoose = require('mongoose');

const userschme = new mongoose.Schema({
    name:{type:String,require:true},
    age:{type:Number,require:true},
    email:{type:String,require:true,unique:true},
    createdAt:{type:Date,default:Date.now}
});

module.exports=mongoose.model('user',userschme);