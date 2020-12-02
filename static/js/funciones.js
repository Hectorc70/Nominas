/* alert("¿Seguro que quiere eliminar este registro?") */
function eliminar() {
	let x = confirm("¿ Esta seguro que quiere eliminar ?");
	if (x)
		return true;
	else
		return false;
}

function guardar(){
	let tabla = document.getElementById('table_nom');
	saveAsExcel(tabla, 'hola');
}


async function salirOverlay() {
    let visualizador = document.getElementById("overlay");
    visualizador.setAttribute("class", "no-mostrar")
    
}
async function entrarOverlay() {
    let visualizador = document.getElementById("overlay");
    visualizador.removeAttribute("class", "no-mostrar")  
}


/* Funciones que son para mostrar una animación de loader*/
function loader_tarea(){      
    let carga = document.getElementById("loader");    
    carga.setAttribute("class", "preloader_2");
}

function deshabilitar(elemento){
    let etiqueta = document.getElementById(elemento);
    etiqueta.setAttribute("class", "deshabilitado");
    
    
}
function habilitarElemento(elemento){
    let etiqueta = document.getElementById(elemento);
    etiqueta.removeAttribute("class");
    
    
}

function habilitar(elemento){ 
    let carga = document.getElementById("loader");  
    let etiqueta = document.getElementById(elemento);  
    carga.removeAttribute("class");
    etiqueta.removeAttribute("class");
    
        

}
