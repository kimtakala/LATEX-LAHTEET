from io import BytesIO

from flask import flash, redirect, render_template, request, send_file

from bibtex_convert import to_bibtex
from config import app
from database_service import DatabaseService
from db_util import truncate_db
from form_fields import get_fields_json
from util import UserInputError

from entities.article import Article
from entities.book import Book
from entities.inproceedings import Inproceedings
from entities.tag import Tag

from repositories.article_repository import ArticleRepository
from repositories.book_repository import BookRepository
from repositories.inproceedings_repository import InproceedingsRepository
from repositories.source_repository import SourceRepository
from repositories.tag_repository import TagRepository



@app.route("/", methods=["GET"])
def index_get():
    show_add_form = "show_add_form" in request.args
    form_json = get_fields_json()
    source_repo = SourceRepository(DatabaseService())

    try:
        sources = source_repo.get()
        return render_template(
            "index.html",
            sources=sources,
            form_json=form_json,
            show_add_form=show_add_form,
        )
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            "Lähteiden haku epäonnistui teknisen virheen takia, \
            ota yhteyttä järjestelmänvalvojaan.",
            "error",
        )
        print(error)
        return render_template("index.html")


@app.route("/", methods=["POST"])
def index_post():
    form = request.form
    source_type = form["type"]
    added_key = ""
    #  TODO: Erillisiin funktioihin tämä
    book_repo = BookRepository(DatabaseService())
    article_repo = ArticleRepository(DatabaseService())
    inproceedings_repo = InproceedingsRepository(DatabaseService())

    try:
        match source_type:
            case "book":
                book = Book(
                    {
                        "source_id": 0,
                        "bibtex_key": (
                            form["bibtex_key"] if "bibtex_key" in form else ""
                        ),
                        "title": form["title"] if "title" in form else "",
                        "year": form["year"] if "year" in form else "",
                        "author": form["author"] if "author" in form else "",
                        "source_book_id": 0,
                        "publisher": form["publisher"] if "publisher" in form else "",
                    }
                )

                book_repo.create(book)
                added_key = book.bibtex_key

            case "article":
                article = Article(
                    {
                        "source_id": 0,
                        "bibtex_key": (
                            form["bibtex_key"] if "bibtex_key" in form else ""
                        ),
                        "title": form["title"] if "title" in form else "",
                        "year": form["year"] if "year" in form else "",
                        "author": form["author"] if "author" in form else "",
                        "source_article_id": 0,
                        "journal": form["journal"] if "journal" in form else "",
                        "volume": form["volume"] if "volume" in form else "",
                        "number": form["number"] if "number" in form else "",
                        "pages": form["pages"] if "pages" in form else "",
                        "month": form["month"] if "month" in form else "",
                    }
                )

                article_repo.create(article)
                added_key = article.bibtex_key

            case "inproceedings":
                print("Creating Inproceedings-object")
                inproceedings = Inproceedings(
                    {
                        "source_id": 0,
                        "bibtex_key": (
                            form["bibtex_key"] if "bibtex_key" in form else ""
                        ),
                        "title": form["title"] if "title" in form else "",
                        "year": form["year"] if "year" in form else "",
                        "author": form["author"] if "author" in form else "",
                        "source_inproceeding_id": (
                            form["source_inproceedings_id"]
                            if "source_inproceedings_id" in form
                            else ""
                        ),
                        "booktitle": form["booktitle"] if "booktitle" in form else "",
                        "editor": form["editor"] if "editor" in form else "",
                        "series": form["series"] if "series" in form else "",
                        "pages": form["pages"] if "pages" in form else "",
                        "address": form["address"] if "address" in form else "",
                        "month": form["month"] if "month" in form else "",
                        "organization": (
                            form["organization"] if "organization" in form else ""
                        ),
                        "publisher": form["publisher"] if "publisher" in form else "",
                        "volume": form["volume"] if "volume" in form else "",
                    }
                )
                print("Adding inproceeding object")
                inproceedings_repo.create(inproceedings)
                added_key = inproceedings.bibtex_key

            case _:
                flash("Lähteen tyyppiä ei tueta", "error")
                return redirect("/?show_add_form")

        flash(f"Lähde {added_key} lisätty onnistuneesti!", "success")
        return redirect("/")

    except UserInputError as error:
        flash(str(error), "error")
        return redirect("/?show_add_form")

    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            "Lähteen lisääminen epäonnistui teknisen virheen takia, \
            ota yhteyttä järjestelmänvalvojaan.",
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/delete/<int:source_id>", methods=["POST"])
def delete_source(source_id):
    source_repo = SourceRepository(DatabaseService())
    try:
        source_repo.delete(source_id)
        flash("Lähde poistettu onnistuneesti!", "success")
        return redirect("/")
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            "Lähteen poistaminen epäonnistui teknisen virheen takia, \
            ota yhteyttä järjestelmänvalvojaan.",
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/delete_tag/<int:source_id>/<string:tag>", methods=["POST"])
def delete_tag(source_id, tag):
    tag_repo = TagRepository(DatabaseService())
    try:
        tag_repo.delete(source_id, tag)
        flash("Tunniste poistettu onnistuneesti!", "success")
        return redirect("/")
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            "Tunnisteen poistaminen epäonnistui teknisen virheen takia, \
            ota yhteyttä järjestelmänvalvojaan.",
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/tag", methods=["POST"])
def tag_post():
    tag_repo = TagRepository(DatabaseService())
    form = request.form
    try:
        tag_repo.create(
            Tag(
                {
                    "name": form["name"] if "name" in form else "",
                    "source_id": form["source_id"] if "source_id" in form else "",
                    "tag_id": 0,
                }
            )
        )
        flash("Tunniste lisätty onnistuneesti!", "success")
        return redirect("/")
    except UserInputError as error:
        flash(str(error), "error")
        return redirect("/")
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            str(error),
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/download", methods=["GET"])
def download():
    source_repo = SourceRepository(DatabaseService())
    bibtex_string = to_bibtex(source_repo.get_full())

    # doing it this way instead of creating a proper file
    # means it doesn't have to be stored anywhere
    bibtex_bytes = BytesIO(bibtex_string.encode("utf-8"))

    return send_file(
        bibtex_bytes,
        mimetype="text/bib",
        as_attachment=True,
        download_name="references.bib",
    )


@app.route("/reset_db", methods=["GET"])
def reset_db():
    truncate_db()
    return redirect("/")
