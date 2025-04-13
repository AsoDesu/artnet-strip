💡 ArtNet Strip

python program for controlling a WS281x LED Strip over Art-Net with a Raspberry Pi

## how to use

1. Install Python & Pip
2. Run `python -m venv .venv/` to setup virtual environment
3. Run `./.venv/bin/pip install -r /path/to/requirements.txt` to install dependencies
4. Update `index.py` with the following info
   - `LED_COUNT` to the amount of LEDs in your strip
   - `PATCH_UNIVERSE` what ArtDMX universe to listen on
   - `PATCH_ADDRESS` your starting DMX address
5. Run `sudo ./.venv/bin/python3 index.py` (need to run as sudo for GPIO stuff)
6. Patch in your lighting desk of choice, the DMX parameters look like this:
   (all values are 8-bit percent ranges)
   - 1: Master Intensity
   - For each individual LED (referred to as a cell)
     - 2: Cell Intensity
     - 3: Cell Red
     - 4: Cell Green
     - 5: Cell Blue
