# Einspeise-Reserve

Begrenzt das Laden der Batterie so, dass tagsüber mindestens `einspeise_reserve_w` (Standard 1000 W) eingespeist werden. Nachts fällt das Ladelimit von selbst auf 0 W, das Grid-Soll bleibt unverändert (-40 W).

Stellgröße ist `number.gx_device_ess_maximale_ladeleistung` (ESS-Ladeleistungsbegrenzung, -1 = aus). Sie ist unabhängig von DVCC und vom `max_battery_charge_current` des Treibers.

## Einrichten

1. In `configuration.yaml` Packages aktivieren: `homeassistant: { packages: !include_dir_named packages }`
2. `einspeise_reserve.yaml` nach `<config>/packages/` kopieren, Konfiguration prüfen und neu laden.
3. Im Dashboard `einspeise_reserve_w` (1000), `einspeise_reserve_max_ladeleistung_w` (3500) und `einspeise_reserve_max_anstieg_w` (500) setzen.

## Erst beobachten, dann aktivieren

`input_boolean.einspeise_reserve_aktiv` steht zunächst auf `off`. Die Automation berechnet dann nur `input_number.einspeise_reserve_ladelimit_w` und schreibt nichts an den GX. Einige Sonnentage mit dem Verlauf dieses Wertes vergleichen.

## Einmal von Hand prüfen, bevor aktiviert wird

Ohne DVCC ist nicht sicher, dass die ESS-Ladeleistungsbegrenzung greift.

1. Bei laufender Ladung `number.gx_device_ess_maximale_ladeleistung` auf z. B. 500 W setzen.
2. In `sensor.gx_device_dc_batterie_leistung` muss die Ladeleistung innerhalb weniger Sekunden auf etwa 500 W fallen.
3. Danach den Wert wieder auf -1 setzen.

Greift die Begrenzung nicht, bleibt die Regelung wirkungslos. Dann muss ein anderer Stellhebel her.

## Verhalten

- Einspeisung über der Reserve: Ladelimit steigt um die Hälfte des Überschusses, höchstens um `max_anstieg_w` je Durchlauf (alle 10 s).
- Einspeisung unter der Reserve: Ladelimit sinkt sofort um das Defizit, nie unter 0 W.
- Netz- oder Batteriesensor nicht verfügbar: Ladelimit 0 W.
- Ausschalten von `einspeise_reserve_aktiv` setzt die Begrenzung auf -1 zurück.
- Geschrieben wird nur bei Abweichung von mindestens 100 W, damit die Einstellung im GX nicht ständig neu gespeichert wird.

`simulate_einspeise_reserve.py` zeigt das Regelverhalten gegen eine einfache Anlage mit Wolke.
