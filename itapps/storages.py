from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "c1007012dcbs"
    account_key = "DS1EBYxckQHSlUUKYXVRnkUsEpjZYb5w95wufKVTALRhllh1+GDdaFHO9ypcuq5nFgOn/BnZ5cAG+AStzq3iUQ=="
    azure_container = "media"
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = "c1007012dcbs"
    account_key = "DS1EBYxckQHSlUUKYXVRnkUsEpjZYb5w95wufKVTALRhllh1+GDdaFHO9ypcuq5nFgOn/BnZ5cAG+AStzq3iUQ=="
    azure_container = "static"
    expiration_secs = None