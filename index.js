const io = require('socket.io')(server);

io.on('connection', (socket) => {
    console.log('user is connected');
    
    socket.on('disconnect', (event) => {
        console.log('user is disconnected');
    })
})