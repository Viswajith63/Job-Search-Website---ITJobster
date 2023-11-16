document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("resume-form");
  const resume = document.querySelector(".resume");

  form.addEventListener("submit", function (event) {
    // event.preventDefault();

    const data = new FormData(form);

    for (const key of data.keys()) {
      const element = document.getElementById(`resume-${key}`);
      if (element) {
        element.textContent = data.get(key);
      }
    }
    resume.style.display = "block";
  });
});

var submit_button = document.getElementById("submit_button");

submit_button.addEventListener("click", function(e) {
  var required = document.querySelectorAll("input[required]");
  required.forEach(function(element) {
    if(element.value.trim() == "") {
      element.style.borderColor = "red";
    } else {
      element.style.backgroundColor = "white";
    }
  });
});

function printResume() {
  const printWindow = window.open("", "", "width=800,height=600");
  const resumeHTML = document.querySelector(".resume").outerHTML;

  printWindow.document.open();
  printWindow.document.write(
    "<html><head><title>Print Resume</title></head><body>"
  );
  printWindow.document.write(resumeHTML);
  printWindow.document.write("</body></html>");
  printWindow.document.close();
  printWindow.print();
  printWindow.close();
}