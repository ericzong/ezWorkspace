/*
 * Copyright (c) 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */

package com.github.ericzong.stopwatch;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.util.StopWatch;
import org.testng.annotations.Test;

/**
 * Spring 工具类。用来统计任务耗时。
 */
public class SpringStopWatchTest {
    public static final Logger logger = LoggerFactory.getLogger(SpringStopWatchTest.class);

    @Test
    public void testCase1() throws InterruptedException {
        StopWatch sw = new StopWatch();
        sw.start();
        Thread.sleep(1000);
        sw.stop();
        logger.info(String.valueOf(sw.getTotalTimeMillis()));
    }

    @Test
    public void testCase2() throws InterruptedException {
        StopWatch sw = new StopWatch();

        sw.start("task1");
        Thread.sleep(500);
        sw.stop();

        sw.start("task2");
        Thread.sleep(300);
        sw.stop();

        sw.start("task3");
        Thread.sleep(200);
        sw.stop();

        logger.info(sw.prettyPrint());
        logger.info(String.valueOf(sw.getTotalTimeMillis()));
    }
}
