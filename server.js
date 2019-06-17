const express = require ('express');
const app = express();
const mariadb = require('mariadb');
const bodyParser = require('body-parser');
const cors = require('cors');

const pool = mariadb.createPool({
	host: '192.168.213.128',
	user: 'devops',
	password: 'bournigal',
	connectionLimit: 5,
	database: 'TPDevOps'
});

var data;

pool.getConnection()
	.then(conn => {
		const now = new Date();
		conn.query(`SELECT * FROM MesuresAutomates WHERE dateMesure < DATE_SUB(NOW(), INTERVAL 1 HOUR) `)
			.then((rows) => {
				data = rows;
				conn.end();
			})
			.catch(err => {
				console.log(err);
			})
	})
	.catch(err => {
		console.log('Not connected')
	})

const hostname = '192.168.213.128';
const port = 4000;

app.use(bodyParser.json());
app.use(cors());

app.get('/', function(req, res){
	res.send('Hello World');
});

app.get('/mesures', function(req, res) {
	res.json(data);
});

let automate = 1;
let unite = 1;

app.get('/mesures/:unite/:automate', function(req, res) {
	const unite = req.params.unite;
	const automate = req.params.automate;
	pool.getConnection().then(conn => {
		conn.query(`SELECT * FROM MesuresAutomates WHERE dateMesure > DATE_SUB(NOW(), INTERVAL 1 HOUR) AND numUnite = ${unite} AND numAutomate = ${automate}`)
			.then((rows) => {
				data = rows;
				conn.end();
				res.json(data)
			}).catch(err => {
				res.send("no")
			})
	})
	.catch(err => console.log(err))
})

const server = app.listen(port, hostname, function(){
	console.log(`Server running at http://${hostname}:${port}/`);
});

const io = require('socket.io')(server);

io.on('connection', function(socket){
	console.log(socket.id);

	socket.on('SEND_MESURE', function(data){
		io.emit('MESURE', data)
	});
});
