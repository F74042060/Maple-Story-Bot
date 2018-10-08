import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '518306299:AAEDIR55YBaJuscizfLV2aZixje9TSDGsEc'
WEBHOOK_URL = 'https://87c26abb.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'introduction',
        'points',
        'job_advancement',
        'training_map',
        'warrior', 
        'magician',
        'bowman',
        'thief',
        'pirate',
        'end'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': [
                'user',
                'end'
            ],
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'introduction',
            'conditions': 'is_going_to_introduction'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'points',
            'conditions': 'is_going_to_points'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'job_advancement',
            'conditions': 'is_going_to_job_advancement'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'training_map',
            'conditions': 'is_going_to_training_map'
        },
        {
            'trigger': 'advance',
            'source': [
                'introduction',
                'points',
                'job_advancement',
                'training_map'
            ],
            'dest': 'warrior',
            'conditions': 'is_going_to_warrior'
        },
        {
            'trigger': 'advance',
            'source': [
                'introduction',
                'points',
                'job_advancement',
                'training_map'
            ],
            'dest': 'magician',
            'conditions': 'is_going_to_magician'
        },
        {
            'trigger': 'advance',
            'source': [
                'introduction',
                'points',
                'job_advancement',
                'training_map'
            ],
            'dest': 'bowman',
            'conditions': 'is_going_to_bowman'
        },
        {
            'trigger': 'advance',
            'source': [
                'introduction',
                'points',
                'job_advancement',
                'training_map'
            ],
            'dest': 'thief',
            'conditions': 'is_going_to_thief'
        },
        {
            'trigger': 'advance',
            'source': [
                'introduction',
                'points',
                'job_advancement',
                'training_map'
            ],
            'dest': 'pirate',
            'conditions': 'is_going_to_pirate'
        },
		{
            'trigger': 'go_back',
            'source': [
                'warrior', 
                'magician',
                'bowman',
                'thief',
                'pirate'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'end',
            'conditions': 'is_going_to_end'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))

@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'

@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    machine.graph.draw('fsm.png', prog='dot')
    app.run()
