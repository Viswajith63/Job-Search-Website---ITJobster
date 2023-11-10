// JavaScript to populate the resume fields from the forms and remove empty sections
document.getElementById("submit-button").addEventListener("click", function () {
  // Check and remove sections with empty input fields
  var nameElement = document.getElementById("name");
  if (
    nameElement &&
    document.getElementById("name-input").value.trim() === ""
  ) {
    nameElement.remove();
  }

  var jobTitleElement = document.getElementById("job-title");
  if (
    jobTitleElement &&
    document.getElementById("job-title-input").value.trim() === ""
  ) {
    jobTitleElement.remove();
  }

  var emailElement = document.getElementById("email");
  if (
    emailElement &&
    document.getElementById("email-input").value.trim() === ""
  ) {
    emailElement.remove();
  }

  var phoneElement = document.getElementById("phone");
  if (
    phoneElement &&
    document.getElementById("phone-input").value.trim() === ""
  ) {
    phoneElement.remove();
  }

  var websiteElement = document.getElementById("website");
  if (
    websiteElement &&
    document.getElementById("website-input").value.trim() === ""
  ) {
    websiteElement.remove();
  }

  var linkedinElement = document.getElementById("linkedin");
  if (
    linkedinElement &&
    document.getElementById("linkedin-input").value.trim() === ""
  ) {
    linkedinElement.remove();
  }

  // Check and remove sections with empty input fields
  var summaryElement = document.getElementById("summary");
  if (
    summaryElement &&
    document.getElementById("summary-input").value.trim() === ""
  ) {
    summaryElement.remove();
  }

  // Check and remove sections with empty input fields
  var degreeElement = document.getElementById("degree");
  if (
    degreeElement &&
    document.getElementById("degree-input").value.trim() === ""
  ) {
    degreeElement.remove();
  }

  var schoolElement = document.getElementById("school");
  if (
    schoolElement &&
    document.getElementById("school-input").value.trim() === ""
  ) {
    schoolElement.remove();
  }

  var educationYearElement = document.getElementById("education-year");
  if (
    educationYearElement &&
    document.getElementById("education-year-input").value.trim() === ""
  ) {
    educationYearElement.remove();
  }

  // Check and remove sections with empty input fields
  var jobTitleElementExp = document.getElementById("job-title-exp");
  if (
    jobTitleElementExp &&
    document.getElementById("job-title-input-exp").value.trim() === ""
  ) {
    jobTitleElementExp.remove();
  }

  var companyElement = document.getElementById("company");
  if (
    companyElement &&
    document.getElementById("company-input").value.trim() === ""
  ) {
    companyElement.remove();
  }

  var locationElement = document.getElementById("location");
  if (
    locationElement &&
    document.getElementById("location-input").value.trim() === ""
  ) {
    locationElement.remove();
  }

  var experienceDatesElement = document.getElementById("experience-dates");
  if (
    experienceDatesElement &&
    document.getElementById("experience-dates-input").value.trim() === ""
  ) {
    experienceDatesElement.remove();
  }

  var descriptionElement = document.getElementById("description");
  if (
    descriptionElement &&
    document.getElementById("description-input").value.trim() === ""
  ) {
    descriptionElement.remove();
  }
});

// JavaScript to trigger the print functionality and open a new window for printing
document.getElementById("print-button").addEventListener("click", function () {
  var printWindow = window.open("", "", "width=600,height=600");
  printWindow.document.open();
  printWindow.document.write(
    "<html><head><title>Print Resume</title></head><body>"
  );

  // Conditional checks before accessing outerHTML
  var nameElement = document.getElementById("name");
  if (nameElement) {
    printWindow.document.write(nameElement.outerHTML);
  }
  var jobTitleElement = document.getElementById("job-title");
  if (jobTitleElement) {
    printWindow.document.write(jobTitleElement.outerHTML);
  }
  var emailElement = document.getElementById("email");
  if (emailElement) {
    printWindow.document.write(emailElement.outerHTML);
  }
  var phoneElement = document.getElementById("phone");
  if (phoneElement) {
    printWindow.document.write(phoneElement.outerHTML);
  }
  var websiteElement = document.getElementById("website");
  if (websiteElement) {
    printWindow.document.write(websiteElement.outerHTML);
  }
  var linkedinElement = document.getElementById("linkedin");
  if (linkedinElement) {
    printWindow.document.write(linkedinElement.outerHTML);
  }

  // Check and remove sections with empty input fields
  var summaryElement = document.getElementById("summary");
  if (summaryElement) {
    printWindow.document.write(summaryElement.outerHTML);
  }

  // Check and remove sections with empty input fields
  var degreeElement = document.getElementById("degree");
  if (degreeElement) {
    printWindow.document.write(degreeElement.outerHTML);
  }
  var schoolElement = document.getElementById("school");
  if (schoolElement) {
    printWindow.document.write(schoolElement.outerHTML);
  }
  var educationYearElement = document.getElementById("education-year");
  if (educationYearElement) {
    printWindow.document.write(educationYearElement.outerHTML);
  }

  // Check and remove sections with empty input fields
  var jobTitleElementExp = document.getElementById("job-title-exp");
  if (jobTitleElementExp) {
    printWindow.document.write(jobTitleElementExp.outerHTML);
  }
  var companyElement = document.getElementById("company");
  if (companyElement) {
    printWindow.document.write(companyElement.outerHTML);
  }
  var locationElement = document.getElementById("location");
  if (locationElement) {
    printWindow.document.write(locationElement.outerHTML);
  }
  var experienceDatesElement = document.getElementById("experience-dates");
  if (experienceDatesElement) {
    printWindow.document.write(experienceDatesElement.outerHTML);
  }
  var descriptionElement = document.getElementById("description");
  if (descriptionElement) {
    printWindow.document.write(descriptionElement.outerHTML);
  }

  printWindow.document.write("</body></html>");
  printWindow.document.close();
  printWindow.print();
  printWindow.close();
});
