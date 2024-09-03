### A basic Azure Function App that is deployed via zip upload to a storage account

Note: had to specify
```bash
azure-functions>=1.12.0
fastapi
pydantic==1.10.12
```
to avoid the error:
```bash
No module named 'pydantic_core._pydantic_core'
```

To deploy:
```bash
CONTAINTER_NAME=functionpackages
STORAGE_ACC_NAME=strtestname
FUNCTION_APP_NAME=fa-test-name
RESOURCE_GROUP=rg-test-name

pip install -r requirements.txt --target=".python_packages/lib/site-packages"
zip -r ../MyFunctionApp.zip . 
az storage blob upload --container-name $CONTAINTER_NAME --file ../MyFunctionApp.zip --name MyFunctionApp.zip --account-name $STORAGE_ACC_NAME --overwrite 
az functionapp restart --name $FUNCTION_APP_NAME --resource-group $RESOURCE_GROUP
```