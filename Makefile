run:
	uvicorn main:app --reload

init_alembic:
	alembic init alembic

migrations:
	alembic revision --autogenerate -m "auto migrate"

install_postgis:
	docker run -p 5432:5432 --name dolphin-postgis -e POSTGRES_PASSWORD=admin -d postgis/postgis
	
run_postgis:
	docker exec -ti dolphin-postgis psql -U postgres

psql:
	docker exec -ti dolphin-postgis psql -U postgres