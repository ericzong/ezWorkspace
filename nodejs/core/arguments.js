const changeTest = function(one, two) {
	arguments[0] = 'change';
	two = 'me';
	console.log(arguments[0], arguments[1]);
	console.log(one, two);
	console.log(one === arguments[0]);
	console.log(two === arguments[1]);
}

changeTest('hello', 'world');
