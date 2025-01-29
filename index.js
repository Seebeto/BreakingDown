const { Client, GatewayIntentBits, EmbedBuilder } = require('discord.js');
const { CHANNEL_ID1, CHANNEL_ID2, CHANNEL_ID3, ICONURL1 } = require('./config.js');
const keep_alive = require('./keep_alive.js')
require('dotenv').config();
const TOKEN = process.env.TOKEN;

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds, // สำหรับการเข้าถึงข้อมูลเซิฟเวอร์
    GatewayIntentBits.GuildMembers, // สำหรับการเช็คสมาชิกในเซิฟเวอร์
    GatewayIntentBits.GuildMessages, // สำหรับการอ่านข้อความในเซิฟเวอร์
    GatewayIntentBits.MessageContent, // สำหรับการอ่านเนื้อหาข้อความ
    GatewayIntentBits.GuildVoiceStates // สำหรับการติดตามการเปลี่ยนแปลงสถานะเสียง
  ]
});

client.once('ready', () => {
  console.log('╔═════════════════════════════════════╗');
  console.log('║   BreakingDown Bot Is Now Online!   ║');
  console.log('╚═════════════════════════════════════╝');
});

// เมื่อมีคนเข้าร่วม
client.on('guildMemberAdd', async (member) => {
  const channel = member.guild.channels.cache.get(CHANNEL_ID1);  // ใช้ CHANNEL_ID1
  const name = member.toString(); // ใช้ member.toString() แทน member.mention
  const serverName = member.guild.name;
  const embed = new EmbedBuilder()
    .setTitle("BreakingDown")
    .setURL("https://discord.gg/r9bGzAZHMe")
    .setDescription(`***มีคนเข้าร่วม ${serverName} Server !***`)
    .setColor(0x00ff1e)
    .setTimestamp()
    .setAuthor({ name: 'แจ้งเตือน' })
    .addFields({ name: 'ชื่อ', value: name, inline: false })
    .setFooter({
      text: "เวลาที่เข้า",
      iconURL: (ICONURL1),
    })
    .setThumbnail(member.user.avatarURL());

  await channel.send({ embeds: [embed] });
});

// เมื่อมีคนออกจาก
client.on('guildMemberRemove', async (member) => {
  const channel = member.guild.channels.cache.get(CHANNEL_ID1);  // ใช้ CHANNEL_ID1
  const name = member.toString(); // ใช้ member.toString() แทน member.mention
  const serverName = member.guild.name;
  const embed = new EmbedBuilder()
    .setTitle("BreakingDown")
    .setURL("https://discord.gg/r9bGzAZHMe")
    .setDescription(`***มีคนออกจาก ${serverName} Server !***`)
    .setColor(0xff0000)
    .setTimestamp()
    .setAuthor({ name: 'แจ้งเตือน' })
    .addFields({ name: 'ชื่อ', value: name, inline: false })
    .setFooter({
      text: "เวลาที่ออก",
      iconURL: (ICONURL1),
    })
    .setThumbnail(member.user.avatarURL());

  await channel.send({ embeds: [embed] });
});

// การติดตามการเปลี่ยนแปลงสถานะเสียง
client.on('voiceStateUpdate', (oldState, newState) => {
  const channel = client.channels.cache.get(CHANNEL_ID2);
  const channellog = client.channels.cache.get(CHANNEL_ID3);
  
  if (!channel || !channellog) {
    console.error('Channel not found!');
    return;
  }

  if (oldState.channelId !== newState.channelId) {
    if (!newState.channelId) { // ถ้าออกจากห้อง
      const embed = new EmbedBuilder()
        .setTitle(`${newState.member.user.tag}\nออกจาก\n${oldState.channel.name}`)
        .setColor(0xFF7373) // สีแดงเมื่อออกจากห้อง
        .setThumbnail(newState.member.user.avatarURL())
        .setAuthor({ name: newState.member.user.tag, iconURL: newState.member.user.avatarURL() });
      channel.send({ embeds: [embed] });
      console.log(`${newState.member.user.tag} ออกจาก [${oldState.channel.name}]`);
      channellog.send(`\`${newState.member.user.tag} ออกจาก [${oldState.channel.name}]\``);

    } else if (!oldState.channelId) { // ถ้าเข้าห้องใหม่
      const embed = new EmbedBuilder()
        .setTitle(`${newState.member.user.tag}\nเข้าร่วม\n${newState.channel.name}`)
        .setColor(0xc7ffab) // สีเขียวเมื่อเข้าห้องใหม่
        .setThumbnail(newState.member.user.avatarURL())
        .setAuthor({ name: newState.member.user.tag, iconURL: newState.member.user.avatarURL() });
      channel.send({ embeds: [embed] });
      console.log(`${newState.member.user.tag} เข้าร่วม [${newState.channel.name}]`);
      channellog.send(`\`${newState.member.user.tag} เข้าร่วม [${newState.channel.name}]\``);

    } else { // ถ้าย้ายห้อง
      const embed = new EmbedBuilder()
        .setTitle(`${newState.member.user.username}\nย้ายจาก\n${oldState.channel.name}\nไปยัง\n${newState.channel.name}`)
        .setColor(0x7da8ff) // สีน้ำเงินสำหรับการย้ายห้อง
        .setThumbnail(newState.member.user.avatarURL())
        .setAuthor({ name: newState.member.user.tag, iconURL: newState.member.user.avatarURL() });
      channel.send({ embeds: [embed] });
      console.log(`${newState.member.user.tag} ย้ายจาก [${oldState.channel.name}] ไปยัง [${newState.channel.name}]`);
      channellog.send(`\`${newState.member.user.tag} ย้ายจาก [${oldState.channel.name}] ไปยัง [${newState.channel.name}]\``);
    }
  }
});

client.login(TOKEN);
