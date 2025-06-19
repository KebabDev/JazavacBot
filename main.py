import discord
from discord.ext import commands
from discord import app_commands
from config import BOT_ID, JAZAVAC_IMG1, SIGMA_IMG1, JAZAVAC_IMG2, SIGMA_IMG2, JAZAVAC_IMG3, SIGMA_IMG3, NOT_JAZAVCI

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="j!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=1370815385200492634))
    await bot.change_presence(activity=discord.Game(name="Ivan je peder!"))

    print(f"[i] Logged in as {bot.user}")

async def is_user_jazavac(id):
    for not_jazavac in NOT_JAZAVCI:
        if id == not_jazavac:
            return False
    return True

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="jazavac", description="Da li je osoba jazavac?!", guild=discord.Object(id=1370815385200492634)) # Remove this later for global)
@app_commands.describe(user="Koga želiš nazvati jazavcem?")
async def jazavac(interaction: discord.Interaction, user: discord.User):
    is_jazavac = await is_user_jazavac(user.id)

    if is_jazavac:
        embed=discord.Embed(
            title="Jazavac",
            description=f"{user.mention} je jazavac!",
            color=discord.Color.green()
        )

        embed.set_image(url=JAZAVAC_IMG1)
    else:
        embed=discord.Embed(
            title="Sigma",
            description=f"{user.mention} je sigma!",
            color=discord.Color.red()
        )

        embed.set_image(url=SIGMA_IMG1)

    await interaction.response.send_message(embed=embed)

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="depresivan", description="Da li je jazavac depresivan? ;[", guild=discord.Object(id=1370815385200492634))
@app_commands.describe(user="Koga želiš nazvati depresivnim jazavcem?")
async def depresivan(interaction: discord.Interaction, user: discord.User):
    is_jazavac = await is_user_jazavac(user.id)

    if is_jazavac:
        embed=discord.Embed(
            title="Depresivni jazavac",
            description=f"{user.mention} je depresivan mali jazavac (pička mala) :[",
            color=discord.Color.green()
        )

        embed.set_image(url=JAZAVAC_IMG2)
    else:
        embed=discord.Embed(
            title="Sigma",
            description=f"{user.mention} je sigma (radi 200kg bench za zagrijavanje)",
            color=discord.Color.red()
        )

        embed.set_image(url=SIGMA_IMG2)

    await interaction.response.send_message(embed=embed)

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="uhvati", description="Prikaži uhvaćenog jazavca u 4k!", guild=discord.Object(id=1370815385200492634))
@app_commands.describe(user="Kog jazavca želiš uhvatiti u 4k?")
async def uhvati(interaction: discord.Interaction, user: discord.User):
    is_jazavac = await is_user_jazavac(user.id)

    if is_jazavac:
        embed=discord.Embed(
            title="Jazavac uhvaćen u 4k",
            description=f"Jazavac {user.mention} je uhvaćen na kameri! Prikaz uslikane fotografije:",
            color=discord.Color.green()
        )

        embed.set_image(url=JAZAVAC_IMG3)
    else:
        embed=discord.Embed(
            title="Sigma uhvaćen u 4K",
            description=f"Sigma {user.mention} je uhvaćen na kameri! Prikaz uslikane fotografije:",
            color=discord.Color.red()
        )

        embed.set_image(url=SIGMA_IMG3)

    await interaction.response.send_message(embed=embed)
    
bot.run(BOT_ID)