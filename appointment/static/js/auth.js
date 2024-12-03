const validateUsername = document.querySelector('#username-field');
const validateEmail = document.querySelector('#email-field');
const validatePassword = document.querySelector('#password-field');
const usernameErrorArea = document.querySelector('.username-error-field');
const emailErrorArea = document.querySelector('.email-error-field');
const emailCheck = document.querySelector('.email-check');
const usernameCheck = document.querySelector('.username-check');
const showPassword = document.querySelector('.show-password');
const submitBtn = document.querySelector('.submit-btn');

// const handleToggleInput = (e) => {
//     if(showPassword.textContent == "Show") {
//         showPassword.textContent == "Hide";
//     } else {
//         showPassword.textContent == "Show";
//     }
// }

showPassword.addEventListener('click', () => {
    if(showPassword.textContent === "Show") {
        showPassword.textContent = "Hide";
        validatePassword.setAttribute("type", "text");
    } else {
        showPassword.textContent = "Show";
        validatePassword.setAttribute("type", "password");
    }
});

validateUsername.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;

    usernameCheck.style.display = "block"
    usernameCheck.style.color = "grey"
    validateUsername.style.border = "none";
    usernameErrorArea.style.display = "none";
    usernameCheck.textContent = `Checking ${usernameVal}`
    

    if(usernameVal.length > 0){
        fetch('/authentication/validate-username', {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res => res.json()).then(data => {
            usernameCheck.style.display = "none"
            if(data.username_error){
                submitBtn.disabled = true;
                usernameErrorArea.innerHTML=`<p>${data.username_error}</p>`;
                validateUsername.style.border = ".3rem solid red";
                usernameErrorArea.style.display = "block";
                usernameErrorArea.style.color = "red";
            } else {
                submitBtn.removeAttribute('disabled');
                usernameErrorArea.innerHTML=`<p>${"Good"}</p>`;
                validateUsername.style.border = ".3rem solid green";
                usernameErrorArea.style.display = "block";
                usernameErrorArea.style.color = "green";
            }
        });
    }
});

validateEmail.addEventListener('keyup', (e) => {
    const emailVal = e.target.value;
    emailCheck.style.display = "block"
    emailCheck.style.color = "grey"

    validateEmail.style.border = "none";
    emailErrorArea.style.display = "none";
    emailCheck.textContent = `Checking ${emailVal}`

    if(emailVal.length > 0){
        fetch('/authentication/validate-email', {
            body: JSON.stringify({email: emailVal}),
            method: "POST",
        }).then(res => res.json()).then(data => {
            emailCheck.style.display = "none"
            if(data.email_error){
                submitBtn.disabled = true;
                emailErrorArea.innerHTML=`<p>${data.email_error}</p>`;
                validateEmail.style.border = ".3rem solid red";
                emailErrorArea.style.color = "red";
                emailErrorArea.style.display = "block";
            } else {
                submitBtn.removeAttribute('disabled');
                emailErrorArea.innerHTML=`<p>${"Good"}</p>`;
                validateEmail.style.border = ".3rem solid green";
                emailErrorArea.style.display = "block";
                emailErrorArea.style.color = "green";
            }
        });
    }
});