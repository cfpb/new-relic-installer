VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.box = "centos65"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/centos-65-x64-virtualbox-puppet.box"

  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioners/provision.yml"
    ansible.verbose = 'v'
    ansible.groups = {
        "php-app" => ["default"],
    }
  end
end
