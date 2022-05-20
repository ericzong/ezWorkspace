package com.github.ericzong.param;

import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParamOnConstructor {
    private String name;

    @Parameters({"param"})
    public ParamOnConstructor(String name) {
        this.name = name;
    }

    @Test
    public void testConstructor() {
        System.out.println("【构造器上@Parameters传参】" + this.name);
    }
}
