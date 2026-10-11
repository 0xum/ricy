# English dates and Cosmópolis/SP location in Noctalia

The integration uses `shell.lang = "en"`, `LC_TIME=en_US.UTF-8`, and
`TZ=America/Sao_Paulo` only in the Noctalia unit. The desktop region and keyboard
composition rules retain their existing settings. `LC_ALL` is removed from that
unit's environment so it cannot override LC_TIME. The en_US.UTF-8 locale must be
generated on the destination.

Location is fixed with `auto_locate = false` and
`address = "Cosmopolis, Sao Paulo, Brazil"`. The full address avoids the city
with the same name in the United States. The native API resolved the destination
as Cosmópolis, Brazil, latitude -22.64583, longitude -47.19611.

Weather is enabled in metric units (°C); Noctalia queries Open-Meteo.
Calendar/events are enabled without adding accounts, event sources, or holidays.
Personal events require connecting Google, CalDAV, ICS, or vdir later through
Noctalia settings. Location is used for weather; the calendar uses the session's
time zone and events from its sources.

## Apply

After preparing the permanent integration and notification contribution:

```bash
cd "$HOME/Projects/ricy/ricy-kit"
python contributions/noctalia-language-and-localization/apply.py
```

The script changes only the keys listed in PREFERENCES in the profile and its
private settings.toml (interface preferences may override the template).
It preserves accounts and other options, validates the configuration, and installs
`60-ricy-idioma-localizacao.conf` in the noctalia-teste.service unit.
It restarts only shell/adapter through the existing application-preservation helper.
It does not install packages or change the global system locale.
Public kit templates already include language, location, weather, and calendar;
the applicator adds the date environment and corrects local overrides.

## Verification and reversal

In the original installation: configuration validated; the calendar displayed
Saturday/October; geocoding confirmed Brazil; weather received data and a seven-day
forecast with the America/Sao_Paulo time zone. No calendar account was synchronized,
as requested by the user. Installation on another machine was not performed.

Previous profile, settings, and drop-in backups are stored in
`$HOME/.local/state/ricy-idioma-localizacao-backups/DATA-HORA/`, with a manifest
indicating files that did not exist. To restore, review the manifest, restore only
the desired files, and remove the drop-in if previously absent.
Restoring the entire settings.toml also reverses later preference changes.
Reload systemd and restart shell/adapter using the application-preservation helper
used by apply.py; avoid an ordinary shell restart if child applications must
remain open. Templates are independent of local state; also adjust their keys if
the reversal should persist through reinstallation.

Location source: [geocoding used by Noctalia](https://api.noctalia.dev/geocode?city=Cosmopolis%2C%20Sao%20Paulo%2C%20Brazil).
