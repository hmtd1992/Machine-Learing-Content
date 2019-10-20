import os
import platform
My_OS = platform.system()

env_name=input("Enter Virtual Environment Name:- ")
configuration_file=input('Enter the name of configuration file (Put the file in the current directory):- ')

enable_vir_env='pip3 install virtualenv'
os.system(enable_vir_env)
print("virtualenv Package Installed")

create_vir_env='virtualenv {}'.format(env_name)
os.system(create_vir_env)
print("Virtual Environment Created Successfully")

if(My_OS=='Linux'):
    activate_vir_env='source {}/bin/activate'.format(env_name)
elif(My_OS=='Windows'):
    activate_vir_env='{}\Scripts\activate'.format(env_name)

activate_vir_env='source {}/bin/activate'.format(env_name)
os.system(activate_vir_env)
print("Virtual Environment Activated Successfully")

install_packages='pip3 install -r {}'.format(configuration_file)
os.system(install_packages)
print("Packages Installed Successfully")

deactivate_vir_env='deactivate'
os.system(deactivate_vir_env)

print("Virtual Environment is ready to use")