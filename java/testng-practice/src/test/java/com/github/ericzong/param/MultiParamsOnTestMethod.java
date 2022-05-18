package com.github.ericzong.param;

import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class MultiParamsOnTestMethod {
    @Parameters({"param", "param2"})
    @Test
    public void testMultiParams(String p1, String p2) {
        System.out.println("【@Test多参】param: " + p1 + "; param2: " + p2);
    }
}
