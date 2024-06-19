import discord
from discord.embeds import Embed
import config
import say
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"คำสั่งพร้อมใช้งาน {len(synced)} คำสั่ง")
    print(f"╔═════════════════════════════════════╗")
    print(f"║         ไอ้ ฮ้ง Is Now Online         ║")
    print(f"╚═════════════════════════════════════╝")

@bot.tree.command(name='hong01', description='รูปไอ้ฮ้ง')
async def hong01(interaction):
    await interaction.response.send_message(f"https://i.ytimg.com/vi/j8Whob6XLNc/maxresdefault.jpg")

@bot.tree.command(name='hong', description='พี่ฮ้งแนะนำตัว')
async def hong(interaction: discord.Interaction):
    embed = discord.Embed(title="Hong",
                      description="สวัสดีครับผม **\"ฮ้ง\"**\nผู้เล่น SMW\nสามารถติดตามผลงานผมได้ที่ลิ้งด้านล่างได้เลย\n\n```Enjoy and excite```",
                      colour=0xeeff00)

    embed.set_author(name="พี่ฮ้งแนะนำตัวนะครับ")

    embed.add_field(name="```Facebook```",
                value="https://www.facebook.com/HONGKFC/",
                inline=False)

    embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkZaCIY-sC1LSkvZ28flLm1KUhGk04wBWvY2WY1MW5gA&s")

    embed.set_thumbnail(url="https://scontent.fphs2-1.fna.fbcdn.net/v/t39.30808-6/242804261_227095192810338_3566160038483885197_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEWlMUNR-9dZEoI_Nk1vMsY34PLGDz4peTfg8sYPPil5AtVcy9AchTTBH4mN2oWYf2N-SSZA4VJG0RBI7k3_OGj&_nc_ohc=qppL8lV0gMoAb4P9deE&_nc_ht=scontent.fphs2-1.fna&oh=00_AfAaFtwCbXdPcitBrcYNqEjhyPp42MHo_EpTvel_QMFlyg&oe=6627FAC3")

    embed.set_footer(text="พี่ฮ้ง",
                 icon_url="https://scontent.fphs2-1.fna.fbcdn.net/v/t39.30808-6/242804261_227095192810338_3566160038483885197_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEWlMUNR-9dZEoI_Nk1vMsY34PLGDz4peTfg8sYPPil5AtVcy9AchTTBH4mN2oWYf2N-SSZA4VJG0RBI7k3_OGj&_nc_ohc=qppL8lV0gMoAb4P9deE&_nc_ht=scontent.fphs2-1.fna&oh=00_AfAaFtwCbXdPcitBrcYNqEjhyPp42MHo_EpTvel_QMFlyg&oe=6627FAC3")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='smwdata', description='รวมลิ้งค์เว็บในข้อมูลต่างๆ')
async def smwdata(interaction: discord.Interaction):
    embed = discord.Embed(title="รวมลิ้งแหล่งข้อมูลเกม Summoners War",
                      description="**นี้ คุณ อยากได้แห่งข้อมูลเกม Summoners War สินะ\nผม ฮ้ง จัดให้เอง**",
                      colour=0xf5ed00)

    embed.set_author(name="/smwdata")

    embed.add_field(name="```เว็บ sw-tt.com```",
                value="```ในเว็บมี\nข้อมูลMonster\nข้อมูลตาราง 3 อินุ\nเครื่องมือคำนวนเทียบ ATK\nคำนวนเอสเซ้น\n>> https://sw-tt.com/ <<```",
                inline=True)
    embed.add_field(name="```คำสั่งบอทเพิ่มเติม```",
                value="```/hong = พี่ฮ้งแนะนำตัว\n/hong01 = รูปพี่ฮ้ง\n/smwdata = รวมลิ้งค์เว็บในข้อมูลต่างๆ```",
                inline=False)

    embed.set_image(url="https://media.discordapp.net/attachments/921227813619630100/921256910517317642/Ver4.gif?ex=6634675b&is=6621f25b&hm=722444e0f740d5882bbffdf6dcea723d8fda68b3ab4089446bb57eb62ffc3078&=&width=676&height=676")

    embed.set_footer(text="พี่ฮ้ง",
                 icon_url="https://scontent.fphs2-1.fna.fbcdn.net/v/t39.30808-6/242804261_227095192810338_3566160038483885197_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEWlMUNR-9dZEoI_Nk1vMsY34PLGDz4peTfg8sYPPil5AtVcy9AchTTBH4mN2oWYf2N-SSZA4VJG0RBI7k3_OGj&_nc_ohc=qppL8lV0gMoAb4P9deE&_nc_ht=scontent.fphs2-1.fna&oh=00_AfB6SQkLN4n3d5ECbxaLgMadnz1YsmGekRf0YZU5ydfNOA&oe=66286B43")

    await interaction.response.send_message(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for word in (say.usay1):
        if word in message.content.lower():
            response_message = random.choice(say.botsay1)
            await message.channel.send(response_message)
            break

bot.run(config.TOKEN)