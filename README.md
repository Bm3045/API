# 🌍 Global Trend API Integration Project

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![API](https://img.shields.io/badge/API-JSONPlaceholder-orange)](https://jsonplaceholder.typicode.com)

A Python CLI application that fetches and displays data from JSONPlaceholder API with filtering, caching, and comprehensive error handling. Built for the Global Trend API Integration Internship Assignment.

## 📋 Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Filtering Options](#-filtering-options)
- [Error Handling](#-error-handling)
- [Testing](#-testing)
- [Assumptions & Notes](#-assumptions--notes)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## ✨ Features

### ✅ Core Features
- **Dual API Integration**: Fetches data from 2 different endpoints (Posts & Users)
- **Smart Caching**: Local JSON caching with auto-expiry (1 hour)
- **CLI Interface**: User-friendly command-line interface
- **Filtering System**: Multiple filtering options for data
- **Detailed Views**: Complete information display for single items

### 🔧 Technical Features
- **Comprehensive Error Handling**: Network, timeout, JSON, and validation errors
- **Data Validation**: Checks API response structure and data types
- **Session Management**: Efficient HTTP session reuse
- **Modular Design**: Clean separation of concerns

## 📁 Project Structure


global-trend-api-project/
│
├── main.py # Main CLI application
├── api_handler.py # API calls with error handling
├── cache.py # Data caching logic
├── config.py # Configuration settings
│
├── requirements.txt # Python dependencies
├── README.md # This documentation file
├── data_cache.json # Auto-generated cache file
│
├── screenshots/ # Screenshots folder
│ ├── main_menu.png
│ ├── posts_list.png
│ └── user_details.png
│
└── tests/ # Test files (optional)
├── test_api_handler.py
└── test_cache.py


### File Descriptions

| File | Purpose |
|------|---------|
| **main.py** | Entry point with CLI interface and menu system |
| **api_handler.py** | Handles all API communication with error handling |
| **cache.py** | Manages data storage and retrieval with expiry |
| **config.py** | Centralized configuration and constants |
| **requirements.txt** | Project dependencies |

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Internet connection (for initial API fetch)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/global-trend-api-project.git
   cd global-trend-api-project

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

3. **Install dependencies**

   ```bash
pip install -r requirements.txt
Verify installation

  ```bash
python --version
pip list
