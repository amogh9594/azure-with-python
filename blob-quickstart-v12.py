import os
import yaml
from azure.storage.blob import ContainerClient
'''
def load_config():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open(dir_root + '/config.yaml',"r") as yamlfile:
        return yaml.load(yamlfile,Loader=yaml.FullLoader)
'''
azure_storage_connectionstring = "DefaultEndpointsProtocol=https;AccountName=invoicedocument;AccountKey=f+k1Txhfm39DPTiVJvVUtZN0ROPsrX+IFbcuv7gk1z4s5ay9+Ga3iszz7C5ltg61S1fiSn/qRLEp7+hLc7gOZw==;EndpointSuffix=core.windows.net"
file_container_name = "testinvoice"
source_folder = "/home/openbravo/Downloads/dashboard/blob-quickstart-v12"

def get_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry

def upload(files,connection_string, connection_name):
    container_client = ContainerClient.from_connection_string(connection_string,connection_name)
    print("Uploading files...")

    for file in files:
        blob_client = container_client.get_blob_client(file.name)
        with open(file.path,"rb") as data:
            blob_client.upload_blob(data)
            print(f'{file.name} uploaded to blob.')


data_file = get_files(source_folder+"/data")
upload(data_file,azure_storage_connectionstring,file_container_name)
print(*data_file)