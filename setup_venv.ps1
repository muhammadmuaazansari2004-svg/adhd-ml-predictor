# PowerShell script to set up Python virtual environment and install dependencies

param(
    [string]$PythonCmd = "python"
)

# Check if Python is available
$pythonCheck = & $PythonCmd --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Python not found. Install Python from https://www.python.org or use 'winget install Python.Python.3'."
    exit 1
}

Write-Host "✅ Found: $pythonCheck"

# Create virtual environment
Write-Host "Creating virtual environment..."
& $PythonCmd -m venv .venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to create venv."
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
& ".\.venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..."
& python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..."
& pip install -r requirements.txt

Write-Host "✅ Setup complete! Activate the venv with: .\.venv\Scripts\Activate.ps1"
