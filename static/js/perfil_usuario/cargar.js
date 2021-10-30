function cargarImg(){
    let input = document.querySelector('#upload')
    let image = document.querySelector('.display_Img')

    input.addEventListener('change', ()=>{
        let lector = new FileReader()
        lector.readAsDataURL(input.files[0])

        lector.onload=()=>{
            image.style.backgroundImage = `url(${lector.result})`
        }
    })
}
