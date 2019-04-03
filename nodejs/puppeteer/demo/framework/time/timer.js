
export default {
    tenSecond: 10000,
    halfMin: 30000,
    oneMin: 60000,
    fiveMin: 300000,
    tenMin: 600000
}

export const delay = timeout => new Promise(resolve => {
    setTimeout(resolve, timeout)
});