# 🕌 NamazTime  

**NamazTime** is a Python package that retrieves Islamic prayer times for a given city using the Aladhan API. It provides daily and weekly prayer schedules based on different calculation methods.

## 🌟 Features
- Retrieve today's prayer times for any city.
- Get prayer times for the next 7 days.
- Supports multiple calculation methods and fiqh schools.
- Timezone detection for accuracy.

## 📦 Installation  
Install NamazTime using pip:  
```bash
pip install namaztime
```

```
from namaztime import NamazTime as namaztime

namaz = namaztime("Tashkent")
print(namaz.today())  # Get today's prayer times
print(namaz.weekly())  # Get weekly prayer times
```


---

## **📄 README.md (O‘zbek tilida)**  


# 🕌 NamazTime  

**NamazTime** — bu Islomiy namoz vaqtlari haqida ma'lumot beruvchi Python paketi. U **Aladhan API** orqali namoz vaqtlarini olib keladi va kunlik yoki haftalik namoz jadvalini taqdim etadi.

## 🌟 Xususiyatlari
- Istalgan shahar uchun bugungi namoz vaqtlarini olish.
- Kelgusi 7 kunlik namoz vaqtlarini chiqarish.
- Turli hisoblash usullari va fiqh maktablarini qo‘llab-quvvatlash.
- To‘g‘ri vaqtni aniqlash uchun vaqt zonalarini aniqlash.

## 📦 O‘rnatish  
NamazTime'ni pip orqali o‘rnating:
```bash
pip install namaztime
```
```
from namaztime import NamazTime

namoz = NamazTime("Toshkent")
print(namoz.today())  # Bugungi namoz vaqtlarini olish
print(namoz.weekly())  # Haftalik namoz vaqtlarini olish
```

# 🕌 NamazTime  

**NamazTime** — это Python-библиотека, которая предоставляет расписание исламских молитв для указанного города, используя **Aladhan API**. Позволяет получать данные как на один день, так и на неделю.

## 🌟 Возможности
- Получение времени намаза на сегодня для любого города.
- Получение расписания намазов на 7 дней.
- Поддержка различных методов расчёта и мазхабов.
- Определение часового пояса для точности времени.

## 📦 Установка  
Установите NamazTime с помощью pip:  
```bash
pip install namaztime
```

```pythonfrom namaztime import NamazTime

namaz = NamazTime("Ташкент")
print(namaz.today())  # Получить время намаза на сегодня
print(namaz.weekly())  # Получить расписание намазов на неделю
```


## 📚 Supported API
NamazTime uses the Aladhan API to fetch prayer times.

API Documentation: [aladhan.com](https://aladhan.com)

### 🙏 Acknowledgment  
This project uses the **Aladhan API** to provide accurate prayer times.  
A huge **thank you** to the **Aladhan team** for their incredible service!  
