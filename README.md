
# 🧨 APNG Bomb (700GB RAM) - Minimal RAM Strategy

This project demonstrates how to generate a 4–8MB APNG file that consumes **700+ GB RAM** when opened, using chunked creation to avoid memory exhaustion on weak machines.

## ⚠️ Educational Use Only
This is a research and awareness project only. Do not upload these files to public systems.

## 🛠 Requirements

```bash
pip install pillow apng
```

## 📄 Script: create_apng_bomb_700gb.py

```python
# Full script automates creation of 30 frames (90k x 90k) using low RAM
# Saves each frame separately to avoid memory overload
# Merges all into one APNG bomb (apng_bomb_700gb_final.png)
```

## ✅ Final Output
- File size: ~4–8MB
- Memory usage on open: ~700GB+
- Safe to create even with 4GB RAM machine

---

**Brought to you by Pablo Rotem / פבלו רותם**
