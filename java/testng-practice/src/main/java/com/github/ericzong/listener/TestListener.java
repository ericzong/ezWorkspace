package com.github.ericzong.listener;

import org.testng.ISuite;
import org.testng.ISuiteListener;

public class TestListener implements ISuiteListener {

    @Override
    public void onStart(ISuite suite) {
        if(suite.getName().equals("已登录")) {
            System.out.println("Suite login start...");
            System.out.println(suite.getParameter("user"));
        }
    }

    @Override
    public void onFinish(ISuite suite) {
        if(suite.getName().equals("已登录")) {
            System.out.println("Suite login end...");
        }
    }
}
