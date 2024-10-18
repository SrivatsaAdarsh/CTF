$passwordListFilePath = "passwordlist.txt"

# Path to the zip file
$zipFilePath = "ctf.zip"

# Temporary extract path
$tempExtractPath = "temp"

# Read passwords from the file
$passwords = Get-Content -Path $passwordListFilePath

# Add necessary assemblies for working with zip files
Add-Type -AssemblyName System.IO.Compression.FileSystem

# Function to attempt extraction with a given password
function Try-Extract-Zip {
    param (
        [string]$zipPath,
        [string]$extractPath,
        [string]$password
    )
    
    # Clear temp extract path
    if (Test-Path -Path $extractPath) {
        Remove-Item -Path $extractPath -Recurse -Force
    }
    
    try {
        $zipFile = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
        foreach ($entry in $zipFile.Entries) {
            [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, "$extractPath\$($entry.FullName)", $password)
        }
        $zipFile.Dispose()
        return $true
    } catch {
        return $false
    }
}

# Iterate through the passwords and try to open the zip file
foreach ($password in $passwords) {
    if (Try-Extract-Zip -zipPath $zipFilePath -extractPath $tempExtractPath -password $password) {
        Write-Host "Password found: $password"
        break
    } else {
        Write-Host "Password failed: $password"
    }
}