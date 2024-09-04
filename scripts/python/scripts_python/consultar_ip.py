from requests import get 

def resolver_ip():
    servidor = get('https://api.ipify.org')
    # status_code = variable del sistema, solo recopila la informacion de la respuesta https en este caso 200
    if servidor.status_code==200:
        # text propiedad, pide a los datos obtenidos del servidor la ip 
        ip_publica = servidor.text
        return ip_publica
    else:
        return None
ip2=resolver_ip()

print(ip2)

# hola como estas 