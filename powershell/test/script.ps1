# 普通执行脚本，其中的变量和函数作用域为 Script，脚本执行完成即删除
# 要想脚本执行完成后变量和函数可用，需要作用域为 Global
# 需要“dot-sourcing”操作来实现：
# . ./script.ps1
$testValue = '脚本中的变量'