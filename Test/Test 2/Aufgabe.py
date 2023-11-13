# In unserem Modell müssen wir unterschiedliche Personen abbilden:
# Es gibt Mitarbeiter und Kunden.
# Die Mitarbeiter unterteilen sich wiederum in Arbeiter und Angestellte.
# Von allen Personen speichern wir den Vor- und Nachnamen, die Telefonnummer
# und die E-Mail-Adresse sowie die Wohn- bzw. Geschäftsadresse.
# Von den Mitarbeitern brauchen wir noch das Eintrittsdatum und die Versicherungsnummer.
# Bei unseren Kunden brauchen wir den Firmennamen.
# Für alle Angestellten ist eine Methode email_senden() vorgesehen.
# Unsere Kunden haben die Methode erteile_auftrag(). Der Rückgabewert ist ein String.
# (Siehe ganz unten im Angabezettel die erwünschte Ausgabe)
# Die Angestellten haben außerdem noch die Methode bearbeite_auftrag().
# Jeder Kunde hat einen Mitarbeiter, der ihn betreut.
# Alle Mitarbeiter haben die Methode check_in() und check_out(), die erfaßt ob sie in der
# Arbeit anwesend sind.
# Arbeitet mit Rückgabewerten!



# HIERHER KOMMT DEIN CODE
class Person():
    def __init__(self, vorname, nachname, telefonNummer, eMail) -> None:
        self.vorname = vorname
        self.nachname = nachname
        self.telefonNumner = telefonNummer
        self.eMail = eMail

class Mitarbeiter(Person):
    checked_in = False
    
    def __init__(self, vorname, nachname, telefonNummer, eMail, geschaftsAdresse, eintrittsdatum, versicherungsNummer) -> None:
        super().__init__(vorname, nachname, telefonNummer, eMail)
        self.geschaftsAdresse = geschaftsAdresse
        self.eintrittsdatum = eintrittsdatum
        self.versicherungsNummer = versicherungsNummer
        
    def check_in(self):
        if self.checked_in:
            return f'{self.nachname} ist bereits im Dienst!'
        
        self.checked_in = True
    
    def check_out(self):
        if not self.checked_in:
            return f'{self.nachname} ist shon weg!'
        
        self.checked_in = False
    
    def check_status(self) -> str:
        if self.checked_in:
            return f'{self.nachname} im Dienst'
        else:
            return f'{self.nachname} nicht anwesend'

class Arbeiter(Mitarbeiter):
    def __str__(self) -> str:
        return f'Arbeiter {self.vorname} {self.nachname}'

class Angestellter(Mitarbeiter):
    def email_senden(self):
        pass
    
    def bearbeite_auftrag(self):
        pass
    
    def __str__(self) -> str:
        return f'Angestellter {self.vorname} {self.nachname}'

class Kunde(Person):
    def __init__(self, vorname, nachname, telefonNummer, eMail, wohnAdresse, firmenNamen, betreuer: Mitarbeiter) -> None:
        super().__init__(vorname, nachname, telefonNummer, eMail)
        self.wohnAdrese = wohnAdresse
        self.firmenNamen = firmenNamen
        self.betreuer = betreuer
        
    def erteile_auftrag(self, empfanger: Mitarbeiter) -> str:
        return f'Kunde {self.nachname} erteilt einen Auftrag an {empfanger.nachname}'
    
    def get_betreuer(self) -> str:
        return f'{self.betreuer} email: {self.betreuer.eMail}'
    
    def __str__(self) -> str:
        return f'Kunde {self.vorname} {self.nachname}'




# Dieser Code darf nicht verändert werden!!!
def testing():
    huber = Angestellter('Hans', 'Huber', '0676 1234567', 'hh@xy.net',
                         'Villach, Bergweg 4', '1.1.2010', '1212 121283')
    meier = Angestellter('Martin', 'Meier', '0676 1000067', 'mm@xy.net',
                         'Villach, Flurgasse 4', '1.1.2010', '3287 111283')
    polster = Angestellter('Peter', 'Polster', '0660 1234567', 'pp@xy.net',
                           'Klagenfurt, Bergweg 4', '1.1.2014', '8454 121287')
    kunze = Angestellter('Klaus', 'Kunze', '0676 1234567', 'kk@xy.net',
                         'Villach, Hochoben 4', '1.10.2011', '8448 191191')
    winter = Arbeiter('Walter', 'Winter', '9876543', 'ww@xy.net', 'Wolfsberg',
                      '15.4.2000', '9275 050278')
    adeg = Kunde('Alfred', 'Adamitsch', '23456789', 'adamitsch@adeg.at', 'Klagenfurt',
                 'Adeg', polster)
    spar = Kunde('Sigfried', 'Sommer', '23456789', 'sommer@spar.at', 'Salzburg',
                 'Spar', meier)
    billa = Kunde('Bertram', 'Baumann', '23456789', 'baumann@billa.at', 'Wien',
                  'Billa', kunze)

    mitarbeiter = {'Huber': huber, 'Meier': meier, 'Polster': polster, 'Kunze': kunze, 'Winter': winter}
    kunden = {'Adeg': adeg, 'Spar': spar, 'Billa': billa}

    # für 3 Mitarbeiter die check_in() Methode aufrufen
    polster.check_in()
    kunze.check_in()
    winter.check_in()

    # für alle Mitarbeiter ausgeben, ob sie anwesend sind oder nicht
    print("für alle Mitarbeiter ausgeben, ob sie anwesend sind oder nicht:")
    
    for values in mitarbeiter.values():
        print(values.check_status())


    # für den Kundenbetreuer von Spar die Email ausgeben (Zugriff über das kunden Dictionary!)
    print("\nfür den Kundenbetreuer von spar die Email ausgeben (Zugriff über das kunden Dictionary!)")
    
    print(kunden['Spar'].get_betreuer())




    # alle Kunden ausgeben:
    print('\nalle Kunden ausgeben:')
    
    for key, value in kunden.items():
        print(f'{key} : {value}')





    # Kunde Adeg erteilt einen Auftrag
    print('\nKunde Adeg erteilt einen Auftrag:')
    
    print(kunden['Adeg'].erteile_auftrag(mitarbeiter['Polster']))




    # alle Mitarbeiter ausgeben:
    print('\nalle Mitarbeiter ausgeben:')
    
    for i in mitarbeiter.values():
        print(i)







testing()