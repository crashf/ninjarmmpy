import os
os.environ['NRMM_KEY_ID'] = 'TC8RN6QGT8VJS8PFGE7V'
os.environ['NRMM_SECRET'] = 'kce6aa6t5c8mnmo7u3a18avpqb36efbd0eje74k4'

env_var_value = os.getenv('NRMM_KEY_ID')
if env_var_value is not None:
    print(f"Value of VARIABLE_NAME: {env_var_value}")
else:
    print("Environment variable VARIABLE_NAME is not set.")

# Using environ.get()
env_var_value = os.environ.get('NRMM_SECRET')
if env_var_value is not None:
    print(f"Value of VARIABLE_NAME: {env_var_value}")
else:
    print("Environment variable VARIABLE_NAME is not set.")

