// native jest:
// yarn test [file]

describe('Baidu', () => {
    beforeAll(async () => {
        await page.goto('http://www.baidu.com');
    })

    it('baidu', async () => {
        await new Promise(resolve => setTimeout(resolve, 10000));

        await page.screenshot({path: '__test__/demo.png'});
    }, 30000)
})
