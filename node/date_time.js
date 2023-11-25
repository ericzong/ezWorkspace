function getTime(secondOffset) {
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false,
    };
	const dd = new Date();
    if(!secondOffset) secondOffset = 0;
	const time = (Math.floor(dd.getTime() / 1000) + secondOffset) * 1000;
	console.log(time);
	dd.setTime(time);
	
	const timeString = dd.toLocaleString('zh-CN', options)
		.replace(/\//g, '-') // 将斜杠替换为短横线
		.replace('T', ' ')
		.substring(0, 16);
	
	return timeString;
}

function getDate(dayOffset) {
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false,
    };
	const theDay = new Date();
    if(!dayOffset) dayOffset = 1;
	theDay.setDate(theDay.getDate() + dayOffset);
	
	const dayString = theDay.toLocaleString('zh-CN', options)
		.replace(/\//g, '-') // 将斜杠替换为短横线
		.substring(0, 10);
	
	return dayString;
}

console.log('1h后：', getTime(3600))
console.log('3d后：', getDate(3))
