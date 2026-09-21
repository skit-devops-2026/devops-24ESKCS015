.PHONY: install test build run docker-build docker-up

install:
	cd client && npm ci
	cd server && npm ci

test:
	python3 -m unittest discover -s tests -p "test_*.py" -v

build:
	cd client && npm run build

run:
	cd client && npm run dev

docker-build:
	@echo "TODO: docker build for frontend and backend"

docker-up:
	docker compose up --build