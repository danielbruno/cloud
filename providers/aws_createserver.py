from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import credentials

credential = credentials.identify('aws')

AWS_key = credential.getKey()
AWS_secret = credential.getSecret()

cls = get_driver(Provider.EC2_US_EAST)
driver = cls(AWS_key, AWS_secret)

sizes = driver.list_sizes()
#for size in sizes:
#    print size

images = driver.list_images()
#for image in images:
#    print image

EC2_IMAGE = "ami-21362b48"
EC2_SIZE = "m1.medium"

size = [s for s in sizes if s.id == EC2_SIZE][0]
image = [i for i in images if i.id == EC2_IMAGE][0]

# Crear instancia
node = driver.create_node(name="ServerName", image=image, size=size)
