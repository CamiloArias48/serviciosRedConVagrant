# -*- mode: ruby -*-
# vi: set ft=ruby :

# Created by: @CamiloArias47

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "destmon"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision "shell", path: "installStuff.sh"
  config.vm.synced_folder "pythonServer", "/home/vagrant" 
end
