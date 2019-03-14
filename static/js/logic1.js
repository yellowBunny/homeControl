console.log('jestes w js')
var sensor_list = [document.getElementById('salon'), 
					document.getElementById('p1'),
					document.getElementById('p2'),
					document.getElementById('kitchen'),
					document.getElementById('bathroom')];

function read_data() {
	var my_read = new XMLHttpRequest();
	my_read.open('GET', '/back');		
	my_read.onload = function() {  // onload wczytuje dane zamieszzone w funkcji anonimowej po załadowaniu strony pradopodobnie domyslnie jest null
		console.log(my_read.responseText);
		var json_data = JSON.parse(my_read.responseText);
		console.log(json_data);
		unzip(json_data, sensor_list);

	// 	temp1.innerHTML = json_data['temp'] + ' ' + 'stopni' + ' '+ 'wilgotność'+ ' ' + json_data['humidity'] + '%';
	};
	my_read.send();
	setTimeout('read_data()', 20000); // pierwszy arg to wywoływana funkcja, zas drugi to czas odswierzania podanu w ms
}

var readed = read_data();
console.log(readed);

function unzip(data, sensor_list){
    var ascii = String.fromCharCode(176) + 'C';
	for (var i in data) {
                
		console.log(i + ' temp: ' + data[i]['temp'] + ' wilgotność ' + data[i]['humidity'] + ' ' + '%');
		sensor_list[i].innerHTML = 'temp: ' + data[i]['temp'] + ' '+ ascii +' wilgotność ' + data[i]['humidity'] + ' ' + '%';
	};
};

