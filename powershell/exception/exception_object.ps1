function redirectToFile
{
    dir "NoSuchDirectory" 2> Error.txt
    Get-Content Error.txt
}

function redirectToVar
{
    $myError = dir "NoSuchDirectory" 2>&1
    $myError.Exception
    $myError.InvocationInfo
    $myerror.FullyQualifiedErrorId
}

function errorVariable
{
    Remove-Item "NoSuchDirectory" -ErrorVariable ErrorStore -ErrorAction "SilentlyContinue"
    $ErrorStore
    $ErrorStore.GetType().fullName
    $ErrorStore[0].getType().fullName
    $ErrorStore[0].Exception.Message
}

function appendErrorVariable
{
    dir "NoSuchDirectory" -ErrorAction SilentlyContinue -ErrorVariable +ErrorStore
    Remove-Item "NoSuchDirectory" -ErrorAction SilentlyContinue -ErrorVariable +ErrorStore
    Get-Item "NoSuchDirectory" -ErrorAction SilentlyContinue -ErrorVariable +ErrorStore
    $ErrorStore.Count
}
