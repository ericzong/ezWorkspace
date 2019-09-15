function unique(array) {
	const obj = {};
	array = array.filter((item, index, array) => {
		return obj.hasOwnProperty(typeof item + Object.prototype.toString.call(item)) ? false : (obj[typeof item + Object.prototype.toString.call(item)] = true);
	});
	
	return array;
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));