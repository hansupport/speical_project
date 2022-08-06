from flask import Flask, render_template, request, redirect, url_for
import sys
app = Flask(__name__)
import database


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/upload")
def apply():
    return render_template("upload.html")

@app.route("/upload_photo")
def upload_photo():
    date = request.args.get("date")
    title = request.args.get("title")
    feeling = request.args.get("feeling")
    contents = request.args.get("contents")
    
    database.save(date, title, feeling, contents)
    return render_template("upload_photo.html")

@app.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("main"))

@app.route("/list")
def list():
    diary_list = database.load_list()
    length = len(diary_list)
    for diary in diary_list:
        print(diary[1])
    return render_template("list.html", diary_list = diary_list, length = length)

@app.route("/diary_info/<int:index>/")
def diary_info(index):
    diary_info = database.load_diary(index)
    date = diary_info["date"]
    title = diary_info["title"]
    feeling = diary_info["feeling"]
    contents = diary_info["contents"]
    
    photo = f"img/{index}.jpeg"
    
    return render_template("diary_info.html", 
        date = date, title = title, feeling = feeling, contents = contents, photo = photo)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
