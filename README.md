# Alarmas

Contiene todo lo necesario para la ejecucion del despliegue de información hidrológica 
de las alarmas comunitarias de **SIATA**. 

- Consulta de niveles, pluvio a partir de **CPR**.
- Generación de reportes a partir de **CPR**.
- Despliegue *web* de los resultados. 
- Integración de resultados de modelación. 
- Integra resultados de campos de lluvia agregados a la cuenca. 

## Requisitos:

Para su correcta ejecución se deben tener los siguientes requisitos:

- Estar al interior de la red de SIATA para la realizaciónd e consultas. 
- Modelo **WMF** (https://github.com/nicolas998/WMF.git).
- Paquete de radares (https://github.com/nicolas998/Radar.git)
- Los siguientes paquetes de **Python**:
	- Pandas.
	- numpy.
	- matplotlib.
	- datetime.
	- reportlab.
	- cpr.

## Instalación:

Para instalar este paquete en su equipo debe en una terminal de bash indicar el siguiente 
codigo:

Primero debe desplazar la **terminal** hasta la carpeta *clonada* o *descargada* de este repo.

```bash
cd Path/Alarmas
```

Luego se realiza la instalación, para esto debe tener privilegios de **sudoer**.

```bash
sudo python setup.py install
```

## Contacto:

Dudas sobre el codigo, y sugerencias:

- Para dudas escribir a: *hidrosiata@gmail.com*.
- Reporte de bugs y problemas favor escribirlos en: https://github.com/SIATAhidro/Alarmas/issues

