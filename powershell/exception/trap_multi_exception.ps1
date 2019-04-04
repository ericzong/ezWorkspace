
function trapDefault
{
    Trap {"Get Exception"}
    1/$null
    Get-Process "NoSuchProcess"
    Dir Miss:
}

function trapStop
{
    Trap {"Get Exception: $($PSItem.Exception.Message)"}
    1/$null
    Get-Process "NoSuchProcess" -ErrorAction Stop
    Dir Miss: -ErrorAction Stop
}

function trapContinue
{
    Trap {
        "Get Exception: $($_.Exception.Message)"
        Continue
    }
    1/$null
    Get-Process "NoSuchProcess" -ErrorAction Stop
    Dir Miss: -ErrorAction Stop
}

function trapBreak
{
    Trap {
        "Get Exception: $($_.Exception.Message)"
        Break
    }
    1/$null
    Get-Process "NoSuchProcess" -ErrorAction Stop
    Dir Miss: -ErrorAction Stop
}

function test
{
    1/$null
    Get-Process "NoSuchProcess"
    Dir Miss:
}

function callerContinue
{
    Trap {
        "Trap Error: $($_.Exception.Message)"
        Continue
    }

    test
    test
}

function callerBreak
{
    Trap {
        "Trap Error: $($_.Exception.Message)"
        Break
    }

    test
    test
}
