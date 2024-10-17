const markdownTextarea = document.getElementById("markdown-text");
const generateButton = document.querySelector(".generate-btn");

function handleAddPageBreak() {
  const markdown_text = markdownTextarea.value;
  markdownTextarea.value = markdown_text.trim() + "\n\n[page-break]\n\n";
  markdownTextarea.focus();
}

function handleAddCoverTitle() {
  const markdown_text = markdownTextarea.value;
  markdownTextarea.value =
    markdown_text.trim() + "\n[cover-title]\n\n[cover-title]\n";
  markdownTextarea.focus();
}

function handleAddSectionTitle() {
  const markdown_text = markdownTextarea.value;
  markdownTextarea.value =
    markdown_text.trim() + "\n\n[section-title]  [section-title]\n";
  markdownTextarea.focus();
}

function handleSidebarMenuBtn() {
  const sidebar = document.querySelector(".sidebar");
  console.log(sidebar);

  sidebar.classList.toggle("sidebar-open");
}

function handleGenerate() {
  const markdown_text = markdownTextarea.value;

  if (!markdown_text) {
    showToast("Please provide some markdown or html to generate pdf!");
    return;
  }

  generateButton.disabled = true;

  const pageNumberCheckbox = document.getElementById("display-page-number");
  const themeRadio = document.querySelector("input[name='theme']:checked");

  const data = {
    markdown: markdown_text,
    display_page_number: pageNumberCheckbox?.checked || false,
    theme: themeRadio?.value || "light",
  };

  // else
  fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then(async (res) => {
    const blob = await res.blob();

    const pdfUrl = URL.createObjectURL(blob);
    window.open(pdfUrl);

    generateButton.disabled = false;

    // Revoke link after 2 minutes
    setTimeout(() => {
      URL.revokeObjectURL(pdfUrl);
    }, 120000);
  });
}
