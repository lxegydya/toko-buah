from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient, DESCENDING

client = MongoClient('mongodb+srv://lxegydya:admin@cluster0.s4ymqoi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.chapter6

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    
    num = 0
    last = db.bucket.find_one({}, sort=[('_id', DESCENDING)])

    if(last):
        num = last['num'] + 1
    else:
        num = 1

    doc = {
        'num': num,
        'bucket': bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)
    
    return jsonify({'msg': 'data saved!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form["num_give"]
    db.bucket.update_one(
        {'num': int(num_receive)},
        {'$set': {'done': 1}}
    )
    return jsonify({'msg': 'Update done!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets':buckets_list})

@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    num_receive = request.form["num_give"]
    db.bucket.delete_one({'num': int(num_receive)})
    return jsonify({'msg': 'Item deleted!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)