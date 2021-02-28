# Befehle, die sich gut als Shortcuts eignen:

## Schnellsuche:
```bash
bash -c "xclip -o | jq -sRr @uri | awk '{print \"https://www.qwant.com/?q=\" $1}' | xargs firefox"
```
Benötigte Pakete: xclip, jq, firefox
Beschreibung: Sucht nach dem markierten Text mithilfe von Qwant in Firefox.
Hinweise: Suchmaschine und Browser können natürlich beliebig ausgetauscht werden.

## Schnellübersetung:
```bash
bash -c "xclip -o | jq -sRr @uri | awk '{print \"https://www.deepl.com/translator#*/de/\" $1}' | xargs surf"
```
Benötigte Pakete: xclip, jq, surf (Hinweis für Arch-Nutzer: Surf gibt es im AUR als surf-git)
Beschreibung: Öffnet ein neues Fenster mit DeepL und des markierten Textes als Eingabe.
Hinweise: Übersetzer und Browser können natürlich beliebig ausgetauscht werden.