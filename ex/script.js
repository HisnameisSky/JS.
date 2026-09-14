const togglebtn=document.getElementById("toggle-btn");
const card = document.getElementById("card");

togglebtn.addEventListener("click",()=>{
    card.classList.toggle("is-active");
});