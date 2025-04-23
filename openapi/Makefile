API_SPEC_PATH = openapi/openapi.json
OUTPUT_DIR = generated_code/openapi
GENERATOR = openapi-generator-cli

generate-client:
	$(GENERATOR) generate -i $(API_SPEC_PATH) -g python -o $(OUTPUT_DIR)

clean:
	rm -rf $(OUTPUT_DIR)
