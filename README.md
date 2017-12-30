# safe
A homemade safe powered by a raspberry pi.
      <p> Web server also on it:</p>
      <img src="https://www.gaborszita.tk/my-creations/safe/web1.JPG" alt="Web server image 1"><br>
      <img src="https://www.gaborszita.tk/my-creations/safe/web2.JPG" alt="Web server image 2"><br>
      <p>Instructions:</p>
      <p>1. <b>Hardware</b></p>
      <p>First, buy a raspberry pi($35), an Adafruit CharLCD plate, an electric
        lock,an NPN transistor and an adapter, that has both 12V and 5V output.
        Then build a case(could be wood, like mine or anything you want.) For
        setting up the raspberry pi see <a href="https://www.raspberrypi.org/help/noobs-setup/2/">this
          tutorial</a>. Enabling vnc and ssh is also helpful.</p>
      <br>
      <br>
      <p>2. <b>Building it</b></p>
      <p>Mount the raspberry pi and the electric lock in the safe and the
        Adafruit CharLCD plate on the rpi. I also recommend buiding a keyhole,
        because the software may crash.</p>
      <img src="https://www.gaborszita.tk/my-creations/safe/safeoff1.jpg" alt="Safe image 1" height="300px"><br>
      <img src="https://www.gaborszita.tk/my-creations/safe/safeoff2.jpg" alt="Safe image 2" height="300px">
      <p>3.<b>Wiring</b></p>
      <p>Connect the wires as shown. You can connect the NPN to another pin, but
        then you will need to change the code.</p>
      <img src="https://www.gaborszita.tk/my-creations/safe/schematics.gif" alt="Schematics" height="700px"><br>
      <p>4.<b>Software</b></p>
      <p>Configure the Adafruit CharLCD plate using <a href="https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black/usage">this
          tutorial</a>. Download the <a href="safe.py">safe.py</a> and the <a
	href="code.txt"> code.txt</a> file and paste it in /home/pi/safe (you
        can put it anywhere, but then you will need to change the code.) Run it.
        It work's! Button up and down change the value of the digits, and the
        left and right set's what digit to change. And it start's to display the
        time if it's inactive for 2 minutes. To start it every time on startup
        edit the /etc/rc.local and type ```sudo python /path/to/safe.py/file``` before the exit0</p>
      <p>If you want also web server on it intall the apache2 web server and
        configure python script running using <a href="https://www.raspberrypi.org/forums/viewtopic.php?t=155229">this
          tutorial</a>. Paste <a href="index.html">this</a> file in
        /var/www/html. Download the <a href="safeweb.py">safeweb.py</a>
        file and paste it in /usr/lib/cgi-bin. Make it executable, so type in
        the terminal window ```sudo chmod +x /usr/lib/cgi-bin/swafeweb.py ```
	Restart the web server using ```sudo service apache2 restart```.
	Make the code.txt
	writeable by anyone, so code.txt →right click →Properties →Permissions
 	→Change content →Anyone</p>

