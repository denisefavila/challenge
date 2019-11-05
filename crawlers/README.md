
# Crawler

O Reddit é um site de mídia social no qual os usuários podem divulgar ligações para conteúdo na Web.
Os otros usuários podem então votar positiva ou negativamente nas ligações divulgadas, fazendo com que apareçam de uma forma mais ou menos destacada na sua página inicial

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas threads.

Neste projeto temos um bot no telegram com um crawler do reddit que nos fornece as top threads daquele momento : as threads recentes que estão bombando com mais de 5mil votos.

## Utilização
O bot do telegram se chama RedditBot e pode ser encontrado pelo link http://t.me/da_reddit_bot. 

Para ativá-lo você deve deixar o arquivo main.py em execução. 

Para obter as threads você deve enviar \NadaPraFazer + os nomes dos subreddits separados por ponto-virgula:

ex. `\NadaPraFazer cats;dogs`

Se você deseja obter os resultados no terminal, você só precisar passar como parâmetro

`--debugger subreddits, -d subreddits`
