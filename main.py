import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/tips.eco.help"):
        await message.channel.send(
"""7 formas sencillas para proteger el medio ambiente
1. Cultiva tus propios alimentos.
2. Planta árboles.       
3. Ahorrar agua.    
4. Separa la basura.
5. Reutiliza todo lo que puedas.
6. No uses mucho el coche.
7. No quemar cosas.
8. En sus compras no use bolsas de plástico.
9. Use focos ahorradores.                                       
10. No dejes abierto el refrigerador.
11. No prenda los focos en el día.
12. Cuida el agua.
13. No estes en la ducha mucho tiempo. 
14. No seques tu pelo y ropa con secadoras, dejelo al sol.
15. Puedes donar a campañas.""")
        
    if message.content.startswith("/hello"):
        await message.channel.send("""Bienvenido, soy el Bot de Discord, EcoGreen.
                                    Te puedo ayudar a aprender algunos tips para ayudar al ecosistema!
                                    Escribe /tips.eco.help para ayudarte :D""")  
                                        

client.run("token aqui!")
