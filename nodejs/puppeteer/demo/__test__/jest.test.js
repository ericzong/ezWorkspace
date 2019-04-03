import { testCase, testSuite } from "../framework/jest/testAssets";
import { container } from "../framework/io/container";

testSuite('ts test', async () => {

    testCase('tc1 test', async () => {
        await page.goto('https://www.baidu.com/')

        await console.log(container.cradle)
    });

})

// describe('jest-test', () => {
//     beforeAll(() => {
//         console.log('before all')
//     });

//     beforeEach(() => {
//         console.log('before each')
//     });

//     afterAll(() => {
//         console.log('after all')
//     });

//     afterEach(() => {
//         console.log('after each')
//     })

//     test('test1', () => {
//         console.log('test1');
//     });

//     test('test2', () => {
//         console.log('test2');
//     });

//     test('test3', () => {
//         console.log('test3');
//     });
// });