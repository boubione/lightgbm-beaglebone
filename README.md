# lightgbm-lite

A minimal, stripped-down version of [LightGBM](https://github.com/microsoft/LightGBM) optimized for edge devices running Debian 10+.

This version is **precompiled** and **removes the SciPy dependency** to reduce disk usage and simplify deployment on embedded Linux systems like the BeagleBone.

---

##  Features

-  **No need for CMake, make, or building anything**
-  **No SciPy dependency**
-  Lightweight shared library (~6MB)
-  Compatible with Python 3.7+
-  Ideal for edge and embedded Linux systems
-  Maintains core LightGBM functionality

---

##  Notes

- This package is **precompiled**, so it's **ready to use** — no building required.
- `lgb._version` will not work. To check if the installation works, run a simple train + predict test (test.py included).
- Make sure `lib_lightgbm.so` is correctly placed in `lightgbm/lib/`.

---

##  Installation Guide – LightGBM-BeagleBone

A **minimal, precompiled version of LightGBM** without SciPy or build tools.  
Designed for lightweight environments like **BeagleBone (Debian 9+)**.

---

###  Requirements

Make sure Python 3.7 and NumPy are installed:

```bash
sudo apt-get update
sudo apt-get install python3-numpy libgomp1
```

##  Step 1: Download the Repository

```bash
git clone https://github.com/DanielaKaws/lightgbm-beaglebone.git
cd lightgbm-beaglebone
```

##  Step 2: Ensure the correct directory structure exists

```bash
mkdir -p ~/.local/lib/python3.7/site-packages/ #if not present
mkdir -p ~/var/lightgbm
```

```bash
cp -r lightgbm ~/.local/lib/python3.7/site-packages/
cp lightgbm/lib/lib_lightgbm.so ~/var/lightgbm/
```

##  Step 3: Run the test script

```bash
python3 test.py
```

You should see prediction output like:
Predictions: [0.5513 0.4623 0.4553 0.4623 0.5299]




