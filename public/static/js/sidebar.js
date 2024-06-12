const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  const sideBarElement = document.querySelector("#sidebar");
  sideBarElement.classList.toggle("expand");
//  add cursor as pointer
  sideBarElement.style.cursor = "pointer";
});