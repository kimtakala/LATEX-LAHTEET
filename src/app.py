from flask import redirect, render_template, request
from entities.source_book import SourceBook
from repositories import source_book_repository
from config import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/source", methods=["POST"])
def source():
    book = SourceBook(
        0,
        request.form["title"],
        request.form["year"],
        0,
        request.form["author"],
        request.form["publisher"],
    )

    # TODO: Validoi syöte ja palauta virheitä käyttäjälle
    source_book_repository.create_book(book)
    return redirect("/")
