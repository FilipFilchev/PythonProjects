from flask import Flask, render_template
# from flask import jsonify 
# import json
app = Flask(__name__)

"""
with open('intents.json', 'r') as dataset:
    content = json.load(dataset)

print(content)
"""
# @app.route('/')
@app.route("/")
def func():


    """
    test_masiv_list = [0, 1, 2, 3, 4, 5, "some testing data"]

    message = "Hello World :)"
    data = str(test_masiv_list) 
    """
    

    # return jsonify(content, data)
    return render_template('base.html')

    
if __name__ == '__main__':
    app.run()




