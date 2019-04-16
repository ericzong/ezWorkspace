
let testFunction = function() {
	console.log('test...');
}

let timer = setInterval(testFunction, 3000);
let timer2 = setInterval(testFunction, 3000);
timer.unref();
timer2.unref();
//timer.ref();