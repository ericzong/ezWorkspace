package com.github.ericzong.param;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class DataProviderInSameClassTest {

    @DataProvider(name = "data")
    private Object[][] createData() {
        return new Object[][]{
                {"@DataProvider"},
                {"位于同类中"}
        };
    }

    @Test(dataProvider = "data")
    public void test(String desc) {
        System.out.println(desc);
    }
}
