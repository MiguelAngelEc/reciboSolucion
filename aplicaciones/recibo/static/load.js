// Obtener referencia al elemento select y al elemento span
const selectValor = document.getElementById("id_select");
const pValor = document.getElementById("pValor");

// Agregar un evento change al elemento select
selectValor.addEventListener("change", function() {
  // Obtener el valor seleccionado
  const valorSeleccionado = selectValor.value;
  // Establecer el valor seleccionado como texto del elemento span
  pValor.textContent = "Valor seleccionado: " + valorSeleccionado;
});

document.getElementById("print_view").addEventListener("click", function() {
  // Imprimir la página
  window.print();
});


