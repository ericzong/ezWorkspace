package com.github.ericzong.param;

import org.testng.annotations.*;

@Test(groups = {"前后置处理器"})
public class ParamOnBeforeAfterMethod {
    @Parameters({"param"})
    @BeforeSuite(groups = {"前后置处理器"})
    public void beforeSuite(String data) {
        System.out.println("【@BeforeSuite】" + data);
    }

    @Parameters({"param"})
    @AfterSuite(groups = {"前后置处理器"})
    public void afterSuite(String data) {
        System.out.println("【@AfterSuite】" + data);
    }

    @Parameters({"param"})
    @BeforeGroups({"前后置处理器"})
    public void beforeGroups(String data) {
        System.out.println("【@BeforeGroups】" + data);
    }

    @Parameters({"param"})
    @AfterGroups({"前后置处理器"})
    public void afterGroups(String data) {
        System.out.println("【@AfterGroups】" + data);
    }

    @Test(groups = {"前后置处理器"})
    public void testNone() {
        System.out.println("测试前后置处理器");
    }
}
