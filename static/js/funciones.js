'use strict'

/* alert("¿Seguro que quiere eliminar este registro?") */
function eliminar() {
	let x = confirm("¿ Esta seguro que quiere eliminar ?");
	if (x)
		return true;
	else
		return false;
}

function guardar() {
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
function loader_tarea() {
	let carga = document.getElementById("loader");
	carga.setAttribute("class", "preloader_2");
}

function deshabilitar(elemento) {
	let etiqueta = document.getElementById(elemento);
	etiqueta.setAttribute("class", "deshabilitado");


}
function habilitarElemento(elemento) {
	let etiqueta = document.getElementById(elemento);
	etiqueta.removeAttribute("class");


}

function habilitar(elemento) {
	let carga = document.getElementById("loader");
	let etiqueta = document.getElementById(elemento);
	carga.removeAttribute("class");
	etiqueta.removeAttribute("class");



}


/* Suma columnas de tablas */

function sumarColumna(id, idCeldaT) {
	
	let columnaImporte = document.getElementsByClassName(id);
	let importes = []
	let suma = 0
	
	for (let i = 0; i < columnaImporte.length; i++) {
		let fila_importe = document.getElementsByClassName(id)[i].innerText;
		
		let fila_num
		fila_num = 	parseFloat(fila_importe)
		
		suma = suma + fila_num
	}
	debugger;
	document.getElementsByClassName(idCeldaT)[0].innerHTML = suma.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,'); ;

	
	console.log(suma.toFixed(2))
}
