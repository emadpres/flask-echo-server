# Running
1. `python3 -m venv .venv`
1. `source .venv/bin/activate`
1. `pip3 install -r ./requirements`
1. Decice between HTML or Text mode, by setting `HTML_MODE` variable
1. `flask run --host=0.0.0.0 --port=5500`
   - you can run multiple servers on different ports. Simply, open new terminal in the same directory and run line 
above with a new port (no need to duplicate this project directory)
