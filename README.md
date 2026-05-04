# MON-Milk-Bar-ai

Caption Generator for MON-MILK-BAR Cafe Instagram Posts

## Overview
This tool generates 3 creative Instagram caption variants for MON-MILK-BAR cafe menu items using Google's Gemini 2.5 Flash API. It produces captions in 3 styles:
- **Cute**: Adorable, playful with emojis
- **Minimal**: Clean, sophisticated aesthetic
- **Gen-Z**: Trendy, casual, relatable vibes

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Google API Key
1. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Add your API key to `.env`:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Usage

### Basic Usage (with example)
```bash
python caption1.py
```

### Generate Captions for a Menu Item
```bash
python caption1.py "Strawberry Milk Tea" "$5.99"
python caption1.py "Mango Boba" "$6.49"
python caption1.py "Taro Smoothie" "$7.99"
```

## Output Example
```
════════════════════════════════════════════════════════════════
📸 Instagram Caption Variants for: Strawberry Milk Tea ($5.99)
════════════════════════════════════════════════════════════════

✨ CUTE STYLE:
🍓✨ Sweet dreams are made of THIS! 🥛💕 Our Strawberry Milk Tea is pure happiness in a cup! Perfect for your cozy afternoon vibes ☁️😊

────────────────────────────────────────────────────────────────

🎯 MINIMAL STYLE:
Strawberry Milk Tea. $5.99. Crafted with premium ingredients for the perfect moment.

────────────────────────────────────────────────────────────────

🔥 GEN-Z STYLE:
not u NOT ordering our strawberry milk tea rn... this is literally THEE drink of the season no cap 🍓✨ $5.99 and ur welcome

════════════════════════════════════════════════════════════════
```

## Features
- ✅ Loads API key securely from `.env` file
- ✅ Uses Gemini 2.5 Flash for fast, creative responses
- ✅ Generates 3 distinct caption styles
- ✅ Command-line interface for easy usage
- ✅ Formatted output with visual separators

## Requirements
- Python 3.8+
- Google API Key with Gemini access
- Dependencies in `requirements.txt`