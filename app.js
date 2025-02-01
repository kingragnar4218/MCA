const express = require('express');
const mongoose = require('mongoose');

const userRouter = require('./Router/router');

const app = express();
const PORT = 3000;

app.use(express.json());

mongoose
    .connect('mongodb://127.0.0.1/demo')
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('connection is failed:', err));
   
app.use('/api/users', userRouter);

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
