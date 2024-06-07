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

function lexCode(code){
    fetch('/lexer', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://127.0.0.1:5000',
            'Access-Control-Credentials' : 'true'
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
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}

function parseCode(code){
    var codeLex = lexCode(code);
    fetch('/parser', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://127.0.0.1:5000',
            'Access-Control-Credentials' : 'true'
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
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar el código');
    });
}

function verifyCode(){
    var code = getInput();
    lexCode(code);
}

function parseCode(){
    var code = getInput();
    parseCode(code);
}