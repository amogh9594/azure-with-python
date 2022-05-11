# Azure With Python

## 1. Azure Form Recognizer [Form Recognizer Sample Labeling Tool](https://fott-2-1.azurewebsites.net/)
Azure Cognitive Services Form Recognizer is a cloud service that uses machine learning to recognize text and table data from form documents. 
* Custom models - Recognize field values and table data from forms. These models are trained with your own data, so they're tailored to your forms.
* Content API - Recognize text, table structures, and selection marks, along with their bounding box coordinates, from documents. Corresponds to the REST  
  service's Layout API.
* Prebuilt models - Recognize data using the following prebuilt models.  [code](https://github.com/amogh9594/azure-with-python/blob/main/Azure_Form_Rcognizer_For_invoice.ipynb)

Install Packages
```
pip install azure-ai-formrecognizer
```
```
pip install azure-identity
```
```
pip install azure-core
```
```
pip install azure-storage-blob
```

## Authenticate the client
In order to interact with the Form Recognizer service, you will need to create an instance of a client. An endpoint and credential are necessary to instantiate the client object. 

## Azure blob storage 
Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data. 
[Upload files to blob storage](https://github.com/amogh9594/azure-with-python/blob/main/blob-quickstart-v12.py)
