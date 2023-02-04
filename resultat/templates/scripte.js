var divisions = document.getElementsByClassName("container-content-div");

for (var i = 0; i < divisions.length; i++) {
  divisions[i].style.width = parseFloat(divisions[i].textContent) + "%";
}
