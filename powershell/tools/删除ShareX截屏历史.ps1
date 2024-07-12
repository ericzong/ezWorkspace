$date = Get-Date
$ymDate = $date.ToString('yyyy-MM')
$rootPath = 'D:\scoop\apps\sharex\current\ShareX\Screenshots'
cd $rootPath
Get-ChildItem -Path $rootPath -Director | ForEach-Object {
	if ($_.Name -ne $ymDate) {  # 只删除当前月份之前的历史数据
        Remove-Item $_.FullName -Recurse -Force
    }
}