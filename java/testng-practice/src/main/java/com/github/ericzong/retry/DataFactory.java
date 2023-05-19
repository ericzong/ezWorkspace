package com.github.ericzong.retry;

public class DataFactory {
    private static int number = 0;

    public static int getNumber() {
        number++;

        if(number % 3 != 0) {
            throw new RuntimeException("故意出错……");
        }

        return number;
    }
}
