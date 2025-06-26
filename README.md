
# 🔍 Expert Port Scanner — Advanced Python-Based Network Tool

**Expert Port Scanner** is a high-performance, full-featured port scanning tool built using Python. Designed for cybersecurity professionals, penetration testers, and network engineers, this tool goes beyond basic scanning by providing fast, reliable, and informative results with a beautiful CLI interface.

## 🚀 Features
- ✅ **Flexible Port Input**: Scan single ports, multiple ports, or ranges (e.g., `80`, `22,443`, `20-1024`)
- ⚡ **Multi-threaded Scanning**: Fast scanning with ThreadPoolExecutor
- 🧠 **Banner Grabbing**: Attempts to detect service banners on open ports
- 🎯 **Smart Host Validation**: Supports both IP addresses and domain names
- 🎨 **Rich CLI UI**: Built with `rich` for colorful and interactive output
- 💾 **Export Results**: Save output to `.txt` and `.json` files
- 📈 **Progress Bar & Timer**: Real-time feedback during scans

## 🛠️ Tech Stack
- Python 3.8+
- Modules: `socket`, `concurrent.futures`, `rich`
- Modular architecture for scalability and maintainability

## 📂 Project Structure
```
port-scanner/
├── main.py         # Entry point
├── scanner.py      # Scanning logic
├── utils.py        # Input parsing & validation
├── output.py       # Result export to file
├── requirements.txt
```

## ✅ How to Run
```bash
git clone https://github.com/yourusername/expert-port-scanner.git
cd expert-port-scanner
pip install -r requirements.txt
python3 main.py
```

## 📜 License
MIT License

---

