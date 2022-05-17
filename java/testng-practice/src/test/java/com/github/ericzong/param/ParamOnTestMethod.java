package com.github.ericzong.param;

import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParamOnTestMethod {
    @Parameters({"param"})
    @Test
    public void test(String data) {
        System.out.println(data);
    }
}
