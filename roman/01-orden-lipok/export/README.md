# Экспорт — три формата адаптации

**Источник**: Роман «Орден Липок» (Том 1 цикла «Кабала Манхэттен»)  
**Материал**: 17 глав ядра + 8 глав орбиты, ~25 000 слов  
**Жанр**: Психологический шпионский триллер  
**Период**: 1992–1993, Киев + международная орбита

---

## Три полных пакета адаптации

### 1. 📖 `izdanie/` — Печатное издание для портала

**Готово к публикации**

- ✅ Чистая проза (25 глав)
- ✅ 26 промптов иллюстраций (обложка + 25 глав)
- ✅ Метаданные, аннотация, структура книги
- ✅ Технические параметры (формат, объём)

**Использование**: Публикация на литературном портале, печать POD, электронная книга (ePub/PDF)

**Иллюстрации**: AI-generated (Midjourney/SD) или commissioned artist, noir realism style

---

### 2. 🎨 `manga/` — Манга-адаптация

**Готово к производству**

- ✅ Дизайны 16 персонажей с промптами
- ✅ Референсы 20+ локаций с промптами
- ✅ Полный сценарий главы 1 (~20 страниц, 100+ панелей)
- ✅ Технические ноты для мангаки
- 📋 Шаблоны для глав 2–25 (создать по образцу главы 1)

**Формат**: Seinen manga, реалистичный стиль (Monster/20th Century Boys влияние), ~400–600 страниц

**Использование**: 
- Веб-манга (публикация online)
- Печатное издание (tankobon)
- Webtoon adaptation (vertical scroll)

**Производство**: Найм мангаки или AI-assisted (character consistency tech required)

---

### 3. 🎬 `dorama/` — Сериал (live-action или AI)

**Готово к производству**

- ✅ Структура сезона (8–10 эпизодов по 45–60 мин)
- ✅ Кастинг-промпты 16 персонажей (AI или live actors)
- ✅ Shooting script эпизода 1, открывающая сцена (8–10 мин, 36 shots)
- ✅ Production design: локации, костюмы, реквизит, cinematography, sound
- 📋 Shooting scripts эп. 2–8 (создать по шаблону)

**Формат**: Limited series, 8 episodes, ~6–8 часов total

**Бюджет**:
- Live-action: $12–16M (streaming prestige series)
- AI-generated: $500K–1M (экспериментальный формат)

**Использование**:
- Pitch к Netflix, HBO, Apple TV+
- Ukrainian co-production (local filming incentives)
- AI-дорама для YouTube/experimental platforms

**Comp titles**: The Americans, Tinker Tailor Soldier Spy, Chernobyl, Mindhunter

---

## Сравнение форматов

| Формат | Бюджет | Timeline | Охват | Лучше для |
|--------|--------|----------|-------|-----------|
| **Издание** | Низкий ($0–5K) | 1–2 месяца | Литературная аудитория | Чистая проза, глубина |
| **Манга** | Средний ($10–50K) | 6–12 месяцев | Визуальная аудитория | Noir aesthetic, панели |
| **Дорама** | Высокий ($500K–16M) | 12–24 месяца | Массовая аудитория | Cinematic, actors |

---

## Общие технические параметры

### Исходный материал
- **Проза**: `../text/` (glava-01–17, orbita/18–25)
- **Канон**: `../setings/` (персонажи, локации, хронология)
- **Правила**: `../.cursorrules` (голос, регистр, запреты)

### Ключевые визуальные мотивы (через все форматы)
1. **Капсула в кулаке** — улика, выбор, груз
2. **Четыре комнаты** — жалюзи, фосфор, переноска, паркет
3. **Лампа как проверка** — ритуал контроля
4. **Марго прядь справа** — signature gesture
5. **Инженер монета** — nervous habit
6. **Жако крик** — вместо телефона
7. **Дождь Киева** — маркировка, очищение
8. **Глаза открыты** — финальный образ

### Стилистика (universal)
- **Tone**: cold, clinical, noir, slow burn
- **Palette**: desaturated, institutional greens/grays, amber accents
- **Период**: 1990s post-Soviet authenticity critical
- **Языки**: русский + украинский (билингвизм важен)
- **Themes**: вербовка-фильтр, учреждение без устава, тайный суд, улика раньше приговора

---

## Как использовать этот пакет

### Для издателя
1. Читай `izdanie/README.md`
2. Бери прозу из `izdanie/text/`
3. Генерируй иллюстрации по `izdanie/illustration-prompts.md`
4. Публикуй

### Для мангаки / студии
1. Читай `manga/README.md`
2. Дизайн персонажей по `manga/character-designs.md`
3. Локации по `manga/locations-reference.md`
4. Сценарий главы 1 как эталон: `manga/scene-breakdown-chapter-01.md`
5. Рисуй остальные 24 главы по тому же шаблону

### Для продюсера / режиссёра
1. Читай `dorama/README.md`
2. Структура сезона: `dorama/series-structure.md` (8–10 эп)
3. Кастинг: `dorama/casting-prompts.md`
4. Shooting script эталон: `dorama/shooting-script-e01-opening.md`
5. Production bible: `dorama/production-design.md`
6. Пиши остальные эпизоды, снимай, продавай стримингу

### Для AI-генератора
- **Все три формата** содержат AI-промпты:
  - Illustration prompts (издание)
  - Character/location prompts (манга)
  - Casting/scene prompts (дорама)
- **Consistency tech**: character reference lock, LoRA training
- **Tools**: Midjourney, Stable Diffusion, Runway, Pika, ElevenLabs

---

## Права и лицензия

Материал основан на романе **«Орден Липок»**, том 1 цикла **«Кабала Манхэттен»**.

**Adaptation rights**: определяются автором.  
**Использование пакетов**: требует согласования с правообладателем.

Для коммерческого использования (публикация, производство, продажа адаптаций) свяжитесь с автором.

---

## Контакты и источники

- **Исходная проза**: `/data/projects/noise-floor/roman/01-orden-lipok/text/`
- **Канон и настройки**: `/data/projects/noise-floor/roman/01-orden-lipok/setings/`
- **Git repo**: `/data/projects/noise-floor/` (если есть remote, добавить)

---

## Changelog

**2026-09-17**: Initial export package created
- Издание: metadata, 26 illustration prompts, prose files
- Манга: 16 character designs, 20+ locations, full ch1 script
- Дорама: 8-ep structure, 16 casting prompts, e01 opening script, full production bible

---

**Все три формата готовы к производству.**

Выбирай формат, начинай создавать.
