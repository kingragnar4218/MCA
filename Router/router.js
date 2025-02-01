
const express = require('express');
const router = express.Router();
const { addUser  , alluser  , getUserById , deleteUser } = require('../Controller/user_controller')

router.post('/create', addUser);

router.get('/all' , alluser );

router.get('/:id', getUserById);


router.delete('/delete/:id', deleteUser);

module.exports = router;