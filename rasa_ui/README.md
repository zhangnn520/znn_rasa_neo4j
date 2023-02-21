# Rasa-UI
A simple Rasa UI implemented with [Bootstrap 3](https://getbootstrap.com/docs/3.3/)

![a.gif](https://i.loli.net/2020/06/18/KEG1atwnScQFIgV.gif)

# README.md
[简体中文](README.zh_CN.md)

# Usage
1. Init Rasa
```bash
rasa init
```
2. Run Rasa API (Allow cross-domain)
```bash
rasa run --enable-api --cors "*"
```
3. Directly open `index.html`

# PS
utter_greet in domain.yml can change to it for buttons:
```yaml
responses:
  utter_greet:
  - text: Hey! How are you?
    buttons:
      - payload: '/mood_great'
        title: 'great'
      - payload: '/mood_unhappy'
        title: 'sad'
```