# VirtualBox and Vagrant [14 Nov 2022 Homework]

## What is VirtualBox?

VirtualBox is a hypervisor used to run operating systems in a special environment, called a virtual machine, on top of the existing operating system.

## What is Vagrant?

Vagrant is an open-source software product for building and maintaining portable virtual software development environments. Vagrant <strong>IS NOT</strong> a virtual machine provider so the user needs to have a provider as <font color="#33FCFF">VirtualBox</font>, <font color="#33FCFF">Hyper-V</font>, <font color="#33FCFF">Docker</font> or <font color="#33FCFF">VMware</font> to work with.

## Installing VirtualBox in Arch Based Linux

1. Install the [VirtualBox](https://archlinux.org/packages/?name=virtualbox) core packages

<pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">sudo</font> <font color="#33FCFF">pacman</font> <font color="#33FCFF">virtualbox</font></pre>

2. Install host modules

   Can use [virtualbox-host-modules-arch](https://archlinux.org/packages/?name=virtualbox-host-modules-arch) for linux kernel

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">sudo</font> <font color="#33FCFF">pacman</font> <font color="#33FCFF">virtualbox-host-modules-arch</font></pre>

   or can use [virtualbox-host-dkms](https://archlinux.org/packages/?name=virtualbox-host-dkms) for other kernels

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">sudo</font> <font color="#33FCFF">pacman</font> <font color="#33FCFF">virtualbox-host-dkms</font></pre>

3. Install the appropiate headers package for the kernel

   Example: For linux-lts kernel can use [linux-lts-headers](https://archlinux.org/packages/?name=linux-lts-headers)

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">sudo</font> <font color="#33FCFF">pacman</font> <font color="#33FCFF">linux-lts-headers</font></pre>

4. Validate install

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">virtualbox</font> <font color="#33FCFF">-h</font></pre>

   Reponse should look like this:

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">virtualbox</font> <font color="#33FCFF">-h</font>
    Oracle VM VirtualBox VM Selector v7.0.2
    Copyright (C) 2005-2022 Oracle and/or its affiliates
   
    No special options.
   
    If you are looking for --startvm and related options, you need to use VirtualBoxVM.</pre>

## Installing Vagrant

1. Install the [Vagrant](https://archlinux.org/packages/?name=vagrant) package

   <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">sudo</font> <font color="#33FCFF">pacman</font> <font color="#33FCFF">vagrant</font></pre>

2. Validate install
   <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">vagrant</font> <font color="#33FCFF">-v</font>
   </pre>

    Reponse should look like this:
    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#337DFF">vagrant</font> <font color="#33FCFF">-v</font>
    Vagrant 2.3.2</pre>

## Using Vagrant

1. Start by exploring vagrant box subcommands

   <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">vagrant</font> <font color="#2AA1B3">box</font></pre>

   ```
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

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">vagrant</font> <font color="#2AA1B3">box</font> <font color="#2AA1B3">add</font> <font color="#2AA1B3">ubuntu/focal64</font></pre>

4. It can list all the local boxes ready to be mount in Vagrant using the following command

    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">vagrant</font> <font color="#2AA1B3">box</font> <font color="#2AA1B3">list</font></pre>
    ```
    generic/fedora35 (virtualbox, 4.2.2)
    ubuntu/focal64   (virtualbox, 20221107.0.0)
    ```

5. Create a dir to store the config file for the box
   <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">mkdir</font> <font color="#2AA1B3">ubuntu-vagrant-test</font></pre>
   <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">cd</font> <font color="#2AA1B3">ubuntu-vagrant-test</font></pre>

6. In created dir intialize vagrant
   <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">vagrant</font> <font color="#2AA1B3">init</font> <font color="#2AA1B3">ubuntu/focal64</font></pre>
   ```
   A `Vagrantfile` has been placed in this directory. You are now
   ready to `vagrant up` your first virtual environment! Please read
   the comments in the Vagrantfile as well as documentation on
   `vagrantup.com` for more information on using Vagrant.
   ```
7. Stand the virtual machine
    <pre><font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">vagrant</font> <font color="#2AA1B3">up</font></pre>

8. Get inside command line of virtual machine
    <pre> <font color="#F66151"><b>╰─λ</b></font> <font color="#12488B">vagrant</font> <font color="#2AA1B3">ssh</font>
    Last login: Tue Nov 15 12:40:14 2022 from 10.0.2.2
    [vagrant@fedora35 ~]$</pre>

9. Open VirtualBox to watch it running


## Considerations

1. Be sure Safe Virtual Machine mode is enabled in your motherboard and OS
2. In case of finding this error:
    <pre><font color="#C01C28">The private key to connect to the machine via SSH must be owned</font>
    <font color="#C01C28">by the user running Vagrant. This is a strict requirement from</font>
    <font color="#C01C28">SSH itself. Please fix the following key to be owned by the user</font>
    <font color="#C01C28">running Vagrant:</font>

    <font color="#C01C28">/mnt/<font color="#FFE633">specific_dir</font>/.vagrant/machines/default/virtualbox/private_key</font>
    </pre>
