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
