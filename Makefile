install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	pylint --disable=R,C,W1203,W0702,E0611 app.py

build:
	docker build -t workout-change:latest .

run:
	docker run -p 8080:8080 workout-change

invoke:
	curl http://127.0.0.1:8080/calculate_bmr/male/72/172/23/1.3

run-kube:
	kubectl apply -f kube-hello-change.yaml

all: install lint