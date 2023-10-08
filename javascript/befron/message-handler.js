const { EmbedBuilder } = require("discord.js");

const logChannel = "";
let ghostping = require("./ghostping.json");

module.exports = { handleDeletedMsg };

function handleDeletedMsg(msg, client) {
  // Checks
  if (!msg.guildId || !ghostping[msg.guildId]) {
    return;
  }
  if (!ghostping[msg.guildId]["enabled"]) {
    return;
  }

  if (msg.mentions.users.size !== 0 || msg.mentions.everyone) {
    let mentions = {};
    mentions[msg.id] = [];

    for (user of msg.mentions.users) {
      mentions[msg.id].push(user[0]);
    }

    const amountOfUserIds = mentions[msg.id] ? mentions[msg.id].length : 0;
    const userIds = mentions[msg.id] ? mentions[msg.id].map((id) => `<@${id}>`).join(", ") : [];

    let embed = new EmbedBuilder()
      .setTitle("Ghost ping notification")
      .setDescription(
        `${
          amountOfUserIds == 0
            ? "@everyone"
            : `The user${amountOfUserIds === 1 ? "" : "s"} ${userIds} ${
                msg.mentions.everyone ? "and @everyone" : ""
              }`
        } \
        ${[0, 1].includes(amountOfUserIds) ? "was" : "were"} ghost pinged by <@${msg.author.id}>`
      )
      .addFields({ name: "Message", value: msg.content })
      .setColor("#ff007d")
      .setFooter({ text: `© Befron | ${msg.guild.name}`, ephemeral: true })
      .setTimestamp();

    client.channels.cache.get(msg.channelId).send({ embeds: [embed] });

    // Send it also in a log channel
    if (ghostping.log) {
      if (false) {
        client.channels.cache
          .get(logChannel)
          .send({ embeds: [embed.addFields({ name: "Channel", value: `<#${msg.channelId}>` })] });
      }
    }
  }
}
