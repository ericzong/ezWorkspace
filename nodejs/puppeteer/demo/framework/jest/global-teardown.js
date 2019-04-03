import { teardown as teardownPuppeteer } from 'jest-environment-puppeteer';

export default async function globalTeardown(globalConfig) {
  // Your global teardown
  await teardownPuppeteer(globalConfig)
}
