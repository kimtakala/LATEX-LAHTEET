from flask import flash, redirect, render_template, request
from entities.source_book import SourceBook
from repositories import source_book_repository
from config import app
from util import UserInputError


@app.route("/", methods=["GET"])
def index_get():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def index_post():
    form = request.form
    book = SourceBook(
        0,
        form["bibtex_key"] if "bibtex_key" in form else "",
        form["title"] if "title" in form else "",
        form["year"] if "year" in form else "",
        form["author"] if "author" in form else "",
        0,
        form["publisher"] if "publisher" in form else "",
    )

    try:
        source_book_repository.create_book(book)
        flash(f"Lähde {book.bibtex_key} lisätty onnistuneesti!", "success")
        return redirect("/")
    except UserInputError as error:
        return render_template(
            "index.html", show_add_form=True, error=error, form_data=request.form
        )
