# FlipperZero - L80GPS integration

Found a dusty GPS module in the drawer and decided to give it some life:

![](./media/blink.gif)

1. `python3 -m venv .`
2. `source ./venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. `patch -d venv/lib/python3.12/site-packages/microstacknode/hardware/gps < l80gps.patch`
5. `python3 read_gps.py`
