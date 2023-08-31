package com.github.ericzong.retry;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;

public class TestNGRetry implements IRetryAnalyzer {
    public static final Logger logger = LoggerFactory.getLogger(TestNGRetry.class);
    private int retryCount = 0;
    private static final int MAX_RETRY_COUNT = 3;

    @Override
    public boolean retry(ITestResult iTestResult) {
        if(retryCount < MAX_RETRY_COUNT) {
            retryCount++;
            logger.warn("重跑，第{}次", retryCount);
            return true;
        }

        return false;
    }
}
