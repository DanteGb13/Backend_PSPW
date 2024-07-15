function editarProducto(id, nombre, categoria, precio, imagen) {
    document.getElementById('producto_id').value = id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('categoria').value = categoria;
    document.getElementById('precio').value = precio;
    document.getElementById('imagen').value = imagen;
    document.getElementById('agregar').style.display = 'none';
    document.getElementById('editar').style.display = 'block';
}

function resetFormulario() {
    document.getElementById('producto_id').value = '';
    document.getElementById('nombre').value = '';
    document.getElementById('categoria').value = '';
    document.getElementById('precio').value = '';
    document.getElementById('imagen').value = '';
    document.getElementById('agregar').style.display = 'block';
    document.getElementById('editar').style.display = 'none';
}
