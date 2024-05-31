# Discord Bot para Gerenciamento de Servidor

Este bot de Discord foi desenvolvido usando a biblioteca `discord.py` para facilitar a interação e gerenciamento de um servidor específico através de comandos slash. Abaixo estão detalhadas as funcionalidades e instruções de uso.

## Funcionalidades

- **Lançar Moeda**: Permite ao usuário lançar uma moeda, resultando em "Cara" ou "Coroa".
- **Data e Hora Atual**: Mostra a data e a hora atual com formatação adequada.
- **Informações do Servidor**: Exibe detalhes sobre o servidor como nome, ID, data de criação, dono, número de membros e ícone.
- **Visualizar Avatar**: Mostra o avatar de um usuário especificado.
- **Comandos de Moderação**: Inclui funcionalidades para banir ou expulsar membros do servidor, com opções para adicionar uma razão explicativa.
- **Verificar Latência**: Apresenta a latência do bot em milissegundos.
- **Criar Embed Personalizado**: Permite a criação de mensagens embed personalizadas, disponível apenas para membros com o papel específico "subordinados".

## Pré-requisitos

Para executar este bot, você precisará:
- Python 3.8 ou superior.
- Biblioteca `discord.py`.
- Um token de bot do Discord, que você pode obter através do [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).

## Configuração e Instalação

1. Clone este repositório para sua máquina local usando `git clone`.
2. Instale as dependências necessárias com:
   ```bash
   pip install -r requirements.txt
