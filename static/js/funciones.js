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