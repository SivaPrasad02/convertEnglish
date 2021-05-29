# The library is created for Conversion of spoken text to written text  
---
<b> It has two both flask file (app.py) and main.py file </b>

The Function of this library is used to convert the spoken text to written test <br>

------------
Feature I have Implemented Aree given Below </br>
Ex : 
```
Input : Two Dollors
Output : $2
```
```
Input : H T M L 
Output : HTML
Explanation : while speaking we will pronounnce HTMl seperately but while writing there will be no spaces
```
```
Input : C M D
Output : CMD
```
```
Input : Triple B
Output: BBB
```
```
Input: Four A
output: AAAA
```
--------------
#### File Descriptions
<ol>
    <li> written English folders contains our COnvert.py file which converts</li>
    <li> app.py will have the flask file which have to run with input shown below</li>
    <li>  Main.py Run the file with python main.py file</li>
</ol>

### How to run the File 
```
1.Frist clone this repository 
2. Change directory to written_english 
        'cd written_english'
3. Type this command in the for installing requirements
        pip3 install requirements.txt
4. Then if you want to run in cmd then type 
        python main.py
        Enter the Spoken English Text :  Two dollors 
  otuput : spoken english ' two dollors '  Conversion to written english ' $2 '

```

<b> If you want to run with API (Flask)then type this in cmd or python interpreter </b>

```python app.py```

```
Output
  * Serving Flask app "app" (lazy loading)
  * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
  * Debug mode: on
  * Restarting with windowsapi reloader
  * Debugger is active!
  * Debugger PIN: XXXXX
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
  
<b> Next go to the browser then copy paste the url +input you want <b>
Ex: <br>

```
Format : http://127.0.0.1:5000/INPUT
Ex : http://127.0.0.1:5000/two dollors 
Output you will see in the page
```
```
Requirements:
            Flask==1.1.2
            python >= 3.6
```