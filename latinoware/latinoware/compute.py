#!/usr/bin/python
#-*- encoding: utf-8 -*-
# Daniel Bruno <dbruno@fedoraproject.org>
# Latinoware 2015

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

class compute():

    def __init__(self, provider, credentials):

        self.provider = str.upper(provider)
        # parâmetros de autenticação
        userkey = credentials[self.provider][0]['userkey']
        secret = credentials[self.provider][0]['secret']

        # Definindo o provedor
        if self.provider == 'AWS':
            provider_driver = Provider.EC2_US_EAST # DRIVER DA AMAZON
            cursor = get_driver(provider_driver)
            self.driver = cursor(userkey, secret)

        elif self.provider == 'DIGITALOCEAN':
            provider_driver = Provider.DIGITAL_OCEAN # DRIVER DA DIGITAL OCEAN
            cursor = get_driver(provider_driver)
            self.driver = cursor(secret, api_version='v2')

        elif self.provider == 'RACKSPACE':
            provider_driver = Provider.RACKSPACE # DRIVER DA RACKSPACE 
            cursor = get_driver(provider_driver)
            self.driver = cursor(userkey, secret, region='iad')


    def listar_sizes(self):
        # Listar os tipos de flavors disponiveis
        sizes = self.driver.list_sizes()
        return sizes

    def listar_servers(self):
        # Listar servidores existentes
        servers = self.driver.list_nodes()
        return servers 

    def listar_imagens(self):
        # Listar as imagens
        imagens = self.driver.list_images()
        return imagens

    def listar_regioes(self):
        # Listar regioes
        regions = self.driver.list_locations()
        return regions

    def criar_servidor(self, serverdata):

       sizes = self.listar_sizes()
       images = self.listar_imagens()
       size = [s for s in sizes if s.id == serverdata['size']][0]
       image = [i for i in images if i.id == serverdata['imagem']][0]

       if self.provider == 'AWS':
           # fedora AMI: ami-76dfc41e
            server = self.driver.create_node(name=serverdata['nome'],\
                 image=image, size=size)

       elif self.provider == 'DIGITALOCEAN':

            # Parametros para criar uma instancia Digital Ocean
            locations = self.listar_regioes()
            zona = [j for j in locations if j.id == serverdata['zona']][0]
            # Criando a instancia
            server = self.driver.create_node(name=serverdata['nome'], image=image,\
                     size=size, location=zona)
            
       elif self.provider == 'RACKSPACE':

            # Criando a instancia
            server = self.driver.create_node(name=serverdata['nome'], size=size,\
                     image=image)
