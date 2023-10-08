const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("kick")
    .setDescription("Kick a user from the server")
    .addUserOption((option) =>
      option.setName("user").setDescription("Select a user to kick").setRequired(true)
    )
    .addStringOption((option) =>
      option.setName("reason").setDescription("Reason for the kick").setRequired(false)
    ),

  // The code getting executed
  async execute(interaction) {
    const member = interaction.options.getMember("user");
    const reason =
      interaction.options.getString("reason") || language(interaction.guild, "NO_REASON_PROVIDED");

    if (!member.bannable) {
      return interaction.reply("Unable to kick this user.");
    }

    try {
      await member.kick({ reason: reason });
      await interaction.reply(`${member.user.tag} has been kicked.`);
    } catch (error) {
      console.error(error);
      await interaction.reply("There was an error trying to kick this user.");
    }
  },
};
