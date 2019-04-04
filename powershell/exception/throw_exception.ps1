function throwException($a, $b=$(throw "required"))
{
    
}

function throwException2
{
    Param(
        $a,
        $b=$(throw "required")
    )
    $a + $b
}