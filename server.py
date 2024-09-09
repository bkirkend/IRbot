from flask import Flask, request, abort, json
from post_to_groupme import post_to_groupme
from post_to_groupme_food import post_to_groupme_food

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    with open("comp_tables.json", 'r') as f:
        tables = json.load(f)

    if request.method == 'POST':
        formData = request.json
        #app.logger.info(formData)
        header = '𝐂𝐨𝐦𝐩𝐚𝐧𝐲 𝐑𝐞𝐪𝐮𝐞𝐬𝐭\n'
        info = ''
        isFood = False
        if formData is None:
            return 'failure', 400
        for question in formData['embeds'][0]['fields']:
            name = question['name']
            value = question['value']
            if len(name.split()) < 3:
                info += f'{name}: {value} \n'
            else:
                info += f'{value} \n'
            if value.strip().lower() in tables:
                info += f'Table(from bot): {tables[value.strip().lower()]} \n'
            if value == "Food":
                isFood = True

        if(True):
            post_to_groupme(header + info)
        else: #check isFood condition for separate food groupme
            #is food here
            post_to_groupme_food(header + info)

        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
