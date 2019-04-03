"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _jestEnvironmentPuppeteer = require("jest-environment-puppeteer");

var _expectPuppeteer = require("expect-puppeteer");

var _timer = require("../time/timer");

var _timer2 = _interopRequireDefault(_timer);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = async function globalSetup(globalConfig) {
  await (0, _jestEnvironmentPuppeteer.setup)(globalConfig);
  // Your global setup
  (0, _expectPuppeteer.setDefaultOptions)({ timeout: _timer2.default.tenSecond, visible: true });
}; // const { setup: setupPuppeteer } = require('jest-environment-puppeteer')
//# sourceMappingURL=global-setup.js.map