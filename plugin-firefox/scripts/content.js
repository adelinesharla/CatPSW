(function() {
    if (window.hasRun) {
      return;
    }
    window.hasRun = true;
  
    function handleFile(request, sender, sendResponse) {
      fetchFile(request.fileURL).then(fileContent => {
        sendToAPI(fileContent);
      });
    }
  
    function fetchFile(fileURL) {
      return fetch(fileURL).then(response => response.text());
    }
  
    function sendToAPI(fileContent) {
      const blob = new Blob([fileContent], { type: 'text/csv' });
      const formData = new FormData();
      formData.append('csv_file', blob);
  
      fetch('http://localhost:5000/passwords/import', {
        method: 'POST',
        body: formData
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
  
    // Assign handleFile as a listener for messages from the extension.
    browser.runtime.onMessage.addListener(handleFile);
  })();
  