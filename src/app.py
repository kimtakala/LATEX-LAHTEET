from io import BytesIO

from flask import flash, redirect, render_template, request, send_file

from db_util import truncate_db
from entities.article import Article
from entities.book import Book
from entities.inproceedings import Inproceedings
from form_fields import get_fields_json
from config import app
from repositories.article_repository import ArticleRepository
from repositories.book_repository import BookRepository
from repositories.inproceedings_repository import InproceedingsRepository
from repositories.source_repository import SourceRepository
from util import UserInputError


@app.route("/", methods=["GET"])
def index_get():
    show_add_form = "show_add_form" in request.args
    form_json = get_fields_json()
    try:
        sources = SourceRepository.get()
        return render_template(
            "index.html",
            sources=sources,
            form_json=form_json,
            show_add_form=show_add_form,
        )
    except Exception as error: # pylint: disable=broad-exception-caught
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
    print(form.__dict__)
    source_type = form["type"]
    added_key = ""

    try:
        match source_type:
            case "book":
                book = Book(
                    0,
                    form["bibtex_key"] if "bibtex_key" in form else "",
                    form["title"] if "title" in form else "",
                    form["year"] if "year" in form else "",
                    form["author"] if "author" in form else "",
                    0,
                    form["publisher"] if "publisher" in form else "",
                )

                BookRepository.create(book)
                added_key = book.bibtex_key

            case "article":
                article = Article(
                    0,
                    form["bibtex_key"] if "bibtex_key" in form else "",
                    form["title"] if "title" in form else "",
                    form["year"] if "year" in form else "",
                    form["author"] if "author" in form else "",
                    0,
                    form["journal"] if "journal" in form else "",
                    form["volume"] if "volume" in form else "",
                    form["number"] if "number" in form else "",
                    form["pages"] if "pages" in form else "",
                    form["month"] if "month" in form else "",
                )

                ArticleRepository.create(article)
                added_key = article.bibtex_key

            case "inproceedings":
                inproceedings = Inproceedings(
                    form["source_id"] if "source_id" in form else "",
                    form["bibtex_key"] if "bibtex_key" in form else "",
                    form["title"] if "title" in form else "",
                    form["year"] if "year" in form else "",
                    form["author"] if "author" in form else "",
                    (
                        form["source_inproceedings_id"]
                        if "source_inproceedings_id" in form
                        else ""
                    ),
                    form["booktitle"] if "booktitle" in form else "",
                    form["editor"] if "editor" in form else "",
                    form["series"] if "series" in form else "",
                    form["pages"] if "pages" in form else "",
                    form["address"] if "address" in form else "",
                    form["month"] if "month" in form else "",
                    form["organization"] if "organization" in form else "",
                    form["publisher"] if "publisher" in form else "",
                    form["volume"] if "volume" in form else "",
                )

                InproceedingsRepository.create(inproceedings)
                added_key = inproceedings.bibtex_key

            case _:
                flash("Lähteen tyyppiä ei tueta", "error")
                return redirect("/?show_add_form")

        flash(f"Lähde {added_key} lisätty onnistuneesti!", "success")
        return redirect("/")

    except UserInputError as error:
        flash(str(error), "error")
        return redirect("/?show_add_form")

    except Exception as error: # pylint: disable=broad-exception-caught
        flash(
            "Lähteen lisääminen epäonnistui teknisen virheen takia, \
            ota yhteyttä järjestelmänvalvojaan.",
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/delete/<int:source_id>", methods=["POST"])
def delete_source(source_id):
    try:
        SourceRepository.delete(source_id)
        flash("Lähde poistettu onnistuneesti!", "success")
        return redirect("/")
    except Exception as error: # pylint: disable=broad-exception-caught
        flash(
            "Lähteen poistaminen epäonnistui teknisen virheen takia, \
            ota yhteyttä järjestelmänvalvojaan.",
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/download", methods=['GET'])
def download():
    latex_text = SourceRepository.download()

    # doing it this way instead of creating a proper file
    # means it doesn't have to be stored anywhere
    latex_bytes = BytesIO(latex_text.encode('utf-8'))

    return send_file(
        latex_bytes,
        mimetype="text/bib",
        as_attachment=True,
        download_name="references.bib"
    )


@app.route("/reset_db", methods=["GET"])
def reset_db():
    truncate_db()
    return redirect("/")
