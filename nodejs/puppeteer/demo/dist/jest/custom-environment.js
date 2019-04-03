"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _jestEnvironmentPuppeteer = require("jest-environment-puppeteer");

var _jestEnvironmentPuppeteer2 = _interopRequireDefault(_jestEnvironmentPuppeteer);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

class CustomEnvironment extends _jestEnvironmentPuppeteer2.default {
  async setup() {
    await super.setup();
    // Your setup
    this.global.page.setViewport({ width: 1920, height: 1080 });
  }

  async teardown() {
    // Your teardown
    await super.teardown();
  }
}

// module.exports = CustomEnvironment
// const PuppeteerEnvironment = require('jest-environment-puppeteer');
// import PuppeteerEnvironment from "jest-environment-puppeteer";
exports.default = CustomEnvironment;
//# sourceMappingURL=custom-environment.js.map