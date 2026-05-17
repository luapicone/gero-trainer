# gero-trainer

Landing estática multi-page para el universo de **Hermes Onori / personal training**, basada en la estructura original replicada desde `hermesonori.com` pero rediseñada con una dirección visual más premium y atlética.

## Páginas

- `index.html` → selector principal Argentina / Worldwide
- `pagina1.html` → versión Argentina
- `pagina2.html` → versión Worldwide
- `coaching.html` → checkout / instrucciones para coaching 1:1

## Scripts

- `npm install`
- `npm run dev`
- `npm run build`
- `npm run preview`

## Power Automate

Se agregó un paquete base en `power-automate/procedimiento-package/` para importar/usar como plantilla del flujo **Procedimiento**.

- `power-automate/procedimiento-package/Procedimiento-import.zip` → paquete base
- `power-automate/build_procedimiento_package.py` → regenera el zip si se editan los JSON
