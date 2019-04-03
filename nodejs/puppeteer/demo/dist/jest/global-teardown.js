'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _jestEnvironmentPuppeteer = require('jest-environment-puppeteer');

exports.default = async function globalTeardown(globalConfig) {
  // Your global teardown
  await (0, _jestEnvironmentPuppeteer.teardown)(globalConfig);
};
//# sourceMappingURL=global-teardown.js.map