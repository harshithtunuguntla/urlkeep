from flask import Flask, render_template, request, redirect, Response
from pymongo import MongoClient


app = Flask(__name__)



def get_database(DB):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb://localhost:27017"
    CONNECTION_STRING = "mongodb+srv://admin:root@cluster0.u1hsn.mongodb.net/learning?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING, connect=False)
    return client[DB]
    
db_name = get_database('short_url')
collection = db_name["all_urls_data"]



def is_keyword_present(keyword):
    present=0
    for item in collection.find():
        if(item['short_url']==keyword):
            present=1
    return present

def url_shortener(a):
    return "hLOO"



@app.route('/', methods=['POST','GET'])
def begin():
    status=2
    if request.method == 'POST':
        url_received = request.form["entered_url"]
        keyword_received = request.form["entered_keyword"]

        # shortened_url = url_shortener(url_received)

        keyword_status = is_keyword_present(keyword_received)

        if(keyword_status==1):
            status = 0
        else:
            new_item = {
            "short_url" : keyword_received,
            "long_url": url_received,
            "clicks":0
            }
            collection.insert_one(new_item)
            status = 1

        return render_template("form.html", status=status,link="https://harshithurl.up.railway.app/" + str(keyword_received))

    else:
        return render_template("form.html", status=status)

@app.route('/all_urls')
def all_urls():
    return render_template("all_urls.html")

@app.route('/<received_url>')
def reroute(received_url):
    link_status=0
    for item in collection.find():
        if(item['short_url']==received_url):
            redirection = item['long_url']
            # filter = { 'short_url': received_url }
            # newvalues = { "$set": { 'clicks': item['clicks']+1 } }
            # collection.update_one(filter, newvalues) 
            link_status=1
    if(link_status==0):
        return "Link Not Found" #Link not found, wanna create one with this name? click here

    return redirect(redirection, code=302)

if __name__ == '__main__':
    app.run(debug=True)