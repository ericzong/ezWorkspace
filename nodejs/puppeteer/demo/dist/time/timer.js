"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.default = {
    tenSecond: 10000,
    halfMin: 30000,
    oneMin: 60000,
    fiveMin: 300000,
    tenMin: 600000
};
const delay = exports.delay = timeout => new Promise(resolve => {
    setTimeout(resolve, timeout);
});
//# sourceMappingURL=timer.js.map