# Importing necessary libraries
import discord
import asyncio
from colorama import Fore, init, Style

# ASCII art for visual appeal
print("\033[91m")
print(f"""
██████╗ ███████╗██╗  ██╗██╗   ██╗   ██████╗ ███████╗██╗   ██╗
██╔══██╗██╔════╝╚██╗██╔╝██║   ██║   ██╔══██╗██╔════╝██║   ██║
██║  ██║█████╗   ╚███╔╝ ██║   ██║   ██║  ██║█████╗  ██║   ██║
██║  ██║██╔══╝   ██╔██╗ ██║   ██║   ██║  ██║██╔══╝  ╚██╗ ██╔╝
██████╔╝███████╗██╔╝ ██╗╚██████╔╝██╗██████╔╝███████╗ ╚████╔╝ 
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ╚══════╝  ╚═══╝  
""")
print("\033[0m")

# Input for token and guild IDs
token = input(f'[>] Paste here your token: ')
guild_s = input('[>] Please enter guild ID of server what you want to copy: ')
guild = input('[>] Please enter guild ID where you want to paste it: ')
input_guild_id = guild_s
output_guild_id = guild
token = token
print("=============================================================================")

# Event handler for when the bot is ready
@client.event
async def on_ready():
    # Getting source and target guilds
    extrem_map = {}
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))

    # Cloning process
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print("Thanks for using this cloner made by dexu.dev")

# Initializing Discord client
client = discord.Client()

# Functions for printing messages with color codes
def print_add(message):
    print(f'{Fore.CYAN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.CYAN}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.ORANGE}[WARNING]{Style.RESET_ALL} {message}')

def print_error(message):
    print(f'{Fore.RED}[ERROR]{Style.RESET_ALL} {message}')

# Class for cloning guild elements
class Clone:
    # Method for deleting roles
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
        for role in guild_to.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    print_delete(f"Deleted Role: {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Delete Role: {role.name}")

    # Method for creating roles
    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != "@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Created Role {role.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Role: {role.name}")
            except discord.HTTPException:
                print_error(f"Unable to Create Role: {role.name}")

    # Method for deleting channels
    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Channel: {channel.name}")

    # Method for creating categories
    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
                print_add(f"Created Category: {channel.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Category: {channel.name}")
            except discord.HTTPException:
                print_error(f"Unable To Delete Category: {channel.name}")

    # Method for creating channels
    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        # Creating text channels
        channel_text: discord.TextChannel
        category = None
        for channel_text in guild_from.text_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        print_warning(f"Channel {channel_text.name} doesn't have any category!")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Created Text Channel: {channel_text.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Text Channel: {channel_text.name}")
            except discord.HTTPException:
                print_error(f"Unable To Creating Text Channel: {channel_text.name}")
            except:
                print_error(f"Error While Creating Text Channel: {channel_text.name}")

        # Creating voice channels
        category = None
        for channel_voice in guild_from.voice_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        print_warning(f"Channel {channel_voice.name} doesn't have any category!")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                        )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Created Voice Channel: {channel_voice.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Voice Channel: {channel_voice.name}")
            except discord.HTTPException:
                print_error(f"Unable To Creating Voice Channel: {channel_voice.name}")
            except:
                print_error(f"Error While Creating Voice Channel: {channel_voice.name}")

    # Method for deleting emojis
    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Deleted Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Deleting Emoji{emoji.name}")
            except discord.HTTPException:
                print_error(f"Error While Deleting Emoji {emoji.name}")

    # Method for creating emojis
    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        emoji: discord.Emoji
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(
                    name=emoji.name,
                    image=emoji_image)
                print_add(f"Created Emoji {emoji.name}")
            except discord.Forbidden:
                print_error(f"Error While Creating Emoji {emoji.name} ")
            except discord.HTTPException:
                print_error(f"Error While Creating Emoji {emoji.name}")

    # Method for editing guild information
    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read()
            except discord.errors.DiscordException:
                print_error(f"Can't read icon image from {guild_from.name}")
                icon_image = None
            await guild_to.edit(name=f'{guild_from.name}')
            if icon_image is not None:
                try:
                    await guild_to.edit(icon=icon_image)
                    print_add(f"Guild Icon Changed: {guild_to.name}")
                except:
                    print_error(f"Error While Changing Guild Icon: {guild_to.name}")
        except discord.Forbidden:
            print_error(f"Error While Changing Guild Icon: {guild_to.name}")

# Running the bot with the provided token (bot=False as it's a self-bot)
client.run(token, bot=False)