import sys
import json



class player:
    player_items=[]
    player_room=0

    def go(self, direction, exits):
        if direction in exits:
            print("You go "+direction+".\n")
            self.player_room=self.player_room+1
            return False
        else:
            print("There's no way to go "+direction+".")
            return True
    def look(self):
        return False
    def inventory(self):
        if len(self.player_items)>=1:
            print("Inventory:")
            for i in range(len(self.player_items)-1):
                print(self.player_items[i], end=" ")
            if len(self.player_items)>=1:
                print(self.player_items[-1])
            return False
        else:
            print("You're not carring anything.")
            return True
    def get(self, item, items):
        if item in items:
            print("You pick up the "+item+".")
            self.player_items.append(item)
            rooms[self.player_room]['items'].remove(item)
        else:
            print("There's no "+item+" anywhere.")
            return True
    def drop(self, item):
        if item in self.player_items:
            print("You drop the "+item+".")
            self.player_items.remove(item)
            rooms[self.player_room]['items'].append(item)
            return True
        else:
            print("You don't have "+item+" to drop.")
            return True
    def quit():
        return True
    def win(self):
        if rooms[self.player_room]==rooms[len(rooms)-1]:
            print("You win")
        else:
            print("You Lose")

        

f = open(sys.argv[1], "r")
try:
    with open(sys.argv[1]) as f:
        rooms = json.load(f)
except ValueError as err:
        print("False")
def main():
    global rooms
    p = player()
    while p.player_room<len(rooms):
        print("> "+rooms[p.player_room]['name']+"\n")
        print(rooms[p.player_room]['desc']+"\n")
        print('Exits: ', end = "")
        exits = list(rooms[p.player_room]['exits'].keys())
        for x in range(0,len(exits)-1):
            print(exits[x], end=' ')
        print(exits[-1]+"\n")
        if(len(list(rooms[p.player_room].keys()))>=4):
            items = rooms[p.player_room]['items']
            if(len(items)>=1):
                print('Items:', end = " ")
                for x in range(0,len(items)-1):
                    print(items[x], end=' ')
                print(items[-1])
        else:
            rooms[p.player_room]['items']=[]
            items = rooms[p.player_room]['items']
        to_repeat = True
        while to_repeat:
            action = input("What would you like to do? ")
            action = action.lower()
            action = action.split(" ")
            if action[0] == 'quit':
                p.quit()
                print('Goodbye!')
                return 0
            if action[0] == 'go':
                if len(action)>=2:
                    to_repeat=p.go(action[1], exits)
                else:
                    print("Sorry, you need to 'go' somewhere.")
            if action[0] == 'look':
                to_repeat=p.look()
            if action[0] == 'inventory':
                to_repeat=p.inventory()
            if action[0] == 'get':
                if len(action)>=2:
                    to_repeat=p.get(action[1],items)
                else:
                    print("Sorry, you need to 'get' something.")
            if action[0] == 'drop':
                if len(action)>=2:
                    to_repeat=p.drop(action[1])
                else:
                    print("Sorry, you need to 'drop' something.")
            if action[0] == 'win':
                p.win()
                return 0
            if action[0] == 'help':
                methods = dir(player)
                help_methods=[]
                for x in methods:
                    if not x.startswith('__'):
                        help_methods.append(x)
                help_methods.remove('player_items')
                help_methods.remove('player_room')
                print("You can run the following commands:")
                for x in help_methods:
                    print(x)

if __name__ == "__main__":
    main()