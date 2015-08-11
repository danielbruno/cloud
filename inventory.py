#!/usr/bin/python

"""
"""

from libcloud.loadbalancer.providers import get_driver as get_driver_lb
from libcloud.loadbalancer.types import Provider
import ConfigParser

class inventory(object):

	def __init__(self, region):

		cfgfile = "inventory.cfg"
		# configuracoes do inventario
		self.config = ConfigParser.RawConfigParser()
		self.config.read(cfgfile)

		# Auth
		username = self.config.get("rackspace", "username")
		apikey = self.config.get("rackspace", "apikey")

		lb = get_driver_lb(Provider.RACKSPACE)
		self.loadbalancer = lb(username, apikey, region=region)

	def getLoadbalancers(self):
		"""
		Return a list with all loadbalancer objects
		"""
		lbs = []
		for i in self.loadbalancer.list_balancers():
			lbs.append(i)
		
		return lbs

	def makeInventory(self):

		inventoryFile = open(self.config.get("inventory", "file"), "w")
		
		lbs = self.getLoadbalancers()
		for lb in lbs:
			inventoryFile.write("["+lb.name+"]\n")
			for host in lb.list_members():
				inventoryFile.write(host.ip+"\n")
			inventoryFile.write("\n")
		inventoryFile.close()