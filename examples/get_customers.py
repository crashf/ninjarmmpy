import ninjarmmpy
import os

# Create our client
# Assuming we are storing our keys in environment variables we can access
client = ninjarmmpy.Client(
    AccessKeyID=os.environ.get('BDJOL0UG3BKVLHFGCGIM'),
    SecretAccessKey=os.environ.get('k5j8slrat6goabvd4obn9pm43e5k8h5v5g3097o6'),
    Europe=False
)
# Get list of organizations!
organizations = client.getOrganizations()
# Now we can print the organizations out to the terminal.
print(organizations)
