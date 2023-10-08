const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");
const fs = require("node:fs");
let selfrole = require("../selfrole.json");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("self-role")
    .setDescription("Get or remove a role using this command")
    .addSubcommand((getSelfRole) =>
      getSelfRole
        .setName("get")
        .setDescription("Get a self-role")

        .addRoleOption((option) =>
          option.setName("role").setDescription("Set the role").setRequired(true)
        )
    ),
  async execute(interaction) {
    if (interaction.options.getSubcommand() === "get") {
    }
  },
};
