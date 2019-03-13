console.log('jestes w js')
var temp1 = document.getElementById('temp1');

function read_data() {
	var my_read = new XMLHttpRequest();
	my_read.open('GET', '/back');	
	console.log('cokolwiek!!');	
	my_read.onload = function() {  // onload wczytuje dane zamieszzone w funkcji anonimowej pradopodobnie domyslnie jest null
		console.log(my_read.responseText);
		var json_data = JSON.parse(my_read.responseText);
		console.log(json_data);
		unzip(json_data);

	// 	temp1.innerHTML = json_data['temp'] + ' ' + 'stopni' + ' '+ 'wilgotność'+ ' ' + json_data['humanidity'] + '%';
	};
	my_read.send();
	// setTimeout('read_data()', 5000); // pierwszy arg to wywoływana funkcja, zas drugi to czas odswierzania podanu w ms
}

var readed = read_data();
console.log(readed);

function unzip(data){
	for (var i in data) {
		console.log(i + ' temp: ' + data[i]['temp'] + ' wilgotność ' + data[i]['humanidity']);
	};
};

