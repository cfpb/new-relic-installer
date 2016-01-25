VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.box = "centos65"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/centos-65-x64-virtualbox-puppet.box"

  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioners/provision.yml"
    ansible.verbose = 'v'
    ansible.vault_password_file = 'password.txt'
    ansible.extra_vars = "@license.yml"
    ansible.raw_arguments ='--extra-vars={"env_file":"../default_environment.yml"}'
    ansible.groups = {
        "php-app" => ["default"],
        "python-app" => ["default"],
    }
  end
end
