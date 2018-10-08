from transitions.extensions import GraphMachine

import telegram
API_TOKEN = '518306299:AAEDIR55YBaJuscizfLV2aZixje9TSDGsEc'
bot = telegram.Bot(token=API_TOKEN)

class TocMachine(GraphMachine):
    num = 0

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == '/start'

    def is_going_to_introduction(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_points(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_job_advancement(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def is_going_to_training_map(self, update):
        text = update.message.text
        return text.lower() == 'd'

    def is_going_to_warrior(self, update):
        text = update.message.text
        return text.lower() == 'e'

    def is_going_to_magician(self, update):
        text = update.message.text
        return text.lower() == 'f'

    def is_going_to_bowman(self, update):
        text = update.message.text
        return text.lower() == 'g'

    def is_going_to_thief(self, update):
        text = update.message.text
        return text.lower() == 'h'

    def is_going_to_pirate(self, update):
        text = update.message.text
        return text.lower() == 'i'

    def is_going_to_end(self, update):
        text = update.message.text
        return text.lower() == '/end'

    def on_enter_user(self, update):
        update.message.reply_text("You can search for:\n(a) introduction\n(b) AP/SP\n(c) job advancement\n(d) training map\nType '/end' to end searching.")

    def on_enter_introduction(self, update):
        self.num = 1
        update.message.reply_text("You can look up introduction of:\n(e) warrior\n(f) magician\n(g) bowman\n(h) thief\n(i) pirate")

    def on_enter_points(self, update):
        self.num = 2
        update.message.reply_text("You can look up AP/SP of:\n(e) warrior\n(f) magician\n(g) bowman\n(h) thief\n(i) pirate")

    def on_enter_job_advancement(self, update):
        self.num = 3
        update.message.reply_text("You can look up job advancement of:\n(e) warrior\n(f) magician\n(g) bowman\n(h) thief\n(i) pirate")

    def on_enter_training_map(self, update):
        self.num = 4
        update.message.reply_text("You can look up training map of:\n(e) warrior\n(f) magician\n(g) bowman\n(h) thief\n(i) pirate")

    def on_enter_warrior(self, update):
        if self.num == 1:
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/MS_Warrior_art.png', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='https://cdn.wikimg.net/strategywiki/images/b/b4/MS_Warrior_art.png')
            update.message.reply_text("Warriors display awesome attacking prowess and everlasting stamina. They show their worth fighting up close and personal.")
        elif self.num == 2:
            update.message.reply_text("AP: STR, DEX\n\nSP: see https://strategywiki.org/wiki/MapleStory/Warrior/Builds")
        elif self.num == 3:
            update.message.reply_text("The job advancement path for the warriors reveals a 3-way job route as shown below.")
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/JBWarr.JPG', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='http://media.playpark.net/MapleStory/uploadimages/JBWarr.JPG')
        elif self.num == 4:
            update.message.reply_text("PERION\n\nLocation: A dry highland located at the northern part of Victoria Island.\n\nCharacteristic: The dry and dusty warrior town is built on a rocky highlands and culture of the natives is strong here.")
        self.go_back(update)

    def on_enter_magician(self, update):
        if self.num == 1:
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/MS_Magician_art.png', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='https://cdn.wikimg.net/strategywiki/images/9/9f/MS_Magician_art.png')
            update.message.reply_text("Magicians may not have much of attacking abilities, but they can handle awesome, spectacular magic at will.")
        elif self.num == 2:
            update.message.reply_text("AP: INT, LUK\n\nSP: see https://strategywiki.org/wiki/MapleStory/Magician/Builds")
        elif self.num == 3:
            update.message.reply_text("The job advancement path for the magicains reveals a 3-way job route as shown below.")
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/Magepath.JPG', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='http://media.playpark.net/MapleStory/uploadimages/Magepath.JPG')
        elif self.num == 4:
            update.message.reply_text("ELLINIA\n\nLocation: A deep, bright forest at the eastern region of Victoria Island.\n\nCharacteristic: Home to the town of the magicians, this is the place to go to board the airships leaving for Orbis and Erev.")
        self.go_back(update)

    def on_enter_bowman(self, update):
        if self.num == 1:
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/MS_Bowman_art.png', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='https://cdn.wikimg.net/strategywiki/images/5/54/MS_Bowman_art.png')
            update.message.reply_text("Bowmen embrace dexterity for powerful attacks. They are superior in long-range attacks in battles.")
        elif self.num == 2:
            update.message.reply_text("AP: DEX, STR\n\nSP: see https://strategywiki.org/wiki/MapleStory/Bowman/Builds")
        elif self.num == 3:
            update.message.reply_text("The job advancement path for the bowmen reveals a 2-way job route as shown below.")
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/bowmanroute.JPG', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='http://media.playpark.net/MapleStory/uploadimages/bowmanroute.JPG')
        elif self.num == 4:
            update.message.reply_text("HENESYS\n\nLocation: A peaceful mushroom town located at the southern region of Victoria Island.\n\nCharacteristic: The town of the bowman, this is a peaceful town with a busy marketplace worth visiting.")
        self.go_back(update)

    def on_enter_thief(self, update):
        if self.num == 1:
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/MS_Thief_art.png', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='https://cdn.wikimg.net/strategywiki/images/2/24/MS_Thief_art.png')
            update.message.reply_text("Luck with minor amount of dexterity, and power are the highlights of being a thief.")
        elif self.num == 2:
            update.message.reply_text("AP: LUK, DEX\n\nSP: see https://strategywiki.org/wiki/MapleStory/Thief/Builds")
        elif self.num == 3:
            update.message.reply_text("The job advancement path for the thieves reveals a 2-way job route as shown below.")
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/thiefroute.JPG', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='http://media.playpark.net/MapleStory/uploadimages/thiefroute.JPG')
        elif self.num == 4:
            update.message.reply_text("KERNING CITY\n\nLocation: An urban city west of Victoria Island.\n\nCharacteristic: This city hides many mysterious NPCs and offer many services... at a fee, of course.")
        self.go_back(update)

    def on_enter_pirate(self, update):
        if self.num == 1:
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/MS_Pirate_art.png', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='https://cdn.wikimg.net/strategywiki/images/1/1b/MS_Pirate_art.png')
            update.message.reply_text("Pirates are essentially masters of attack and defence, requiring a balance of strength and dexterity to utilize their powers to the max.")
        elif self.num == 2:
            update.message.reply_text("AP: STR, DEX\n\nSP: see https://strategywiki.org/wiki/MapleStory/Pirate/Builds")
        elif self.num == 3:
            update.message.reply_text("The job advancement path for the pirates reveals a 2-way job route as shown below.")
            bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/pirateroute.JPG', 'rb'))
            #bot.send_photo(chat_id=update.message.chat_id, photo='http://media.playpark.net/MapleStory/uploadimages/pirateroute.JPG')
        elif self.num == 4:
            update.message.reply_text("NAUTILUS\n\nLocation: A whale-shaped submarine located at the southern-east of Victoria Island.\n\nCharacteristic: Pirate town.")
        self.go_back(update)

    def on_enter_end(self, update):
        update.message.reply_text("Searching End.\nType '/start' to start searching.")

    def on_exit_training_map(self, update):
        bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/user/TOC-Project-2017/img/victoria.JPG', 'rb'))
        #bot.send_photo(chat_id=update.message.chat_id, photo='http://media.playpark.net/MapleStory/uploadimages/victoria.JPG')
