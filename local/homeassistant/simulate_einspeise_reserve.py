import sys

RESERVE_W = 1000
MAX_LADELEISTUNG_W = 3500
MAX_ANSTIEG_W = 500
ANSTIEGS_FAKTOR = 0.5
GRID_SOLL_W = -40
REGELINTERVALL_S = 10
ANLAGEN_TRAEGHEIT_S = 6


def naechstes_ladelimit(einspeisung_w: float, ladeleistung_w: float) -> float:
    ueberschuss_w = einspeisung_w - RESERVE_W
    aenderung_w = min(ueberschuss_w * ANSTIEGS_FAKTOR, MAX_ANSTIEG_W) if ueberschuss_w > 0 else ueberschuss_w
    return min(max(ladeleistung_w + aenderung_w, 0), MAX_LADELEISTUNG_W)


def simuliere(pv_verlauf_w: list[float], verbrauch_w: float) -> None:
    ladeleistung_w = 0.0
    limit_w = 0.0
    for sekunde, pv_w in enumerate(pv_verlauf_w):
        gewuenscht_w = pv_w - verbrauch_w - GRID_SOLL_W * -1
        ladeleistung_w += (min(max(gewuenscht_w, -3000), limit_w) - ladeleistung_w) / ANLAGEN_TRAEGHEIT_S
        einspeisung_w = pv_w - verbrauch_w - ladeleistung_w
        if sekunde % REGELINTERVALL_S == 0:
            limit_w = naechstes_ladelimit(einspeisung_w, max(ladeleistung_w, 0))
            print(f"t={sekunde:4d}s PV={pv_w:5.0f} Einspeisung={einspeisung_w:6.0f} Laden={ladeleistung_w:6.0f} Limit={limit_w:5.0f}")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sonnig = [4500.0] * 200
    wolke = [1200.0] * 100
    wieder_sonnig = [4500.0] * 100
    simuliere(sonnig + wolke + wieder_sonnig, verbrauch_w=500)


if __name__ == "__main__":
    main()
