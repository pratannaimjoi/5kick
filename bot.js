const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

client.login('tokenNjY1NDI0MDA5NDcwNTQxODM1.XlkXQg.QF5JCvSp8f-uVzF7byPOT9YS7yw');
