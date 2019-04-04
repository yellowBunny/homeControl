console.log('jestes w js')
var sensor_list = [document.getElementById('salon'), 
					document.getElementById('p1'),
					document.getElementById('p2'),
					document.getElementById('kitchen'),
					document.getElementById('bathroom')];

function read_data() {
	var my_read = new XMLHttpRequest();
	my_read.open('GET', '/back');		
	my_read.onload = function() {  // onload wczytuje dane zamieszzone w funkcji anonimowej pradopodobnie domyslnie jest null
		console.log(my_read.responseText);
		var json_data = JSON.parse(my_read.responseText);
		console.log(json_data);
		unzip(json_data, sensor_list);
	};
	my_read.send();
	update_data();
	sys_ver();
	setTimeout(read_data, 30000); // pierwszy arg to wywoływana funkcja, zas drugi to czas odswierzania podanu w ms
}

function unzip(data, sensor_list){
	for (var i in data) {
		var celcius_sing = String.fromCharCode(176) + 'C';
		console.log(i + ' temp: ' + data[i]['temp'] + ' wilgotność ' + data[i]['humanidity']);
		if (data[i]['temp'] > 30){ //we set here font color if temp will be grater then 30. This colors are configure in css files.
			sensor_list[i].setAttribute('class', 'warning');
			// console.log('temp czyjnika puwyzej 30C', data[i])

		}else{ //otherwise color will be in normal color. This colors are configure in css files.
			sensor_list[i].setAttribute('class', 'normal');
		}

		sensor_list[i].innerHTML = data[i]['temp']+ celcius_sing +' '+ data[i]['humanidity'] + '%';

	};
};
function update_data(){
    console.log('in  update_data')
    var my_read = new XMLHttpRequest();
	my_read.open('GET', '/update');
	my_read.send();
	my_read.onload = function(){console.log('wczytywany plik: ',my_read.responseText)};
}
function sys_ver(){
    var read = new XMLHttpRequest();
    read.open('GET', '/up')
    read.send();
    read.onload = function(){console.log('test_f: sys version: ', read.responseText)};

}

var readed = read_data();
console.log(readed);



