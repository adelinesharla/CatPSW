// Listen for connections
chrome.runtime.onConnect.addListener(function(port) {
    if (port.name === 'importPasswords') {
        // Listen for messages
        port.onMessage.addListener(function(message) {
            // The message is the content of the file
            const fileContent = message.file;

            // Now you can use fileContent to import the passwords
            importPasswords(fileContent);
        });
    }
});

// Function to import passwords
function importPasswords(fileContent) {
    const formData = new FormData();
    const blob = new Blob([fileContent], {type: 'text/csv'});

    formData.append('csvFile', blob); 

    fetch('YOUR_API_URL/import', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        // Handle the API response here, if necessary.
        console.log(data);
    })
    .catch((error) => {
        // Handle the error, if necessary.
        console.error('Error when sending the file: ', error);
    });
}
