import discord
import asyncio

#globals
quote_list = []
scarizard_server = None
mod_role = None
subscriber_role = None

quotes_on_cooldown = False
quote_cooldown_length = 10

with open("quotes.txt", "r", encoding="utf-8") as quotes:
    for line in quotes:
        quote_list.append(line)

client = discord.Client()

@client.event
async def on_ready():
    global scarizard_server
    global mod_role
    global subscriber_role
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    scarizard_server = client.get_server("redacted")
    mod_role = discord.utils.get(scarizard_server.roles, name="Scariguards")
    subscriber_role = discord.utils.get(scarizard_server.roles, name="Submeleons")
    print("Bot running...")

@client.event
async def on_message(message):
    global quotes_on_cooldown
    global quote_list
    if message.content.startswith("!quote") and not quotes_on_cooldown:
        if message.author.top_role >= subscriber_role:
            quotes_on_cooldown = True
            try:
                quoteIndex = int(message.content[7:])
                await client.send_message(message.channel, quote_list[quoteIndex]) #get the quote from index 6 of the message to the end
                await asyncio.sleep(quote_cooldown_length) #debounce quotes
                quotes_on_cooldown = False
            except:
                print("Invalid quote command sent: " + message.content)
                await asyncio.sleep(quote_cooldown_length) #debounce quotes
                quotes_on_cooldown = False
        else:
            print("Not authorized to request quote: " + message.author.name)
    if message.content.startswith("!addquote"):
        if message.author.top_role >= mod_role or message.author.id == "redacted":
            with open("quotes.txt", "a", encoding="utf-8") as quotes:
                try:
                    new_quote = message.content[10:]
                    quote_list.append(new_quote)
                    quotes.write(new_quote + "\n")
                    await client.send_message(message.channel, "Added quote number " + str(len(quote_list) - 1))
                except:
                    print("error saving quote:  " + message.content)
        else:
            print("Not authorized to add quote: " + message.author.name)

client.run('redacted')
