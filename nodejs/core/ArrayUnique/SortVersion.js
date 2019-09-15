function unique(array) {
	array = array.sort((a, b) => {
		const strA = typeof a + Object.prototype.toString.call(a);
		const strB = typeof b + Object.prototype.toString.call(b);
		if(strA < strB) return -1;
		if(strA > strB) return 1;
		return 0;
	});
	const list = [];
	for(let i = 0; i < array.length; i++) {
		if(array[i] !== array[i-1]) {
			list.push(array[i]);
		}
	}
	
	return list;
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));