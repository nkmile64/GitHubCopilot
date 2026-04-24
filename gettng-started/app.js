// regex to match the phone number in the format (123) 456-7890
const phoneRegex = /^\(\d{3}\) \d{3}-\d{4}$/;

// test phoneRegex against the phone number
const phoneNumber = "(123) 456-7890";
if (phoneRegex.test(phoneNumber)) {
  console.log("The phone number is valid.");
} else {
  console.log("The phone number is invalid.");
}