document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Realize a autenticação aqui
    // Se bem-sucedido, redirecione para a página de senhas disponíveis
    window.location.href = '../pages/index.html';
});
