1 PASSO:
RODAR O SERVIDOR:
Executamos no prompt de comando e colocamos o comando: python3 server.py

O servidor vai se comportar da seguinte forma:
 - Aparecerá a mensagem 'Aguardando conexão de um cliente' na tela e o programa ficará aguardando até que algum cliente entre.
 - Após a conexão do cliente, aparecerá na tela, 'Conectado em (IP, HOST)' os dados do cliente.
 - Após o cliente digitar o arquivo desejado, caso tudo saia como planejado, aparecerá na tela a mensage 'Arquivo enviado com sucesso'.
 - E o servidor será encerrado.
  
Obs: Para rodar o servidor, o arquivo de qualquer formato que deve ser enviado para o cliente deve estar na mesma pasta do arquivo servidor.py.

2 PASSO:
RODAR O CLIENTE:
Executamos no prompt de comando e colocamos o comando: python3 cliente.py

O cliente vai se comportar da seguinte forma:
 - Caso o servidor já esteja aberto e tudo ocorra como planejado, aparecerá na tela, a seguinte mensagem: 'Conectado com sucesso!'.
 - Em seguida, o programa vai pedir o arquivo que você deseja receber do servidor.
 - Após digitar o arquivo desejado e tudo ocorra como planejado, você irá receber uma mensagem informando que o arquivo foi recebido.

Obs: O arquivo recebido pelo cliente será recebido e armazenado na pasta onde está localizado o arquivo cliente.py.