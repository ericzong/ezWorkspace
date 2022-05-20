package com.github.ericzong.param;

import org.testng.annotations.*;

@Test(groups = {"前后置处理器"})
public class ParamOnBeforeAfterMethod {
    @Parameters({"param"})
    @BeforeSuite
    public void beforeSuite(String data) {
        System.out.println("【@BeforeSuite】" + data);
    }

    @Parameters({"param"})
    @AfterSuite
    public void afterSuite(String data) {
        System.out.println("【@AfterSuite】" + data);
    }

    @Parameters("param")
    @BeforeTest
    public void beforeTest(String data) {
        System.out.println("【@BeforeTest】" + data);
    }

    @Parameters("param")
    @AfterTest
    public void afterTest(String data) {
        System.out.println("【@AfterTest】" + data);
    }

    @Parameters({"param"})
    @BeforeGroups(groups = {"前后置处理器"})
    public void beforeGroups(String data) {
        System.out.println("【@BeforeGroups】" + data);
    }

    @Parameters({"param"})
    @AfterGroups({"前后置处理器"})
    public void afterGroups(String data) {
        System.out.println("【@AfterGroups】" + data);
    }

    @Parameters({"param"})
    @BeforeClass
    public void beforeClass(String data) {
        System.out.println("【@BeforeClass】" + data);
    }

    @Parameters({"param"})
    @AfterClass
    public void afterClass(String data) {
        System.out.println("【@AfterClass】" + data);
    }

    @Parameters({"param"})
    @BeforeMethod
    public void beforeMethod(String data) {
        System.out.println("【@BeforeMethod】" + data);
    }

    @Parameters({"param"})
    @AfterMethod
    public void afterMethod(String data) {
        System.out.println("【@AfterMethod】" + data);
    }

    @Test
    public void testNone() {
        System.out.println("测试");
    }
}
