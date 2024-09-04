# realizamos la instalacion de nuestra pila elastic
sudo parrot-upgrade -y 
#
sudo apt install wget apt-transport-https -y
#
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
#
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
#
sudo apt update && sudo apt install elasticsearch logstash kibana -y 
#################################################################

# Verificar si el archivo existe
archivo="/etc/elasticsearch/elasticsearch.yml"

# -f comprueba si el archivo existe 
if [ -f "$archivo" ]; then
# cambiamos configuraciones del archivo, por las de nuestro interes
  sudo sed -i 's/#cluster.name: my-application/cluster.name: pila_elk/g' "$archivo"
  sudo sed -i 's/#node.name: node-1/node.name: nodo_1/g' "$archivo"
  sudo sed -i 's/#network.host: 192.168.0.1/network.host: 0.0.0.0/g' "$archivo"
  sudo sed -i 's/#http.port: 9200/http.port: 9200/g' "$archivo"
  # agregamos en la ultima linea el tipo de nodo
  sudo echo discovery.type: single-node | sudo tee -a "$archivo"
  echo -e "\nEl archivo " $archivo " se ha editado correctamente\n"
  echo -e "\nAhora editamos kibana\n"
  sleep 5
else
  echo -e "\nEl archivo no existe.\n"
fi

echo -e "\nIniciamos elasticsearch\n"
systemctl start elasticsearch

# consultamos el estado nuestras configuraciones
curl -XGET http://localhost:9200/_cluster/health?pretty

archivo1="/etc/kibana/kibana.yml"
# pedimos la direccion ip del usuario para anexarla a nuestro fichero de configuracion
read -p  "dame la direccion tu ip   " ip

# Verificar si el archivo existe
# -f comprueba si el archivo existe 
if [ -f "$archivo1" ]; then
# Buscar y reemplazar las cadenas de interes 
  sudo sed -i 's/#server.port: 5601/server.port: 5601/g' "$archivo1"
  #sudo sed -i 's|#server.publicBaseUrl: ""|server.publicBaseUrl: "http://$ip:5601/"|g' "$archivo1"
  # escapamos para que sed pueda reconocer las variables y barras invertidas
  sudo sed -i "s|#server.publicBaseUrl: \"\"|server.publicBaseUrl: \"http://$ip:5601/\"|g" "$archivo1"
  sudo sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/g' "$archivo1"
  sudo sed -i 's/#server.name: "your-hostname"/server.name: "pila_kibana"/g' "$archivo1"
  #sudo sed -i 's/#elasticsearch.hosts: ["http://localhost:9200"]/elasticsearch.hosts: ["http://localhost:9200"]/g' "$archivo1"
  sudo sed -i 's/#elasticsearch.hosts: \["http:\/\/localhost:9200"\]/elasticsearch.hosts: \["http:\/\/localhost:9200"\]/g' "$archivo1"

  echo -e "\nReemplazo realizado correctamente.\n"
else
  echo -e "El archivo no existe."
fi

echo -e "\ninicializamos kibana\n"
systemctl start kibana
sleep 3
echo -e "\ndemonio elastic\n"
sleep 3
systemctl enable elasticsearch
echo -e "\ndemonio kibana\n"
sleep 3
systemctl enable kibana
