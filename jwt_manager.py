from jwt import encode, decode

def create_token(data : dict) -> str:
    token: str = encode(payload=data, key= "secret_key", algorithm="HS256")#convertimos el contenido en token y le colocamos una clave
    return token

def validate_token(token : str) -> dict:
    data : str = decode(token, key= "secret_key", algorithms= ['HS256'])
    return data

'''
Como buenas practicas:
1- La información contenida en el payload es facilmente 
detectable, por lo que es importante que no vaya información 
sencible o podra ser hackeada.
2- La llave es gran parte de lo que da la seguridad en jwt, 
por lo que no debe quedar expuesta en el código y es sano 
usar un .env depronto con la libreria

pip install dotenv

3- la llave es mejor que no sea tan facil de decifrar por lo 
que se puede usar

https://www.allkeysgenerator.com/Random/Security-Encryption-Key-Generator.aspx

Nota:Buen video! Pero cuidado con lo que guardan en las 
tokens!

La clave secreta es necesaria para verificar que fueron 
creadas por nuestro server, pero no para ver el contenido 
que guardan (ya que solo las pasa a base64)

Páginas como jwt.io te enseñan sus componentes:

'''