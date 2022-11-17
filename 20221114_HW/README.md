# VirtualBox and Vagrant [14 Nov 2022 Homework]

## The homework

- Virtualization
  1. Install VirtualBox in your machine
  2. Install Vagrant in your machine
  3. Stand up Fedora 35 VM Server
  4. Stand up Ubuntu 20.04.x Server LTS VM
- Concepts
  - Investigate: What is software architecture and how it is related to Enterprise Architecture

## What is VirtualBox?

VirtualBox is a hypervisor used to run operating systems in a special environment, called a virtual machine, on top of the existing operating system.

## What is Vagrant?

Vagrant is an open-source software product for building and maintaining portable virtual software development environments. Vagrant **IS NOT** a virtual machine provider so the user needs to have a provider as **_VirtualBox_**, **_Hyper-V_**, **_Docker_** or **_VMware_** to work with.

## Installing VirtualBox in Arch Based Linux

1. Install the [VirtualBox](https://archlinux.org/packages/?name=virtualbox) core packages

   ```
   ╰─λ sudo pacman virtualbox
   ```

2. Install host modules

   Can use [virtualbox-host-modules-arch](https://archlinux.org/packages/?name=virtualbox-host-modules-arch) for linux kernel

   ```
   ╰─λ sudo pacman virtualbox-host-modules-arch
   ```

   or can use [virtualbox-host-dkms](https://archlinux.org/packages/?name=virtualbox-host-dkms) for other kernels

   ```
   ╰─λ sudo pacman virtualbox-host-dkms
   ```

3. Install the appropiate headers package for the kernel

   Example: For linux-lts kernel can use [linux-lts-headers](https://archlinux.org/packages/?name=linux-lts-headers)

   ```
   ╰─λ sudo pacman linux-lts-headers
   ```

4. Validate install

   ```
   ╰─λ virtualbox -h
   Oracle VM VirtualBox VM Selector v7.0.2
   Copyright (C) 2005-2022 Oracle and/or its affiliates

   No special options.

   If you are looking for --startvm and related options, you need to use VirtualBoxVM.</pre>
   ```

   ## Installing Vagrant

5. Install the [Vagrant](https://archlinux.org/packages/?name=vagrant) package
   ```
   ╰─λ sudo pacman vagrant
   ```
6. Validate install
   ```
   ╰─λ vagrant -v
   Vagrant 2.3.2</pre>
   ```

## Using Vagrant

1. Start by exploring vagrant box subcommands

   ```
   ╰─λ vagrant box
   Usage: vagrant box <subcommand> [<args>]

   Available subcommands:
       add
       list
       outdated
       prune
       remove
       repackage
       update

   For help on any individual subcommand run `vagrant box &lt;subcommand&gt; -h`
           --[no-]color                 Enable or disable color output
           --machine-readable           Enable machine readable output
       -v, --version                    Display Vagrant version
           --debug                      Enable debug output
           --timestamp                  Enable timestamps on log output
           --debug-timestamp            Enable debug output with timestamps
           --no-tty                     Enable non-interactive output
   ```

2. Search for the box needed. It's possible to find many templates here [https://app.vagrantup.com/boxes/search](https://app.vagrantup.com/boxes/search)

3. After you find the template add it to vagrant. Using ubuntu/focal64 as example

   ```
   ╰─λ vagrant box add ubuntu/focal64
   ```

4. It can list all the local boxes ready to be mount in Vagrant using the following command

   ```
   ╰─λ vagrant box list
   generic/fedora35 (virtualbox, 4.2.2)
   ubuntu/focal64   (virtualbox, 20221107.0.0)
   ```

5. Create a dir to store the config file for the box

   ```
   ╰─λ mkdir ubuntu-vagrant-test
   ╰─λ cd ubuntu-vagrant-test
   ```

6. In created dir intialize vagrant

   ```
   ╰─λ vagrant init ubuntu/focal64

   A `Vagrantfile` has been placed in this directory. You are now
   ready to `vagrant up` your first virtual environment! Please read
   the comments in the Vagrantfile as well as documentation on
   `vagrantup.com` for more information on using Vagrant.
   ```

7. Stand the virtual machine
   ```
   ╰─λ vagrant up
   ```
8. Get inside command line of virtual machine

   ```
   ╰─λ vagrant ssh
   Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-131-generic x86_64)

   - Documentation: https://help.ubuntu.com
   - Management: https://landscape.canonical.com
   - Support: https://ubuntu.com/advantage

   System information as of Tue Nov 15 14:38:11 UTC 2022

   System load: 0.0 Processes: 121
   Usage of /: 3.5% of 38.70GB Users logged in: 0
   Memory usage: 20% IPv4 address for enp0s3: 10.0.2.15
   Swap usage: 0%

   0 updates can be applied immediately.

   The list of available updates is more than a week old.
   To check for new updates run: sudo apt update
   New release &apos;22.04.1 LTS&apos; available.
   Run &apos;do-release-upgrade&apos; to upgrade to it.

   vagrant@ubuntu-focal:~
   ```

9. Open VirtualBox to watch it running

    <img src="./Screenshot from 2022-11-15 09-40-25.png" alt="Screenshot of virtualbox" style="height: 500px; width: auto;"/>

10. To shutdown the virtual machine use
    ```
    ╰─λ vagrant halt
    ```
11. To destroy the virtual machine use
    ```
    ╰─λ vagrant destroy
    ```

## Vagrant on Arch considerations

1.  Be sure **_Safe Virtual Machine_** mode is enabled in your motherboard and OS
2.  In case of finding this error:

    ```
    The private key to connect to the machine via SSH must be owned
    by the user running Vagrant. This is a strict requirement from
    SSH itself. Please fix the following key to be owned by the user
    running Vagrant:

    /mnt/specific_dir/.vagrant/machines/default/virtualbox/private_key
    ```

    - If using NTFS format on file system, SSH won't work so it can be disabled on Vagrantfile adding this lines:

        ```ruby
        config.ssh.insert_key=false
        ```

    - If using a Linux file system check status with:

        ```
        stat /mnt/specific_dir/.vagrant/machines/default/virtualbox/private_key
        ```

        Check actual user with:

        ```
        id
        ```

        Set owner with

        ```
        chown '[username]' /mnt/specific_dir/.vagrant/machines/default/virtualbox/private_key
        ```
## Arquitecture

_"Más allá de los algoritmos y estructuras de datos de la computación; el diseño y especificación de la estructura global del sistema es un nuevo tipo de problema."_  **An introduction to Software Architecture, David Garlan & Mary Shaw** 

Architecture, referring to software, is a concept that emerged in the 1960s and refers to planning based on models, patterns and theoretical abstractions, when creating a piece of software of a certain complexity and as a prior step to any implementation. In this way, we have a detailed theoretical guide that allows us to understand how each of the pieces of our product or service will fit together.

Therefore, in architecture we call a pattern any general and reusable solution for recurring problems in software engineering in a given context, they are similar to the patterns used in programming, but specifically oriented to the structure at a higher and more generic level.

### Some design patterns

- Client-server pattern
- Layered pattern
- Master-slave pattern
- Model-View-Controller (MVC) pattern
- Broker pattern
- Pipelining pattern

([Read more...](https://openwebinars.net/blog/arquitectura-de-software-que-es-y-que-tipos-existen/))

### How Software Architecture is related to Enterprise Architecture
- Similarities
   + Methods for specifing architectures
   + Modeling language and meta models
   + Reuse approach
   + Using architecture templates & architecture patterns

</br>

- Diferences

|Enterprise|Software|
|-|-|
|Business requirements based|Functional and technological requirements based|
|Multi-system vision approach|User cases approach|
|Business scenarios|Software frameworks|
|Business strategy & Business operation guided|Software lifecycle guided|