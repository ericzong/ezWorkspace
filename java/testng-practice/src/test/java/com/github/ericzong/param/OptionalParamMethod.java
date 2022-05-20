package com.github.ericzong.param;

import org.testng.annotations.Optional;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class OptionalParamMethod {
    @Parameters({"param"})
    @Test
    public void testOptionalParam(@Optional("默认值") String data) {
        System.out.println("【@Optional】" + data);
    }
}
