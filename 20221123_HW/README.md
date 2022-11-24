# Ansible [23 Nov 2022 Homework]

## Creating Ansible Playbook with Archlinux VM and Ubuntu VM

1. Mount Archlinux and Ubuntu VM's (Using Vagrant for this example)
2. Set properties of ssh conection in remote-host (Ubuntu will be the remote host in this example)

```
╰─λ sudo nano /etc/ssh/sshd_config
```

Search and make sure the following options are set as follows:

```
PasswordAuthentication yes
ChallengeResponseAuthentication no
```

Then restart ssh service by using:

```
sudo systemctl restart sshd
```

3. Ask the remote-host for it's ip using:

```
╰─λ ip --brief addr show
lo          UNKNOWN     127.0.0.1
eth0        UP          192.10.101.40 ---> This is the IP Adress
```

4. Create ssh key in the local-host (Archlinux will be the localhost in this example) as follows:

```bash
╰─λ ssh-keygen -o
#Leave empty all the next options
```

5. Copy the key from the local-host to the remote host as follows:

```
╰─λ ssh-copy-id -i ~/.ssh/id_rsa.pub <username>@<IP adress>
```

In this example

```bash
╰─λ ssh-copy-id -i ~/.ssh/id_rsa.pub vagrant@192.10.101.40
#Say yes if it ask if you're sure to continue
#It will ask you for password this time
```

6. Test connection using:

```bash
╰─λ ssh vagrant@192.10.101.40
#Must not ask for password this time
```

7. Install Ansible in local-host:

```
╰─λ sudo pacman -Sy ansible
```

8. Create Host Inventory file. In this example will be called hosts. Include the information of remote-host.

```ansible
[servers]
server1 ansible_host=192.10.101.40

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

9. Test the Host Inventory file using:

```
╰─λ ansible-inventory -i <path or file> --list -y
```

In this example:

```
╰─λ ansible-inventory -i hosts --list -y
all:
  children:
    servers:
      hosts:
        server1:
          ansible_host: 192.10.101.40
          ansible_python_interpreter: /usr/bin/python3
    ungrouped: {}
```

10. Test ansible connection using:

```
╰─λ ansible all -i <path or file (Host Inventory file)> -m ping -u <username>
```

In this example:

```
╰─λ ansible all -i hosts -m ping -u vagrant
server1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

11. Create a playbook.yml in the same folder where is Host Inventory file

12. Set up the playbook.yml file:

```yml
---
- hosts: all
  become: true
  tasks:
    - name: Install Packages
      apt: name={{ item }} update_cache=yes state=latest
      loop: ["nginx", "vim"]
      tags: ["setup"]

    - name: Copy index page
      copy:
        src: index.html
        dest: /var/www/html/index.html
        owner: www-data
        group: www-data
        mode: "0644"
      tags: ["update", "sync"]
```

13. Add the example index.html file to the sema folder and write inside:

```html
<html>
  <head>
    <title>Testing Ansible Playbooks</title>
  </head>
  <body>
    <h1>Testing Ansible Playbooks</h1>
    <p>This server was set up using an Nginx playbook.</p>
  </body>
</html>
```

14. Execute the playbook using:

```
ansible-playbook -i hosts playbook.yml
```
