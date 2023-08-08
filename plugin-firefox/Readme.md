Para testar sua extensão no Firefox, siga os passos abaixo:

1. Abra o Firefox no seu computador.

2. Digite "about:debugging" na barra de endereços e pressione Enter. Isso abrirá a página de depuração do Firefox.

3. Na página de depuração, clique na opção "Este Firefox" no menu lateral esquerdo.

4. Em seguida, clique no botão "Carregar suplemento temporário..." (ou "Load Temporary Add-on..." em inglês).

5. Navegue até a pasta onde você criou a extensão e selecione o arquivo `manifest.json`. Isso carregará temporariamente sua extensão no Firefox para fins de teste.

6. Agora, sua extensão deve aparecer na barra de ferramentas do Firefox, dependendo das configurações que você definiu no arquivo `manifest.json`.

7. Interaja com sua extensão para testar as funcionalidades que você implementou. Verifique se tudo funciona conforme o esperado.

8. Se necessário, use as ferramentas de desenvolvedor do Firefox (pressionando F12 ou clicando com o botão direito do mouse na extensão e selecionando "Inspecionar elemento") para depurar e verificar o comportamento da extensão.

9. Após testar e depurar sua extensão, você pode fazer as alterações necessárias no código e repetir o processo de carga temporária para testar novamente.

Lembre-se de que a carga temporária da extensão só permanecerá enquanto o Firefox estiver em execução. Se você fechar o navegador, precisará carregar a extensão temporariamente novamente na próxima vez que iniciar o Firefox.

Para fins de distribuição pública ou para testes mais avançados, você pode considerar a publicação da extensão na loja de extensões do Firefox. Isso permitirá que outros usuários instalem sua extensão diretamente no navegador sem a necessidade de carregamento temporário.