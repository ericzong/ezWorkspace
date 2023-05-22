package com.github.ericzong.retry;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class DataProviderRetryTest {
    public static final Logger logger = LoggerFactory.getLogger(DataProviderRetryTest.class);

    @Test(dataProvider = "data")
    public void test(int count) {
        logger.info("传入的数据是 {}", count);
        int i = 0;
        while(i++ < count) {
            var number = DataFactory.getNumber();
            logger.info("test() 获取到的数字是 {}", number);
        }
    }

    @DataProvider(name = "data")
    private Object[][] createData() {
        return new Object[][] {
                {1},
                {2}
        };
    }
}
