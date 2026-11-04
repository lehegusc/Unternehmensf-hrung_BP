# BP Analyse

Unternehmensanalyse von BP (British Petroleum) im Rahmen des Moduls Unternehmensführung & Organisation, HWG Ludwigshafen.

## Docs-Wiki starten

Das Projekt enthält eine lokale Website, die alle Markdown-Dateien als Wiki anzeigt. Dafür wird nur **Python 3** benötigt (keine weiteren Pakete).

### Mac

1. Python 3 installieren (falls nicht vorhanden): `brew install python3` oder von [python.org](https://www.python.org/downloads/)
2. Doppelklick auf **`start-docs.command`**
3. Der Browser öffnet sich automatisch unter `http://localhost:8000`
4. Terminal-Fenster schließen, um den Server zu stoppen

Falls macOS den Doppelklick blockiert ("nicht verifizierter Entwickler"): Rechtsklick auf die Datei, dann "Öffnen" wählen.

### Windows

1. Python installieren von [python.org](https://www.python.org/downloads/). Beim Installer das Häkchen bei **"Add Python to PATH"** setzen.
2. Doppelklick auf **`start-docs.bat`**
3. Der Browser öffnet sich automatisch unter `http://localhost:8000`
4. Kommandozeilen-Fenster schließen, um den Server zu stoppen

## Ordnerstruktur

```
bp-analyse/
  01-mission-werte-ziele/    Schritt 1: Purpose, Mission, Werte, Ziele
  02-umfeldanalyse/          Schritt 2: PESTLE, Megatrends, Chancenanalyse
  03-branche-wettbewerb/     Schritt 3: Five Forces, Strategische Gruppen
  04-ressourcen-faehigkeiten/ Schritt 4: VRIO, Wertkette
  05-strategie-organisation/ Schritt 5: Strategie & Organisation
  06-synthese/               Schritt 6: SWOT, Empfehlungen
  folien-md/                 Vorlesungsfolien als Markdown
  paper/                     Paper-Entwürfe
  _docs-site/                Website-Code (nicht bearbeiten)
  STATUS.md                  Aktueller Projektstatus
  notizen-dozentin.md        Mündliche Hinweise von Prof. Raschke
  quellen.md                 Quellensammlung (APA 7)
```

## Workflow

1. Neue Inhalte als `.md` Dateien in den passenden Ordner legen
2. Wiki starten, um die Inhalte formatiert zu lesen
3. Änderungen per `git pull` / `git push` synchronisieren
