# Damclock

Damclock is a Flask clock app with selectable digital clock faces, including an F-91W-inspired face and an interactive World Time watch.

## Run locally

From this folder, create and activate a virtual environment, install the requirements, then start the app:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `https://localhost:5000`. If the browser warns about the local development certificate, that warning applies only to local use.

## Use the watch faces

1. Open **Settings** and choose **Casio F-91W** or **Casio World Time** under **Clock Style**.
2. Press **M** on the watch to cycle through time, world time (World Time face), date, stopwatch, and alarm.
3. In World Time mode, press **S** to cycle cities. The selected city is saved in this browser.
4. In time mode, **S** changes between 12-hour and 24-hour time.
5. In stopwatch mode, **S** starts or pauses and **R** resets.
6. In alarm mode, hold **M** to enter or leave setting. Press **S** to change the selected hour or minute and **R** to switch between them. Press **M** to save. Press **S** to toggle the alarm; **R** disables or silences it.
7. Press **L** for a brief backlight effect.

Alarm and clock-face preferences are stored in the browser. The alarm can sound only while the site is open.

## Publish the website with Render

The `render.yaml` file is a Render Blueprint for this folder. Create a **private** GitHub repository for the contents of this folder, push the project to it, then in Render choose **New > Blueprint**, connect that repository, and apply the Blueprint. Render will provide a public HTTPS URL while the source repository stays private.

The local `.pem` certificates, Python caches, virtual environments, and generated design drafts are excluded by `.gitignore`; do not add private keys to a repository.
