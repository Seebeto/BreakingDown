import discord
import png
import config
from discord.ext import commands
import datetime
from datetime import datetime
from myserver import server_on
import os

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"╔═════════════════════════════════════╗")
    print(f"║   Breaking Down Bot Is Now Online   ║")
    print(f"╚═════════════════════════════════════╝")

#-----------------------------------------------------------------
# เช็คคนเข้าออกหรือย้ายห้องเสียง
@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(config.CHANNEL_ID2)  # แทน YOUR_CHANNEL_ID ด้วย ID ของช่องที่ต้องการส่งข้อความ
    channellog = bot.get_channel(config.CHANNEL_ID3)
    if before.channel != after.channel:  # ตรวจสอบว่าสมาชิกเคยอยู่ใน voice channel หรือไม่
        if after.channel is None:  # ถ้าเข้าห้องแล้วออก
            embed = discord.Embed(
                title=f"{member.name} \nออกจาก \n{before.channel.name}",
                color=discord.Color.red(),
            )
            embed.set_thumbnail(url=member.avatar)  # เพิ่มรูปโปรไฟล์ของสมาชิก
            embed.set_author(name=member.name, icon_url=member.avatar)  # เพิ่มข้อมูลผู้แต่ง
            await channel.send(embed=embed)
            print(f"{member.name} ออกจาก [{before.channel.name}]")
            await channellog.send(f"`{member.name} ออกจาก [{before.channel.name}]`")


        elif before.channel is None:  # ถ้ายังไม่ได้เข้าห้อง
            embed = discord.Embed(
                title=f"{member.name} \nเข้าร่วม \n{after.channel.name}",
                color=discord.Color.green(),
            )
            embed.set_thumbnail(url=member.avatar)  # เพิ่มรูปโปรไฟล์ของสมาชิก
            embed.set_author(name=member.name, icon_url=member.avatar)  # เพิ่มข้อมูลผู้แต่ง
            await channel.send(embed=embed)
            print(f"{member.name} เข้าร่วม [{after.channel.name}]")
            await channellog.send(f"`{member.name} เข้าร่วม [{after.channel.name}]`")

        else:  # ถ้าย้ายจากห้องไปห้อง
            embed = discord.Embed(
                title=f"{member.name} \nย้ายจาก \n{before.channel.name} \nไปยัง \n{after.channel.name}",
                color=discord.Color.blue(),
            )
            embed.set_thumbnail(url=member.avatar)  # เพิ่มรูปโปรไฟล์ของสมาชิก
            embed.set_author(name=member.name, icon_url=member.avatar)  # เพิ่มข้อมูลผู้แต่ง
            await channel.send(embed=embed)
            print(f"{member.name} ย้ายจาก [{before.channel.name}] ไปยัง [{after.channel.name}]")
            await channellog.send(f"`{member.name} ย้ายจาก [{before.channel.name}] ไปยัง [{after.channel.name}]`")
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# เช็คเข้าออกเซิฟ
@bot.event # เช็คคนเข้า
async def on_member_join(member):
    channel = bot.get_channel(config.CHANNEL_ID1)
    name = member.mention
    server_name = member.guild.name
    embed = discord.Embed(title="BreakingDown",
                      url="https://discord.gg/vSTy94Ec9W",
                      description=f"***มีคนเข้าร่วม {server_name} Server !***",
                      colour=0x00ff1e,
                      timestamp=datetime.now())
    embed.set_author(name="แจ้งเตือน")
    embed.add_field(name="ชื่อ",
                value=f"{name}",
                inline=False)
    embed.set_footer(text="เวลาที่เข้า",
                     icon_url=png.profilebot)
    embed.set_thumbnail(url=member.avatar)  # ตั้งภาพรูปโปรไฟล์ของสมาชิก
    await channel.send(embed=embed)

@bot.event # เช็คคนออก
async def on_member_remove(member):
    channel = bot.get_channel(config.CHANNEL_ID1)
    name = member.mention
    server_name = member.guild.name
    embed = discord.Embed(title="BreakingDown",
                      url="https://discord.gg/vSTy94Ec9W",
                      description=f"***มีคนออกจาก {server_name} Server !***",
                      colour=0xff0000,
                      timestamp=datetime.now())
    embed.set_author(name="แจ้งเตือน")
    embed.add_field(name="ชื่อ",
                value=f"{name}",
                inline=False)
    embed.set_footer(text="เวลาที่เข้า",
                     icon_url=png.profilebot) 
    embed.set_thumbnail(url=member.avatar)  # ตั้งภาพรูปโปรไฟล์ของสมาชิก
    await channel.send(embed=embed)
#-----------------------------------------------------------------

server_on()
bot.run(os.getenv('TOKEN'))
