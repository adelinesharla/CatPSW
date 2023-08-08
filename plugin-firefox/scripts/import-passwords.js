// Event listener for when a file is selected
document.getElementById('csvFile').addEventListener('change', function(event) {
    // Get the selected file
    const selectedFile = event.target.files[0];
    document.getElementById('selectedFileName').innerText = 'Arquivo selecionado: ' + selectedFile.name;
    
    // Read the selected file
    const reader = new FileReader();
    reader.onload = function(event) {
        const fileContent = event.target.result;

        // Connect to the background script to import passwords
        const port = browser.runtime.connect({ name: 'importPasswords' });
        port.postMessage({ file: fileContent });
    }
    reader.readAsText(selectedFile);
});

document.getElementById('customLabel').addEventListener('click', function() {
    document.getElementById('csvFile').click();
});

// Function to display passwords
function displayPasswords() {
    // Logic to retrieve and display passwords
    // ...
}