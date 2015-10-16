#!/usr/bin/python
# -*- enconding: utf-8 -*-
from latinoware.credentials import providers
from latinoware.compute import compute

# Obtendo as chaves de autenticacao
auth = providers.credentials

## AWS
#servers = compute('AWS', auth)
#conf = {"nome": "testelatino", "size": "m1.medium", "zona": 0, "imagem": "ami-9ed8c3f6"} # AWS

## Rackspace
servers = compute('RACKSPACE', auth)
conf = {"nome": "latinoteste", "size": "performance1-2", "zona": "iad", "imagem": "0976b31e-f6d7-4d74-81e9-007fca25067e"} # RAX

## Digital Ocean
#servers = compute('DIGITALOCEAN', auth)
#conf = {"nome": "latinoteste", "size": "2gb", "zona": "nyc1", "imagem": "12065782"} # DO


## Metodos
#i = servers.listar_imagens()
servers.criar_servidor(conf)
