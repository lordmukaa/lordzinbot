import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
import random

id_do_servidor = 000000000000000000 #colocar o ID do server

class CustomClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.define_commands()
        await self.tree.sync(guild=discord.Object(id=id_do_servidor))

    def define_commands(self):
        @self.tree.command(name='moeda', description='Lança uma moeda')
        async def slash_moeda(interaction: discord.Interaction):
            resultado = random.choice(['Cara', 'Coroa'])
            await interaction.response.send_message(f"A moeda caiu em: {resultado}", ephemeral=True)

        @self.tree.command(name='datahora', description='Mostra a data e hora atual')
        async def slash_datahora(interaction: discord.Interaction):
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            await interaction.response.send_message(f"A data e hora atual é: {agora}", ephemeral=True)

        @self.tree.command(name='serverinfo', description='Mostra informações do servidor')
        async def slash_serverinfo(interaction: discord.Interaction):
            guild = interaction.guild
            embed = discord.Embed(title="Informações do Servidor", color=discord.Color.purple())
            embed.add_field(name="Nome", value=guild.name, inline=True)
            embed.add_field(name="ID", value=guild.id, inline=True)
            embed.add_field(name="Criado em", value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
            embed.add_field(name="Dono", value=guild.owner.name, inline=True)
            embed.add_field(name="Membros", value=guild.member_count, inline=True)
            embed.set_thumbnail(url=guild.icon.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @self.tree.command(name='avatar', description='Mostra o avatar de um usuário')
        async def slash_avatar(interaction: discord.Interaction, user: discord.User):
            embed = discord.Embed(title=f"Avatar de {user.name}", color=discord.Color.purple())
            embed.set_image(url=user.display_avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @self.tree.command(name='ban', description='Bane um usuário')
        @app_commands.checks.has_permissions(ban_members=True)
        async def slash_ban(interaction: discord.Interaction, user: discord.User, reason: str = "Nenhuma razão fornecida"):
            await interaction.guild.ban(user, reason=reason)
            await interaction.response.send_message(f"{user.name} foi banido. Razão: {reason}", ephemeral=True)

        @self.tree.command(name='kick', description='Expulsa um usuário')
        @app_commands.checks.has_permissions(kick_members=True)
        async def slash_kick(interaction: discord.Interaction, user: discord.User, reason: str = "Nenhuma razão fornecida"):
            await interaction.guild.kick(user, reason=reason)
            await interaction.response.send_message(f"{user.name} foi expulso. Razão: {reason}", ephemeral=True)

        @self.tree.command(name='ping', description='Mostra a latência do bot')
        async def slash_ping(interaction: discord.Interaction):
            latency = self.latency * 1000  # Converte para milissegundos
            await interaction.response.send_message(f"Pong! Latência: {latency:.2f} ms", ephemeral=True)

        @self.tree.command(name='customembed', description='Cria um embed personalizado para ser enviado no servidor')
        @app_commands.describe(titulo='O título do embed', descricao='A descrição do embed', rodape='O rodapé do embed')
        @app_commands.checks.has_role("subordinados")
        async def slash_customembed(interaction: discord.Interaction, titulo: str, descricao: str, rodape: str):
            embed = discord.Embed(title=titulo, description=descricao, color=discord.Color.purple())
            embed.set_footer(text=rodape)
            await interaction.response.send_message(embed=embed, ephemeral=False)

    async def on_ready(self):
        print(f"Entramos como {self.user}.")


aclient = CustomClient()
aclient.run('Colocar a token do app')