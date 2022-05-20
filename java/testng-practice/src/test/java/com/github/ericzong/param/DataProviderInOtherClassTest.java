package com.github.ericzong.param;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class DataProviderInOtherClassTest {
    @Test(dataProvider = "data", dataProviderClass = Provider.class)
    public void test(String desc) {
        System.out.println(desc);
    }
}

class Provider {
    @DataProvider(name = "data")
    private static Object[][] createData() {
        // 注意：
        // 1. 访问修饰符权限是任意的
        // 2. 若为实例方法，则要求该类具有公有构造器
        return new Object[][]{
                {"@DataProvider"},
                {"位于不同类中"}
        };
    }
}