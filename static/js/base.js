function showToast(message) {
  const toast = document.querySelector(".toast");
  const toastText = document.querySelector(".toast-text");

  if (toast.classList.contains("toast-visible")) {
    return;
  }

  toastText.innerHTML = message;

  toast.classList.add("toast-visible");

  // Remove the toast after a delay
  setTimeout(() => {
    toast.classList.remove("toast-visible");
    // toast.classList.add("toast-hidden");
  }, 3000); // Show the toast for 3 seconds
}
