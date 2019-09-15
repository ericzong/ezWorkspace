function unique(array) {
	return array.filter((item, index, array) => {
		return array.indexOf(item, 0) === index;
	});
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));