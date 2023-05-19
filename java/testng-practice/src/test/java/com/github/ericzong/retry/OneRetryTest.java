package com.github.ericzong.retry;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

@Test(retryAnalyzer = TestNGRetry.class)
public class OneRetryTest {
    public static final Logger logger = LoggerFactory.getLogger(OneRetryTest.class);

    public void test() {
        var num = DataFactory.getNumber();
        logger.info("test() 获取到的数字是 {}", num);
    }

    public void test2() {
        var num = DataFactory.getNumber();
        num = DataFactory.getNumber();
        logger.info("test2() 获取到的数字是 {}", num);
    }
}
