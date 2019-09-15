function unique(array) {
	return array.reduce((prev, current) =>
		prev.includes(current) ? prev : [...prev, current],
		[]
	);
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));