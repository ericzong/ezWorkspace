function unique(array) {
	for(let i = 0; i < array.length; i++) {
		for(let j = i + 1; j < array.length; j++) {
			if(typeof array[i] == typeof array[j] && array[i] == array[j]) {
				array.splice(j, 1);
				j--;
			}
		}
	}
	
	return array;
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));