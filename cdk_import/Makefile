account-name ?=
account-id ?=
infra-stack ?=

.PHONY: help init deploy set-credentials destroy

help:
	@echo "Usage: make [target] account-name=$(account-name) account-id=$(account-id) infra-stack=$(infra-stack)"
	@echo ""
	@echo "Targets:"
	@echo "	install-dev			Install required libraries for local development"
	@echo "	deploy				Deploy CICD for all Observability Tools associated to an account (Assuming config file is exists)"
	@echo "	setup				(Optional) Deploy basic infrastructure resources needed by Observability Tools CICD"
	@echo "	destroy				Remove all CICD and Observability Tools associated to an account"

init:
	@echo "Under construction..."

install-dev:
	pip3 install -r requirements-dev.txt

setup:
	cdk deploy -a "python codepipeline_infra_setup.py $(account-id)" CodePipelineInfraSetup

deploy:
ifeq ($(account-name),)
	$(error account-name is not set. Please specify with account-name=aws-account-name)
else
	cdk deploy --app "python app.py $(account-name)"
endif

destroy:
	@echo "Under construction..."
