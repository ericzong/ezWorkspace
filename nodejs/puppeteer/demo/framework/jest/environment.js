const PuppeteerEnvironment = require('jest-environment-puppeteer');
// import PuppeteerEnvironment from "jest-environment-puppeteer";

class CustomEnvironment extends PuppeteerEnvironment {
  async setup() {
    await super.setup()
    // Your setup
    this.global.page.setViewport({ width: 1920, height: 1080 })
  }

  async teardown() {
    // Your teardown
    await super.teardown()
  }
}

module.exports = CustomEnvironment
// export default CustomEnvironment
