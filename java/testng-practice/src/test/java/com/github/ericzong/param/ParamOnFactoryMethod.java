package com.github.ericzong.param;

import org.testng.annotations.Factory;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParamOnFactoryMethod {
    private String data;

    public ParamOnFactoryMethod(String data) {
        this.data = data;
    }

    @Parameters("param")
    @Factory
    public Object[] createInstances(String param) {
        Object[] instances = new ParamOnFactoryMethod[3];
        for (int i = 0; i < 3; i++) {
            instances[i] = new ParamOnFactoryMethod("【@Factory】实例" + i + ": " + param);
        }

        return instances;
    }

    @Test
    public void testInstance() {
        System.out.println(this.data);
    }
}
