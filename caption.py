import os
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Initialize the new GenAI Client
# ถ้าในไฟล์ .env ของคุณตั้งชื่อตัวแปรเป็น GEMINI_API_KEY โค้ดจะดึงไปใช้เองโดยไม่ต้องใส่พารามิเตอร์
client = genai.Client(api_key=api_key)

def generate_ig_captions(menu_name, price):
    print(f"เดี๋ยวจัดให้เลย... กำลังคิดแคปชันสำหรับ {menu_name} ราคา {price} บาท นะครับ/ค่ะ\n")
    
    # 3. Create the prompt for 3 specific styles
    prompt = f'''
    คุณคือตัวแทน Social Media Manager สุดชิลของร้าน "MOON-MILK-BAR"
    ช่วยเขียนแคปชัน Instagram 3 แบบ เป็นภาษาไทยแบบกันเองเหมือนเพื่อนคุย สำหรับเมนูนี้:
    - ชื่อเมนู: {menu_name}
    - ราคา: {price} บาท

    กรุณาเขียนตาม 3 สไตล์นี้:
    1. Cute: น่ารักสดใส อีโมจิเยอะ ๆ ฟีลอ้อน ๆ ให้คนอยากมากิน
    2. Minimal: เรียบง่าย เท่ ๆ คลีน ๆ เน้นความมินิมอล ไม่เกิน 2 บรรทัด
    3. Gen-Z: วัยรุ่นเทสดี ติดตลกนิด ๆ ใช้ศัพท์วัยรุ่นฮิต ๆ พิมพ์ตัวเล็กตัวใหญ่ปนกัน หรือฟีลเพื่อนคุยกัน

    ขอให้ผลลัพธ์เป็นภาษาไทยล้วน ใช้คำพูดสบาย ๆ เป็นกันเอง
    แยกหัวข้อชัดเจน และบอกชื่อสไตล์แต่ละแบบ
    '''

    # 4. Generate content using Gemini 2.5 Flash
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    return response.text

# --- ทดสอบการทำงาน (Input จากผู้ใช้) ---
if __name__ == "__main__":
    menu = input("พิมพ์ชื่อเมนูที่อยากได้แคปชัน: ")
    price = input("ใส่ราคาประมาณนี้เป็นบาท: ")
    
    print("\n" + "-" * 30 + "\n")
    captions = generate_ig_captions(menu, price)
    print(captions)
    print("\nลองเลือกแคปชันที่ใช่ แล้วเอาไปลงโพสต์เลยนะครับ/ค่ะ 😊")