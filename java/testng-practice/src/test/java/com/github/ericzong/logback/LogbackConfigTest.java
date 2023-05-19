package com.github.ericzong.logback;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.annotations.Test;

public class LogbackConfigTest {
    public static final Logger logger = LoggerFactory.getLogger(LogbackConfigTest.class);

    @Test
    public void testConfig() {
        logger.debug("debug from LogbackConfigTest");
    }
}
