const { SlashCommandBuilder, EmbedBuilder, PermissionFlagsBits } = require("discord.js");
const fs = require("node:fs");
let selfrole = require("../selfrole.json");
let ghostping = require("../ghostping.json");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("setup")
    .setDescription("Setup command to set up commands.")
    .setDefaultMemberPermissions(PermissionFlagsBits.ManageGuild)

    .addSubcommand((ghostPing) =>
      ghostPing
        .setName("ghost-ping")
        .setDescription("Setup the ghost ping notifier.")

        .addBooleanOption((option) =>
          option
            .setName("enabled")
            .setDescription("Enable or disable the ghost-ping notifier.")
            .setRequired(true)
        )

        .addBooleanOption((option) =>
          option
            .setName("log")
            .setDescription("Toggle to log ghost pings (default: false).")
            .setRequired(false)
        )
    )

    .addSubcommandGroup((selfRole) =>
      selfRole
        .setName("self-role")
        .setDescription("Setup command to allow members to self-role")

        .addSubcommand((makeSelfRole) =>
          makeSelfRole
            .setName("make")
            .setDescription("Make a self-role")

            .addRoleOption((option) =>
              option.setName("role").setDescription("Set the role").setRequired(true)
            )
        )

        .addSubcommand((removeSelfRole) =>
          removeSelfRole
            .setName("delete")
            .setDescription("Delete a self-role")

            .addRoleOption((option) =>
              option.setName("role").setDescription("Set the role").setRequired(true)
            )
        )

        .addSubcommand((removeSelfRole) =>
          removeSelfRole.setName("list").setDescription("List all self-roles")
        )
    ),

  async execute(interaction) {
    if (interaction.options.getSubcommand() === "ghost-ping") {
      const enabled = interaction.options.getBoolean("enabled");
      const log = enabled ? interaction.options.getBoolean("log") ?? false : false;

      ghostping[interaction.guild.id] = { enabled: enabled, log: log };
      fs.writeFileSync("../ghostping.json", JSON.stringify(ghostping, null, 4));

      let embed = new EmbedBuilder()
        .setTitle("Ghost ping notifier")
        .setDescription(
          `The ghost-ping notifier is now ${enabled ? "enabled" : "disabled"} ${
            log ? "(logging is on)" : ""
          }`
        )
        .setColor("#ff007d")
        .setFooter({ text: `© Befron | ${interaction.guild.name}`, ephemeral: true })
        .setTimestamp();

      await interaction.reply({ embeds: [embed] });
    }

    if (interaction.options.getSubcommandGroup() === "self-role") {
      if (interaction.options.getSubcommand() === "make") {
        const role = `<@&${interaction.options.getRole("role")["id"]}>`;

        if (!selfrole[interaction.guild.id]) {
          selfrole[interaction.guild.id] = [];
        }

        if (!selfrole[interaction.guild.id].includes(role)) {
          selfrole[interaction.guild.id].push(role);

          fs.writeFileSync("./selfrole.json", JSON.stringify(selfrole, null, 4));

          let embed = new EmbedBuilder()
            .setTitle("Self role added succesfully")
            .setDescription(`Members can now get the ${role} role by doing:\n/self-role ${role}`)
            .setColor("#ff007d")
            .setFooter({ text: `© Befron | ${interaction.guild.name}`, ephemeral: true })
            .setTimestamp();

          await interaction.reply({ embeds: [embed] });
        } else {
          let embed = new EmbedBuilder()
            .setTitle("Self role already exists")
            .setDescription(`Members can already get this role by using:\n/self-role ${role}`)
            .setColor("#ff007d")
            .setFooter({ text: `© Befron | ${interaction.guild.name}`, ephemeral: true })
            .setTimestamp();

          await interaction.reply({ embeds: [embed] });
        }
      } else if (interaction.options.getSubcommand() === "delete") {
        const role = `<@&${interaction.options.getRole("role")["id"]}>`;

        if (selfrole[interaction.guild.id].includes(role)) {
          selfrole[interaction.guild.id].pop(role);

          fs.writeFileSync("./selfrole.json", JSON.stringify(selfrole, null, 4));

          let embed = new EmbedBuilder()
            .setTitle("Self role deleted succesfully")
            .setDescription(`The ${role} role was deleted succesfully from the self roles.`)
            .setColor("#ff007d")
            .setFooter({ text: `© Befron | ${interaction.guild.name}`, ephemeral: true })
            .setTimestamp();

          await interaction.reply({ embeds: [embed] });
        } else {
          let embed = new EmbedBuilder()
            .setTitle("Self role doesn't exist")
            .setDescription(
              `The role ${role} couldn't be deleted from the self roles as it's not there.`
            )
            .setColor("#ff007d")
            .setFooter({ text: `© Befron | ${interaction.guild.name}`, ephemeral: true })
            .setTimestamp();

          await interaction.reply({ embeds: [embed] });
        }
      } else if (interaction.options.getSubcommand() === "list") {
        if (Object.keys(selfrole[interaction.guild.id]) === 0) {
          console.log("error");
        }
        let embed = new EmbedBuilder()
          .setTitle("List of all self-roles")
          .setDescription(`${selfrole[interaction.guild.id].join(", ")}`)
          .setColor("#ff007d")
          .setFooter({ text: `© Befron | ${interaction.guild.name}`, ephemeral: true })
          .setTimestamp();

        await interaction.reply({ embeds: [embed] });
      }
    }
  },
};
