"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.testSuite = exports.testCase = undefined;

var _timer = require("../time/timer");

var _timer2 = _interopRequireDefault(_timer);

var _container = require("../io/container");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

const testCase = exports.testCase = async (comment, fn, delayTime = 100) => test(comment, async () => {
    await fn(_container.container.cradle);
    await (0, _timer.delay)(delayTime);
}, _timer2.default.tenMin);

const testSuite = exports.testSuite = (suiteName, fn) => describe(suiteName, () => {
    fn(_container.container.cradle);
    return;
});
//# sourceMappingURL=testAssets.js.map