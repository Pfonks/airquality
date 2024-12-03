# airquality
Script to measure co2-leves using a mh_z19 sensor on a raspberrypi and display the current level using a traffic light with LEDs

![My current setup showing two panes of plexiglas containing a raspberry pi, a traffic light made of LEDs and the bespoken mh_z19 sensor.]()

Using cron to run periodically:

```*/2 * * * * python3 /home/pi/airquality_service.py```

```airquality.R``` contains the R source I use to visualize the data I've collected
