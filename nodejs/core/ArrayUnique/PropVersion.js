function unique(array) {
	const obj = {};
	const list = [];
	
	for(let i = 0; i < array.length; i++) {
		if(!obj[typeof array[i] + Object.prototype.toString.call(array[i])]) {
			list.push(array[i]);
			obj[typeof array[i] + Object.prototype.toString.call(array[i])] = true;
		}
	}
	
	return list;
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));