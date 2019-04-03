export const launch = {
    dumpio: true,
    ignoreHTTPErrors: true,
    headless: process.env.headless || false,
    timeout: 300000,
    slowMo: process.env.headless ? 0 : 300,
    args: [
        '--start-maximized'
    ]
};