import discord
from discord.ext import commands
from discord import app_commands
from config import BOT_ID, JAZAVAC_IMG, SIGMA_IMG, NOT_JAZAVCI

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="j!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="Ivan je peder!"))

    print(f"[i] Logged in as {bot.user}")

async def is_user_jazavac(id):
    for not_jazavac in NOT_JAZAVCI:
        if id == not_jazavac:
            return False
    return True

@bot.tree.command(name="jazavac", description="Da li je osoba jazavac?!")
@app_commands.describe(user="Koga želiš nazvati jazavcem?")
async def jazavac(interaction: discord.Interaction, user: discord.User):
    is_jazavac = await is_user_jazavac(user.id)

    if is_jazavac:
        embed=discord.Embed(
            title="Jazavac",
            description=f"{user.mention} je jazavac!",
            color=discord.Color.green()
        )

        embed.set_image(url=JAZAVAC_IMG)
    else:
        embed=discord.Embed(
            title="Sigma",
            description=f"{user.mention} je sigma!",
            color=discord.Color.red()
        )

        embed.set_image(url=SIGMA_IMG)

    await interaction.response.send_message(embed=embed)
    
bot.run(BOT_ID)