
function updateLineNumbers() {
    const editor = document.getElementById('code-editor');
    const lineNumbers = document.getElementById('line-numbers');
    
    const lines = editor.value.split('\n').length;
    lineNumbers.innerHTML = Array(lines).fill('').map((_, index) => index + 1).join('<br>');
}

function syncScroll() {
    const editor = document.getElementById('code-editor');
    const lineNumbers = document.getElementById('line-numbers');
    lineNumbers.scrollTop = editor.scrollTop;
}

document.addEventListener('DOMContentLoaded', function() {
    updateLineNumbers();
});

function getInput(){
    var code = document.getElementById("code-editor").value;
    return code;
}

function lexCode(){
    var code = getInput();
    fetch('http://127.0.0.1:5000/lexer', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ codeInput: code })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al enviar el código al backend');
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del backend:', data);
        if (data.error) {
            alert('Error en el análisis del código: ' + data.error);
        } else {
            var resultJSON = JSON.stringify(data);
            var result = JSON.parse(resultJSON);
            showResults(result);
        }       
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}

function parseCode(){
    var code = getInput();
    fetch('http://127.0.0.1:5000/parser', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ codeInput: code })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al enviar el código al backend');
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del backend:', data);
        if (data.error) {
            alert('Error en el análisis del código: ' + data.error);
        } else {
            var resultJSON = JSON.stringify(data);
            var result = JSON.parse(resultJSON);
            showResults(result);
        }  
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}

function showResults(resultJSON) {
    // Parse the JSON string into an object
    var result = JSON.parse(JSON.stringify(resultJSON));
    
    // Get the textarea element
    var resultsTextarea = document.getElementById('results');
    
    // Initialize an empty string to hold the results
    var resultsText = '';
    
    // Iterate over the result object to construct the results text
    Object.keys(result).forEach(index =>{
        let content = result[index].content
        let result2 = result[index].result

        resultsText += `${content}\n`
    });
    
    // Set the results text to the textarea
    resultsTextarea.value = resultsText;
}