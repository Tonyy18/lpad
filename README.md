# Launchpad API
<p>Python library to interact with your midi devices</p>
<p>This library is build for Novation launchpads unsing Launchpad Pro.</p>
<p>Suitability for other Launchpads is not quaranteed</p>
<p></p>
<a href="https://player.vimeo.com/video/461906308">Preview video</a>

<h2>Usage</h2>

<p>The library is wrapped around pygame library in order to get access to midi devices</p>

```python
import lpad
launchpad = lpad.Init("live")
```

<p>Make sure you are using the right mode. Live mode uses a different channel and therefore needs to be told as an argument.</p>

<h3>Events</h3>
<p>Listening events happens using the feature decorator</p>

<b>onData</b>
<p>Is called on every data object received. Use this to implement your own events</p>

```python
@launchpad.feature
def ondata(data):
    print(data)
    
@launchpad.feature
def keypress(note):
    print(note)
```

<p>Before you can receive any events you must start listening incoming data</p>
<p>This is done by calling the <b>poll</b> method</p>

```python
launchpad.poll()
```

<p>Make sure you call the <b>poll</b> method after you have defined all your events since it runs in the same thread</p>

<p>When you are done using the midi ports make sure you close them using the <b>close</b> method</p>

```python
launchpad.close()
```

<h3>Controlling the lights</h3>
<p><b>on</b>, <b>off</b>, and <b>clear</b> methods are part of light controlling</p>

```python
launchpad.on(key=81, color=51)
launchpad.off(key=81)
```

<p><b>on</b> method takes an extra argument which is the color of the button. The color integers can be found below</p>

```python
launchpad.clear()
```

<p><b>clear</b> is used to turn off all lights</p>

![alt text](https://lh3.googleusercontent.com/proxy/LeyiuHzIYylNTwewdXMBBs2hid4rXDo91P1jGucPC8_fVXJSwrpbe_QIX5_pKUPNtZT-9NB2QfT9blIyGbYDQNYTrWLWqqSlT5UDmVN6rLWG_w287UjlyMY-gJbjYl_KFGB1nHY-)

<h2>Important</h2>
<p>Launchpad pro has 5 different modes. <b>live</b>, <b>note</b>, <b>drum</b>, <b>fader</b> and <b>programmer</b></p>
<p>Make sure you import the right mode in the constructor, otherwise it wont work properly</p>
<p>Use the <b>onData</b> event to implement your own events for different modes</p>
