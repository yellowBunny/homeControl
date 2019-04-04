console.log('in socket_logic1')
window.onload = init;

function init() {
	var btn = document.getElementById('saveBTN');
	btn.onclick = get_data;
}

function get_data(event) {
	console.log('button was cliked');
	var selector = document.getElementById('selector');
	var value = selector.value;
	console.log(value);
	swip_data(value);
}

function swip_data(argument) {
	var show_hour = document.getElementById('hour');
	var show_minute = document.getElementById('minute');
	show_hour.innerHTML = argument;
	show_minute.innerHTML = 'default';
	run_python()
}

function run_python(){
    var read = new XMLHttpRequest();
    read.open('GET', '/sendtopython');
    read.send();
    read.onload = function(){console.log('odpowidz z pythona', read.responseText)}

}

