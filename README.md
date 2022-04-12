# RaspberryPi-Firmware
Repository นี้เก็บการทำงานของ Firmware ที่ใช้กับตัว **Raspberry Pi 3 Model 3B** และ **MCU Board(Practicum Board)** พัฒนาโดยใช้ภาษา `Python` และ `C`  
สำหรับไฟล์ที่ใช้ Shellscript มีไว้เพื่อเรียกไฟล์ `main` มีไว้สำหรับการทำงานแต่ละส่วน เพื่อความสะดวกในการใช้งานร่วมกับไลบรารี่ `pm2`

## mcu
โฟล์เดอร์นี้เก็บการทำงานสำหรับของตัว Practicum Board ประกอบด้วยโฟลเดอร์ `firmware` และ `python`
### firmware
ทำหน้าที่ควบคุมการทำงานโดยจากผ่าน PORT ต่างๆบน Board
- `main.c` โปรแกรมหลักที่ใช้ทำงานของ MCU
- `peri.c` Module สำหรับควบคุมการเปิด/ปิดของเลเซอร์

### python
ทำหน้าที่รับ/ส่งข้อมูลจาก Raspberry Pi ไปยังตัว Practicum Board โดยข้อมูลในที่นี้ก็คือค่าข้อมูลไฟเลเซอร์แต่ละดวงเพื่อเช็คว่าจะต้องติดหรือดับ
- `main-mcu.py` โปรแกรมหลักสำหรับการรับ/ส่งข้อมูล
- `practicum.py` Module สำหรับการรับส่งข้อมูล

## raspi-GPIO
โฟล์เดอร์นี้เก็บการทำงานของตัว Raspberry Pi GPIO โดยตรง
- `api.py` Module สำหรับการส่ง HTTP Request ไปยังฝั่งของ Backend
- `game.py` Module เกมสำหรับการเล่นเกมใน 1 ตา
- `light.py` Module สำหรับการอ่านค่าของ LDR แต่ละตัว
- `main-raspi.py` โปรแกรมหลักสำหรับการทำงานของ Raspberry Pi GPIO