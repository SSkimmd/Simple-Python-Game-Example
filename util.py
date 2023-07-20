import requests
import json
import os
import random
import net

class Item(dict):
    def __init__(self, name, description):
        dict.__init__(self, name=name, description=description)

class User:
    def __init__(self, username: str, inventory):
        self.username = username
        self.inventory = inventory

class Option:
    def __init__(self, text: str = "", cmd: str = "", event = None, argument = None):
        self.text = text
        self.cmd = cmd

        self.event = event
        self.argument = argument

class Command:
    def __init__(self, options: list[Option]):
        self.options = options
        self.input_callback = None
        self.fail_callback = None

    def get(self):
        for option in self.options:
            print(option.text)
        cmd = input("|:  ").lower()

        #   Call registered callback with input from command
        if self.input_callback is not None:
            data = self.input_callback(cmd)
            return data

        for option in self.options:
            if cmd == option.cmd:
                if option.argument is not None and option.event is not None:
                    option.event(option.argument)
                    return
                else:
                    if option.event is not None:
                        option.event()
                return
        
        if self.fail_callback:
            self.fail_callback()
            return

        os.system("cls")
        self.get()

    def register_oninput(self, callback):
        if self.input_callback is None and len(self.options) == 1:
            self.input_callback = callback

    def register_onfail(self, callback, use_input: bool = False):
        if self.fail_callback is None:
            self.fail_callback = callback


def random_item(min: int, max: int):
    names = ["Sword", "Shield", "Bow", "Crossbow", "Health Potion"]
    chance = random.randint(min, max)

    name = names[chance]
    description = f"A {name}"

    return Item(name, description)


def open_box(type: str):
    if type == "c":
        item = random_item(0, 4)

        net.add_item(user.username, item)
    if type == "u":
        item = random_item(0, 4)
    if type == "r":
        item = random_item(0, 4)
    
    print(item['name'])
    return item

user = None