import { setup as setupPuppeteer } from "jest-environment-puppeteer";
import { setDefaultOptions } from "expect-puppeteer";
import time from "../time/timer";

export default async function globalSetup(globalConfig) {
  await setupPuppeteer(globalConfig)
  // Your global setup
  setDefaultOptions({ timeout: time.tenSecond, visible: true })
}
