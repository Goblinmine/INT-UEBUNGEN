from prettytable import PrettyTable

# Liste der Dateierweiterungen und Beschreibungen
file_extensions = [
    ['A', '.apk', 'Installationsdatei für Android-Anwendungen'],
    ['B', '.bmp', 'Bitmap-Datei'],
    ['C', '.csv', 'Komma-getrennte Werte-Datei'],
    ['D', '.docx', 'Microsoft Word-Dokument'],
    ['E', '.eml', 'E-Mail-Nachricht-Datei'],
    ['F', '.flv', 'Flash Video-Datei'],
    ['G', '.gif', 'Grafikformat'],
    ['H', '.html', 'Hypertext Markup Language-Datei'],
    ['I', '.ico', 'Icon-Datei'],
    ['J', '.jpg', 'Joint Photographic Experts Group-Datei'],
    ['K', '.key', 'Apple Keynote-Präsentationsdatei'],
    ['L', '.log', 'Protokolldatei'],
    ['M', '.mp3', 'MPEG Audio Layer III-Datei'],
    ['N', '.numbers', 'Apple Numbers-Tabellenkalkulationsdatei'],
    ['O', '.obj', '3D-Modell-Datei'],
    ['P', '.pdf', 'Portable Document Format-Datei'],
    ['Q', '.qt', 'QuickTime-Datei'],
    ['R', '.rar', 'RAR-komprimierte Archivdatei'],
    ['S', '.svg', 'Scalable Vector Graphics-Datei'],
    ['T', '.txt', 'Textdatei'],
    ['U', '.url', 'Internet-Verknüpfungsdatei'],
    ['V', '.vcf', 'vCard-Datei'],
    ['W', '.wav', 'Waveform Audio File Format'],
    ['X', '.xls', 'Microsoft Excel-Arbeitsmappe'],
    ['Y', '.yml', 'YAML-Datei'],
    ['Z', '.zip', 'Komprimierte Archivdatei']
]

# Erstellen einer Tabelle mit PrettyTable
table = PrettyTable()
table.field_names = ["Buchstabe", "Erweiterung", "Beschreibung"]

# Hinzufügen von Daten zur Tabelle
for ext in file_extensions:
    table.add_row(ext)

# Ausgabe der Tabelle
print(table)