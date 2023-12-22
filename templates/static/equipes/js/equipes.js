function add_mecanico(){
    container = document.getElementById('form-mecanico')

    html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='Mecanico' class='form-control' name='mecanico' > </div> <div class='col-md'><input type='text' placeholder='Email' class='form-control' name='email' ></div> <div class='col-md'> <input type='text' placeholder='Cpf' class='form-control' name='cpf'> </div> </div>"

    container.innerHTML += html
}