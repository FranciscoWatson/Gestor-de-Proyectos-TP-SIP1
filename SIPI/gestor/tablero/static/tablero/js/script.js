const tarea = {
    id: '',
    nombre: '',
    descripcion: '',
    responsable: ''
}

let isEditando = false
let isValido = false

function drag(event) {
    event.dataTransfer.setData("text", event.target.id)
}

function allowDrop(event) {
    event.preventDefault()
}

function drop(event) {
    event.preventDefault()
    const data = event.dataTransfer.getData("text")
    event.currentTarget.appendChild(document.getElementById(data))
}

function crearTarea(event) {
    event.preventDefault()

    validarCampos(
        document.getElementById("tarea-nombre").value,
        document.getElementById("tarea-descripcion").value
    )

    if(isValido) {
        if (isEditando) {
            const divTarea = document.getElementById(tarea.id)
            divTarea.childNodes[0].textContent = document.getElementById("tarea-nombre").value
            divTarea.childNodes[1].textContent = document.getElementById("tarea-descripcion").value
            divTarea.childNodes[2].textContent = document.getElementById("tarea-responsable").value

            const btnEditar = document.getElementById("btn-crear-editar")
            btnEditar.value = "Crear Tarea"
            btnEditar.classList.remove('btn-editar')
            btnEditar.classList.add('btn-crear')
        } else {
            tarea.nombre = document.getElementById("tarea-nombre").value
            tarea.descripcion = document.getElementById("tarea-descripcion").value
            tarea.responsable = document.getElementById("tarea-responsable").value
            registrarTarea()
        }
    }

    limpiarCampos()
    limpiarObj()
}

function limpiarCampos() {
    document.getElementById("tarea-nombre").value = ''
    document.getElementById("tarea-descripcion").value = ''
    document.getElementById("tarea-responsable").value = ''
    
} 

function limpiarObj() {
    tarea.id = ''
    tarea.nombre = ''
    tarea.descripcion = ''
    tarea.responsable = ''

    isValido = false
    isEditando = false
}

function validarCampos(nombre, descripcion) {
    if (nombre === '' || descripcion === '') {
        alert('Debes asignar el nombre y la descripción de la tarea')
        isValido = false
    } else {
        isValido = true
    }
}

function registrarTarea() {

    
 const divElemento = document.createElement('div');

    // Crea tres elementos de párrafo (p) con cadenas de texto
    const p1 = document.createElement('div');
    p1.textContent = 'Texto 1';

    const p2 = document.createElement('div');
    p2.textContent = 'Texto 2';

    const p3 = document.createElement('div');
    p3.textContent = 'Texto 3';

    // Agrega los elementos de párrafo al div
    divElemento.appendChild(p1);
    divElemento.appendChild(p2);
    divElemento.appendChild(p3);

    // Obtén el div específico por su id
    const miDiv = document.getElementById('pendientes');

    // Agrega el nuevo div con los elementos al div específico
    miDiv.appendChild(divElemento);


    
}

const btnEjecutar = document.getElementById("btn-ejecutar");

btnEjecutar.addEventListener("click", function() {
    // Llama a la función cuando se haga clic en el botón
    registrarTarea();
});


