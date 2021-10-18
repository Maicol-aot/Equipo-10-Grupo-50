document.getElementById("texto").onload = function() {cambiarText()}

function cambiarText(){
    let str= "Aquí tenemos las últimas novedades para ti."
    let arrFromStr = str.split('');
    let i=0;
    let printStr = setInterval(function(){
        if(arrFromStr[i] == 12 ){
            document.getElementById("texto").innerHTML += "\r\n"
        }
        else{
            if(arrFromStr[i] === ' '){
                document.getElementById("texto").innerHTML += arrFromStr[i];
                document.getElementById("texto").innerHTML += arrFromStr[i + 1];
                i+=2;
            }else{
                document.getElementById("texto").innerHTML += arrFromStr[i];
                i++;
            }

            if(i == arrFromStr.length){
                clearInterval(printStr);
            }
        }  
    },100);
};