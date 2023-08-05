========================
Zeep-adv: Python SOAP client + mtom with mime type management
========================

Based on : http://docs.python-zeep.org/
And this mtom extention : https://github.com/mvantellingen/python-zeep/pull/314/files

```
pip install python-zeep-adv
```

````python

    from zeep import Client

    client = Client('tests/wsdl_files/example.rst')
    client.service.ping()

```

This was developed for a specific usage and this code whould not be used for other puposes has it.

