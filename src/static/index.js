const addSourceBtn = document.getElementById('add-source-btn');
const addSourceForm = document.getElementById('add-source-form');
const addFormFields = document.getElementById('add-form-fields');
const addFieldType = document.getElementById('add-field-type');

const addSourceFormSubmitButton = document.querySelector(
    '#add-source-form button[type="submit"]',
);
const addSourceFormCloseButton = document.querySelector(
    '#add-source-form button.close',
);
const messages = document.querySelectorAll('.message');

addSourceBtn.onclick = () => {
    addSourceForm.classList.add('show');
};

const closeAddSourceForm = () => {
    addSourceForm.classList.remove('show');
    // Hankkiutuu eroon GET-parametreista
    window.history.replaceState(null, '', window.location.pathname);
};

addSourceFormCloseButton.onclick = closeAddSourceForm;

const downloadButton = document.querySelector(
    '#download-btn'
)

downloadButton.onclick = () => {
    location.href = "/download";
}

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAddSourceForm();
});

messages.forEach((message) => {
    message.onclick = () => message.classList.add('hide');
});

// Generoidaan lomakekentät backendistä saadun JSON-datan perusteella
const updateFormFields = () => {
    const type = addFieldType.value ?? 'book';

    allFieldsHtml = '';

    for (const field of [
        ...formFields['common'],
        ...(formFields[type] ?? []),
    ]) {
        fieldHtml = `
<label for="add-field-${field.name}" class="${field.required ? 'required' : ''}">${field.name_friendly}</label>
<input type="${field.input_type}" name="${field.name}" placeholder="${field.name_friendly}" id="add-field-${field.name}" />
`;
        allFieldsHtml += fieldHtml;
    }

    addFormFields.innerHTML = allFieldsHtml;
};

updateFormFields();
addFieldType.onchange = updateFormFields;
