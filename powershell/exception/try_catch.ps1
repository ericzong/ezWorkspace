
try {
  dir "nothing" -ErrorAction Stop
  Write-Host "no executed"
} catch {
  Write-Warning "Error: $_"
  Write-Host $_.getType().fullname
  Write-Warning "Error: $PSItem"
} finally {
  Write-Host "Always run"
}

Write-Host "will be executed"
