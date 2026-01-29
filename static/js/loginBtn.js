const loginBtn = document.querySelector(".loginBtn");
const loginBox = document.querySelector(".loginBox");

const removeHidden = () => {
    if (loginBox.classList.contains("hidden")) {
        loginBox.classList.remove("hidden");
    }
}

const addHidden = () => {
    if (!loginBox.classList.contains("hidden")) {
        loginBox.classList.add("hidden")
    }
}

loginBtn.addEventListener("click", e => {
    e.stopPropagation();
    removeHidden();
})

loginBox.addEventListener("click", e => {
    e.stopPropagation();
})

window.addEventListener("click", addHidden)