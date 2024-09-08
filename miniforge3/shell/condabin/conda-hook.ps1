$Env:CONDA_EXE = "/Users/nic/Python/transcribee/miniforge3/bin/conda"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "/Users/nic/Python/transcribee/miniforge3"
$Env:_CONDA_EXE = "/Users/nic/Python/transcribee/miniforge3/bin/conda"
$CondaModuleArgs = @{ChangePs1 = $False}
Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs