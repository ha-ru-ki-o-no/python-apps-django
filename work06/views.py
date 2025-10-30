from django.shortcuts import render

# 和暦→西暦


def wareki_to_seireki(era, year):
    era_starts = {"明治": 1868, "大正": 1912, "昭和": 1926, "平成": 1989, "令和": 2019}
    if era not in era_starts:
        return "未知の元号です"
    seireki = era_starts[era] + year - 1
    return f"{seireki}年"


# 西暦→和暦


def seireki_to_wareki(year):
    eras = [
        ("令和", 2019),
        ("平成", 1989),
        ("昭和", 1926),
        ("大正", 1912),
        ("明治", 1868),
    ]
    for era, start in eras:
        if year >= start:
            wareki_year = year - start + 1
            if wareki_year == 1:
                return f"{era}元年"
            else:
                return f"{era}{wareki_year}年"
    return "それ以前の元号は未対応"


def index(request):
    result = ""
    if request.method == "POST":
        mode = request.form["mode"]
        if mode == "to_seireki":
            era = request.form["era"]
            year = int(request.form["year"])
            result = wareki_to_seireki(era, year)
        elif mode == "to_wareki":
            year = int(request.form["year"])
            result = {"message": seireki_to_wareki(year)}
    return render(request, "work06/index.html", result)


# work06/views.py


def reiwa_view(request):
    return render(request, "reiwa.html")
