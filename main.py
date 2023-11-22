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
        
    if message.content.startswith("/eco"):
        await message.channel.send("""El ecosistema es el conjunto de especies de un área determinada que interactúan entre ellas y con su ambiente abiótico;
                                    mediante procesos como la depredación, el parasitismo, la competencia y la simbiosis,
                                    y con su ambiente al desintegrarse y volver a ser parte del ciclo de energía y de nutrientes.""")
    
    if message.content.startswith("/recycle"):
        await message.channel.send("""El reciclaje es el proceso de recolección y transformación de materiales para convertirlos en nuevos productos.
                                    Estos deshechos, de otro modo, serían descartados como basura.
                                    ¿Qué tipos de reciclaje existen? 
                                    Existen algunos tipos de Reciclajes.
                                    Reciclaje mecánico.
                                    Reciclaje químico. 
                                    Reciclaje energético. 
                                    Reciclaje por residuo. 
                                    Reciclaje de papel y carton. 
                                    Reciclaje de plástico. 
                                    Reciclaje de vidrio. 
                                    Reciclaje del textil y calzado. """)
                                        

client.run("MTE3Njk4Mjk3NDkyODAwMzE3Mg.GMGXNC.hauv-4WIujj5G9LatX6onVzAdlO2hU3dNpgxZ0")
