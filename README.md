<div align="center">
  <img alt="Discord Bot Banner" src="https://cdn.squarecloud.app/png/github-readme.png">
</div>

> 📌 **Note:** This README is written in Portuguese because this project was created as part of a YouTube tutorial in Portuguese.

<h1 align="center">bot-de-reaction-role</h1>

<p align="center">Um bot de Discord para gerenciar reaction roles, criado durante um tutorial no YouTube usando <a href="https://discordpy.readthedocs.io/en/stable/" target="_blank">discord.py</a>.</p>

---

Este projeto é um **bot de reaction roles** desenvolvido durante um vídeo no canal do YouTube da **Square Cloud**. Ele mostra como entregar e remover cargos automaticamente quando os membros reagem a uma mensagem com um emoji.

O vídeo que originou este projeto está disponível no YouTube:
https://youtu.be/E3uPTbR4GFU

## Funcionalidades

- `/rr create`: cria uma mensagem de reaction role em um canal
- `/rr add`: liga um emoji a um cargo em uma mensagem
- `/rr remove`: remove a ligação de um emoji com um cargo
- `/rr list`: lista os emojis e cargos configurados em uma mensagem
- Entrega e remove os cargos automaticamente quando os membros reagem

---

## ☁️ Como hospedar na Square Cloud

Nunca usou a Square Cloud? Siga os passos abaixo, na ordem: você vai criar uma conta, escolher um plano, criar o bot no Discord e enviar o projeto.

### 1️⃣ Crie sua conta na Square Cloud

Cadastre-se na [página de cadastro da Square Cloud](https://squarecloud.app/pt-br/signup) com o seu e-mail.

### 2️⃣ Escolha um plano

A hospedagem na Square Cloud precisa de um plano ativo, e o envio do passo 5 pede um, então escolha agora.

Este bot usa só **256 MB de RAM**: o **[plano Hobby](https://squarecloud.app/pt-br/pricing)** é suficiente e ainda sobra espaço para outros bots. Compare todos os planos e preços na [página de planos](https://squarecloud.app/pt-br/pricing).

### 3️⃣ Crie o bot no Discord

1. No [Discord Developer Portal](https://discord.com/developers/applications), clique em **New Application** e dê um nome ao bot.
2. Na aba **Bot**, clique em **Reset Token** e copie o token. Guarde-o em segredo: ele controla o seu bot.
3. Na mesma aba, em **Privileged Gateway Intents**, ative **Presence Intent**, **Server Members Intent** e **Message Content Intent**.
4. Convide o bot para o seu servidor: em **OAuth2 > URL Generator**, marque `bot` e `applications.commands`, dê a permissão **Manage Roles** e abra o link gerado.
5. No seu servidor, arraste o cargo do bot para **acima** dos cargos que ele vai entregar: o Discord só deixa um bot gerenciar cargos abaixo do dele.

### 4️⃣ Prepare o projeto

1. No topo desta página, clique em **Code > Download ZIP** e extraia o arquivo.
2. Abra a pasta extraída, selecione **todos os arquivos dentro dela** e compacte-os em um novo `.zip`. Compacte os arquivos, não a pasta: o `squarecloud.app` precisa ficar na raiz do zip.

### 5️⃣ Envie para a Square Cloud

1. Acesse a [página de upload da Square Cloud](https://squarecloud.app/pt-br/dashboard/new).
2. Selecione a opção de **zip** e envie o arquivo que você criou.
3. Abra **Configuração avançada** e adicione a variável de ambiente `TOKEN` com o token do bot (passo 3).
4. Clique em **Deploy**.

![Enviando um projeto para a Square Cloud](https://cdn.squarecloud.app/docs/articles/dashboard/uploading.gif)

### 6️⃣ Teste o bot

Use `/rr create` para criar a mensagem e `/rr add` para ligar um emoji a um cargo. Se o bot não responder, abra a aplicação no [dashboard da Square Cloud](https://squarecloud.app/pt-br/dashboard) e confira os logs.

📖 Mais detalhes no [guia de bots do Discord](https://docs.squarecloud.app/pt-br/tutorials/bots/discord) da documentação da Square Cloud.

---

## 💻 Rodando no seu computador

1. Instale as dependências: `pip install -r requirements.txt`
2. Preencha o `TOKEN` no arquivo `.env`.
3. Rode o bot: `python main.py`

Requer Python 3.10 ou mais recente.
