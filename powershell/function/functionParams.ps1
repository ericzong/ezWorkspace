function paramFunction ($arg1, $arg2) 
{
    $arg1
    $arg2
}

# $args
function sum
{
    $sum = 0
    $args | foreach { $sum += $_ }
    $sum
}

# 开关参数
function boolParam([bool]$switch)
{
    $switch
}

# 默认值
function Add([int]$one=1, [int]$another=1)
{
	$one + $another
}

# 异常默认值
function doNotMiss($arg=$(throw "请提供参数 arg！"))
{
    $arg
}
