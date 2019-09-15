function unique(array) {
	const list = [];
	for(let i = 0; i < array.length; i++) {
		//if(list.indexOf(array[i]) === -1) {
		if(!list.includes(array[i])) {
			list.push(array[i]);
		}
	}
	
	return list;
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));