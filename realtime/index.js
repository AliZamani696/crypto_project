
const WebSocket = require('ws');
const redis = require('redis');


const binanceSocketUrl = 'wss://stream.binance.com:9443/ws/btcusdt@trade';
const redisClient = redis.createClient({url:'redis://redis:6379'});






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
                const fakePrice = (90000 + Math.random() * 10000).toFixed(2);
                console.log(`Simulated BTC/USDT Price: $${fakePrice}`);
                checkWatchlist(fakePrice);
        },3000)
}
redisClient.connect().then(() => {
        console.log('Connected to Redis');
}).catch((err) => {
        console.error('Redis connection error:', err);
});
async function checkWatchlist(price) {
        const symbol = 'BTC';
        const list = redisClient.lRange(`watchlist: ${symbol}`, 0, -1);
        (await list).forEach((item)=>{
                const watch = JSON.parse(item);
                if (price >= watch.target_price) {
                        console.log(`ALERT: User ${watch.user_id}, ${symbol} has reached your target price of $${watch.target_price}. Current price: $${price}`);
                }
        })

}
connect();