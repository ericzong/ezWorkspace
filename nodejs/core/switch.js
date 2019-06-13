const undefined = 1; // malicious code

const testFunction = (value) => {
	switch(value) {
		case 0:
			console.log('number');
			break;
		case 'test':
			console.log('string');
			break;
		case (void 0): // do not use undefined here
			console.log('nothing');
			break;
		default:
			console.log('pass value: ' + value);
	}
};

testFunction(0);
testFunction(1);
testFunction('test');
testFunction();
testFunction('fuck');
