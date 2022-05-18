package com.github.ericzong.param;

import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class SingleParamOnTestMethod {
    @Parameters({"param"})
    @Test
    public void testSingleParam(String data) {
        System.out.println("【@Test单参】" + data);
    }
}
