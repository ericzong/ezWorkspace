function unique(array) {
    const map = new Map();
    const list = [];
    
    for(let i = 0; i < array.length; i++) {
        if(!map.has(array[i])) {
            map.set(array[i], true);
            list.push(array[i]);
        }
	}
    
    return list;
}

const array = [null, null, undefined, undefined, true, true, 42, 42, 42n, 42n, 'ez', 'ez', Symbol.for('ez'), Symbol.for('ez'), {}, {}];

console.log(unique(array));