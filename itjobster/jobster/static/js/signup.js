const usernameEl = document.querySelector("#username");
const emailEl = document.querySelector("#email");
const ageE1 = document.querySelector("#age");
const phonenoE1 = document.querySelector("#phoneno");
const locationE1 = document.querySelector("#location");
const aadharnoE1 = document.querySelector("#aadharno");
const passwordEl = document.querySelector("#password");

const cinE2 = document.querySelector("#cin");
const cnameE2 = document.querySelector("#cname");
const clocationE2 = document.querySelector("#clocation");
const cphonenoE2 = document.querySelector("#cphoneno");
const cpasswordE2 = document.querySelector("#cpassword");

const u_form = document.querySelector("#u_signup");
const c_form = document.querySelector("#c_signup");

const checkUsername = () => {
  let valid = false;

  const min = 3,
    max = 25;

  const username = usernameEl.value.trim();

  if (!isRequired(username)) {
    showError(usernameEl, "Username cannot be blank");
  } else if (!isBetween(username.length, min, max)) {
    showError(usernameEl, "Username not valid");
  } else {
    showSuccess(usernameEl);
    valid = true;
  }
  return valid;
};

const checkEmail = () => {
  let valid = false;

  const email = emailEl.value.trim();

  if (!isRequired(email)) {
    showError(emailEl, "Email cannot be blank");
  } else if (!isEmailValid(email)) {
    showError(emailEl, "Email is not valid");
  } else {
    showSuccess(emailEl);
    valid = true;
  }
  return valid;
};

const checkAge = () => {
  let valid = false;

  const age = ageE1.value.trim();

  if (!isRequired(age)) {
    showError(ageE1, "Age connot be blank");
  } else if (!(age >= 18 && age <= 80)) {
    showError(ageE1, "Age is not valid");
  } else {
    showSuccess(ageE1);
    valid = true;
  }
  return valid;
};

const checkPhoneno = () => {
  let valid = false;
  const phoneno = phonenoE1.value.trim();
  if (!isRequired(phoneno)) {
    showError(phonenoE1, "ph.no connot be blank");
  } else if (phoneno.length != 10) {
    showError(phonenoE1, "ph.no not valid");
  } else {
    showSuccess(phonenoE1);
    valid = true;
  }
  return valid;
};

const checklocation = () => {
  let valid = false;

  var regName = /^[a-zA-Z]+$/;

  const location = locationE1.value.trim();

  if (!isRequired(location)) {
    showError(locationE1, "Username cannot be blank.");
  } else if (!regName.test(location)) {
    showError(locationE1, "Invalid location given");
  } else {
    showSuccess(locationE1);
    valid = true;
  }
  return valid;
};

const checkaadharno = () => {
  let valid = false;

  const aadharno = aadharnoE1.value.trim();

  if (!isRequired(aadharno)) {
    showError(aadharnoE1, "Aadhar no connot be blank");
  } else if (aadharno.length != 12) {
    showError(aadharnoE1, "Aadhar no not valid");
  } else {
    showSuccess(aadharnoE1);
    valid = true;
  }
  return valid;
};

const checkPassword = () => {
  let valid = false;

  const password = passwordEl.value.trim();

  if (!isRequired(password)) {
    showError(passwordEl, "Password cannot be blank.");
  } else if (!isPasswordSecure(password)) {
    showError(
      passwordEl,
      "Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)"
    );
  } else {
    showSuccess(passwordEl);
    valid = true;
  }

  return valid;
};

// company sign-up

const checkcin = () => {
  let valid = false;

  const min = 16,
    max = 16;

  var regno = /^.*(?=.*[A-Z])(?=.*\d).*$/;
  const cin = cinE2.value.trim();

  if (!isRequired(cin)) {
    showError(cinE2, "CIN no cannot be blank");
  } else if (!isBetween(cin.length, min, max) && !regno.test(cin)) {
    showError(cinE2, "CIN no is not valid");
  } else {
    showSuccess(cinE2);
    valid = true;
  }
  return valid;
};

const checkcname = () => {
  let valid = false;

  const min = 3,
    max = 25;

  const cname = cnameE2.value.trim();

  if (!isRequired(cname)) {
    showError(cnameE2, "Username cannot be blank");
  } else if (!isBetween(cname.length, min, max)) {
    showError(cnameE2, "Username not valid");
  } else {
    showSuccess(cnameE2);
    valid = true;
  }
  return valid;
};

const checkclocation = () => {
  let valid = false;

  var regName = /^[a-zA-Z]+$/;

  const clocation = clocationE2.value.trim();

  if (!isRequired(clocation)) {
    showError(clocationE2, "Location cannot be blank.");
  } else if (!regName.test(clocation)) {
    showError(clocationE2, "Invalid location given");
  } else {
    showSuccess(clocationE2);
    valid = true;
  }
  return valid;
};

const checkcphoneno = () => {
  let valid = false;

  const cphoneno = cphonenoE2.value.trim();

  if (!isRequired(cphoneno)) {
    showError(cphonenoE2, "ph.no connot be blank");
  } else if (cphoneno.length != 10) {
    showError(cphonenoE2, "ph.no not valid");
  } else {
    showSuccess(cphonenoE2);
    valid = true;
  }
  return valid;
};

const checkcPassword = () => {
  let valid = false;

  const cpassword = cpasswordE2.value.trim();

  if (!isRequired(cpassword)) {
    showError(cpasswordE2, "Password cannot be blank.");
  } else if (!isPasswordSecure(cpassword)) {
    showError(
      passwordEl,
      "Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)"
    );
  } else {
    showSuccess(cpasswordE2);
    valid = true;
  }

  return valid;
};

const isEmailValid = (email) => {
  const re =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
};

const isPasswordSecure = (password) => {
  const re = new RegExp(
    "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})"
  );
  return re.test(password);
};

const isRequired = (value) => (value === "" ? false : true);
const isBetween = (length, min, max) =>
  length < min || length > max ? false : true;

const showError = (input, message) => {
  const formField = input.parentElement;

  formField.classList.remove("success");
  formField.classList.add("error");

  const error = formField.querySelector("small");
  error.textContent = message;
};

const showSuccess = (input) => {
  const formField = input.parentElement;

  formField.classList.remove("error");
  formField.classList.add("success");

  const error = formField.querySelector("small");
  error.textContent = "";
};

u_form.addEventListener("submit", function (e) {
  e.preventDefault();

  let isUsernameValid = checkUsername(),
    isEmailValid = checkEmail(),
    isagevalid = checkAge(),
    isphonenovalid = checkPhoneno(),
    islocationvalid = checklocation(),
    isaadharnovalid = checkaadharno(),
    isPasswordValid = checkPassword();

  let isFormValid =
    isUsernameValid &&
    isEmailValid &&
    isPasswordValid &&
    isagevalid &&
    isphonenovalid &&
    islocationvalid &&
    isaadharnovalid;

  if (isFormValid) {
  }
});

c_form.addEventListener("submit", function (e) {
  e.preventDefault();

  let iscinValid = checkcin(),
    iscnameValid = checkcname(),
    isclocationvalid = checkclocation(),
    iscphonenovalid = checkcphoneno(),
    iscPasswordValid = checkcPassword();

  let iscFormValid =
    iscinValid &&
    iscnameValid &&
    iscphonenovalid &&
    isclocationvalid &&
    iscPasswordValid;
  if (iscFormValid) {
  }
});

const debounce = (fn, delay = 500) => {
  let timeoutId;
  return (...args) => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      fn.apply(null, args);
    }, delay);
  };
};

u_form.addEventListener(
  "input",
  debounce(function (e) {
    switch (e.target.id) {
      case "username":
        checkUsername();
        break;
      case "email":
        checkEmail();
        break;
      case "age":
        checkAge();
        break;
      case "phoneno":
        checkPhoneno();
        break;
      case "location":
        checklocation();
        break;
      case "aadharno":
        checkaadharno();
        break;
      case "password":
        checkPassword();
        break;
    }
  })
);

c_form.addEventListener(
  "input",
  debounce(function (e) {
    switch (e.target.id) {
      case "cin":
        checkcin();
        break;
      case "cname":
        checkcname();
        break;
      case "clocation":
        checkclocation(); // Fix the function name here
        break;
      case "cphoneno":
        checkcphoneno();
        break;
      case "cpassword":
        checkcPassword();
        break;
    }
  })
);
