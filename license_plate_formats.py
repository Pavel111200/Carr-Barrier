formats = {
    "Albania": r"^[A-Z]{2}\s?[0-9]{3}\s?[A-Z]{2}",
    "Andora": r"^[A-Z]{1}\s?[0-9]{4}",
    "Austria": r"^[A-Z]{1}\s?[0-9]{3}\s?[A-Z]{2}",
    "Belarus": r"^[0-9]{4}\s?[A-Z]{2}-?[0-9]{1}",
    "Belgum": r"^[0-9]{1}-?[A-Z]{3}-?[0-9]{3}",
    "Bosnia and Herzegovina": r"[A-Z]{1}[0-9]{2}-?[A-Z]{1}-?[0-9]{3}",
    "Bulgaria": r"^[A-Z]{1,2}\s?[0-9]{4}\s?[A-Z]{2}",
    "Croatia": r"^[A-Z]{2}[0-9]{3,4}-?[A-Z]{1,2}",
    "Cyprus": r"^[A-Z]{3}\s?[0-9]{3}",
    "Czech Republic": r"[0-9]{1}[A-Z]{1}[0-9A-Z]{1}\s?[0-9]{4}",
    "Denmark": r"^[A-Z]{2}\s?[0-9]{2}\s?[0-9]{3}",
    "Estonia": r"^[0-9]{3}\s?[A-Z]{3}",
    "Finland": r"^[A-Z]{3}-?[0-9]{3}",
    "France": r"^[A-Z]{2}-?[0-9]{3}-?[A-Z]{2}",
    "Germany": r"^[A-Z]{2}\s?[A-Z]{2}\s?[0-9]{4}",
    "Greece": r"^[A-Z]{3}-?[0-9]{4}",
    "Hungary": r"^[A-Z]{2}\s?[A-Z]{2}-?[0-9]{3}",
    "Iceland": r"^[A-Z]{3}[0-9]{2}",
    "Ireland": r"^[0-9]{3}-?[A-Z]{2}-?[0-9]{6}",
    "Italy": r"^[A-Z]{2}\s?[0-9]{3}[A-Z]{2}",
    "Latvia": r"^[A-Z]{2}-?[0-9]{1,4}",
    "Liechtenstein": r"^FL\s?[0-9]{1,5}",
    "Lithuania": r"^[A-Z]{3}[0-9]{3}",
    "Luxembourg": r"^[A-Z]{2}\s?[0-9]{4}",
    "Malta": r"^[A-Z]{3}\s?[0-9]{3}",
    "Moldova": r"^[A-Z]{3}\s?[0-9]{3}",
    # "Monaco": r"^[A-Z0-9]{4}",
    "Montenegro": r"^[A-Z]{2}\s?[A-Z]{2}[0-9]{3}",
    "Netherlands": r"^[A-Z]{1}-?[0-9]{3}-?[A-Z]{2}",
    "North Macedonia": r"^[A-Z]{2}\s?[0-9]{4}\s?[A-Z]{2}",
    "Norway": r"^[A-Z]{2}\s?[0-9]{4,5}",
    # "Poland": r"^[A-Z]{2,3}\s?[A-Z0-9]{4,5}",
    "Portugal": r"^[A-Z]{2}-?[0-9]{2}-?[A-Z]{2}",
    "Romania": r"^^(B\s?[0-9]{2,3}\s?[A-Z]{3})|([A-Z]{2}\s?[0-9]{2}\s?[A-Z]{3})",
    "San Marino": r"^[A-Z][0-9]{4}",
    "Serbia": r"^[A-Z]{2}\s?[0-9]{3,4}-?[A-Z]{2}",
    "Slovakia": r"^[A-Z]\s?-?[0-9]{3}[A-Z]{2}",
    "Slovenia": r"^[A-Z]{2}\s?[0-9]{3,4}-?[A-Z]{2}",
    "Spain": r"^[0-9]{4}\s?[A-Z]{3}",
    "Sweden": r"^[A-Z]{3}\s?[0-9]{2}[A-Z0-9]",
    "Switzerland": r"^[A-Z]{2}\s?[0-9]{1,6}",
    "Ukraine": r"^[A-Z]{2}\s?[0-9]{4}\s?[A-Z]{2}",
    "United Kingdom": r"^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}",
    "Vatican City": r"^S?CV\s?[0-9A-Z]{1,5}"
}

test_formats = {
    "Spain": r"[0-9]{4}\s?[^AEIOQUa-z\d\W_]{3}",
    "Old Spain": r"(MA|CA)\s?[0-9]{4}\s?[^AEIOQUa-z\d\W_]{2}"
    # "Bulgaria": r"^[A-Z]{1,2}\s?[0-9]{4}\s?[A-Z]{2}"
}