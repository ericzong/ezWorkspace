module.exports = {
    launch: {
        dumpio: true,
        ignoreHTTPErrors: true,
        headless: process.env.headless || false,
        timeout: 300000, // 5min
        slowMo: process.env.headless ? 0 : 300, 
        args: [
            '--start-maximized'
        ]
    }
}