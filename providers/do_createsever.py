from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import credentials
c = credentials.identify('digitalocean')

DO_key = c.getKey()
DO_secret = c.getSecret()

cls = get_driver(Provider.DIGITAL_OCEAN)
driver = cls(DO_key, DO_secret)

sizes = driver.list_sizes()
images = driver.list_images()
locations = driver.list_locations()
droplets = driver.list_nodes()

DO_IMAGE = "6370882"
DO_SIZE = "65"
DO_LOCATION = "8"

size = [s for s in sizes if s.id == DO_SIZE][0]
image = [i for i in images if i.id == DO_IMAGE][0]
location = [j for j in locations if j.id == DO_LOCATION][0]
#droplet = [y for y in droplets if y.uuid == DO_UUID][0]

#node = driver.create_node(name="hadoop.localdomain", image=image, size=size,\
 #      location=location)

#driver.destroy_node(droplet)
