const User = require('../Models/user_module');


const addUser = async (req, res) => {
    const data = req.body;
    try {
        const user = new User(data);
        const savedUser = await user.save();
        res.status(200).json(savedUser);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
}


const alluser = async (req, res) => {
    try {
        const user = await User.find();
        res.status(200).json(user);	
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
}


// id 


const getUserById = async (req, res) => {
    const { id } = req.params;
    try {
        const user = await User.findById(id);
        res.status(200).json(user);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
}

// delete 

const deleteUser = async (req, res) => {
    const { id } = req.params;
    try {
        const deletedUser = await User.findByIdAndDelete(id);
        res.status(200).json(deletedUser);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
}

module.exports = { addUser  , alluser  , getUserById , deleteUser}