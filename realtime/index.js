
const WebSocket = require('ws');


const binanceSocketUrl = 'wss://stream.binance.com:9443/ws/btcusdt@trade';


let socket;


function connect() {
        socket = new WebSocket(binanceSocketUrl);
        socket.on('open', () => {
                console.log('Connected to Binance WebSocket');
        });
        socket.on('message',(data)=> {
                const message = JSON.parse(data);
                const price = parseFloat(message.p).toFixed(2);
                console.log(`BTC/USDT Price: $${price}`);
                checkWatchlist(price);
        });
        socket.on('error',(err)=>{
                console.error('WebSocket error:', err);
                startSimulator();
        })
}

function startSimulator() {
        console.log('Starting price simulator...');
        setInterval(() => {
                const fakePrice = (30000 + Math.random() * 10000).toFixed(2);
                console.log(`Simulated BTC/USDT Price: $${fakePrice}`);
                checkWatchlist(fakePrice);
        },3000)
}

function checkWatchlist(price) {}
connect();