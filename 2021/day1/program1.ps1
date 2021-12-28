$data   =   import-csv -path "datos.csv" -Encoding default


$cont =1
$bef=0
$data | foreach-Object {
    $numCur = $_.numes
    #write-host "analizando $numCur"
    if(($bef -lt $numCur) -and ($numCur -ne 180)){
        $cont++
    }


    $bef = $numCur
}

Write-Host "$cont"