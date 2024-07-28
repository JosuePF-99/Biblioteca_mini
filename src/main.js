const h1 = document.getElementById("mih1")

const ContePadre = document.getElementById("contenedorPadre")
console.log(ContePadre.childNodes)

for(let i=0;i<14;i++){
    const ContendoresHijos = document.createElement("div");
    ContendoresHijos.id = "ConteHijos"
    ContendoresHijos.textContent = `Hijo ${i + 1}`;
    ContePadre.appendChild(ContendoresHijos)

    ContendoresHijos.addEventListener("click", () => {
        console.log()
    });
}

