import sys
import virtualbox
vbox = virtualbox.VirtualBox()

if len(sys.argv) < 2:
    print('You need to specify the action tu execute')
    sys.exit()

input_request = sys.argv[1]

if input_request == "list":
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()
    for m in vbox.machines:
        print(m.name)

if input_request == "up":
    if len(sys.argv) < 3:
        print('You need to specify the box name to stand up')
        sys.exit()
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()
    name = sys.argv[2]
    session = virtualbox.Session()
    machine = vbox.find_machine(name)
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()

if input_request == "create":
    if len(sys.argv) < 3:
        print('You need to specify the name of the box')
        sys.exit()
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()
    name = sys.argv[2]
    machine = vbox.create_machine("", name, [], "Linux", "")
    vbox.register_machine(machine)
    sys.exit()

if input_request == "delete":
    if len(sys.argv) < 3:
        print('You need to specify the name of the box')
        sys.exit()
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        sys.exit()
    name = sys.argv[2]
    machine = vbox.find_machine(name)
    machine.rm(delete=True)
    sys.exit()
