from datetime import datetime

def parse_date(str):
    """
    een correct geformatteerde datum moet geparset worden
    >>> parse_date("2019-10-01")
    datetime.date(2019, 10, 1)

    een foute date-string moet de default waarde 2000-01-01 geven
    >>> parse_date("bla")
    datetime.date(2000, 1, 1)
    """
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except:
        return date(2000, 1, 1,)

def aantal_waarden(aantal_bits):
    """
    Met 2 bits kunnen we 4 waarden voorstellen
    >>> aantal_waarden(2)
    4
    
    Met 4 bits kunnen we 16 waarden voorstellen
    >>> aantal_waarden(4)
    16
    
    Bij invoer van een ongeldige string moet een exception geworpen worden
    >>> aantal_waarden("bla")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
    """
    return 2 ** aantal_bits

def controleer_leeftijd(leeftijd):
    """

    Als de leeftijd tussen 12 en 18 jaar, return True
    >>> controleer_leeftijd(12)
    False

    >>> controleer_leeftijd(13)
    True
    
    >>> controleer_leeftijd(17)
    True
    
    >>> controleer_leeftijd(18)
    False
    """
    if(leeftijd > 12 and leeftijd < 18):
        return True
    else:
        return False


def controleer_stringlengte(str):
    """
    
    >>> controleer_stringlengte("Pythonopdracht3")
    15

    >>> controleer_stringlengte("woord")
    5

    TODO: schrijf zelf de doctests en de implementatie v.d. functie
    Bij controle van de stringlengte, geef lengte weer met een getal
    

    """
    return len(str)


def maak_groet_boodschap(naam, namenlijst):
    """

    Als naam in namenlijst voorkomt, maak een groet-boodschap
    >>> maak_groet_boodschap("Jos", ["Jos", "Mieke"])
    'Hallo Jos!'

    Als de naam niet voorkomt, is de groet-string
    >>> maak_groet_boodschap("Willy", ["Jos", "Mieke"])
    'Hallo onbekende gebruiker!'

    Als de naam "Joren" wordt meegegeven, begroet CEO
    >>> maak_groet_boodschap("Joren", ["Mieke", "Jos"])
    'Welkom terug CEO.'

    Als naam in namenlijst voorkomt, maak een groet-boodschap
    >>> maak_groet_boodschap("voorbeeld", ["voorbeeld", "nogeenvoorbeeld"])
    'Hallo voorbeeld!'

    TODO: voeg nog 2 doctests toe met een andere namenlijst

    """
    if naam in namenlijst:
        return 'Hallo' + ' ' + naam + '!'

    elif naam == "Joren":
        return 'Welkom terug CEO.'

    else: 
        return 'Hallo onbekende gebruiker!'

def laatste_x_letters(s, x):
    """

    >>> laatste_x_letters("Jos", 3)
    'Jos'

    >>> laatste_x_letters("Willy", 3)
    'lly'

    Als de string korter is dan het gevraagde aantal, toon alles
    >>> laatste_x_letters("Jo", 3)
    'Jo'

    """
    if len(s) < x:
        return s
    else:
        return s[-x:]

def aantal_dagen_in_leven(geboortedatum):
    """

    >>> aantal_dagen_in_leven("2019-10-01")
    24

    Merk op: Je kan hier moeilijk een gepaste test voor schrijven!

    We zouden hier moeten gebruik maken van mock-objecten
    maar dit valt waarschijnlijk buiten de scope van doctest.
    """
    geboortedatum_date = datetime.strptime(geboortedatum_date, "%Y-%m-%d")
    return datetime.now().day - geboortedatum_date.day

if __name__ == "__main__":
    import doctest
    doctest.testmod()

