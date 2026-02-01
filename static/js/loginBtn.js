// Logged-out elements
const loginBtn = document.querySelector(".loginBtn");
const loginBox = document.querySelector(".loginBox");

// Logged-in elements
const usernameOutput = document.querySelector(".usernameOutput");
const usernameOutputContainer = document.querySelector(".usernameOutputContainer");

// --------------------
// LOGGED-OUT BEHAVIOR
// --------------------
if (loginBtn && loginBox) {
    loginBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        loginBox.classList.remove("hidden");
        loginBtn.classList.add("hidden");
    });

    loginBox.addEventListener("click", (e) => {
        e.stopPropagation();
    });
}

// --------------------
// LOGGED-IN BEHAVIOR
// --------------------
if (usernameOutput && usernameOutputContainer) {
    usernameOutput.addEventListener("click", (e) => {
        e.stopPropagation();
        usernameOutputContainer.classList.toggle("hidden");
    });

    usernameOutputContainer.addEventListener("click", (e) => {
        e.stopPropagation();
    });
}

// --------------------
// CLICK OUTSIDE → CLOSE
// --------------------
window.addEventListener("click", () => {
    // Close login box (logged out)
    if (loginBox && loginBtn) {
        loginBox.classList.add("hidden");
        loginBtn.classList.remove("hidden");
    }

    // Close user dropdown (logged in)
    if (usernameOutputContainer) {
        usernameOutputContainer.classList.add("hidden");
    }
});
