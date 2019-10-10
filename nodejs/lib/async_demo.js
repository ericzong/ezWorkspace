async = require("async");
a = function (callback) {
    // 延迟5s模拟耗时操作
    setTimeout(function () {
        console.log("hello world a");
        // 回调给下一个函数
        callback(null, "function a");
    }, 5000);
};

b = function (callback) {
    // 延迟1s模拟耗时操作
    setTimeout(function () {
        console.log("hello world b");
        // 回调给下一个函数
        callback(null, "function b");
    }, 1000);
};

c = function (callback) {
    console.log("hello world c");
    // 回调给下一个函数
    callback(null, "function c");
};

// 根据b, a, c这样的顺序执行
async.series([b, a, c], function (error, result) {
    console.log(result);
});

console.log('done');