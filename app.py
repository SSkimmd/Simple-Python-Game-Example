import util
import net
import os

def start():
    os.system("cls")

    cmd = util.Command([util.Option("\n|L| Login", "l", scene_login), 
                        util.Option("|C| Create Account", "c", scene_create)
    ]).get()


def scene_create():
    global user

    cmd = util.Command([util.Option("\n|Enter Username|")])

    cmd.register_oninput(net.create)
    user = cmd.get()
    util.user = user

    if user is not None:
        print(f"\n|Successfully Created Account: {user.username}")
        input("|Enter to continue: ")
        scene_main()
    else:
        scene_create()


def scene_login():
    global user

    cmd = util.Command([util.Option("\n|Enter Username|")])

    cmd.register_oninput(net.login)
    user = cmd.get()
    util.user = user

    if user is not None:
        print(f"\n|Successfully Logged In: {user.username}")
        input("|Enter to continue: ")
        scene_main()
    else:
        scene_login()

def scene_main():
    os.system("cls")

    print(f"\n|Logged In: {user.username}|")
    
    opt_store = util.Option("\n|S| Enter Store", "s", scene_store)
    opt_inventory = util.Option("|I| Enter Inventory", "i", scene_inventory)
    opt_quit = util.Option("\n|Q| Exit", "q", exit)

    cmd = util.Command([opt_store, opt_inventory, opt_quit])
    cmd.register_onfail(scene_main)
    cmd.get()

def scene_store():
    os.system("cls")

    print("\n|Box Store|")

    opt_common = util.Option("\n[C] Common Box", 'c', util.open_box, 'c')
    opt_uncommon = util.Option("[U] Uncommon Box", 'u', util.open_box, 'u')
    opt_rare = util.Option("[R] Rare Box", 'r', util.open_box, 'r')
    opt_quit = util.Option("\n[Q] Back", 'q', scene_main)


    cmd = util.Command([opt_common, opt_uncommon, opt_rare, opt_quit])
    cmd.register_onfail(scene_store)
    cmd.get()

    input()
    scene_store()

def scene_inventory():
    os.system("cls")

    print("\n|Inventory|")
    print("|Items: " + str(len(user.inventory)) + "|")
        
    for i, item in enumerate(user.inventory):
        print(f"\n|{i}|\n|name| {item['name']}\n|info| {item['description']}")
    input()
    scene_main()

user = None


if __name__ == "__main__":
    start()