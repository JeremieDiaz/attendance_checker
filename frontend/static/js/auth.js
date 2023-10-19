const container = document.querySelector(".container"),
  pwShowHide = document.querySelectorAll(".showHidePw"),
  pwFields = document.querySelectorAll(".password"),
  signUp = document.querySelector(".signup-link"),
  login = document.querySelector(".login-link");
//   js code to show/hide password and change icon
pwShowHide.forEach((eyeIcon) => {
  eyeIcon.addEventListener("click", () => {
    pwFields.forEach((pwField) => {
      if (pwField.type === "password") {
        pwField.type = "text";
        pwShowHide.forEach((icon) => {
          icon.classList.replace("uil-eye-slash", "uil-eye");
        });
      } else {
        pwField.type = "password";
        pwShowHide.forEach((icon) => {
          icon.classList.replace("uil-eye", "uil-eye-slash");
        });
      }
    });
  });
});

//login

function submitForm(event) {
  event.preventDefault();  // Prevent the default form submission

  // Get form data and send it to the server
  const email = document.querySelector('input[name="lemail"]').value;
  const password = document.querySelector('input[name="lpassword"]').value;

  console.log("Email:", email);
  console.log("Password:", password);

  // You can use fetch or XMLHttpRequest to send the data to the server here

  // Clear the input fields
  document.querySelector('input[name="lemail"]').value = '';
  document.querySelector('input[name="lpassword"]').value = '';
}