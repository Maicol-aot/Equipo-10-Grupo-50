function validacion(){
    let nombre = document.formulario.nombre;
    let apellido = document.getElementById('apellido');
    let email = document.getElementById('email');
    let password = document.getElementsById('password');
    let sexo = document.getElementsByName('sexo');
    let edad = document.getElementsById('edad');

    let nombre_len = nombre.value.length;
    if (nombre_len>5){
        alert('No');
        return false;
    }
}