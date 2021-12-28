$data   =   import-csv -path "datos.csv" -Encoding default


$conta=1
$control=1

$data | foreach-Object {
    $numCur = $_.numes
    

    if($control -eq 1){
        $letterA=$numCur
    }
    if($control -eq 2){
        $letterB=$numCur
    }
    if($control -eq 3){
        $letterC=$numCur

        $resultA=[int]$letterA+[int]$letterB+[int]$letterC
    }
    if($control -eq 4){
        $letterD=$numCur

        $resultB=[int]$letterB+[int]$letterC+[int]$letterD

        if($resultA -lt $resultB){$conta++}
    }
    if($control -eq 5){
        $letterE=$numCur

        $resultC=[int]$letterE+[int]$letterC+[int]$letterD
        
        if($resultB -lt $resultC){$conta++}
    }
    if($control -eq 6){
        $letterF=$numCur

        $resultD=[int]$letterE+[int]$letterF+[int]$letterD
        
        if($resultC -lt $resultD){$conta++}
    }
    if($control -eq 7){
        $letterG=$numCur

        $resultE=[int]$letterE+[int]$letterF+[int]$letterG

        if($resultD -lt $resultE){$conta++}
    }
    if($control -eq 8){
        $letterH=$numCur

        $resultF=[int]$letterF+[int]$letterG+[int]$letterH

        if($resultE -lt $resultF){$conta++}
    }
    if($control -eq 9){
        $letterH2=$numCur

        $resultG=[int]$letterH2+[int]$letterG+[int]$letterH

        if($resultF -lt $resultG){$conta++}
    }
    if($control -eq 10){
        $letterH3=$numCur

        $resultH=[int]$letterH2+[int]$letterH3+[int]$letterH

        if($resultG -lt $resultH){$conta++}
    }


    $control++

    
    if($control -eq 11){$control = 1}

}