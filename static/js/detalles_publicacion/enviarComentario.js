function checkearTecla(e){    
    if (e.keyCode == 13 && !e.shiftKey) {
        document.getElementById("formID").submit();
    }
}