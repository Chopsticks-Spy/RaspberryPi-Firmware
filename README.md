# RaspberryPi-Firmware
Repository นี้เก็บการทำงานของ Firmware ที่ใช้กับตัว Raspberry Pi 3 Model 3B และ MCU Board(Practicum Board) พัฒนาโดยใช้ภาษา `Python` และ `C`

## mcu
โฟล์เดอร์นี้เก็บการทำงานสำหรับของตัว Practicum Board ประกอบด้วยโฟลเดอร์ `firmware` และ `python`
### firmware
ทำหน้าที่ควบคุมการทำงานโดยจากผ่าน PORT ต่างๆบน Board
- `main.c` โปรแกรมหลักที่ใช้ทำงานของ MCU
- `peri.c` Module สำหรับควบคุมการเปิด/ปิดของเลเซอร์
### python

