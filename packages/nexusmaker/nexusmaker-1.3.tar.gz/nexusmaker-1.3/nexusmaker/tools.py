import re
import unicodedata

is_unique = re.compile(r"""^(.*)_(u_?\d+)$""")

def parse_word(label, delimiter="_"):
    """
    Returns a tuple of word, cognate_id.
    """
    if is_unique.match(label):
        return is_unique.findall(label)[0]
    elif delimiter in label:
        return tuple(label.rsplit(delimiter, 1))
    else:
        raise ValueError("No delimiter %s in %s" % (delimiter, label))


def slugify(var):
    var = var.replace("(", "").replace(")", "")
    var = var.replace(" / ", "_").replace("/", "_")
    var = unicodedata.normalize('NFKD', var)
    var = "".join([c for c in var if not unicodedata.combining(c)])
    var = var.replace(" - ", "_")
    var = var.replace(":", "").replace('?', "")
    var = var.replace('’', '').replace("'", "")
    var = var.replace(',', "").replace(".", "")
    var = var.replace(" ", "_")
    return var
