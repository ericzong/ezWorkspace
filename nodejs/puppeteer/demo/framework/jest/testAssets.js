import time, {delay} from "../time/timer"
import { container } from "../io/container";

export const testCase = async (comment, fn, delayTime = 100) => test(comment, async () => {
    await fn(container.cradle)
    await delay(delayTime)
}, time.tenMin)

export const testSuite = (suiteName, fn) => describe(suiteName, () => {
    fn(container.cradle)
    return
})