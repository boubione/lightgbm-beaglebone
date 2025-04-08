# lightgbm-lite

A minimal, stripped-down version of [LightGBM](https://github.com/microsoft/LightGBM) optimized for edge devices running Debian 10+.

This version is **precompiled** and **removes the SciPy dependency** to reduce disk usage and simplify deployment on embedded Linux systems like the BeagleBone.

---

## 🚀 Features

- ✅ **No need for CMake, make, or building anything**
- ✅ **No SciPy dependency**
- ✅ Lightweight shared library (~6MB)
- ✅ Compatible with Python 3.7+
- ✅ Ideal for edge and embedded Linux systems
- ✅ Maintains core LightGBM functionality

---

## ⚠️ Notes

- This package is **precompiled**, so it's **ready to use** — no building required.
- `lgb._version` will not work. To check if the installation works, run a simple train + predict test (see below).
- Make sure `lib_lightgbm.so` is correctly placed in `lightgbm/lib/`.

---

## 📦 Installation (Manual)

Since this package is optimized for edge devices, you can manually copy it to your target system
