# api-visiona

# Configuração
sudo apt install make
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

docker run -p 5432:5432 --name dolphin-postgis -e POSTGRES_PASSWORD=admin -d postgis/postgis
# Rodar
docker exec -ti dolphin-postgis psql -U postgres
uvicorn main:app --reload
