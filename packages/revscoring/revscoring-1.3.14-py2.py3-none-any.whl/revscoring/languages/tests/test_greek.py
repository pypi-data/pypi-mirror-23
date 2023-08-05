import pickle

from nose.tools import eq_

from .. import greek
from ...datasources import revision_oriented
from ...dependencies import solve
from .util import compare_extraction

BAD = [
    "αδερφάρα", "αδελφάρα",
    "αλήτης",
    "αλητήριος", "αλητήρια", "αλητήριο",
    "αλητάμπουρας",
    "άχρηστος", "άχρηστη", "αχρηστία",
    "αρχίδι", "αρχίδια",
    "αντινεοφιλελέ",
    "αντινεοφιλελές",
    "βλάκας", "βλακεία",
    "βυζί", "βυζιά", "βυζόμπαλα",
    "γαμώ",
    "γαμημένος", "γαμημένη", "γαμημένο",
    "γαμώτο", "γαμιέται", "γαμιέσαι",
    "γαμιάς",
    "γκαβλί",
    "γκει",
    "γύφτος", "γυφτιά", "γύφτισα",
    "γυφταριό", "γύφτικο",
    "διάολος", "διάολο",
    "διαολεμένος", "διαολεμένη", "διαολεμένο",
    "ελαφροχέρης", "ελαφροχέρα",
    "ηλίθιος", "ηλίθια", "ηλίθιο",
    "καβλί", "καβλιάρης", "καβλωμένος"
    "κουράδα", "κουράδι",
    "κομμουνιστοσυμμορίτης",
    "κώλος", "κόλος", "κωλί",
    "κωλοτρυπίδα", "κώλο",
    "κωλόπαιδο", "κολόπαιδο",
    "κουτός", "κουφάλα",
    "κλανιά", "κλανιάρης",
    "κλάνω", "κλάνεις", "κλάνει",
    "κλέφτης", "κλεφτρόνι",
    "καριόλης", "καυλί",
    "λεσβία", "λούγκρα",
    "μπάσταρδο", "μπάσταρδος", "μπάσταρδα",
    "μπασταρδεμένο",
    "μουνί", "μουνιά", "μουνάρα", "μουνάκι"
    "μουνόσκυλος", "μουνότρυπα",
    "μαλάκας","μαλάκες","μαλακία",
    "μαλακίες",
    "μαλακοκάβλι",
    "μαλακισμένος", "μαλακισμένη", "μαλακισμένο"
    "νταής", "νταηλίκι",
    "νεοφιλελε", "νεοφιλελές",
    "ντουγάνι",
    "ξεδιάντροπος", "ξεδιάντροπη",
    "ξετσίπωτος", "ξετσίπωτη",
    "πεισματάρης", "πεισματάρα", "πεισματάρικο",
    "πουτάνα", "πουτανάκι", "πουτανιά",
    "πούστης", "πουστιά", "πούστικος",
    "πούστικο",
    "ρουφιάνος", "ρουφιάνα","ρουφιανιά",
    "φιλελε", "φιλελές"
]

INFORMAL = [
    "άντε",
    "άσε",
    "άστη", "άστο", "άστα",
    "γεια",
    "εμάς", "εσάς", "μας", "σας",
    "φίλε",
    "μαν",
    "μπαι",
    "τρανς",
    "τρανσεξουαλ",
    "μπλα", "μπλαμπλα", "μπλαμπλαμπλα",
    "χα","χαχα","χαχαχαχα",
    "χε","χεχε","χεχεχεχε",
    "χι","χιχι","χιχιχιχι",
    "χο","χοχο","χοχοχοχο",
]

OTHER = [
    """
    Η Μήδεια είναι όπερα κομίκ σε τρεις πράξεις του Λουίτζι Κερουμπίνι.
    Το λιμπρέτο του Φρανσουά-Μπενουά Οφμάν είναι βασισμένο στην ομώνυμη
    τραγωδία του Ευριπίδη, Μήδεια, καθώς και στο θεατρικό έργο Μήδεια του Πιέρ
    Κορνέιγ. Παρουσιάστηκε πρώτη φορά στις 17 Μαρτίου 1797 στο θέατρο Φεντώ
    στο Παρίσι με τη Γαλλίδα υψίφωνο Ζιλί-Ανζελίκ Σιό στο ρόλο της Μήδειας.
    Είναι ένα από τα πιο γνωστά έργα του Κερουμπίνι και το μόνο που παίζεται
    τακτικά έως σήμερα. Η όπερα, αν και στην πρωτότυπη εκδοχή ήταν στα γαλλικά
    και συμπεριελάμβανε διαλόγους δίχως συνοδεία μουσικής, έγινε γνωστή τον
    περασμένο αιώνα με την Ιταλική εκδοχή του λιμπρέτου του Οφμάν και των
    ρετσιτατίβι του Φραντς Λάχνερ από τον Κάρλο Τσανγκαρίνι.
    """
]

r_text = revision_oriented.revision.text


def test_badwords():
    print(greek.badwords.revision.datasources.matches("βλάκας"))
    compare_extraction(greek.badwords.revision.datasources.matches,
                       BAD, OTHER)
    print(greek.badwords.revision.datasources.matches("βλάκας"))
    eq_(greek.badwords, pickle.loads(pickle.dumps(greek.badwords)))


def test_informals():
    compare_extraction(greek.informals.revision.datasources.matches,
                       INFORMAL, OTHER)

    eq_(greek.informals, pickle.loads(pickle.dumps(greek.informals)))


def test_dictionary():
    cache = {r_text: 'Αυτό είναι γραμμένο λθος. <td>'}
    eq_(solve(greek.dictionary.revision.datasources.dict_words, cache=cache),
        ["Αυτό", "είναι", "γραμμένο"])
    eq_(solve(greek.dictionary.revision.datasources.non_dict_words,
              cache=cache),
        ["λθος"])

    eq_(greek.dictionary, pickle.loads(pickle.dumps(greek.dictionary)))


def test_stopwords():
    cache = {r_text: 'Αυτό είναι γραμμένο λθος. <td>'}
    eq_(solve(greek.stopwords.revision.datasources.stopwords, cache=cache),
        ["Αυτό", "είναι"])
    eq_(solve(greek.stopwords.revision.datasources.non_stopwords,
        cache=cache),
        ["γραμμένο", "λθος"])

    eq_(greek.stopwords, pickle.loads(pickle.dumps(greek.stopwords)))
