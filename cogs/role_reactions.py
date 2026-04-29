import json
import os
import discord
from discord.ext import commands
from discord import app_commands

DATA_FILE = "reaction_roles.json"

def load_data() -> dict:
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data:dict):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

class RoleReactions(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.data = load_data()
    
    rr = app_commands.Group(
        name="rr",
        description="Comandos de reaction role",
        default_permissions=discord.Permissions(manage_roles=True)
    )

    @rr.command(name="create", description="Cria uma mensagem de reaction role em um canal")
    async def rr_create(
        self,
        interaction:discord.Interaction,
        canal:discord.TextChannel,
        titulo:str,
        descricao:str
    ):
        embed = discord.Embed(title=titulo, description=descricao, color=discord.Color.blurple())
        msg = await canal.send(embed=embed)

        guild_id = str(interaction.guild_id)
        msg_id = str(msg.id)

        if guild_id not in self.data:
            self.data[guild_id] = {}

        self.data[guild_id][msg_id] = {
            "channel_id": canal.id,
            "reactions": {}
        }
        save_data(self.data)

        await interaction.response.send_message(f"Mensagem criada em {canal.mention}. Id da mensagem: `{msg.id}`", ephemeral=True)

    @rr.command(name="add", description="Adiciona uma nova reação à mensagem")
    async def rr_add(
        self,
        interaction:discord.Interaction,
        message_id:str,
        emoji:str,
        cargo:discord.Role
    ):
        guild_id = str(interaction.guild_id)
        
        if guild_id not in self.data or message_id not in self.data[guild_id]:
            await interaction.response.send_message("Mensagem não encontrada. Crie com /rr create", ephemeral=True)
            return
        
        channel_id = self.data[guild_id][message_id]["channel_id"]
        channel = interaction.guild.get_channel(channel_id)

        if not channel:
            await interaction.response.send_message("Canal de mensagem não encontrado.", ephemeral=True)
            return
    
        try:
            msg = await channel.fetch_message(int(message_id))
        except discord.NotFound:
            await interaction.response.send_message("Mensagem não encontrada no Discord.", ephemeral=True)
            return
        
        await interaction.response.defer(ephemeral=True)

        try:
            await msg.add_reaction(emoji)
        except discord.HTTPException:
            await interaction.followup.send("Emoji inválido ou sem permissão para reagir.", ephemeral=True)
            return
        
        self.data[guild_id][message_id]["reactions"][emoji] = cargo.id
        save_data(self.data)

        await interaction.followup.send(f"Emoji {emoji} configurado para o cargo {cargo.mention}", ephemeral=True)

    @rr.command(name="remove", description="Remove uma reação de uma mensagem")
    async def rr_remove(
        self,
        interaction:discord.Interaction,
        message_id:str,
        emoji:str
    ):
        guild_id = str(interaction.guild_id)

        if guild_id not in self.data or message_id not in self.data[guild_id]:
            await interaction.response.send_message("Mensagem não encontrada.", ephemeral=True)
            return
        
        reactions = self.data[guild_id][message_id]["reactions"]
        if emoji not in reactions:
            await interaction.response.send_message("Essa reação não está configurada nessa mensagem.", ephemeral=True)
            return
    
        channel_id = self.data[guild_id][message_id]["channel_id"]
        channel = interaction.guild.get_channel(channel_id)
        if channel:
            try:
                msg = await channel.fetch_message(int(message_id))
                await msg.clear_reaction(emoji)
            except (discord.NotFound, discord.HTTPException):
                pass

        del reactions[emoji]
        save_data(self.data)

        await interaction.response.send_message(f"Reação {emoji} removida", ephemeral=True)

    @rr.command(name="list", description="Lista as reações configuradas em uma mensagem")
    async def rr_list(
        self,
        interaction:discord.Interaction,
        message_id:str
    ):
        
        guild_id = str(interaction.guild_id)

        if guild_id not in self.data or message_id not in self.data[guild_id]:
            await interaction.response.send_message("Mensagem não encontrada.", ephemeral=True)
            return
        
        reactions = self.data[guild_id][message_id]["reactions"]
        if not reactions:
            await interaction.response.send_message("Nenhuma reação encontrada para esta mensagem", ephemeral=True)
            return
        
        lines = []
        for emoji, role_id in reactions.items():
            role = interaction.guild.get_role(role_id)
            role_name = role.mention if role else f"Cargo removido. {role_id}"
            lines.append(f"{emoji} -> {role_name}")
        
        embed = discord.Embed(
            title="Reações configuradas",
            description="\n".join(lines),
            color = discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return

        guild_id = str(payload.guild_id)
        message_id = str(payload.message_id)

        if guild_id not in self.data or message_id not in self.data[guild_id]:
            return
        
        emoji_str = str(payload.emoji)
        reactions = self.data[guild_id][message_id]["reactions"]

        if emoji_str not in reactions:
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        role = guild.get_role(reactions[emoji_str])
        if not role:
            return
        
        member = guild.get_member(payload.user_id) or await guild.fetch_member(payload.user_id)

        if not member:
            return
        
        try:
            await member.add_roles(role, reason="Reaction Role")
        except discord.Forbidden:
            pass
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload:discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return

        guild_id = str(payload.guild_id)
        message_id = str(payload.message_id)

        if guild_id not in self.data or message_id not in self.data[guild_id]:
            return
        
        emoji_str = str(payload.emoji)
        reactions = self.data[guild_id][message_id]["reactions"]

        if emoji_str not in reactions:
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        role = guild.get_role(reactions[emoji_str])
        if not role:
            return
        
        member = guild.get_member(payload.user_id) or await guild.fetch_member(payload.user_id)

        if not member:
            return
        
        try:
            await member.remove_roles(role, reason="Reaction Role removido")
        except discord.Forbidden:
            pass

async def setup(bot:commands.Bot):
    await bot.add_cog(RoleReactions(bot))