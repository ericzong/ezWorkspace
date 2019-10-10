var moment = require('moment');

//moment.locale('zh-cn');
//var now = moment();
//console.log(now.format('YYYYMMDDHHmmssSSSS'));
//console.log(now.format('DD MMM YYYY'));
moment.locale('zh-hk');

const getDateByNow = (offsetDays, dateFormat = 'YYYY-MM-DD') => {
    return moment().add(offsetDays).format(dateFormat);
};
console.log(getDateByNow(15));
console.log(getDateByNow(-15, 'DD MMM YYYY'));
//console.log(getDateByNow(15, 'YYYYMMDD'));

