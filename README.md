# safe
A homemade safe powered by a raspberry pi.
      <p> Web server also on it:</p>
      <img src="https://gaborszita.net/wp-content/uploads/2019/08/web1-1.jpg" alt="Web server image 1"><br>
      <img src="https://gaborszita.net/wp-content/uploads/2019/08/web2-1.jpg" alt="Web server image 2"><br>
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
      <img src="https://gaborszita.net/wp-content/uploads/2019/08/safeoff1little-1-576x1024.jpg" alt="Safe image 1" height="300px"><br>
      <img src="https://gaborszita.net/wp-content/uploads/2019/08/safeoff2little-1-1024x576.jpg" alt="Safe image 2" height="300px">
      <p>3.<b>Wiring</b></p>
      <p>Connect the wires as shown. You can connect the NPN to another pin, but
        then you will need to change the code.</p>
      <img src="https://gaborszita.net/wp-content/uploads/2019/08/schematics-1.gif" alt="Schematics" height="700px" width="100%"><br>
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
 	→Change content →Anyone</p> You may wonder how the system declines, when an ananymous(person, who has not logged to to the code 
	managment page) tryes to post action=changecode and newcode=somecode. This is why the form has a hidden input value "securety". 
	It is like a master key, the chain of trust. If someone knows the master key, but doesn't knows the password, he also has full 
	access to the web-based code changing protocol. This is why you should change the master key in the safeweb.py file. If you 
	leave it default and someone checks this GitHub repository, checks the default master key in the safeweb.py file, uses it on 
	your safe and he can change the code on the safe. You can change the master key by replacing all occurences of 
	"TghXCDre54ncDDAG7cxrDsRdCsfdGg" in the safeweb.py file.

