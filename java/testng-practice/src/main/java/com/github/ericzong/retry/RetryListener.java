package com.github.ericzong.retry;

import org.testng.IAnnotationTransformer;
import org.testng.IRetryAnalyzer;
import org.testng.annotations.ITestAnnotation;
import org.testng.internal.annotations.DisabledRetryAnalyzer;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class RetryListener implements IAnnotationTransformer {
    @Override
    public void transform(ITestAnnotation annotation, Class testClass, Constructor testConstructor, Method testMethod) {
        Class<? extends IRetryAnalyzer> retryAnalyzer = annotation.getRetryAnalyzerClass();
        if(retryAnalyzer == DisabledRetryAnalyzer.class) {
            annotation.setRetryAnalyzer(TestNGRetry.class);
        }
    }
}
